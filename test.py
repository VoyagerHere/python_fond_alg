import subprocess
import time
import matplotlib.pyplot as plt
import os

n_values = range(180, 360)
execution_times_default = []
execution_times_pypy = []

for n in n_values:
    print(f"Running generator.py with n = {n}")
    subprocess.run(["python", "generator.py", str(n)])

    print("Running main.py with default Python interpreter")
    start_time = time.time()
    subprocess.run(["python", "main.py"])
    end_time = time.time()

    execution_time_default = end_time - start_time
    execution_times_default.append(execution_time_default)
    print(f"Execution time for main.py (default): {execution_time_default} seconds")

    print("Running main.py with PyPy")
    start_time = time.time()
    os.system('"pypy3.9-v7.3.11-win64\\pypy3.9.exe main.py"')
    end_time = time.time()

    execution_time_pypy = end_time - start_time
    execution_times_pypy.append(execution_time_pypy)
    print(f"Execution time for main.py (PyPy): {execution_time_pypy} seconds")

plt.plot(n_values, execution_times_default, label='CPython')
plt.plot(n_values, execution_times_pypy, label='PyPy')
plt.xlabel('n')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of main.py for different n values')
plt.legend()
plt.show()
