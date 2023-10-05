import ir_commuication as ir
import operate_db as db

TABLE_NAME = "toilet0"

connection = db.connect_database()
#db.create_table(connection,TABLE_NAME)
data = ir.IR_Process()
print("start_recvdata")
d_now,t_now = db.current_time()
for num in ir.send_list:
	print(num+":")
	recog = data.recv_func(num)	
	if recog == 0:
		print("retry!")
		data.send_data(num)
		 #delay(1)
		recog2 = data.recv_func(num)
		if recog2 == 0:
			print("unable")
			#db.insert_table(connection,TABLE_NAME,num,d_now,t_now)
		else:
			print(" OK!")
			#db.insert_table(connection,TABLE_NAME,num,d_now,t_now)
	else:
		print("OK")	
		#db.insert_table(connection,TABLE_NAME,num,d_now,t_now)

print("end")

result = db.read_table(connection,TABLE_NAME,"date ,name ","")
db.delete_tableData(connection,TABLE_NAME,"WHERE name = '1' " )
print(result)

connection.close()
