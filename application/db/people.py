def get_employeesfrom (name_db, password_db, name_user, department, name_column1, name_column2, value_column1, value_column2):
    from sqlalchemy import create_engine
    db = 'postgres://' + name_user + ':' + password_db + '@localhost:5432/' + name_db
    engine = create_engine(db)
    connection = engine.connect()
    employees = connection.execute("""SELECT %s FROM %s WHERE %s = %s""", (name_column1, name_db, name_column2, value_column1, department, name_column1, name_column2, value_column2):
    from sqlalchemy import create_engine
    db = 'postgres://' + name_user + ':' + password_db + '@localhost:5432/' + name_db
    engine = create_engine(db)
    connection = engine.connect()
    employees = connection.execute("""SELECT %s FROM %s WHERE %s = %s""", (name_column1, name_db, name_column2, value_column2))
    return employees