"""
load the emps.scv file into the memory then read all the data from the file an remove email colum and remanining 
data write in another csv file use logging
"""
import csv

with open("emps.csv","r") as fr:
    csv_data=csv.DictReader(fr)
    with open("newemps.csv","w") as fw:
        columns=['fname','lname']
        csvwriter=csv.DictWriter(fw,fieldnames=columns,delimiter=',',lineterminator='\n')
        csvwriter.writeheader()
        for row in csv_data:
            del row['email']
            csvwriter.writerow(row)
print("process done")
                                