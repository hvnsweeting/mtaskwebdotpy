import web
import datetime

#DB
db = web.database(dbn='sqlite', db='/tmp/mtask2.db')

def get_tasks():
	return db.select('tasks', order='enddate, priority DESC')

def new_task(task, startdate, enddate, priority):
	db.insert('tasks', task=task, startdate=startdate, enddate=enddate, priority=priority)
