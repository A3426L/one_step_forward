import operate_db as db
import pandas as pd
import matplotlib.pyplot as plt
TABLE_NAME = "toilet0"
d_now,t_now = db.current_time()
d_prev = db.previous_date()
time_list =  [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

def get_pltList(name,date):
	Y = []
	connection = db.connect_database()
	for time in time_list:
		result = db.read_table(connection,TABLE_NAME,"time,date ,name ",option="WHERE name = '{}' AND (date =  '{}' )  AND (time <= '{}:59') AND (time >= '{}:00')".format(name,date,time ,time))
		print(time)
		Y.append(len(result))
	connection.close()
	return Y

def make_plt():
	Y1 =get_pltList("1",d_now)
	Y2 =get_pltList("2",d_now)
	plt.xticks(time_list)
	plt.ylim(0,10)
	plt.bar(time_list, Y1, align="edge", width=-0.3)
	plt.bar(time_list, Y2, align="edge", width= 0.3)
	plt.savefig("bar_data.png")





plt.show()

