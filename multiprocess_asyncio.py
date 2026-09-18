# Multiprocess example
'''
import multiprocessing

def worker():
    print("Hello from the process")
process1 = multiprocessing.Process(target=worker)
process2 = multiprocessing.Process(target=worker)

process1.start()
process2.start()

process1.join()
process2.join()

print("Main program finished")


# creating and starting process
import multiprocessing
def worker(name):
    print(f"{name} is working")
process1 = multiprocessing.Process(
    target=worker,
    args=("Worker 1",)
)
process2 = multiprocessing.Process(
    target=worker,
    args=("worker 2",)
)
process1.start()
process2.start()

process1.join()
process2.join()

print("Main program finished.")


# Process pool with pool
import multiprocessing
def square(number):
    return number * number
if __name__ == "__main__":
    with multiprocessing.Pool(3) as pool:
        results = pool.map(square, [1,2,3,4,5])
        print(results)
        
# asynchronous function
import asyncio
async def greet():
    print("Hello")
    await asyncio.sleep(2)
    print("Goodbye")
asyncio.run(greet())

import asyncio
async def task1():
    print("Task 1 started")
    await asyncio.sleep(3)
    print("Task 1 finished")


async def task2():
    print("Task 2 started")
    await asyncio.sleep(3)
    print("Task 2 finished")
async def main():
    await asyncio.gather(
    task1(),
    task2()
    )
asyncio.run(main())

# writing coroutine
import asyncio
async def greet():
    print("Hello")
    await asyncio.sleep(2)
    print("Goodbye")
asyncio.run(greet())

# real world application
import asyncio


async def fetch_data():
    print("Requesting data...")

    await asyncio.sleep(2)

    print("Data received")


asyncio.run(fetch_data())
'''
# Running multiple coroutines concurrently

import asyncio
async def task1():
    print("Task 1 started")
    await asyncio.sleep(3)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(3)
    print("Task 2 finished")

async def main():
    await asyncio.gather(
        task1(),
        task2()
    )

asyncio.run(main())
