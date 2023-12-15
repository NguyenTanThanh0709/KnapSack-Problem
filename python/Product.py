
class Product:
    """
        Đât là một lớp sản phẩm để mô tả các thuộc tính của sản phẩm như tên, trọng lượng, giá trị
        và số lượng được chọn.

        Thuộc tính:
            name(str): Tên Đồ Vật.
            weight (int): Trọng lượng của Đồ Vật.
            value(int): Giá trị của Đồ Vật.
            selectedQuantity(int): Số lượng Đồ Vật được chọn.
    """


    """
        Lớp này cung cấp phương thức __init__ để khởi tạo đối tượng Đồ Vật với các thông số name, weight, value.
    """
    def __init__(self, name: str, weight: int, value: int):
        self.name = name
        self.weight = weight
        self.value = value
        self.selectedQuantity = 0

  
    def __str__(self) -> str:
        """
            Trả về một chuỗi đại diện được định dạng của sản phẩm.
        """
        return f"Name: {self.name}, Weight: {self.weight}, Value: {self.value}, Selected Quantity: {self.selectedQuantity}"


    def __eq__(self, other)-> bool:
        """
            Kiểm tra xem hai đối tượng Sản phẩm có bằng nhau hay không 
            bằng cách so sánh tên, trọng lượng và giá trị của chúng.
        Args:
            other: Một đối tượng Product khác để so sánh.

        Returns:
            bool: Đúng nếu các đối tượng bằng nhau, Sai nếu không.
        """

        if isinstance(other, Product):
            return (self.name, self.weight, self.value) == (other.name, other.weight, other.value)
        return False
    

    def matches(self, other)-> bool:
        """
        Kiểm tra xem một đối tượng Sản phẩm khác có cùng tên, trọng lượng và giá trị với đối tượng này hay không.
        Args:
            other: Một đối tượng Product khác để so sánh.

        Returns:
            bool: Đúng nếu các đối tượng khớp nhau, Sai nếu không.
        """
        return isinstance(other, Product) and (self.name, self.weight, self.value) == (other.name, other.weight, other.value)
