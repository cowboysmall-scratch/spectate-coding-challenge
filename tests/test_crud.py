
import unittest

from spectate import crud


class TestCRUD(unittest.TestCase):

    def test_create_basic(self):
        query = crud.create_query("TABLE", something = "1", other = "two", again = "123.45")
        self.assertEqual(query, "insert into TABLE (again, other, something) values (123.45, 'two', 1)")

    def test_create_dict(self):
        values = {"something": "1", "other": "two", "again": "123.45"}
        query  = crud.create_query("TABLE", **values)
        self.assertEqual(query, "insert into TABLE (again, other, something) values (123.45, 'two', 1)")





    def test_retrieve_basic(self):
        query = crud.retrieve_query("TABLE")
        self.assertEqual(query, "select * from TABLE T")


    def test_retrieve_where_basic(self):
        query = crud.retrieve_query("TABLE", "T.something = 1")
        self.assertEqual(query, "select * from TABLE T where T.something = 1")


    def test_retrieve_where_multiple(self):
        query = crud.retrieve_query("TABLE", "T.something = 1", "T.other = True")
        self.assertEqual(query, "select * from TABLE T where T.something = 1 and T.other = True")





    def test_update_basic(self):
        query = crud.update_query("TABLE", 1, something = "1", other = "two")
        self.assertEqual(query, "update TABLE set other = 'two', something = 1 where id = 1")


    def test_update_dict(self):
        values = {"something": "1", "other": "two"}
        query  = crud.update_query("TABLE", 1, **values)
        self.assertEqual(query, "update TABLE set other = 'two', something = 1 where id = 1")





    def test_delete_basic(self):
        query = crud.delete_query("TABLE", "id = 1")
        self.assertEqual(query, "delete from TABLE where id = 1")






if __name__ == '__main__':
    unittest.main()

