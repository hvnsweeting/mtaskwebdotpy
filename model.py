import web
import datetime
import psycopg2

#DB
#postgres://mgzdqjxltjjfbs:TEoACC6-iEkBi8KBudnK3MAI2y@ec2-107-22-163-230.compute-1.amazonaws.com:5432/d8g05oiv7f32o2

db = web.database(dbn='postgres', db='HEROKU_POSTGRESQL_CHARCOAL', user='mgzdqjxltjjfbs:', pw='TEoACC6-iEkBi8KBudnK3MAI2y' )

def get_tasks():
	return db.select('tasks', order='enddate, priority DESC')

def new_task(task, startdate, enddate, priority):
	db.insert('tasks', task=task, startdate=startdate, enddate=enddate, priority=priority)
