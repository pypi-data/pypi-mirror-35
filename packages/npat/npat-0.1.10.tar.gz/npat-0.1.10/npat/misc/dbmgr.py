import os,sqlite3
import npat

DECAY_connection = None
ZIEGLER_connection = None

def get_decay_connection():
	global DECAY_connection
	if DECAY_connection is None:
		DECAY_connection = sqlite3.connect(os.path.join(str(os.path.dirname(npat.__file__)),'data/decay.db'))
	return DECAY_connection

def get_decay_cursor():
	conn = get_decay_connection()
	return conn.cursor()


def get_ziegler_connection():
	global ZIEGLER_connection
	if ZIEGLER_connection is None:
		ZIEGLER_connection = sqlite3.connect(os.path.join(str(os.path.dirname(npat.__file__)),'data/ziegler.db'))
	return ZIEGLER_connection

def get_ziegler_cursor():
	conn = get_ziegler_connection()
	return conn.cursor()

