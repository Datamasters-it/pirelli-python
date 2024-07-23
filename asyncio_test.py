import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

def blocking_io_task(id):
    print(f"Start blocking I/O task {id}")
    time.sleep(2)
    return f"Result from blocking I/O task {id}"

def cpu_bound_task(id):
    print(f"Start CPU-bound task {id}")
    time.sleep(2)
    return f"Result from CPU-bound task {id}"

async def main():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor(max_workers=3) as thread_executor, ProcessPoolExecutor(max_workers=3) as process_executor:
        # Esecuzione delle funzioni bloccanti nel thread pool
        thread_tasks = [
            loop.run_in_executor(thread_executor, blocking_io_task, i)
            for i in range(3)
        ]

        # Esecuzione delle funzioni CPU-bound nel process pool
        process_tasks = [
            loop.run_in_executor(process_executor, cpu_bound_task, i)
            for i in range(3, 6)
        ]

        # Attesa dei risultati
        results = await asyncio.gather(*thread_tasks, *process_tasks)
        for result in results:
            print(result)

if __name__=='__main__':
    asyncio.run(main())
