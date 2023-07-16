import datetime

import pymysql

schema_name = 'roibelodbb' #"sql8618285"


def get_db_connection():
    #conn = pymysql.connect(host='sql8.freemysqlhosting.net', port=3306, user='sql8618285', passwd='LN5hipkRmA',
    #                       db=schema_name)
    conn = pymysql.connect(host='db', port=3306, user='roibelo', passwd='rrdkite1',
                           database='roibelodb')
    conn.autocommit(True)
    return conn


def create_table():
    # Establishing a connection to DB
    conn = get_db_connection()
    # Getting a cursor from Database
    cursor = conn.cursor()
    # Inserting data into table
    statementToExecute = "CREATE TABLE `" + schema_name + "`.`users`(`user_id` INT NOT NULL,`user_name` VARCHAR(50) NOT NULL," \
                                                          "creation_date VARCHAR(50) NOT NULL, PRIMARY KEY (`user_id`));"
    cursor.execute(statementToExecute)
    cursor.close()
    conn.close()


#The function get user id and returns is user name
def get_user_name(user_id):
    user_name = ""
    try:
        # Establishing a connection to DB
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT u.user_name FROM roibelodb.users as u where u.user_id=" + user_id + ";")
        for row in cursor:
            user_name = row

    except Exception as ex:
        raise Exception("getUserName function error: " + ex.__str__())
    finally:
        cursor.close()
        conn.close()

    return user_name


#The function create user in table users, it accept user_id and user_name
def insert_user(user_id, user_name):
    try:
        # Establishing a connection to DB
        conn = get_db_connection()
        # Getting a cursor from Database
        cursor = conn.cursor()
        # Inserting data into table
        cursor.execute(
              "INSERT into sql8618285.users (user_id, user_name, creation_date) VALUES (" + user_id + ", '" + user_name +
              "','" + str(datetime.datetime.now()) + "')")
    except Exception as ex:
        raise Exception("insertUser function error: " + ex.__str__())
    finally:
        cursor.close()
        conn.close()

    return user_name


#The function update user name by its user id
def update_user(user_id, user_name):
    try:
        # Establishing a connection to DB
        conn = get_db_connection()
        # Getting a cursor from Database
        cursor = conn.cursor()
        # Inserting data into table
        cursor.execute("update sql8618285.users set user_name = '" + user_name + "' where user_id = " + user_id)

    except Exception as ex:
        raise Exception("updateUser function error: " + ex.__str__())
    finally:
        cursor.close()
        conn.close()

    return user_name


#The function delete user by its user id
def delete_user(user_id):
    try:
        # Establishing a connection to DB
        conn = get_db_connection()
        # Getting a cursor from Database
        cursor = conn.cursor()
        # Inserting data into table
        cursor.execute("delete from sql8618285.users where user_id = " + user_id)

    except Exception as ex:
        raise Exception("deleteUser function error: " + ex.__str__())
    finally:
        cursor.close()
        conn.close()

    return user_id
