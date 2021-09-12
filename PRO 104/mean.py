import csv
from types import new_class
with open("SOCR-HeightWeight.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    num=file_data[i][1]
    new_data.append(float(num))

count=len(new_data)
total=0
for i in new_data:
    total=total+i

mean=total/count
print("mean of height"+str(mean)) 