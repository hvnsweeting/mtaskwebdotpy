DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
    id integer primary key,
    task text,
    startdate date,
    enddate date,
    priority integer
);
