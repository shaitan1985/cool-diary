import os.path as Path
import sqlite3

def connect(db_name=None):
    """Create BD connection"""
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    # here will be the magic

    return conn



def initialize(conn, creation_script=None):
    """create db and tables"""
    if creation_script is None:
        creation_script = Path.join(Path.dirname(__file__),'resources', 'schema.sql')

    with conn, open(creation_script) as f:
        conn.executescript(f.read())
