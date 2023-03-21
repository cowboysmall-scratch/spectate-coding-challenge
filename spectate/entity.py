
"""

      My initial approach was to implement a lightweight ORM framework, but I
    decided against it as I didn't feel like I had enough years left in my
    life.

      The below would have contained meta information about tables, and various
    utility methiods to help construct queries.

      I decided to take a different approach due to time constraints. I leave
    it here for interests sake - to show the direction I could have gone.

    J.K.

"""


class Entity:

    def __init__(self, name, row):
        self.name = name
        self.row = row


class Row:

    def __init__(self, *columns):
        self.columns = columns
        self.column_names = [c.column_name for c in columns]
        self.column_types = [c.column_type for c in columns]
        self.column_type = {c.column_name: c.column_type for c in columns}
        self.nullable = {c.column_name: c.nullable for c in columns}

    def get_columns(self):
        return ["id"] + self.column_names

    def get_column_type(self, column_name):
        return self.column_type[column_name]

    def is_column_nullable(self, column_name):
        return self.nullable[column_name]


class Column:

    def __init__(self, column_name, column_type, nullable=False):
        self.column_name = column_name
        self.column_type = column_type
        self.nullable = nullable
