import unittest

from spectate import crud


class TestCRUD(unittest.TestCase):

    def test_insert_basic(self):
        query = crud.insert_query("TABLE", something = "1", other = "two", again = "123.45")
        self.assertEqual(query, "insert into TABLE (again, other, something) values (123.45, 'two', 1)")

    def test_insert_dict(self):
        insert = {"something": "1", "other": "two", "again": "123.45"}
        query = crud.insert_query("TABLE", **insert)
        self.assertEqual(query, "insert into TABLE (again, other, something) values (123.45, 'two', 1)")





    def test_read_basic(self):
        query = crud.read_query("TABLE")
        self.assertEqual(query, "select * from TABLE T")


    def test_read_where_basic(self):
        query = crud.read_query("TABLE", "T.something = 1")
        self.assertEqual(query, "select * from TABLE T where T.something = 1")


    def test_read_where_complex(self):
        query = crud.read_query("TABLE", "T.something = 1", "T.other = True")
        self.assertEqual(query, "select * from TABLE T where T.something = 1 and T.other = True")





    def test_update_basic(self):
        query = crud.update_query("TABLE", 1, something = "1", other = "two")
        self.assertEqual(query, "update TABLE set other = 'two', something = 1 where id = 1")


    def test_update_dict(self):
        update = {"something": "1", "other": "two"}
        query  = crud.update_query("TABLE", 1, **update)
        self.assertEqual(query, "update TABLE set other = 'two', something = 1 where id = 1")





    def test_delete_basic(self):
        query = crud.delete_query("TABLE", "id = 1")
        self.assertEqual(query, "delete from TABLE where id = 1")






if __name__ == '__main__':
    unittest.main()
