
def insert_query(table, **insert):
    keys = sorted(insert.keys())
    cols = ", ".join(keys)
    vals = ", ".join(convert(insert[key]) for key in keys)
    return "insert into {} ({}) values ({})".format(table, cols, vals)


def read_query(table, *where):
    basic = "select * from {} {}".format(table, table[0])
    if not where:
        return basic
    else:
        return "{} where {}".format(basic, " and ".join(where))


def update_query(table, id, **update):
    values = ", ".join(["{} = {}".format(key, convert(update[key])) for key in sorted(update.keys())])
    return "update {} set {} where id = {}".format(table, values, id)


def delete_query(table, *where):
    basic = "delete from {}".format(table)
    if not where:
        return basic
    else:
        return "{} where {}".format(basic, " and ".join(where))




def convert(value):
    try:
        float(value)
        return "{}".format(value)
    except:
        return "'{}'".format(value)
