import MySQLdb

class WookieDb:

    def __init__(self, host, user, password, db, select_type="nodict"):
        self.connection = MySQLdb.Connect(host=host, user=user, passwd=password, db=db)
        self.cursor = self.connection.cursor()
        self.select_type = select_type

    def select(self, table, fields, condition=""):
        if self.select_type == "nodict":
            return self.query("SELECT " + fields + " FROM " + table + condition)
        else:
            query = "SELECT " + fields + " FROM " + table + condition
            self.cursor.execute(query)

            description = self.cursor.description
            results = self.cursor.fetchall()

            results_dict = list()
            for res in results:
                res_dict = dict()

                i = 0
                for res_part in res:
                    res_dict[description[i][0]] = res_part
                    i += 1

                results_dict.append(res_dict)

            return results_dict



    def insert(self, table, data):
        raise NotImplementedError("Not yet implemented, planned for future")

    def update(self, table, data, condition=""):
        raise NotImplementedError("Not yet implemented, planned for future")

    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
