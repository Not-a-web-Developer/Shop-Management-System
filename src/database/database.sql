drop database if exists EventManagementSystem;
create database Shop;
use EventManagementSystem;

create table products (
    sr_no varchar(10) primary key not null,
    name tinytext not null,
    description text not null,
    event_manager tinytext not null,
    start_date date not null,
    end_date date not null,
    budget int not null,
    location tinytext not null
);

create table user (
    user_id varchar(5) primary key not null,
    name tinytext not null,
    city tinytext not null,
    phone_number bigint not null,
    item_bought int not null
)