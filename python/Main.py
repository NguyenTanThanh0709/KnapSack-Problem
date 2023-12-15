
from typing import List, Tuple
import time
from Product import Product
from BruteForeKnapSack import brute_force_knapsack
from DynamicProgrammingKnapSack01 import knapsack_dynamic
from KnapsackDynamicUnbounded import knapsack_dynamic_unbounded
from FractionalKnapSackWithGreedy import fractional_knapsack

"""
    BỘ DỮ LIỆU ĐƯỢC LẤY TỪ: https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html
"""


"""
    Tiến Hành đọc file và và nó sẽ trả về một Tuple danh sách các đồ vật có sắn và trả về khả năng
    chịu tải của cái balo
"""
def read_txt(file_path: str) -> Tuple[List[Product], int]:
    products = []
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Extract capacity
        capacity_line = lines[0].strip().split()
        capacity = int(capacity_line[1])

        # Extract product information
        for line in lines[2:]:
            data = line.strip().split()
            name, weight, value = data[0], int(data[1]), int(data[2])
            product = Product(name, weight, value)
            products.append(product)

    return products, capacity
csv_file_path = "p4.txt"
products,capacity = read_txt(csv_file_path)





"""
Ghi kết quả vào file với cấu trúc như sau:
Capacity: Khả năng chịu tải của cái túi
Tên giải thuật
Best Value: Giá trị tốt nhất mà giải thuật đó có thể đạt được
Best Combination tổ hợp các sản phẩm được chọn
...
...
...

TimeOut: thời gian giải thuật đó chạy
"""
def write_results_to_txt(file_path: str, method_name: str, best_choice: List[Product], best_value: int, running_time: float):
    with open(file_path, 'a') as file:
        file.write(f"\nResults for {method_name}:\n")
        file.write(f"Best Value: {best_value}\n")
        file.write("Best Combination:\n")
        for product in best_choice:
            file.write(str(product) + '\n')
        
        file.write(f"TimeOut: {running_time}")

def measure_running_time(algorithm_function, products, capacity):
    start_time = time.perf_counter()  # Use perf_counter for higher precision
    result = algorithm_function(products, capacity)
    end_time = time.perf_counter()
    running_time = end_time - start_time
    return result, running_time



# Brute Force
output_file_path = "out_brute_force.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write(f"Capacity: {capacity}\n")

    
    result, running_time = measure_running_time(brute_force_knapsack, products, capacity)
    best_choice, best_value, best_weight = result

    write_results_to_txt(output_file_path, "Brute Force", best_choice, best_value, running_time)






# knapsack_dynamic
output_file_path = "out_knapsack_dynamic.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write(f"Capacity: {capacity}\n")

    result, running_time  = measure_running_time(knapsack_dynamic, products, capacity)
    best_choice, best_value = result

    write_results_to_txt(output_file_path, "Dynamic Programming 01", best_choice, best_value, running_time)




# knapsack_dynamic_unbounded
output_file_path = "out_knapsack_dynamic_unbounded.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write(f"Capacity: {capacity}\n")

    result, running_time  = measure_running_time(knapsack_dynamic_unbounded, products, capacity)
    best_choice, best_value = result

    write_results_to_txt(output_file_path, "Dynamic Programming Unbounded", best_choice, best_value, running_time)


# fractional_knapsack
output_file_path = "out_fractional_knapsack.txt"
with open(output_file_path, 'w') as output_file:

    output_file.write(f"Capacity: {capacity}\n")


    result, running_time  = measure_running_time(fractional_knapsack, products, capacity)
    selected_items, max_value = result

    write_results_to_txt(output_file_path, "Greedy With Fractional KnapSack Problem", selected_items, max_value,running_time)


import matplotlib.pyplot as plt
import numpy as np

# Function to generate input data for different sizes
def generate_input_sizes(start_size, end_size, step):
    return list(range(start_size, end_size + 1, step))

# Function to measure running time for a given algorithm and input size
def measure_running_times(algorithm_function, sizes):
    running_times = []
    for size in sizes:
        products, capacity = read_txt("p4.txt")
        result, running_time = measure_running_time(algorithm_function, products, capacity)
        running_times.append(running_time)
    return running_times

# Generate input sizes and measure running times
start_size = 1
end_size = 10
step = 1
input_sizes = generate_input_sizes(start_size, end_size, step)

brute_force_running_times = measure_running_times(brute_force_knapsack, input_sizes)
dynamic_running_times = measure_running_times(knapsack_dynamic, input_sizes)
fractional_running_times = measure_running_times(fractional_knapsack, input_sizes)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, brute_force_running_times, label='Brute Force')
plt.plot(input_sizes, dynamic_running_times, label='Dynamic Programming 01')
plt.plot(input_sizes, fractional_running_times, label='Greedy With Fractional KnapSack')

plt.title('Running Time Analysis')
plt.xlabel('Input Size')
plt.ylabel('Running Time (seconds)')
plt.legend()
plt.grid(True)
plt.show()


