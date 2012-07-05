DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
	id integer primary key autoincrement,
	task string not null,
	startdate datetime,
enddate datetime not null,
priority integer not null
);