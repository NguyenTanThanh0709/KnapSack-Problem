# knapsack.py
from typing import List, Tuple

from Product import Product

"""
    Giải quyết vấn đề về KnapSack 0/1 bằng cách sử dụng phương pháp tiếp cận Brute-Force.

    Args:
         products (List[Product]): Danh sách các đối tượng Đồ vật đại diện cho các Đồ vật có sẵn.
         capacity (int): Sức chứa của ba lô.

    Returns:
         Tuple[List[Product], int, int]: Một bộ chứa các mục đã chọn, tổng giá trị và tổng trọng lượng.
"""


def brute_force_knapsack(products: List[Product], capacity: int) -> Tuple[List[Product], int, int]:
    n = len(products)               # số lượng đồ vật có trong danh sách 

    best_choice = [0] * n           # khởi tạo mảng best_choice với giá trị mặc định là 0,
                                    # lưu trữ quyết định chọn hoặc không chọn từng sản phẩm.
                                    # best_choice[i] tại đồ vật thứ i được chọn thì đánh số là 1,
                                    # không chọn thì đánh số là 0

    best_value = 0                  # Khởi tạo best_value và best_weight
    best_weight = 0                 # lần lượt là tổng giá trị và tổng trọng lượng tốt nhất tìm được.
    
    #Duyệt qua tất cả các tổ hợp có thể của các sản phẩm, được biểu diễn bằng số nhị phân từ 0 đến 2^n - 1.
    for i in range(2**n):

        j = n - 1           # Khởi tạo biến j để theo dõi vị trí của sản phẩm trong mảng best_choice.

        temp_weight = 0     # Khởi tạo temp_weight và temp_value để lưu trữ trọng lượng và giá trị tạm thời của từng tổ hợp.
        temp_value = 0      # các biến này sẽ thay đổi khi mà tìm được tổ hợp tốt hơn.
        """
        Tạo một vòng lặp để tạo ra các tổ hợp khác nhau bằng cách thay đổi giá trị 0 và 1 trong mảng best_choice. 
        Vòng lặp này giúp sinh ra tất cả các tổ hợp khác nhau của việc chọn hoặc không chọn từng sản phẩm.
        Khi vòng lặp kết thúc, mảng best_choice sẽ lưu giữ một tổ hợp mới và
        chuẩn bị cho vòng lặp tiếp theo để sinh ra tổ hợp khác.
        """
        while j >= 0:
            if best_choice[j] != 0:         # Kiểm tra nếu sản phẩm tại vị trí j đã được chọn (giá trị là 1).
                best_choice[j] = 0          # Nếu đã được chọn, thì đặt giá trị của sản phẩm này về 0, tức là không chọn.
                j -= 1
            else:                           # Nếu sản phẩm tại vị trí j chưa được chọn (giá trị là 0).
                best_choice[j] = 1          # Đặt giá trị của sản phẩm này về 1, tức là chọn.
                break                       #  Kết thúc vòng lặp, vì đã tìm được một tổ hợp mới.
        for k in range(n):                                      # Duyệt qua từng sản phẩm và tính toán trọng lượng và giá trị tạm thời của tổ hợp hiện tại.
            if best_choice[k] == 1:                             # Nếu vật đó được chọn thì tình xem nó có đóng góp gì cho tổ hợp.
                temp_weight += products[k].weight
                temp_value += products[k].value

        if temp_value > best_value and temp_weight <= capacity:    
            """
                Kiểm tra xem tổ hợp hiện tại có cải thiện kết quả không 
                (tăng giá trị và không vượt quá dung lượng của cặp xách).
                Nếu đáp ứng điều kiện trên, cập nhật các biến lưu trữ kết quả tốt nhất
            """
            best_value = temp_value 
            best_weight = temp_weight
            for m in range(n):
                products[m].selectedQuantity = best_choice[m]               # cập nhật xem đồ vật đó có được chọn hay không

    return products, best_value, best_weight # Trả về một tuple chứa danh sách sản phẩm được chọn, tổng giá trị (int), và tổng trọng lượng tốt nhất. (int)