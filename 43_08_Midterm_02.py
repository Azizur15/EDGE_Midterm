import numpy as np
daily_screen_time=[]
number_of_app_used=[]
gender=[]
fpr=open("D:\\mobile_usage_behavioral_analysis.csv","r")
head=fpr.readline()
line=fpr.readline()
while(len(line)>0):
    arr=line.strip().split(',')
    line=fpr.readline()
    number_of_app_used.append(float(arr[5]))
    daily_screen_time.append(float(arr[4]))
    gender.append(arr[2])
    line = fpr.readline()
fpr.close()
print("Gender:",gender)
print("Daily_screen_time:",daily_screen_time)
print("Number_of_app_used:",number_of_app_used)
x=np.array(daily_screen_time)
print("Average of daily screen time=",x.mean())
print("Highest value of daily screen time=",x.max())
print("Lowest value of daily screen time=",x.min())
y=np.array(number_of_app_used)
print("Average of number of app used=",y.mean())
print("Highest value of number of app used=",y.max())
print("Lowest value of number of app used=",y.min())









