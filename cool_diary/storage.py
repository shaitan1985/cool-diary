import os.path as Path
import sqlite3


def get_path_resource(path):
    return Path.join(Path.dirname(__file__),'resources', path)

def get_sql_select_all():
    query = """
        SELECT
            id, event, begin_date, end_date, active
        FROM
            event_keeper
    """
    return query


def get_sql_select_by_status():
    query = get_sql_select_all() + ' WHERE active=?'
    return query


def get_sql_insert():
    query = """
        INSERT INTO
            event_keeper (event, begin_date, end_date)
        VALUES
            (?, ?, ?)
    """
    return query


def get_sql_update():
    query = """
        UPDATE event_keeper SET event=?, begin_date=?, end_date=?, active=?
        WHERE id=?
    """
    return query


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
        creation_script = get_path_resource('schema.sql')
    with conn, open(creation_script) as f:
        conn.executescript(f.read())


def add_new_event(conn, data): # data is tuple
    with conn:
        cursore = conn.execute(get_sql_insert(), data)


def edit_event(conn, data):
    # Получаем задачу по ID и редактируем в соответствии с флагом
    with conn:
        cursore = conn.execute(get_sql_update(), data)


def get_events_by_status(conn, status):
    query = get_sql_select_by_status()
    if not status:
        query += ' ORDERD BY id DESC'
    with conn:
        cursore = conn.execute(get_sql_select_by_status(), (status,))
    return cursore.fetchall()



