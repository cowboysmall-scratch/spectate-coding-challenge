

def convert(value):
    try:
        float(value)
        return "{}".format(value)
    except:
        return "'{}'".format(value)




def create_query(table, **values):
    keys   = sorted(values.keys())
    cols   = ", ".join(keys)
    values = ", ".join(convert(values[key]) for key in keys)
    return "insert into {} ({}) values ({})".format(table, cols, values)


def retrieve_query(table, *where):
    basic = "select * from {} {}".format(table, table[0])
    if not where:
        return basic
    else:
        return "{} where {}".format(basic, " and ".join(where))


def update_query(table, id, **updates):
    values = ", ".join(["{} = {}".format(key, convert(updates[key])) for key in sorted(updates.keys())])
    return "update {} set {} where id = {}".format(table, values, id)


def delete_query(table, *where):
    basic = "delete from {}".format(table)
    if not where:
        return basic
    else:
        return "{} where {}".format(basic, " and ".join(where))

