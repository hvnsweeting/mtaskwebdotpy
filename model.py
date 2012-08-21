import web
import datetime
import psycopg2

#DB
db = web.database(dbn='postgres', db='mtask', )

def get_tasks():
	return db.select('tasks', order='enddate, priority DESC')

def new_task(task, startdate, enddate, priority):
	db.insert('tasks', task=task, startdate=startdate, enddate=enddate, priority=priority)
