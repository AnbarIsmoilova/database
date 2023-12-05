import sqlite3
a=sqlite3.connect('flowers.db')
b=a.cursor()
b.execute('''
CREATE TABLE IF NOT EXISTS flowers(
    name TEXT
    color TEXT
    cost INTEGER
)''')

b.execute('''
CREATE TABLE IF NOT EXISTS rose(
    color TEXT
    cost INTEGER
)''')

b.execute('''
CREATE TABLE IF NOT EXISTS tulip(
    color TEXT
    cost integer
)''')

b.execute('''
CREATE TABLE IF NOT EXISTS chamomile(
    color TEXT
    cost INTEGER
)''')

b.execute('''
CREATE TABLE IF NOT EXISTS iris(
    color TEXT
    cost INTEGER  
)''')

b.execute('''
CREATE TABLE IF NOT EXISTS bluebell(
    color TEXT
    cost INTEGER    
)
''')


c=sqlite3.connect('people.db')
d=c.cursor()
d.execute('''
CREATE TABLE IF NOT EXISTS people(
    job TEXT
    name TEXT
    age INTEGER
)''')

d.execute('''
CREATE TABLE IF NOT EXISTS student(
    name TEXT
    age INTEGER
)''')

d.execute('''
CREATE TABLE IF NOT EXISTS doctor(
    name TEXT
    age INTEGER
)''')

d.execute('''
CREATE TABLE IF NOT EXISTS teacher(
    name TEXT
    age INTEGER
)''')

e=sqlite3.connect('studens.db')
f=e.cursor()
f.execute('''
CREATE TABLE IF NOT EXISTS madina(
    weight TEXT
    age INTEGER
)''')

f.execute('''
CREATE TABLE IF NOT EXISTS anna(
    weight TEXT
    age INTEGER
)''')

f.execute('''
CREATE TABLE IF NOT EXISTS george(
    weight TEXT
    age INTEGER    
)''')

g=sqlite3.connect('cars.db')
h=g.cursor()
h.execute('''
CREATE TABLE IF NOT EXISTS bmw(
    color TEXT
    cost INTEGER
)''')

h.execute('''
CREATE TABLE IF NOT EXISTS bugatti(
    color TEXT
    cost INTEGER
)''')

h.execute('''
CREATE TABLE IF NOT EXISTS rolls_royse(
    color TEXT
    cost INTEGER
)''')


m=sqlite3.connect('clothes.db')
n=m.cursor()
n.execute('''
CREATE TABLE IF NOT EXISTS hat(
    color TEXT
    size TEXT
)''')

n.execute('''
CREATE TABLE IF NOT EXISTS dress(
    color TEXT
    size TEXT
)''')

n.execute('''
CREATE TABLE IF NOT EXISTS jacket(
    color TEXT
    size TEXT
)''')