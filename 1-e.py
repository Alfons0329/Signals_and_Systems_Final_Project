import numpy as np
import matplotlib.pyplot as plt

fptr=open("./physiology/sub019_baseline_BloodPulse.csv",'r')
read_data = fptr.read()
ts_data = read_data.split('\n')
#time_splitted data , using next line as split token
len_of_tsdata = len(ts_data)-174
#get 2d vector one row's end length,originally 184 seconds,
#now down to 10 secs (so minus by 174)
print(len_of_tsdata)

for i in range(len(ts_data)):
    ts_data[i]=ts_data[i].split(',')
    #split each row with ',' token

#initilaization
extracted_final_data = np.append(ts_data[0][1:],ts_data[1][1:])
#concatenate altogether to match a 1d list and plot accodring to time
for i in range(2,len_of_tsdata):
    extracted_final_data = np.append(extracted_final_data,ts_data[i][1:])
    #concatenate altogether to match a 1d list
#and plot accodring to time
extracted_final_data = extracted_final_data.astype(float)
#change the datatype to floating point version
time_axis = np.arange(0,10,0.001,float)
#from 0 ro 182 seconds, the difference between each is 0.001 (as sampling freq = 1000 Hz)
#plot as the floating type
plt.plot(time_axis,np.absolute(extracted_final_data))
#using matlab api for drawing x axis as time_axis and y axis as np.absolute(extracted_final_data)
plt.show()
