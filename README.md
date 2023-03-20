# 808 Spectate Coding Challenge

Implement a system which manages multiple sports, events, markets, and selections.



## retrieving the code

Execute the following to clone the repository:

```

> git clone git@github.com:cowboysmall-scratch/spectate-coding-challenge.git 
> cd spectate-coding-challenge 

```


## running the code

Execute the following from the root directory to run the application:

```

> python -m query_tool 

```


## running the tests

Execute the following from the root directory to run the tests:

```

> python -m unittest discover -s tests

```



## example filters

### find sports where more than one associated active events 

```

(select count(*) from event e where e.active = 1 and e.sport_id = s.id) > 1

```

### find sports where name satisfies regex

```

name like '%01%'

```
