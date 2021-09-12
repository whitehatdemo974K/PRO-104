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
new_data.sort()
if count % 2 == 0:
    m1=float(new_data[count//2])
    m2=float(new_data[count//2-1])
    median=(m1+m2)/2

else:
    median=float(new_data[count//2])
print("meadian of height is"+str(median))