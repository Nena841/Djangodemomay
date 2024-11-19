import sqlite3

# Sqlite Db connection
con = sqlite3.connect("company.db")
# it returns the reference to the company.db file created inside the sqlite db
# Create table Employees
# sql_command = """create table employees(eid int primary key,
#                                      name varchar(20),
#                                      age int,
#                                      salary int,
#                                      gender varchar(2),
#                                      place varchar(20))"""
# con.execute(sql_command)
# # create table inside database
# print("Database Table created")

# Insertion
# con.execute("insert into employees values(100,'Arun',27,30000,'m','ekm')")
# con.execute("insert into employees values(101,'Amal',28,35000,'m','tvm')")
# con.execute("insert into employees values(102,'Anu',25,30000,'f','thr')")
# con.execute("insert into employees values(103,'Kiran',26,40000,'m','pkd')")
# con.execute("insert into employees values(104,'Anju',23,35000,'f','ekm')")
# con.commit()
# print("Inserted records successfully")

# Read/Retrieval
# * means all attributes without where condition -all rows
# k = con.execute('select * from employees')
# print(k.fetchall())

# specific attribute
# k = con.execute('select name from employees')
# print(k.fetchall())

# specific record with all attributes
# k = con.execute('select * from employees where eid=103')
# print(k.fetchall())

# specific attribute and record with id=100
# k = con.execute('select name,salary from employees where eid=100')
# print(k.fetchall())
# for i in k:
#     print(i)

# starting with letter 'a'
# k = con.execute('select * from employees where name like "a%"')
# print(k.fetchall())

# 3 letter name starting with 'an'
# k = con.execute('select * from employees where name like "an_"')
# print(k.fetchall())

# name ending with 'u'
# k = con.execute('select * from employees where name like "%u"')
# print(k.fetchall())

# 3 letter name ending with 'u'
# k = con.execute('select * from employees where name like "__u"')
# print(k.fetchall())

# between 25000 and 40000(including it)
# k = con.execute('select * from employees where salary between 25000 and 30000')
# print(k.fetchall())

# records having 25000 and 40000
# k = con.execute('select * from employees where salary in (25000,40000)')
# print(k.fetchall())

# and-->both condition must be true
# k = con.execute('select * from employees where name="Arun" and place="ekm" ')
# print(k.fetchall())

# or-->records satisfy any one of the condition
# k = con.execute('select * from employees where name="Arun" or place="ekm" ')
# print(k.fetchall())

# not-->records having place value other than 'ekm'
# k = con.execute('select * from employees where not(place="ekm")')
# print(k.fetchall())

# order by
# k = con.execute('select * from employees order by name')
# print(k.fetchall())
# k = con.execute('select * from employees  order by salary desc')
# print(k.fetchall())

# # distinct
# k = con.execute('select distinct(place) from employees order by salary')
# print(k.fetchall())
# con.close()

# % -->0 or more character
# _ -->Exactly one character

# import sqlite3
#
# con = sqlite3.connect("nobel.db")
# sql_command = """create table nobel_prize(year int primary key,
#                                          subject varchar(20),
#                                          winner varchar(20)
#                                          )"""
# con.execute(sql_command)
# print("Table created successfully")
# con.execute("insert into nobel_prize values(1970,'Physics','Hannes Sweden'")
# con.execute("insert into nobel_prize values(1971,'Literature','Mary johns'")
# con.execute("insert into nobel_prize values(1978,'Physic','Mary johns'")
# con.execute("insert into nobel_prize values(1980,'Chemistry','Louis'")
# con.execute("insert into nobel_prize values(197,'Literature','Mary johns'")
# con.execute("insert into nobel_prize values(1971,'Economics','Mary johns'")
# con.commit()
# print("Records inserted successfully")
# k = con.execute('select * from nobel_prize where year=1970')
# print(k.fetchall())
# k = con.execute('select winner from nobel_prize where subject="Literature" and year=1971')
# print(k.fetchall())
# k = con.execute('select winner from nobel_prize where subject="Physics" and year>=1978')
# print(k.fetchall())
# k = con.execute('select * from nobel_prize where subject="Chemistry" and year between 1970 and 1980')
# print(k.fetchall())
# k = con.execute('select * from nobel_prize where winner like "Louis%"')
# print(k.fetchall())
# k = con.execute('select * from nobel_prize where not(subject in "Physiology,Economics")')
# print(k.fetchall())
# con.close()

