from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import records


def connetdb(connetstr):
    engine = create_engine(connetstr, encoding='utf-8')
    DB_Session = sessionmaker(bind=engine)
    session = DB_Session()
    return session


def onlyquery(conn, sql):
    db = records.Database(conn)
    rows = db.query(sql)  # or db.query_file('sqls/active-users.sql')
    return rows


def execsql(conn, sql):
    session = connetdb(conn)
    tmpresult = session.execute(sql)
    tmplist = []
    try:
        [tmplist.append(x) for x in tmpresult]
    except Exception as e:
        print(e)
    session.commit()
    return tmplist
