#sunlite


# Sunlite Simple Database System

## simple, fast, local, userfriendly


### what is sunlite ?

#### Ans: Sunlite is a module for simple data management. 

* How to use
   * Connect to memory.
     >>
    * connect to a database.
     >>
     * Create a new header .
      >>
      * add data , or pull data
       >>
       * enjoy ^~^

## Connecting

Sunlite lets you connect as you want.

```python
from sunlite.db import connect

db = connect() #for memory
db = connect("my_db") #for connecting with "my_db" , it will be auto generated if doesnt exists.
db = connect("my_db",logs=False)  # for connecting to "my_db" but say no to logs

```

## Generating new header
headers are like boxes which contains your datas , don't forget to make one before pushing or pulling data

```python

db = connect("my_db")

db.new("websites")  #here , we made a header named websites.

```

## Pushing   data to headers

by pushing , we add data in headers to contain . you can push any data .

```python 

db = connect("my_db")

db.new("websites")

name = "google"
data = "http://google.com"

db.push(name,data) #here , we are pushing http://google.com with the name google in websites header
```

## Pullling data from headers

you can pull all data of header or an invidual data

```python

db = connect("my_db",logs=False)

db.new("websites")

name = "google"
data = "http://google.com"

db.push(name,data)

a = db.pull("websites")  #it will pull all data in website header as a dictionary.

a = db.pull("google")  #it will only pull the data of google no matter where it is in which header .
```
don't use same names for two datas as it will remove 2nd one .

## Get a header as you want. This time duplicate names are accepted.
### unlike pull function , this function doesn't update duplicate datas as sends as they are . 
### this is useful in maintaining a large set of same data.

example

```python

db.connect("students",logs=False)

db.new("Allan")

db.push("maths",50)
db.push("english",70)
db.push("science",40)


#now for akmal
db.new("Akmal")

db.push("maths",45)
db.push("english",60)
db.push("science",70)

db.get("Akmal")  #for getting akmal marks
db.get("allan") #for getting allan's marks


```

## Beauty print .

You can beauty print all data's in all headers .

```python

db = connect("my_db",logs=False)

db.new("websites")

name = "google"
data = "http://google.com"

db.push(name,data)

db.beauty()  #this prints all data nicely

```
# Get all headers

```python

db = connect("my_db",logs=False)

db.headers()

```

# Example with a user info system with sunlite 

```python

db = connect("my_db",logs=False)

db.new("users")

name = "Axel"
data = ["age":13 , "nation": "USA"]

db.push(name,data)

name = "Jack"
data = ["age":15, "nation": "England"]
db.push(name,data)

db.beauty()
```



