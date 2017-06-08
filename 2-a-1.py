
import numpy as np
import matplotlib.pyplot as plt
import datetime

fptr=open("./physiology/sub019_film 1_C1.csv",'r')
raw_data = fptr.read()
ts_data = raw_data.split('\n')#time_split data
len_of_tsdata = len(ts_data)-1#get 2d vector each row's end length

print ("Film 1 total time of ",len_of_tsdata," secs")

for i in range(len(ts_data)):
    ts_data[i]=ts_data[i].split(',')
start_time=datetime.datetime.strptime("16:57:20","%H:%M:%S")#time of show stimulation
end_time=datetime.datetime.strptime("17:03:33","%H:%M:%S")#time of show questionnaire
#change timestamp to object parsing with the format "%H:%M:%S"
print ("Film 1 start time of %H:%M:%S",start_time," ")
print ("Film 1 end time of %H:%M:%S",end_time," ")
total_sec=0
start_index=0
#find which time in the csv 2d vector file in what row shall we start
for i in range(0,len_of_tsdata):
	temp_time=datetime.datetime.strptime(ts_data[i][0]," %H:%M:%S.")
	if(start_time<=temp_time):
		total_sec+=1 #ok to start find the start point
		break;
	else:
		start_index=i+1 #keep accumulating the starting index to find in which row of csv file is the start point of watching video
#find the start_index of the 2d array in what row shall we sart to append data that is we really watch the video

final_data = np.array(ts_data[start_index][1:])#initilaization of the final y axis data to plot


#keep append, append until the video ends
for i in range(start_index,len_of_tsdata):
	temp_time=datetime.datetime.strptime(ts_data[i][0]," %H:%M:%S.") #uniformalize the time format
	if(start_time<=temp_time and temp_time<=end_time): #is in the interval, append
		total_sec+=1
		final_data = np.append(final_data,ts_data[i][1:])
	else: #out of interval , append ends
		break
        
total_amplitude=0.0 #as amplitude accumulator
total_round=0 #as count accumulator
for i in range(start_index,start_index+total_sec):#as integer second type
	if((i-start_index)%6==5):#six seconds a group
		temp_arr=np.concatenate((ts_data[i-5][1:],ts_data[i-4][1:],ts_data[i-3][1:],ts_data[i-2][1:],ts_data[i-1][1:],ts_data[i][1:]))
		peak = max(temp_arr)
		down = min(temp_arr)
		total_amplitude+=(peak.astype(float)-down.astype(float))
		total_round+=1
	else:
		continue

average_amplitude = total_amplitude/total_round
final_data = final_data.astype(float)
print("Avreage amplitude : ",average_amplitude)
print("Total video watching time is ",end_time-start_time,"  len of final data is  ",len(final_data)) #will be 375000
time_axis = np.arange(0,10,0.001,float) #from 0 to 10 seconds, the difference between each is 0.001 (as sampling freq = 1000 Hz)
#plot as the floating type
plt.plot(time_axis,final_data[0:10000])#since we sample from 0 to 10 with precision 0.001(1000hz)
plt.show()
