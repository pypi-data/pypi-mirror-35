# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals, division
import pandas as pd
from .dbutils import db_sqlalchemy_str, get_table_fields, getDB
from pandas.io.sql import pandasSQL_builder
import math
from datetime import datetime
from collections import OrderedDict
import logging

log = logging.getLogger("django")


def get_select_sql(sql):
    sql = sql.strip()
    return ' ' in sql.lower() and sql or (u'select * from %s' % sql)


def get_dataframe_from_table(table_name_or_sql, connection="default", coerce_float=True):
    sql = get_select_sql(table_name_or_sql).replace("%", "%%")
    con = connection.startswith("hive://") and connection or db_sqlalchemy_str(connection)
    return pd.read_sql(sql, con, coerce_float=coerce_float)


def write_dataframe_to_table(df, **kwargs):
    kwargs['con'] = db_sqlalchemy_str(kwargs['con'])
    return df.to_sql(**kwargs)


def smart_write_dataframe_to_table(df, **kwargs):
    con = db_sqlalchemy_str(kwargs['con'])


def split_dataframe_into_chunks(df, chunksize=10000):
    for i in range(int(math.ceil(len(df) / chunksize))):
        b = i * chunksize
        e = b + chunksize - 1
        yield df.loc[b:e]


def dtype(dt):
    return dt.startswith('int') and 'int' \
           or dt.startswith('float') and 'float' \
           or dt.startswith('datetime') and 'datetime' \
           or 'string'


def series_dtype(series):
    dt = str(series.dtype)
    return dtype(dt)


def ftype(ft):
    return ft == "string" and "varchar(255)" or ft == "datetime" and "TIMESTAMP" or ft


def format_timestamp(df):
    for c, dt in df.dtypes.iteritems():
        if str(dt).startswith("datetime"):
            df[c] = df[c].apply(lambda x: x.isoformat())
    return df


def clear_dict_nan_value(d):
    for k, v in d.items():
        if pd.isnull(v) or v == 'NaT':
            d[k] = None
    return d


def lower_column_name(df):
    a = {}
    for c in df.columns:
        if c != c.lower():
            a[c] = c.lower()
    if a:
        df.rename(columns=a, inplace=True)


def dataframe_to_table(df, is_preview=False):
    count = len(df)
    if is_preview and count > 20:
        data = df[:10].merge(df[-10:], how='outer')
    else:
        data = df
    data = [clear_dict_nan_value(d) for d in data.to_dict("records")]
    from pandas.io.json.table_schema import build_table_schema
    schema = build_table_schema(df, index=False)
    return dict(data=data, count=count, fields=schema.get('fields'), is_preview=is_preview)


def guess_dimessions(df, nunique_limit=1000):
    columns = OrderedDict()
    rc = len(df)
    for c in df.columns:
        dt = series_dtype(df[c])
        nunique = df[c].agg('nunique')
        dimension_deny = dt != 'datetime' and nunique > nunique_limit * 0.1
        columns[c] = {'name': c, 'type': dt, 'nunique': nunique, 'dimension_deny': dimension_deny}

    cs = [(c['nunique'], c['type'], c['name']) for c in columns.values()]
    cs.sort(reverse=True)
    a = [c[2] for c in cs if c[0] == rc and c[1] != 'datetime']
    id_field = a and a[0] or None
    datetime_dimensions = [c[2] for c in cs if c[1] == 'datetime']
    measures = [c[2] for c in cs if c[1] in ['int', 'float'] and c[2] != id_field]
    category_dimensions = [c[2] for c in cs if c[1] == 'string' and c[2] != id_field]
    return dict(
        columns=columns,
        datetime_dimensions=datetime_dimensions,
        category_dimensions=category_dimensions,
        measures=measures,
        id_field=id_field
    )


