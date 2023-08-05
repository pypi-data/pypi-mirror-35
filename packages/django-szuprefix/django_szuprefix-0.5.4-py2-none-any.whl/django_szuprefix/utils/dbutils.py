#!/usr/bin/env python   
# -*- coding:utf8 -*-   
# Author:DenisHuang
# Date:2013/11/7
# Usage:
from django.db import connections

db = connections['default']
cursor = db.cursor()
cursor._defer_warnings = True


#
# all_types = {}
# all_types["integer"] = ["tinyint", "smallint", "mediumint", "int", "bigint"]
# all_types["decimal"] = ["double", "float", "decimal"]
# all_types["time"] = ["time", "date", "datetime", "timestamp", "year"]
# all_types["string"] = ["char", "varchar", "text", "enum"]
#
#
# def genAllFieldTypesTable(cursor, fieldTypes):
#     tmp_table = "tmp_YxbUm87N13F"
#     fs = ",".join(
#         ["f%s %s" % (t, t == "enum" and "enum('a')" or t == "varchar" and "varchar(1)" or t) for t in fieldTypes])
#     cursor.execute("create table if not exists %s (%s)" % (tmp_table, fs))
#     cursor.execute("select * from %s limit 1" % tmp_table)
#     d = dict([(fd[0][1:], fd[1]) for fd in cursor.description])
#     cursor.execute("drop table if exists %s " % tmp_table)
#     return d
#
#
# #
# # print genAllFieldTypesTable(cursor,reduce(lambda x,y:x+y,all_types.values())
# #
# fieldTypeCodes = {'smallint': 2,
#                   'enum': 254,
#                   'varchar': 253,
#                   'timestamp': 7,
#                   'int': 3,
#                   'mediumint': 9,
#                   'decimal': 246,
#                   'float': 4,
#                   'year': 13,
#                   'datetime': 12,
#                   'char': 254,
#                   'tinyint': 1,
#                   'bigint': 8,
#                   'text': 252,
#                   'time': 11,
#                   'double': 5,
#                   'date': 10}
#
# fieldCodeTypes = dict([(v, k) for k, v in fieldTypeCodes.iteritems()])
#
# fieldCategories = {}
# for cat, types in all_types.iteritems():
#     for type in types:
#         fieldCategories[type] = cat
#         fieldCategories[fieldTypeCodes[type]] = cat
#
#
# def cursorDescription2MapList(cursor):
#     global fieldCategories
#     l = []
#     m = {}
#     for fd in cursor.description:
#         d = {'name': fd[0],
#              'verboseName': fd[0],
#              'category': fieldCategories[fd[1]]}
#         l.append(d)
#         m[fd[0]] = d
#     return m, l
#
#
# def cursorDescription2SortedDict(cursor):
#     from collections import OrderedDict
#     # from django.http.request import SortedDict
#     m = OrderedDict()
#     for fd in cursor.description:
#         d = {'name': fd[0],
#              'verboseName': fd[0],
#              'category': fieldCategories[fd[1]]}
#         m[fd[0]] = d
#     return m


def get_table_fields(conn, table_name, schema=None):
    with conn.cursor() as cursor:
        if schema:
            cursor.execute("set search_path to '%s'" % schema)
        from collections import OrderedDict
        d = OrderedDict()
        introspection = conn.introspection
        primary_key_column = introspection.get_primary_key_column(cursor, table_name)
        for row in introspection.get_table_description(cursor, table_name):
            name = row[0]
            field_params = OrderedDict()
            field_notes = []

            try:
                field_type = introspection.get_field_type(row[1], row)
            except KeyError:
                field_type = 'TextField'
                field_notes.append('This field type is a guess.')

            # This is a hook for data_types_reverse to return a tuple of
            # (field_type, field_params_dict).
            if type(field_type) is tuple:
                field_type, new_params = field_type
                field_params.update(new_params)

            if name == primary_key_column:
                field_params['primary_key'] = True

            # Add max_length for all CharFields.
            if field_type == 'CharField' and row[3]:
                field_params['max_length'] = int(row[3])

            if field_type == 'DecimalField':
                if row[4] is None or row[5] is None:
                    field_notes.append(
                        'max_digits and decimal_places have been guessed, as this '
                        'database handles decimal fields as float')
                    field_params['max_digits'] = row[4] if row[4] is not None else 10
                    field_params['decimal_places'] = row[5] if row[5] is not None else 5
                else:
                    field_params['max_digits'] = row[4]
                    field_params['decimal_places'] = row[5]
            if row[6]:  # If it's NULL...
                if field_type == 'BooleanField(':
                    field_type = 'NullBooleanField('
                else:
                    field_params['blank'] = True
                    field_params['null'] = True
            d[name] = dict(name=name, type=field_type, params=field_params, notes=field_notes)

        return d


def create_table(conn, table, fields):
    try:
        old_fields = get_table_fields(conn, table)
        return  # table exists, do nothing
    except Exception, e:
        pass  # table not exists, continue

    class NoneMeta(object):
        db_tablespace = None

    class NoneModel(object):
        _meta = NoneMeta()

    fs = {}
    model = NoneModel
    from django.db.models import fields as field_types
    column_sqls = []
    with conn.schema_editor() as schema:
        for k, v in fields.items():
            es = "field_types.%s('%s',%s)" % (v['type'], k, ','.join(["%s=%s" % a for a in v['params'].items()]))
            fs[k] = field = eval(es)
            field.column = k
            definition, extra_params = schema.column_sql(model, field)
            column_sqls.append("%s %s" % (
                schema.quote_name(field.column),
                definition,
            ))
        sql = schema.sql_create_table % {
            "table": schema.quote_name(table),
            "definition": ", ".join(column_sqls)
        }
        return schema.execute(sql)


def execute_sql(sql, db_name='default'):
    cur = connections[db_name].cursor()
    return cur.execute(sql), cur


def getDB(dbName='default'):
    return connections[dbName]


def getDBOptionals():
    return [(k, v["HOST"]) for k, v in connections.databases.iteritems()]


def django_db_setting_2_sqlalchemy(sd):
    emap = {"mysql": "mysql+mysqldb"}
    engine = sd['ENGINE'].split(".")[-1]
    engine = emap.get(engine, engine)
    charset = sd.get("OPTIONS", {}).get("charset")
    params = charset and "?charset=%s" % charset or ""
    return "%s://%s:%s@%s/%s%s" % (engine, sd['USER'], sd['PASSWORD'], sd['HOST'], sd['NAME'], params)


def db_sqlalchemy_str(db):
    return django_db_setting_2_sqlalchemy(connections[db].settings_dict)


def get_slave_time(db):
    con = connections[db]
    sd = con.settings_dict
    engine = sd['ENGINE'].split(".")[-1]
    sql = {
        'mysql': "show slave status",
        "postgresql": "select to_char(pg_last_xact_replay_timestamp(),'YYYY-mm-dd HH24:MI:SS') as end_time"
    }.get(engine)
    if not sql:
        return
    import pandas as pd
    from datetime import datetime, timedelta
    now = datetime.now()
    df = pd.read_sql(sql, django_db_setting_2_sqlalchemy(sd))
    print df
    if len(df) == 1:
        if engine == 'mysql':
            sbm = df.iloc[0]['Seconds_Behind_Master']
            return now - timedelta(seconds=sbm)
        elif engine == 'postgresql':
            return df.iloc[0]['end_time']
