DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
	id integer primary key autoincrement,
	task string not null,
	startdate datetime,
enddate datetime not null,
priority integer not null
);

CREATE TABLE todo (
  id serial primary key,
    title text,
  created timestamp default now(),
    done boolean default 'f'    );

CREATE TABLE tasks (
    id serial primary key,
    task text,
    startdate timestamp default now(),
    endate timestamp,
    priority integer,
);
