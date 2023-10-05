import ir_commuication as ir
import operate_db as db
import time

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
		time.sleep(1)
		recog2 = data.recv_func(num)
		if recog2 == 0:
			print("unable")
		else:
			print(" OK!")
			data.send_data("0")
			print("send_ok")
			#db.insert_table(connection,TABLE_NAME,num,d_now,t_now)
	else:
		print("OK")	
		data.send_data("0")
		print("send_ok")
		#db.insert_table(connection,TABLE_NAME,num,d_now,t_now)

print("end")

result_A = db.read_table(connection,TABLE_NAME,"time,date ,name ",option="WHERE name = '1' AND (date =  '{}' ) AND (time < '08:00' OR time > '20:00' )".format(d_now))
result_B = db.read_table(connection,TABLE_NAME,"time,date ,name ",option="WHERE name = '2' AND (date =  '{}' ) AND (time < '08:00' OR time > '20:00' )".format(d_now))
count_A = len(result_A)
count_B = len(result_B)
	
print(count_A)
print(count_B)
	
	
#db.delete_tableData(connection,TABLE_NAME,option="WHERE name = '1' " )

connection.close()