# Update command
# updating employees record whose id=102
# k = con.execute('select * from employees')
# print('Before update', k.fetchall())
# con.execute('update employees set name="Karthika",gender="f" where eid=102')
# con.commit()
# k = con.execute('select * from employees')
# print('After update', k.fetchall())

# Delete command
# k = con.execute('select * from employees')
# print('Before delete', k.fetchall())
# con.execute('delete from employees where eid=101')
# con.commit()
# k = con.execute('select * from employees')
# print('After delete', k.fetchall())

# Alter command
# k=con.execute('select * from employees')
# print('Before alter',k.fetchall())
# con.execute('alter table employees add email varchar(20)')
# k=con.execute('select * from employees')
# print('After alter',k.fetchall())

# insert new record
# con.execute("insert into employees values(106,'vimal',29,50000,'m','Klm','v@gmail.com')")
# con.commit()
# k = con.execute('select * from employees')
# print("After insertion", k.fetchall())

# Drop column
# con.execute('alter table employees drop column email')

# Rename table
# con.execute('alter table employee rename to employees')
# con.execute('alter table employees rename column eid to empid')

# to delete table
# drop table table_name
# drop database dbname
# create database dbname

# aggregate functions
# k = con.execute('select * from employees')
# print(k.fetchall())
# k = con.execute('select sum(salary),avg(age),count(*),min(salary),max(age) from employees')
# print(k.fetchall())

# group by
# k=con.execute('select gender,count(*) from employees group by gender')
# print(k.fetchall())
# k = con.execute('select place,count(*) from employees group by place')
# print(k.fetchall())
# k = con.execute('select gender,sum(salary) from employees group by gender')
# print(k.fetchall())
# k = con.execute('select gender,sum(salary) from employees group by gender having gender=="m" ')
# print(k.fetchall())
# k = con.execute('select gender,sum(salary) from employees group by gender having sum(salary)<70000 ')
# print(k.fetchall())
# k = con.execute('select place,sum(salary) from employees group by place having place=="ekm" ')
# print(k.fetchall())

# import sqlite3
#
# con = sqlite3.connect("shop.db")
# con.execute("""create table customer(customer_id int primary key,
#                                       name varchar(20),
#                                       place varchar(20)
#                                       )""")
# print('Database created')
# con.execute('insert into customer values(1,"John","Ekm")')
# con.execute('insert into customer values(2,"Smith","Tvm")')
# con.execute('insert into customer values(3,"Mike","Klm")')
# con.commit()
# print("Records inserted successfully")
# k = con.execute('select * from customer')
# print(k.fetchall())
#
# con.execute("""create table orders(order_id int primary key,
#                                     c_id int,product varchar(20),
#                                     price int,foreign key(c_id)references customer(customer_id))
#                                     """)
# print('Table created successfully')


# con.execute('insert into orders values(101,1,"Laptop",37000)')
# con.execute('insert into orders values(102,3,"Watch",10000)')
# con.execute('insert into orders values(103,1,"Mobile",25000)')
# con.commit()
# print('Records inserted successfully')

# print("inner join")
# # k=con.execute('select * from customer  ')
# k = con.execute("""select customer_id,name,order_id,product,price from customer
# inner join orders on customer.customer_id=order_id""")
# print(k.fetchall())
# print('left outer join')
# k = con.execute("""select customer_id,name,order_id,product,price from customer
# outer join orders on customer.customer_id=order_id""")
# print(k.fetchall())

import sqlite3

con = sqlite3.connect("db1.db")
# con.execute('create table person(id int primary key,name varchar(20),age int)')
# print('Table created')
# i = int(input("Enter the id:"))
# n = input("Enter the name:")
# a = int(input("Enter the age:"))
# con.execute("insert into person values(?,?,?)", (i, n, a))
# con.commit()
# print('Inserted records successfully')
