import happybase

from dig.io.adapter import KeyValueAdapter
from dig.io.serializer import Serializer, PickleSerializer


class HBaseAdapter(KeyValueAdapter):
    """
    Note: Need to increase timeout for thrift in hbase-site.xml
    <property>
        <name>hbase.thrift.server.socket.read.timeout</name>
        <value>6000000</value>
    </property>
    <property>
        <name>hbase.thrift.connection.max-idletime</name>
        <value>18000000</value>
    </property>
    """

    def __init__(self, host, table, serializer=None, key_prefix='', column_family=None, column_name=None,
                    **kwargs):
        if not serializer:
            serializer = PickleSerializer()
        self._conn = happybase.Connection(host=host, timeout=None, **kwargs)
        self._serializer = serializer
        self._key_prefix = key_prefix
        if column_family is not None:
            self._family_name = column_family
        else:
            self._family_name = 'dig'
        if column_name is not None:
            self._col_name = column_name
        else:
            self._col_name = 'obj'
        self._fam_col_name = '{}:{}'.format(self._family_name, self._col_name).encode('utf-8')

        if table.encode('utf-8') not in self._conn.tables():
            self._create_table(table)
        self._table = self._conn.table(table)

    def _get_key(self, record_id):
        return '{prefix}{record_id}'.format(prefix=self._key_prefix, record_id=record_id)

    def __del__(self):
        try:
            self._conn.close()
        except:
            pass

    def _create_table(self, table_name):
        self._conn.create_table(table_name, {self._family_name:dict()})

    def get(self, record_id):
        row = self._table.row(self._get_key(record_id))
        if row:
            column = row[self._fam_col_name]
            return self._serializer.loads(column)
        return None

    def set(self, record_id, record):
        return self._table.put(self._get_key(record_id), {self._fam_col_name: self._serializer.dumps(record)})

    def __iter__(self):
        return self.__next__()

    def __next__(self):
        for key, data in self._table.scan(
                row_prefix=self._key_prefix, filter=b'FirstKeyOnlyFilter()'):
            yield self._serializer.loads(data[self._fam_col_name])
