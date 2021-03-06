import unittest
import sys
sys.path.append("../")
from WookieDb import *

class TestBasicCommands(unittest.TestCase):

    def setUp(self):
        self.db = WookieDb("localhost", "wookiedbtest", "wookiedbtest", "wookiedbtest")

    def testWorking(self):
        """checks if the object is creatable and localhost accessible"""
        assert True

    def testQuery(self):
        """checks if running a query works"""
        res = self.db.query("select 1")
        self.assertEqual(res[0][0], 1)

    def testCreateTable(self):

        self.db.query("""CREATE TABLE `basic_test` (
                        `id` int(11) NOT NULL AUTO_INCREMENT,
                        `intVar` int(11) DEFAULT NULL,
                        `charVar` varchar(45) DEFAULT NULL,
                         PRIMARY KEY (`id`)
                       ) ENGINE=InnoDB DEFAULT CHARSET=latin1""")

        tables = self.db.query("show tables")
        self.assertTrue(("basic_test",) in tables)

        self.db.query("DROP TABLE basic_test")

if __name__ == "__main__":
    unittest.main()
