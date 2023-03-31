create database sonavel;

use sonavel;

create table class(
class_code int primary key,
class_name varchar(255) not null
);

create table clear_records(
	record_idx int auto_increment primary key,
    user1_class int not null,
    user1_level float not null,
    user2_class int not null,
    user2_level float not null,
    user3_class int not null,
    user3_level float not null,
    user4_class int not null,
    user4_level float not null,
    clear_time int not null
);

select * from clear_records;

select * from class;