'''
import threading
def greet():
    print("Hello from the worker")
thread = threading.Thread(target=greet)
thread.start()
print("Main program is running")


# creating and starting thread
import threading
def greet():
    print("Hello from the thread")
thread = threading.Thread(target=greet)
thread.start()


# creating multiple threads
import threading
def greet():
    print("Hello from a thread")
thread1 = threading.Thread(target=greet)
thread2 = threading.Thread(target=greet)
thread1.start()
thread2.start()

# giving each thread a different task
import threading
def worker(name):
    print(f"{name} is working")
thread1 = threading.Thread(target=worker, args=("Alex",))
thread2 = threading.Thread(target=worker, args=("Jordan",))
thread1.start()
thread2.start()


# creating a thread with join()
import threading
def worker():
    print("Worker is working")
thread = threading.Thread(target=worker)
thread.start()
thread.join()
print("worker has finished")

# creating a lock
import threading
counter = 0
lock = threading.Lock()
def increase_counter():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1
thread1 = threading.Thread(target=increase_counter)
thread2 = threading.Thread(target=increase_counter)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Final counter:", counter)
'''

# threadpoolexecutor
import time
from concurrent.futures import ThreadPoolExecutor


def download_file(name):
    print(f"Starting {name}")

    time.sleep(3)

    print(f"Finished {name}")


with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(download_file, "File 1")
    executor.submit(download_file, "File 2")
