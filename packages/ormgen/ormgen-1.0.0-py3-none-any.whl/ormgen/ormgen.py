# -*- encoding: utf-8 -*-

import re
import sys
import MySQLdb
import argparse

columns_sql = """SELECT DISTINCT TABLE_NAME, COLUMN_NAME, COLUMN_TYPE, COLUMN_DEFAULT, COLUMN_KEY, IS_NULLABLE, CHARACTER_SET_NAME, COLLATION_NAME, COLUMN_COMMENT, Extra
        FROM information_schema.columns
        WHERE TABLE_SCHEMA='{schema}'
        """

engine_sql = """SELECT TABLE_NAME, ENGINE FROM information_schema.TABLES WHERE TABLE_SCHEMA = '{schema}'"""

index_sql = """SELECT DISTINCT TABLE_NAME, INDEX_NAME, COLUMN_NAME, SEQ_IN_INDEX FROM INFORMATION_SCHEMA.STATISTICS WHERE TABLE_SCHEMA = '{schema}' ORDER BY TABLE_NAME, INDEX_NAME, SEQ_IN_INDEX"""

def get_table_columns(cursor, schema):
    table_columns = {}
    cursor.execute(columns_sql.format(schema=schema))
    for item in cursor.fetchall():
        table = item[0]
        if table not in table_columns:
            table_columns[table] = []
        table_columns[table].append(item[1:])
    return table_columns

def get_table_engine(cursor, schema):
    table_engine = {}
    cursor.execute(engine_sql.format(schema=schema))
    for table, engine in cursor.fetchall():
        table_engine[table] = engine
    return table_engine

def get_table_index(cursor, schema):
    table_index = {}
    cursor.execute(index_sql.format(schema=schema))
    for table, index_name, column_name, _ in cursor.fetchall():
        if table not in table_index:
            table_index[table] = {}
        if index_name not in table_index[table]:
            table_index[table][index_name] = []
        table_index[table][index_name].append(column_name)
    return table_index

class Column:
    def __init__(self, column_name, column_type, column_default, column_key, is_nullable, charset, collation, comment, extra):
        self.column_name = column_name
        self.column_type = self._parse_column_type(column_type)
        self.column_default = self._parse_column_default(column_default)
        self.is_primary = False
        self.is_unique = False
        self.is_index = False
        self._parse_column_key(column_key)
        self.is_nullable = is_nullable
        self.charset = self._parse_charset(charset)
        self.collation = self._parse_collation(collation)
        self.comment = comment
        self.is_autoincrement = False
        self._parse_autoincrement(extra)

    def _parse_column_type(self, column_type):
        # varchar
        res = re.fullmatch(r'^(?:var)?char\((\d+)\)$', column_type)
        if res:
            return 'String({})'.format(res.group(1))
        # longtext
        res = re.fullmatch(r'^(longtext)|(mediumtext)$', column_type)
        if res:
            return 'String'
        # text
        res = re.fullmatch(r'^text$', column_type)
        if res:
            return 'Text'
        # decimal
        res = re.fullmatch(r'^decimal\((\d+),?(\d+)\)$', column_type)
        if res:
            return 'Numeric({}, {})'.format(res.group(1), res.group(2))
        # date
        res = re.fullmatch(r'date', column_type)
        if res:
            return 'Date'
        # time
        res = re.fullmatch(r'time', column_type)
        if res:
            return 'Time'
        # datetime
        res = re.fullmatch(r'(datetime)|(timestamp)', column_type)
        if res:
            return 'DateTime'
        # bigint
        res = re.fullmatch(r'^bigint\(\d+\) ?(unsigned)?$', column_type)
        if res:
            return 'BigInteger'
        # int
        res = re.fullmatch(r'^int\(\d+\) ?(unsigned)?$', column_type)
        if res:
            return 'Integer'
        # tinyint
        res = re.fullmatch(r'^tinyint\(\d+\) ?(unsigned)?$', column_type)
        if res:
            return 'SmallInteger'
        # float
        res = re.fullmatch(r'^float$', column_type)
        if res:
            return 'Float'
        # year
        res = re.fullmatch(r'^year\(\d+\)$', column_type)
        if res:
            return 'YEAR'
        raise Exception('unsupported column_type {}'.format(column_type))

    def _parse_column_default(self, column_default):
        if column_default:
            return '''server_default=text("'{}'")'''.format(column_default)

    def _parse_column_key(self, column_key):
        '''column_key = UNI or PRI'''
        if column_key == 'UNI':
            self.is_unique = True
        elif column_key == 'PRI':
            self.is_primary = True
        elif column_key == 'MUL':
            pass
        elif column_key:
            raise Exception('unsupported column_key {} on column {}'.format(column_key, self.column_name))

    def _parse_charset(self, charset):
        return 

    def _parse_collation(self, collation):
        return

    def _parse_autoincrement(self, extra):
        if extra == 'auto_increment':
            self.is_autoincrement = True

    def __str__(self):
        '''
        For example: ID = Column(String(100), nullable=False, primary_key=True, unique=True, server_default=text("''"))
        '''
        res = ''
        res = res + self.column_name + ' = Column(' + self.column_type
        if not self.is_nullable:
            res = res + ', ' + 'nullable=False'
        if self.is_primary:
            res = res + ', ' + 'primary_key=True'
        if self.is_unique:
            res = res + ', ' + 'unique=True'
        if self.is_index:
            res = res + ', ' + 'index=True'
        if self.is_autoincrement:
            res = res + ', ' + 'autoincrement=True'
        if self.column_default:
            res = res + ', ' + self.column_default
        if self.comment:
            res = res + ', ' + "doc={{'comment': '{}'}}".format(self.comment)
        res += ')'

        return res
    
