
import sqlite3


def init_ddl() -> None:
    conn = sqlite3.connect("spectate.db")
    conn.execute("PRAGMA foreign_keys = ON")
    curs = conn.cursor()

    with open("sql/ddl.sql", "r") as ddl:
        curs.executescript(ddl.read())

    conn.commit()
    conn.close()


def init_dml() -> None:
    conn = sqlite3.connect("spectate.db")
    conn.execute("PRAGMA foreign_keys = ON")
    curs = conn.cursor()

    with open("sql/dml.sql", "r") as dml:
        curs.executescript(dml.read())

    conn.commit()
    conn.close()


def columns(table: str) -> list:
    conn = sqlite3.connect("spectate.db")
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row

    cursor = conn.execute("select * from {}".format(table))
    columns = [d[0] for d in cursor.description]

    conn.close()

    return columns


def execute(query: str) -> None:
    conn = sqlite3.connect("spectate.db")
    conn.execute("PRAGMA foreign_keys = ON")

    try:
        conn.execute(query)
    except sqlite3.IntegrityError:
        print("\n")
        print("\tReferential Integrity Error!")

    conn.commit()
    conn.close()


def retrieve(query: str) -> list:
    conn = sqlite3.connect("spectate.db")
    conn.execute("PRAGMA foreign_keys = ON")

    conn.row_factory = dict_factory

    results = []
    for row in conn.execute(query):
        result = {}
        for key in row.keys():
            result[key] = row[key]
        results.append(result)

    conn.close()

    return results


def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}
