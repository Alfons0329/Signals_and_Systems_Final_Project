import numpy as np
import matplotlib.pyplot as plt
import datetime

fptr=open("./physiology/sub019_film 1_ECG.csv",'r')
raw_data = fptr.read()
ts_data = raw_data.split('\n')#time_split data
len_of_tsdata = len(ts_data)-1

for i in range(len(ts_data)):
    ts_data[i]=ts_data[i].split(',')
start_time=datetime.datetime.strptime("13:35:23","%H:%M:%S")
end_time=datetime.datetime.strptime("13:41:40","%H:%M:%S")
total_sec=0
start_index=0;
for i in range(0,len_of_tsdata):
	temp_time=datetime.datetime.strptime(ts_data[i][0]," %H:%M:%S.")
	if(start_time<=temp_time):
		total_sec+=1
		break;
	else:
		start_index=i+1
final_data = np.array(ts_data[start_index][1:])

for i in range(start_index+1,len_of_tsdata):
	temp_time=datetime.datetime.strptime(ts_data[i][0]," %H:%M:%S.")
	if(start_time<=temp_time and temp_time<=end_time):
		total_sec+=1
		final_data = np.append(final_data,ts_data[i][1:])
	else:
		break
print(total_sec)
print(len(final_data))

final_data = final_data.astype(float)
fft_result = np.fft.fft(final_data)
#print(fft_result)
time_asix = np.arange(0,total_sec,0.001,float)
plt.plot(time_asix,np.absolute(fft_result))

plt.show()
