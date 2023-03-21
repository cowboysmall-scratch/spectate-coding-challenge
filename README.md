# 808 Spectate Coding Challenge

Implement a system which manages sports, events, markets, and selections.


## implementation notes

- only standard Python 3.10+ code was used - no libraries or frameworks are required to be installed in order to run this code
- persistence was implemented with sqlite - which is lightweight and requires no external dependencies
- I included some seed data - for convenience
- I assumed a typo in the challenge description document - i.e. that a market should reference an event (as per the system requirements section)
- I made use of triggers to implement the active status updates
- as many filters can be added as required - each filter should be a WHERE clause - some examples have been given below 


## retrieving the code

Execute the following to clone the repository:

```

> git clone git@github.com:cowboysmall-scratch/spectate-coding-challenge.git 
> cd spectate-coding-challenge 

```


## running the tests

Execute the following from the root directory to run the tests:

```

> python -m unittest discover -s tests

```




## running the code

Execute the following from the root directory to run the application:

```

> python -m query_tool 

```




## example usage


### root screen

```

    Options:
    [c]   Create Entity
    [r] Retrieve Entity
    [u]   Update Entity
    [d]   Delete Entity
    [q] Quit


    What would you like to do? 


```




### create sport

```

    Options:
    [b] Back


    Enter table name: sport
    name: name
    display_name: Name
    slug: name
    sport_order: 3
    active: True


    press any key to continue...


    ...


    Options:
    [b] Back


    Enter table name: sport
    Enter where clause: id = 4
    Enter where clause: 
    {'id': 4, 'name': 'name', 'display_name': 'Name', 'slug': 'name', 'sport_order': 3, 'active': 'True'}


    press any key to continue...




```



### find all sports


```

    Options:
    [b] Back


    Enter table name: sport
    Enter where clause: 
    {'id': 1, 'name': 'SPORT_01_NAME', 'display_name': 'SPORT_01_DISPLAY_NAME', 'slug': 'SPORT_01_SLUG', 'sport_order': 1, 'active': 1}
    {'id': 2, 'name': 'SPORT_02_NAME', 'display_name': 'SPORT_02_DISPLAY_NAME', 'slug': 'SPORT_02_SLUG', 'sport_order': 2, 'active': 1}
    {'id': 3, 'name': 'SPORT_03_NAME', 'display_name': 'SPORT_03_DISPLAY_NAME', 'slug': 'SPORT_03_SLUG', 'sport_order': 3, 'active': 0}


    press any key to continue...


```


### find sports where more than one associated events are active 

```

    Options:
    [b] Back


    Enter table name: sport
    Enter where clause: (select count(*) from event e where e.active = 1 and e.sport_id = s.id) > 1
    Enter where clause: 
    {'id': 1, 'name': 'SPORT_01_NAME', 'display_name': 'SPORT_01_DISPLAY_NAME', 'slug': 'SPORT_01_SLUG', 'sport_order': 1, 'active': 1}


    press any key to continue...


```

### find sports where name satisfies regex

```

    Options:
    [b] Back


    Enter table name: sport
    Enter where clause: name like '%02%'        
    Enter where clause: 
    {'id': 2, 'name': 'SPORT_02_NAME', 'display_name': 'SPORT_02_DISPLAY_NAME', 'slug': 'SPORT_02_SLUG', 'sport_order': 2, 'active': 1}


    press any key to continue...


```


### update sport


```

    Options:
    [b] Back


    Enter table name: sport
    id: 4
    name: 
    display_name: 
    slug: some_slug
    sport_order: 
    active: 


    press any key to continue...


    ...


    Options:
    [b] Back


    Enter table name: sport
    Enter where clause: id = 4
    Enter where clause: 
    {'id': 4, 'name': 'name', 'display_name': 'Name', 'slug': 'some_slug', 'sport_order': 3, 'active': 'True'}


    press any key to continue...



```




### delete sport that has associated events

```

    Options:
    [b] Back


    Enter table name: sport
    Enter where clause: id = 1
    Enter where clause: 


    Referential Integrity Error!


    press any key to continue...



```



