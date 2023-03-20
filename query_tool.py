import sys
import os

from spectate import database
from spectate import crud

def root_options():

    os.system('clear')

    print("\n\n")
    print("\tOptions:")
    print("\t[c]   Create Entity")
    print("\t[r] Retrieve Entity")
    print("\t[u]   Update Entity")
    print("\t[d]   Delete Entity")
    print("\t[q] Quit")
    print("\n")

    return input("\tWhat would you like to do? ")



def sub_options():

    os.system('clear')

    print("\n\n")
    print("\tOptions:")
    print("\t[b] Back")
    print("\n")

    return input("\tEnter table name: ")



def create():

    option = sub_options()
    while option not in ['b', '']:
        values = {}
        cols = database.columns(option)
        for c in cols:
            if c != 'id':
                values[c] = input("\t{}: ".format(c))

        database.execute(crud.insert_query(option, **values))

        print("\n")
        input("\tpress any key to continue...")
        option = sub_options()

    return option



def retrieve():

    option = sub_options()
    while option not in ['b', '']:
        where = []
        w = input("\tEnter where clause: ")
        while w != '':
            where.append(w)
            w = input("\tEnter where clause: ")

        rows = database.retrieve(crud.read_query(option, *where))
        for row in rows:
            print("\t{}".format(row))

        print("\n")
        input("\tpress any key to continue...")
        option = sub_options()

    return option



def update():

    option = sub_options()
    while option not in ['b', '']:
        values = {}
        cols = database.columns(option)
        for c in cols:
            value = input("\t{}: ".format(c))
            if value != '':
                values[c] = value

        database.execute(crud.update_query(option, **values))

        print("\n")
        input("\tpress any key to continue...")
        option = sub_options()

    return option



def delete():

    option = sub_options()
    while option not in ['b', '']:
        where = []
        w = input("\tEnter where clause: ")
        while w != '':
            where.append(w)
            w = input("\tEnter where clause: ")

        rows = database.execute(crud.delete_query(option, *where))

        print("\n")
        input("\tpress any key to continue...")
        option = sub_options()

    return option





def main(argv):
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
