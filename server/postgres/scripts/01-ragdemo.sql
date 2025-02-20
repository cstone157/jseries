create database ragdemo;
\c ragdemo

create extension vector;
create table items (id serial primary key, doc text, embedding vector(4096));

