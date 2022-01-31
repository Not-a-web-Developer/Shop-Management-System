drop database if exists Shop;
create database Shop;
use Shop;

create table products (product_id int primary key not null, company text null, phone text not null, price int not null, config text not null);

create table user ( user_id int primary key not null, pwd tinytext not null, name tinytext not null, city tinytext not null, phone_number bigint not null, item_bought int null);

create table employee ( emp_code int primary key not null,pwd tinytext not null, name tinytext not null, city tinytext not null, phone_number bigint not null, designation tinytext not null);

insert into employee(emp_code,pwd,name,city,phone_number,designation) values(21204,'suyash','navi mumbai',9879876565,'admin');

insert into user(user_id,pwd,name,city,phone_number,item_bought) values(12345,'ash','ashutosh','kharghar',9898656543,NULL);

insert into products(product_id,company,phone,price,config) values(10001,'samsung','Galaxy-M32',30000,'RAM-6GB STORAGE-64GB');

insert into products(product_id,company,phone,price,config) values(10002,'samsung','Galaxy-A42',40000,'RAM-6GB STORAGE-128GB');

insert into products(product_id,company,phone,price,config) values(10002,'samsung','Galaxy-M40',20000,'RAM-4GB STORAGE-64GB');

insert into products(product_id,company,phone,price,config) values(10004,'vivo','vivo Y73',20000,'RAM-6GB STORAGE-64GB');

insert into products(product_id,company,phone,price,config) values(10005,'vivo','vivo X60 Pro',40000,'RAM-8GB STORAGE-256GB');

insert into products(product_id,company,phone,price,config) values(10006,'vivo','vivo V23',30000,'RAM-6GB STORAGE-128GB');

insert into products(product_id,company,phone,price,config) values(10007,'apple','iPhone 13 Pro',60000,'RAM-8GB STORAGE-256GB');

insert into products(product_id,company,phone,price,config) values(10008,'apple','iPhone 8 Plus',70000,'RAM-8GB STORAGE-512GB');

insert into products(product_id,company,phone,price,config) values(10009,'apple','iPhone X',50000,'RAM-6GB STORAGE-128GB');