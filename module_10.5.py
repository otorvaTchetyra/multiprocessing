import time
from multiprocessing import Pool
import os

def read_info(filename):
    all_data = []
    try:
        with open(filename, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                all_data.append(line.strip())
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")

if __name__ == '__main__':
    filenames = [
        r'D:\PythonProjects\module_10.5\multiprocessing\file 1.txt', 
        r'D:\PythonProjects\module_10.5\multiprocessing\file 2.txt', 
        r'D:\PythonProjects\module_10.5\multiprocessing\file 3.txt', 
        r'D:\PythonProjects\module_10.5\multiprocessing\file 4.txt'
    ]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_time = time.time() - start_time
    print(f"{linear_time} (линейный)")

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multiprocessing_time = time.time() - start_time
    print(f"{multiprocessing_time} (многопроцессный)")
