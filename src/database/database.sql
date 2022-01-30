drop database if exists Shop;
create database Shop;
use Shop;

create table products (product_id int primary key not null, company text null, phone text not null, price int not null, config text not null);

create table user ( user_id int primary key not null, pwd tinytext not null, name tinytext not null, city tinytext not null, phone_number bigint not null, item_bought int null);

create table employee ( emp_code int primary key not null, name tinytext not null, city tinytext not null, phone_number bigint not null, designation tinytext not null);

insert into products (product_id, company, phone, price, config) values (101, Samsung, GalaxyM32, 21000, 4/64);

insert into employee (emp_code, name, city, phone_number, designation) values (00001, suyash, navi mumbai, 6767676767, admin);

insert into user (user_id, pwd, name, city, phone_number, item_bought) values (12345, password, default, whatever, 0000000000, null)