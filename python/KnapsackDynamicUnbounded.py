from typing import List, Tuple

from Product import Product

def max_value(i, w):
    if i >= w : return i
    return w

"""
    Giải quyết vấn đề về KnapSack 0/1 chọn không giới hạn đồ vật bằng cách sử dụng phương pháp tiếp cận Dynamic.

    Args:
         products (List[Product]): Danh sách các đối tượng Đồ vật đại diện cho các Đồ vật có sẵn.
         capacity (int): Sức chứa của ba lô.

    Returns:
         Tuple[List[Product], int, int]: Một bộ chứa các mục đã chọn, tổng giá trị tốt nhất
"""


def knapsack_dynamic_unbounded(products: List[Product], Capacity: int) -> Tuple[List[Product], int]:
    n = len(products)          # Lấy số lượng sản phẩm

    """
        Tạo một bảng 2D để lưu trữ kết quả tạm thời của các bài toán con
        Có n + 1 hàng, mỗi hàng tương ứng với việc xét đến một sản phẩm trong danh sách (items).
        Có (capacity + 1) cột, mỗi cột tương ứng với một dung lượng từ 0 đến capacity của cặp xách.

        Do đó, table[i][w] sẽ lưu trữ giá trị tạm thời của bài toán con
        với i sản phẩm đầu tiên và dung lượng w.

        Trạng thái ban đầu của bảng là toàn bộ giá trị được khởi tạo là 0, do đó, table[0][w] (với mọi giá trị của w) 
        là trạng thái ban đầu của bài toán con không có sản phẩm nào được xem xét.

        Ví dụ:
            table[3][5] sẽ lưu trữ giá trị tạm thời của bài toán con có 3 sản phẩm đầu tiên và dung lượng cặp xách là 5.
            table[2][2] sẽ lưu trữ giá trị tạm thời của bài toán con có 2 sản phẩm đầu tiên và dung lượng cặp xách là 2.
    
    """
    table : List[List[int]] = [[0] * (Capacity + 1) for _ in range(n + 1)]

    """
        Vòng lặp for i in range(n + 1): và for w in range(Capacity + 1): 
        xây dựng bảng table từ dưới lên. 
        Giá trị table[i][w] đại diện cho giá trị tối ưu của bài toán 
        con với i sản phẩm đầu tiên và dung lượng cặp xách là w.

        if i == 0 or w == 0:        table[i][w] = 0 : 
            Nếu không có sản phẩm nào được xem xét (i == 0) hoặc dung lượng còn lại là 0 (w == 0), 
            giá trị tạm thời là 0 vì không có sản phẩm nào được chọn.
        
            
        Ở đây có sự khác biệt ở KnapSack Problem 0/1 ở đoạn:
        table[i][w] = max(products[i - 1].value + table[i][w - products[i - 1].weight], table[i - 1][w])

        Để ý khi tìm được giá trị tốt hơn giá trị hiện tại trong bảng thì giá trị vật thứ i là Value[i] + với giá trị 
        lớn nhất có hiện tại vì vật i có thể được chọn nhiều lần 

    """
    for i in range(n + 1):
        for w in range(Capacity + 1):
            if i == 0 or w == 0:
                table[i][w] = 0 
            elif products[i - 1].weight <= w:
                table[i][w] = max_value(products[i - 1].value + table[i][w - products[i - 1].weight], table[i - 1][w])
            else:
                table[i][w] = table[i - 1][w]

    # Backtrack to find the selected items
    """
        tương tự với KnapSack 0/1
        nhưng check xem nếu tồn tại đồ vật trong các đồ vật được chọn thì cộng thêm giá trị được trọn 
        không thì thêm nó làm đồ vật được chọn.
    """
    included_items = []
    i, c = n, Capacity
    while i > 0 and c > 0:
        if table[i][c] != table[i - 1][c]:

            found_product = next((p for p in included_items if products[i - 1].matches(p)), None)
            if found_product:   
                found_product.selectedQuantity += 1
            else:
                products[i - 1].selectedQuantity = 1
                included_items.append(products[i - 1])
            c -=  products[i - 1].weight # Corrected line
        else:
            i -= 1


    return included_items, table[n][Capacity] 