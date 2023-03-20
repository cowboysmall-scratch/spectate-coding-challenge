import unittest
import sqlite3

from spectate import database

class TestTriggers(unittest.TestCase):

    def test_event_trigger(self):
        database.init_ddl()
        database.init_dml()

        conn = sqlite3.connect("spectate.db")

        c    = conn.execute("SELECT active FROM sport where id = 2")
        self.assertEqual(c.fetchone()[0], 1)

        conn.execute("UPDATE event SET active = 0 WHERE sport_id = 2 AND id = 3")
        conn.commit()

        c    = conn.execute("SELECT active FROM sport where id = 2")
        self.assertEqual(c.fetchone()[0], 0)



    def test_market_trigger(self):
        database.init_ddl()
        database.init_dml()

        conn = sqlite3.connect("spectate.db")

        c    = conn.execute("SELECT active FROM event where id = 2")
        self.assertEqual(c.fetchone()[0], 1)

        conn.execute("UPDATE market SET active = 0 WHERE event_id = 2 AND id = 3")
        conn.commit()

        c    = conn.execute("SELECT active FROM event where id = 2")
        self.assertEqual(c.fetchone()[0], 0)



    def test_selection_trigger(self):
        database.init_ddl()
        database.init_dml()

        conn = sqlite3.connect("spectate.db")

        c    = conn.execute("SELECT active FROM market where id = 2")
        self.assertEqual(c.fetchone()[0], 1)

        conn.execute("UPDATE selection SET active = 0 WHERE market_id = 2 AND id = 3")
        conn.commit()

        c    = conn.execute("SELECT active FROM market where id = 2")
        self.assertEqual(c.fetchone()[0], 0)


