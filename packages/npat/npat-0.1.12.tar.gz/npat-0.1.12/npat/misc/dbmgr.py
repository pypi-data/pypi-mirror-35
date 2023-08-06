import os,sqlite3
import npat

path = lambda db: os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)),'..','data',db))

print path('decay.db')

DECAY_connection = None
ZIEGLER_connection = None
ENDF_connection = None
TENDL_connection = None
TENDL_rpn_connection = None
TENDL_rpp_connection = None
TENDL_rpd_connection = None

def get_connection(db='decay'):
	if db.lower().replace('.db','') in ['decay']:
		global DECAY_connection
		if DECAY_connection is None:
			DECAY_connection = sqlite3.connect(path('decay.db'))
		return DECAY_connection
	elif db.lower().replace('.db','') in ['ziegler']:
		global ZIEGLER_connection
		if ZIEGLER_connection is None:
			ZIEGLER_connection = sqlite3.connect(paht('ziegler.db'))
		return ZIEGLER_connection
	elif db.lower().replace('.db','') in ['endf']:
		global ENDF_connection
		if ENDF_connection is None:
			ENDF_connection = sqlite3.connect(path('endf.db'))
		return ENDF_connection
	elif db.lower().replace('.db','') in ['tendl']:
		global TENDL_connection
		if TENDL_connection is None:
			TENDL_connection = sqlite3.connect(path('tendl.db'))
		return TENDL_connection
	elif db.lower().replace('.db','') in ['tendl_n_rp','tendl_nrp','tendl_n','nrp','rpn']:
		global TENDL_rpn_connection
		if TENDL_rpn_connection is None:
			TENDL_rpn_connection = sqlite3.connect(path('tendl_n_rp.db'))
		return TENDL_rpn_connection
	elif db.lower().replace('.db','') in ['tendl_p_rp','tendl_prp','tendl_p','prp','rpp']:
		global TENDL_rpp_connection
		if TENDL_rpp_connection is None:
			TENDL_rpp_connection = sqlite3.connect(path('tendl_n_rp.db'))
		return TENDL_rpp_connection
	elif db.lower().replace('.db','') in ['tendl_d_rp','tendl_drp','tendl_d','drp','rpd']:
		global TENDL_rpd_connection
		if TENDL_rpd_connection is None:
			TENDL_rpd_connection = sqlite3.connect(path('tendl_n_rp.db'))
		return TENDL_rpd_connection

	


def get_cursor(db='decay'):
	conn = get_connection(db)
	return conn.cursor()
