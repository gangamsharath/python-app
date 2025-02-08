import multiprocessing as mp
"""
This script demonstrates the use of Python's multiprocessing module to perform
concurrent operations on a shared list of records. The script defines two main
functions: insert_record and print_records.
Functions:
    insert_record(record, records):
        Inserts a new record into the shared list of records.
        Args:
            record (tuple): A tuple containing the name and age to be added.
            records (list): A shared list of records managed by the multiprocessing.Manager.
    print_records(records):
        Prints all records from the shared list of records.
        Args:
            records (list): A shared list of records managed by the multiprocessing.Manager.
Main Process:
    The main process initializes a shared list of records using multiprocessing.Manager.
    It then creates and starts two separate processes:
        - One to insert a new record into the shared list.
        - Another to print all records from the shared list.
    The script measures and prints the time taken to perform these operations using multiprocessing.
"""
import time

def insert_record(record, records):
    print("Inserting new record")
    time.sleep(0.5)
    records.append(record)
    print("New record added successfully")

def print_records(records):
    print("Printing all records")
    for record in records:
        time.sleep(0.5)
        print("Name: ",record[0],", Age: ",record[1])


if __name__ == '__main__':
    print("Main(Paraent) process started")
    with mp.Manager() as manager:
        startt=time.time()
        print("I am, server process")
        #creatoing a list of in server process memory
        records=manager.list([('Pramod',30),('Kiran',25),('Raj',35)])
        # new record to be added
        new_record=('Ravi',40)
        #creating new process
        p1=mp.Process(target=insert_record, args=(new_record,records))
        p2=mp.Process(target=print_records, args=(records,))
        #running process p1 to insert new record
        p1.start()
        p1.join()
        #running process p2 to print all records
        p2.start()
        p2.join()
        endt=time.time()
        print("Time taken with multi-processing ",endt-startt," seconds")
    
    print("Main(Paraent) process ended")