class AutoGrowTable(object):
    def __init__(self, db_name, table_name, primary_key, insert_timestamp_field=None, update_timestamp_field=None):
        self.db_name = db_name
        self.connection = getDB(self.db_name)
        tps = table_name.split(".")
        self.table_name = tps[-1]
        self.schema = len(tps) > 1 and tps[0] or None
        self.full_table_name = self.schema and "%s.%s" % (self.connection.ops.quote_name(self.schema),
                                                          self.connection.ops.quote_name(
                                                              self.table_name)) or self.connection.ops.quote_name(
            self.table_name)
        self.primary_key = primary_key
        self.fields = {}
        self.insert_timestamp_field = insert_timestamp_field
        self.update_timestamp_field = update_timestamp_field
        self.pd_sql = pandasSQL_builder(db_sqlalchemy_str(self.db_name), schema=self.schema)
        self.detect_fields()

    def detect_fields(self):
        try:
            self.fields = [f.lower() for f in get_table_fields(getDB(self.db_name), self.table_name, self.schema)]
        except Exception, e:
            err_str = str(e)
            if "does not exist" in err_str:
                return
            log.error("AutoGroupTable.detect_fields %s %s error: %s", self.db_name, self.table_name, e)

    def get_field_definition(self, fields):
        return ",".join(["%s %s" % (f, ftype(f)) for f in fields])

    def create_table(self, df):
        exists = self.pd_sql.has_table(self.table_name)
        dtypes = dict([(c, dtype(str(dt))) for c, dt in df.dtypes.iteritems()])
        new_fields = ["%s %s" % (f, ftype(dt)) for f, dt in dtypes.iteritems() if f.lower() not in self.fields]
        if self.update_timestamp_field and self.update_timestamp_field not in self.fields:
            new_fields.append("%s timestamp default CURRENT_TIMESTAMP" % self.update_timestamp_field)
        if self.insert_timestamp_field and self.insert_timestamp_field not in self.fields:
            new_fields.append("%s timestamp default CURRENT_TIMESTAMP" % self.insert_timestamp_field)
        with self.connection.cursor() as cursor:
            if not exists:
                sql = "create table %s(%s)" % (self.full_table_name, ",".join(new_fields))
                # print sql
                cursor.execute(sql)
                sql = "alter table %s add primary key(%s)" % (self.full_table_name, self.primary_key)
                # print sql
                cursor.execute(sql)
                self.detect_fields()
            else:
                if new_fields:
                    sql = "alter table %s add column %s" % (self.full_table_name, ", add column ".join(new_fields))
                    # print sql
                    cursor.execute(sql)

    def run(self, data_frame):
        df = data_frame
        lower_column_name(df)
        self.create_table(df)
        errors = self.insert_or_update(df)
        return errors

    def gen_sql_table(self, df):
        from pandas.io.sql import SQLTable
        from sqlalchemy import Column, DateTime
        self.table = SQLTable(self.table_name, self.pd_sql, df, index=False, schema=self.schema).table.tometadata(
            self.pd_sql.meta)
        if self.update_timestamp_field and self.update_timestamp_field not in self.table.columns:
            self.table.append_column(Column(self.update_timestamp_field, DateTime))
        if self.insert_timestamp_field and self.insert_timestamp_field not in self.table.columns:
            self.table.append_column(Column(self.insert_timestamp_field, DateTime))

    def split_insert_and_update(self, df):
        # self.table.select(  df[self.primary_key]
        pass

    def insert_or_update(self, df):
        self.gen_sql_table(df)
        errors = []
        df = format_timestamp(df)
        pks = [k.strip() for k in self.primary_key.split(",")]
        efs = ['1 as a']
        if self.insert_timestamp_field:
            efs.append(self.insert_timestamp_field)
        if self.update_timestamp_field:
            efs.append(self.update_timestamp_field)
        sql_template = "select %s from %s where %%s" % (",".join(efs), self.full_table_name)
        quote_name = self.connection.ops.quote_name
        for i in xrange(len(df)):
            try:
                s = df.iloc[i]
                d = clear_dict_nan_value(s.to_dict())
                where = " and ".join(["%s='%s'" % (quote_name(pk), d[pk.lower()]) for pk in pks])
                sql = sql_template % where
                rs = self.pd_sql.read_sql(sql, coerce_float=False)
                now = datetime.now().isoformat()
                if not rs.empty:
                    r = rs.iloc[0]
                    if self.update_timestamp_field:
                        d[self.update_timestamp_field] = now
                    if self.insert_timestamp_field:
                        d[self.insert_timestamp_field] = r[self.insert_timestamp_field]
                    self.table.update().where(where).values(d).execute()
                else:
                    if self.insert_timestamp_field:
                        d[self.insert_timestamp_field] = now
                    if self.update_timestamp_field:
                        d[self.update_timestamp_field] = now
                    self.table.insert(d).execute()
            except Exception, e:
                errors.append(([d[k.lower()] for k in pks], str(e)))
        if errors:
            log.error("pandas.AutoGrowTable %s.%s insert_or_update got %d errors: %s", self.db_name, self.table_name,
                      len(errors), errors)
        return errors

    def update(self, df):
        for r in xrange(len(df)):
            self.table.update(df.iloc[r].to_dict()).execute()
