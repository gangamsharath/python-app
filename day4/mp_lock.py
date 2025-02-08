import multiprocessing
import time

def add_dollar(balance, lock):
    for _ in range(100):
        time.sleep(0.01)
        with lock:
            balance.value += 1

def minus_dollar(balance, lock):
    for _ in range(100):
        time.sleep(0.01)
        with lock:
            balance.value -= 1

if __name__ == "__main__":
    balance = multiprocessing.Value('i', 100)
    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=add_dollar, args=(balance, lock))
    p2 = multiprocessing.Process(target=minus_dollar, args=(balance, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Final balance: {balance.value}")