class Model:
    def __init__(self, tablename, engine='InnoDB'):
        self.columns = {}
        self.tablename = tablename
        self.engine = engine
        self.composite_index = []

    def add_column(self, column):
        self.columns[column.column_name] = column
    
    def parse_index(self, index):
        for index_name, columns in index.items():
            if index_name == 'PRIMARY':
                if len(columns) > 1:
                    continue
                    #raise Exception('unsupport composite primary key, table {}'.format(self.tablename))
                self.columns[columns[0]].is_primary = True
            elif len(columns) == 1:
                self.columns[columns[0]].is_index = True
            else:
                composite_index = "Index('" + index_name + "', " + ", ".join(["'" + c + "'" for c in columns]) + "),"
                self.composite_index.append(composite_index)

    def __str__(self):
        res = 'class {}(Base):'.format(self.tablename.capitalize()) + '\n'
        res = res + '    ' + "__tablename__ = '{}'".format(self.tablename) + '\n'
        res = res + '    ' + "__table_args__ = (\n"
        for composite_index in self.composite_index:
            res = res + '        ' + composite_index + '\n'
        res = res + '    )\n'
        res = res + '\n'

        for column in self.columns.values():
            res = res + '    ' + str(column) + '\n'
        return res

class OrmGenerator:
    def __init__(self, host, user, password, schema):
        self.db = MySQLdb.connect(host, user, password, schema, charset="utf8", use_unicode=True)
        self.cursor = self.db.cursor()
        self.schema = schema

    def render(self, outfile):
        table_columns = get_table_columns(self.cursor, self.schema)
        table_engine = get_table_engine(self.cursor, self.schema)
        table_index = get_table_index(self.cursor, self.schema)
        models = {}
        for table in table_columns.keys():
            columns = table_columns[table]
            model = Model(table, table_engine[table])
            models[table] = model
            for column_name, column_type, column_default, column_key, is_nullable, charset, collation, comment, extra in columns:
                column = Column(column_name, column_type, column_default, column_key, is_nullable, charset, collation, comment, extra)
                model.add_column(column)

            if table in table_index:
                model.parse_index(table_index[table])

        result = ''
        result += '# coding: utf-8\n\n'
        result += 'from sqlalchemy import BigInteger, Integer, SmallInteger, Column, Date, Time, DateTime, Index, Numeric, Float, String, Text, text\n'
        result += 'from sqlalchemy.dialects.mysql.types import YEAR\n'
        result += 'from sqlalchemy.ext.declarative import declarative_base\n'
        result += '\n\n'
        result += 'Base = declarative_base()\n'
        result += 'metadata = Base.metadata\n'
        result += '\n\n'

        tables = sorted(models.keys())
        for table in tables:
            result += str(models[table]) + '\n'
        print(result, file=outfile)
