import threading,time

data=[4,5,6,7,2]

def calc_square():
    print("Square of given numbers")
    for i in data:
        time.sleep(0.3)
        print("Square of ",i," is ",i*i)

def calc_cube():
    print("Cube of given numbers")
    for i in data:
        time.sleep(0.3)
        print("Cube of ",i," is ",i*i*i)


if __name__ == '__main__':
    print("Main thread started")
    start=time.time()
    th1=threading.Thread(target=calc_square)
    th2=threading.Thread(target=calc_cube)
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    # calc_square()
    # calc_cube()
    end=time.time()
    # print("Time taken without multi-threading ",end-start," seconds")
    print("Time taken with multi-threading ",end-start," seconds")
    print("Main thread ended")