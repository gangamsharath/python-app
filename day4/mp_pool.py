import multiprocessing as mp
import os

def square(n):
    print("Worker process id for {0}: {1}".format(n, os.getpid()))
    return n*n

if __name__ == '__main__':
    num_cores = mp.cpu_count()
    print("Number of CPU cores: ", num_cores)
    #input values
    #p=range(1,1000)
    # mylist = [1,2,3,4,5,6,7,8,9,10]
    mylist = list(range(1, 1000))
    #creating pool of objects
    p=mp.Pool()
    #mapping input values to worker function
    result=p.map(square, mylist)
    print(result)
    #closing pool
    p.close()
