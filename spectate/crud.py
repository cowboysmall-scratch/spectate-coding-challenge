

def convert(value: str) -> str:
    try:
        float(value)
        return "{}".format(value)
    except ValueError:
        return "'{}'".format(value)


def create_query(table: str, **inserts: str) -> str:
    keys = sorted(inserts.keys())
    cols = ", ".join(keys)
    values = ", ".join(convert(inserts[key]) for key in keys)
    return "insert into {} ({}) values ({})".format(table, cols, values)


def retrieve_query(table: str, *where: str) -> str:
    basic = "select * from {} {}".format(table, table[0])
    if not where:
        return basic
    else:
        return "{} where {}".format(basic, " and ".join(where))


def update_query(table: str, id: int, **updates: str) -> str:
    values = ", ".join(["{} = {}".format(key, convert(updates[key]))
                        for key in sorted(updates.keys())])
    return "update {} set {} where id = {}".format(table, values, id)


def delete_query(table: str, *where: str) -> str:
    basic = "delete from {}".format(table)
    if not where:
        return basic
    else:
        return "{} where {}".format(basic, " and ".join(where))
