from typing import List, Tuple
from Product import Product

def max_value(i, w):
    if i >= w : return i
    return w

"""
    Giải quyết vấn đề về KnapSack 0/1 bằng cách sử dụng phương pháp tiếp cận Dynamic.

    Args:
         products (List[Product]): Danh sách các đối tượng Đồ vật đại diện cho các Đồ vật có sẵn.
         capacity (int): Sức chứa của ba lô.

    Returns:
         Tuple[List[Product], int, int]: Một bộ chứa các mục đã chọn, tổng giá trị tốt nhất
"""

def knapsack_dynamic(products: List[Product], capacity: int) -> Tuple[List[Product], int]:
    n = len(products)          # Lấy số lượng sản phẩm

    """
        Tạo một bảng 2D để lưu trữ kết quả tạm thời của các bài toán con
        Có n + 1 hàng, mỗi hàng tương ứng với việc xét đến một sản phẩm trong danh sách (products).
        Có (capacity + 1) cột, mỗi cột tương ứng với một dung lượng từ 0 đến capacity của cặp xách.

        Do đó, table[i][w] sẽ lưu trữ giá trị tạm thời của bài toán con
        với i sản phẩm đầu tiên và dung lượng w.

        Trạng thái ban đầu của bảng là toàn bộ giá trị được khởi tạo là 0, do đó, table[0][w] (với mọi giá trị của w) 
        là trạng thái ban đầu của bài toán con không có sản phẩm nào được xem xét.

        Ví dụ:

            table[3][5] sẽ lưu trữ giá trị tạm thời của bài toán con có 3 sản phẩm đầu tiên và dung lượng cặp xách là 5.
            table[2][2] sẽ lưu trữ giá trị tạm thời của bài toán con có 2 sản phẩm đầu tiên và dung lượng cặp xách là 2.
    
    """
    table : List[List[int]]= [[0] * (capacity + 1) for _ in range(n + 1)]

    # Điền vào bảng DP,Sử dụng vòng lặp để điền vào bảng DP (table), giải quyết từng bài toán con.
    """
        for i in range(1, n + 1):: Vòng lặp chạy qua các sản phẩm từ 1 đến n.
        for w in range(capacity + 1):: Vòng lặp chạy qua các dung lượng của cái balo từ 0 đến capacity.

        if products[i-1].weight <= w: Kiểm tra nếu trọng lượng của sản phẩm thứ i bắt đầu từ 0 không vượt quá dung lượng đang xét.
        đúng: có thể chọn sản phẩm thứ i vào cặp xách. thì có 2 trường hợp xảy ra:
                Kiểm tra xem giá trị Sản phẩm thứ i có tăng lên hay không nếu chọn sản phẩm thứ i, Hay là Giá trị trước đó trong
                Bảng tốt hơn. Sau đó gán giá trị tốt nhật vào bảng

        sai: không thể chọn sản phẩm thứ i vào cặp xách và giữ nguyên giá trị tối ưu hiện tại:
                Giá trị tối ưu của bài toán con giữ nguyên nếu không chọn sản phẩm thứ i.


        => Cả quá trình này lặp qua từng sản phẩm và từng dung lượng, tính toán và điền giá trị tối ưu vào bảng độ động.
            Sau khi vòng lặp hoàn thành, bảng sẽ chứa giá trị tối ưu cho mọi bài toán con.        
    """
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if products[i-1].weight <= w:
                table[i][w] = max_value(products[i-1].value + table[i-1][w - products[i-1].weight], table[i-1][w])
            else:
                table[i][w] = table[i-1][w]



    # Backtrack để tìm các sản phẩm được chọn trong kết quả tối ưu
    included_products = [] # chứa các đồ vật được chọn
    i, c = n, capacity # Biến i sẽ đại diện cho sản phẩm được xem xét, và biến c sẽ đại diện cho dung lượng còn lại trong cặp xách.


    """
        if table[i][c] != table[i-1][c]: Kiểm tra nếu giá trị tối ưu tại bảng table 
        cho sản phẩm thứ i và dung lượng c không giống giá trị tối ưu cho sản phẩm thứ i-1 và dung lượng c.
        Điều này có nghĩa là sản phẩm thứ i đã được chọn vào cặp xách.
        Điều này được làm rõ trong Slide.
    """
    while i > 0 and c > 0:
        if table[i][c] != table[i-1][c]:
            products[i-1].selectedQuantity = 1 # : Đặt selectedQuantity của sản phẩm thứ i bằng 1, chỉ định rằng sản phẩm này đã được chọn.
            included_products.append(products[i-1]) # Thêm sản phẩm thứ i vào danh sách 
            c -= products[i-1].weight # Giảm dung lượng của cặp xách bằng trọng lượng của sản phẩm thứ i, vì sản phẩm này đã được chọn.
        
        i -= 1 #  Di chuyển xuống sản phẩm thứ i-1 để kiểm tra tiếp.

    # Trả về danh sách sản phẩm được chọn và giá trị tối ưu
    return  included_products, table[n][capacity]

