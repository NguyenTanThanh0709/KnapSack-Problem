from typing import List, Tuple
from Product import Product

def merge_sort(items, key_function):
    if len(items) > 1:
        mid = len(items) // 2
        left_half = items[:mid]
        right_half = items[mid:]

        merge_sort(left_half, key_function)
        merge_sort(right_half, key_function)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if key_function(left_half[i]) <= key_function(right_half[j]):
                items[k] = left_half[i]
                i += 1
            else:
                items[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            items[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            items[k] = right_half[j]
            j += 1
            k += 1

def sort_by_ratio(items):
    merge_sort(items, key_function=lambda x: x[0])
    # Đảo ngược danh sách để có thứ tự giảm dần
    items.reverse()


"""
    Giải quyết vấn đề về Fractional KnapSack  bằng cách sử dụng phương pháp tiếp cận Dynamic.

    Args:
         products (List[Product]): Danh sách các đối tượng Đồ vật đại diện cho các Đồ vật có sẵn.
         capacity (int): Sức chứa của ba lô.

    Returns:
         Tuple[List[Product], int, int]: Một bộ chứa các mục đã chọn, tổng giá trị
"""


def fractional_knapsack(items: List[Product],capacity : int) -> Tuple[List[Product], int]:
    n = len(items)
    """
        Tạo một danh sách để lưu tỷ lệ giá trị/trọng lượng của mỗi mục hàng. Mỗi phần tử trong danh sách là một tuple chứa tỷ lệ,
        giá trị và trọng lượng của một mục hàng.

        Duyệt qua từng mục hàng trong danh sách và tính tỷ lệ giá trị/trọng lượng, sau đó thêm vào danh sách ratios.
    """
    ratios = []
    for i in range(n):
        ratios.append((items[i].value / items[i].weight, items[i].value, items[i].weight,i))

    """
        Sắp xếp danh sách ratios theo tỷ lệ giảm dần, để ưu tiên chọn những mục hàng có tỷ lệ cao hơn.
    """
    sort_by_ratio(ratios)

    total_value = 0
    knapsack = [0] * n
    selected_items = []
    i = 0
    while capacity > 0 and i < n:
        # 
        if ratios[i][2] <= capacity:   # nếu trọng lượng thứ i nhỏ hơn hoặc bằng dung tích của balo, thì toàn bộ túi được đặt vào balo, knapsack[i] = 1 để đánh dấu vật
            # được đặt vào balo
            items[ratios[i][3]].selectedQuantity = 1
            selected_items.append(items[ratios[i][3]])
            knapsack[i] = 1 # trị giá của vật đó
            total_value += ratios[i][1] # cộng giá trị của mục hàng vào tổng giá trị
            capacity -= ratios[i][2] # trừ trọng lượng của mục hàng khỏi dung lượng balo còn lại
        else:

                # chỉ lấy một phần phân đoạn của mục đó sao cho trọng lượng của nó là bằng trọng lượng còn lại của túi  
            fraction = capacity / ratios[i][2] 
            items[ratios[i][3]].selectedQuantity = fraction
            selected_items.append(items[ratios[i][3]])
            knapsack[i] = fraction # trị giá của vật đó
            total_value += fraction * ratios[i][1]
            capacity = 0

        i += 1

    return selected_items,total_value 
