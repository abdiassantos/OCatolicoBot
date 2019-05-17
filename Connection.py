import postgresql as psql

class Connection(object):
    _db = None

    def __init__(self, database):
        self._db = psql.open(database)

    def manipulate(self, sql):
        try:
            self._db.execute(sql)
        except:
            return False
        return True

    def consult(self, sql):
        rs = None
        try:
            rs = self._db.prepare(sql)
        except:
            return None
        return rs

    def nextPK(self, table, key):
        sql = 'select max(' + key + ') from ' + table
        rs = self.consult(sql)
        pk = rs.first()
        return pk + 1

    def closeConnection(self):
        self._db.close()