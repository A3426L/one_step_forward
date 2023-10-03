import psycopg2
import datetime
def connect_database():
    connection = psycopg2.connect(
    host="localhost",
    database="toilet",
    user="lego",
    password="lego"
    )
    return connection
def create_schema(connection,schema_name):
    create_schema_query = "CREATE SCHEMA IF NOT EXISTS {}".format(schema_name)
    print(create_schema_query)
    cursor = connection.cursor()
    cursor.execute(create_schema_query)
    connection.commit()

def create_table(connection,table_name):
    query = '''
          CREATE TABLE {}(
			id		SERIAL,
			name	varchar(255),
            date    date,
            time    time,
            PRIMARY KEY(id)
          );
          '''.format(table_name)
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

def insert_table(connection,table_name,name,date,time):
    insert_query = "INSERT INTO {}( name,date,time)VALUES (%s, %s, %s)".format(table_name)
    print(insert_query)
    print(date)
    print(time)
    cursor = connection.cursor()
    cursor.execute(insert_query, (name,date, time,))
    connection.commit()

def read_table(connection,table_name,element,conditional):
    read_query = "SELECT {} FROM {} {}".format(element,table_name,conditional)
    print(read_query)
    cursor = connection.cursor()
    cursor.execute(read_query)
    result = cursor.fetchall()
    return result

def current_time():
	dt_now = datetime.datetime.now()
	d_now = dt_now.strftime('%Y-%m-%d')
	t_now = dt_now.strftime('%H:%M')
	return d_now,t_now


connection = connect_database()
#create_table(connection,"toilet0")
d_now ,t_now = current_time()
#insert_table(connection,"toilet0","A",d_now,t_now)

result = read_table(connection,"toilet0","*","WHERE time ='01:19'")
print(result)



connection.close()
