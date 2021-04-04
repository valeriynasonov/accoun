from sqlalchemy import create_engine
db = 'postgres://' + name_user + ':' + password_db + '@localhost:5432/' + name_db
engine = create_engine(db)
connection = engine.connect()
connection.execute("""INSERT INTO %s (%s, %s) VALUES (%s, %s) """, (name_db, column1, column2, value_column1, value_column2)