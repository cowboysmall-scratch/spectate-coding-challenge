import sys
import os

from spectate import database
from spectate import crud


def root_options() -> str:

    os.system('clear')

    print("\n\n")
    print("\tOptions:")
    print("\t[c] Create")
    print("\t[r] Retrieve")
    print("\t[u] Update")
    print("\t[d] Delete")
    print("\t[q] Quit")
    print("\n")

    return input("\tEnter option: ")


def sub_options() -> str:

    os.system('clear')

    print("\n\n")
    print("\tOptions:")
    print("\t[b] Back")
    print("\n")

    return input("\tEnter table name: ")


def where_clauses() -> list:

    where = []

    w = input("\tEnter where clause: ")
    while w != '':
        where.append(w)
        w = input("\tEnter where clause: ")

    return where


def wait() -> None:

    print("\n")
    input("\tPress any key to continue...")


def print_rows(rows: list) -> None:

    print("\n".join(["\t{}".format(row) for row in rows]))


def create() -> str:

    option = sub_options()
    while option not in ['b', '']:

        values = {}
        for column in database.columns(option):
            if column != 'id':
                values[column] = input("\t{}: ".format(column))

        database.execute(crud.create_query(option, **values))

        wait()
        option = sub_options()

    return option


def retrieve() -> str:

    option = sub_options()
    while option not in ['b', '']:

        print_rows(database.retrieve(
            crud.retrieve_query(option, *where_clauses())))

        wait()
        option = sub_options()

    return option


def update() -> str:

    option = sub_options()
    while option not in ['b', '']:

        values = {}
        for column in database.columns(option):
            value = input("\t{}: ".format(column))
            if value != '':
                values[column] = value

        database.execute(crud.update_query(option, **values))

        wait()
        option = sub_options()

    return option


def delete() -> str:

    option = sub_options()
    while option not in ['b', '']:

        database.execute(crud.delete_query(option, *where_clauses()))

        wait()
        option = sub_options()

    return option


def main(argv: list) -> None:

    database.init_ddl()
    database.init_dml()

    option = root_options()
    while option not in ['q', '']:
        match option:
            case 'c':
                o = create()
                while o not in ['b', '']:
                    o = create()
            case 'r':
                o = retrieve()
                while o not in ['b', '']:
                    o = retrieve()
            case 'u':
                o = update()
                while o not in ['b', '']:
                    o = update()
            case 'd':
                o = delete()
                while o not in ['b', '']:
                    o = delete()

        option = root_options()

    os.system('clear')


if __name__ == "__main__":
    main(sys.argv[1:])
