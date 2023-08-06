import sqlite3

DECAY_connection = None
ZIEGLER_connection = None

def get_decay_connection():
	global DECAY_connection
	if DECAY_connection is None:
		DECAY_connection = sqlite.connect('decay.db')
	return DECAY_connection

def get_decay_cursor():
	conn = get_decay_connection()
	return conn.cursor()

def get_decay_connection_and_cursor():
	return get_decay_connection(),get_decay_cursor()


def get_ziegler_connection():
	global ZIEGLER_connection
	if ZIEGLER_connection is None:
		ZIEGLER_connection = sqlite.connect('ziegler.db')
	return ZIEGLER_connection

def get_ziegler_cursor():
	conn = get_ziegler_connection()
	return conn.cursor()

def get_ziegler_connection_and_cursor():
	return get_ziegler_connection(),get_ziegler_cursor()


