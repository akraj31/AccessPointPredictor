import os
import time
import datetime

cur = ""

def init_logs():
	global cur
	cur = ""

def get_current_time():
	return str(datetime.datetime.now())

def create_log_message(msg):
	global cur
	return cur + get_current_time() + " " + msg + "\n"

def dump_log_to_file():
	with open(log_file, "wb") as f:
        pickle.dump(lp, f)
    