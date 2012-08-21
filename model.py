import web
import datetime
import psycopg2
import dj_database_url
import os

#postgres://mgzdqjxltjjfbs:TEoACC6-iEkBi8KBudnK3MAI2y@ec2-107-22-163-230.compute-1.amazonaws.com:5432/d8g05oiv7f32o2
default=os.environ.get('DATABASE_URL')


db = web.database('postgres://mgzdqjxltjjfbs:TEoACC6-iEkBi8KBudnK3MAI2y@ec2-107-22-163-230.compute-1.amazonaws.com:5432/d8g05oiv7f32o2')

def get_tasks():
	return db.select('tasks', order='enddate, priority DESC')

def new_task(task, startdate, enddate, priority):
	db.insert('tasks', task=task, startdate=startdate, enddate=enddate, priority=priority)
