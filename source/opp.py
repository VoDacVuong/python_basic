# init class and access class
class Car:

    # attribute of class
    loaixe = "Ô tô"
    v_default = 100

    # method
    def t(self, s, v= v_default):
        return s/v
        
    # attribute of object
    def __init__(self, tenxe, mausac, nguyenlieu):
        self.tenxe = tenxe
        self.mausac = mausac
        self.nguyenlieu = nguyenlieu

#init class
toyota = Car("Toyota", "Đỏ", "Deisel")

# access the instance class
print(f"toyota là xe {toyota.loaixe}, có màu {toyota.mausac}, vận hành bằng {toyota.nguyenlieu}")
print("toyota là: {}".format(toyota.__class__.loaixe))
print("toyota là: ", toyota.loaixe)

# access method
print(f'T: {toyota.t(24, 101)}')
#-----------------------------------------
# Kế thừa
class Lamborghini(Car):
    #call back constructor
    def __init__(self, tenxe, mausac, nguyenlieu):
        super().__init__(tenxe, mausac, nguyenlieu)
    
    def t(self, s, v):
        return super().t(s, v)

lamborghini = Lamborghini('Lamborghini', 'Vàng', 'Điện')
print(f'Tên xe: {lamborghini.tenxe}, màu sắc: {lamborghini.mausac}')

#------------------------------------------
# Đóng gói
class Computer:

    def __init__(self):
        self.__price = 850

    def sell(self):
        print(f'Giá bán là: {self.__price}')
    
    def set_price(self, price):
        self.__price = price

computer1 = Computer()

# Thay đổi giá thông thường
computer1.__price = 11
computer1.sell()

# Thay đổi giá thông qua hàm setter
computer1.set_price(1850)
computer1.sell()

#------------------------------------------
# Tính đa hình
class Honda:

     def dungxe(self):
        print("Honda dừng xe để nạp điện")

     def nomay(self):
        print("Honda nổ máy bằng hộp số tự động")

class Porsche:

     def dungxe(self):
        print("Porsche dừng xe để bơm xăng")

     def nomay(self):
        print("Porsche nổ máy bằng hộp số cơ")

# common interface
def kiemtra_dungxe(car): car.dungxe()

# instantiate objects
honda = Honda()
porsche = Porsche()

# passing the object
kiemtra_dungxe(honda)
kiemtra_dungxe(porsche)
