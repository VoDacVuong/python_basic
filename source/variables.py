# STRING
word = 'python'
print(word[0:2])
print(word[-2:])
print(len(word))
word_enum = list(enumerate(word))
print(word.lower())
print(word.upper())
#----------------------

# Number
c = complex(2, 5) # khởi tạo số phức
c.real # lấy ra phần thực
c.imag # lấy ra phần ảo 

# Output: 187
print(0b10111011) # Hệ nhị phân
# Output: 257 (250 + 7)
print(0xFA + 0b111) # Hệ thập lục phân
# Output: 15
print(0o17)

int(3.2) # ép kiểu

#----------------------------------
### LIST
lst = [2, 4, 3, "ABC", 3, [6, 4, 2]] #=> [2, 4, 3, 'ABC', 3, [6, 4, 2]]
print(type(lst)) #=> <type 'list'>

print(lst[2]) #=> 3 

lst[2] = 100
print(lst) #=> [2, 4, 100, 'ABC', 3, [6, 4, 2]]

#Lay do dai mang
print(len(lst)) #=> 6

#Them phan tu vao mang
lst.append(True) #=> [2, 4, 100, 'ABC', 3, [6, 4, 2], True]

#gộp
any_lst = ['one', 'two', 'three']
lst.extend(any_lst) #=> [2, 4, 100, 'ABC', 3, [6, 4, 2], True, 'one', 'two', 'three']

#Sap xep, dao nguoc
lst = [4,3,5,2,7,5,2]

lst.sort() #=> [2, 2, 3, 4, 5, 5, 7]
lst.sort(reverse = True) #=> [7, 5, 5, 4, 3, 2, 2]

#comprehension list
cub3 = [3 ** x for x in range(9)]
#comprehension list with if
cub3_if = [3 ** x for x in range(9) if x > 4]
print(cub3)
print(cub3_if)

#-----------------------------------
#TUPLE
tup = (2, "ABC", 7, 3, [4,3,7], True, 3) #=> (2, 'ABC', 7, 3, [4, 3, 7], True, 3)
print(type(tup)) #=> <type 'tuple'>

#Khong the thay doi gia tri
# tup[1] = 100 #=> TypeError: 'tuple' object does not support item assignment

#Khong the xoa
# del tup[1] #=> TypeError: 'tuple' object doesn't support item deletion

#Dem so lan xuat hien
print(tup.count(3)) #=> 2

# tuple lồng nhau
n_tuple = ("Quantrimang.com", [2, 6, 8], (1, 2, 3))

# index lồng nhau
# Output: 'r'
print(n_tuple[0][5])

# index lồng nhau
# Output: 8
print(n_tuple[1][2])


#-----------------------------------------------
#SET
st_a = { 2, 7, 3, 2, 5 } #=> set([2, 3, 5, 7])
st_b = { 2, 72, 32, 2, 51 }

print(type(st_a)) #=> <type 'set'>

#Them phan tu vao set
st_a.add(100) #=> set([2, 3, 100, 5, 7])

#Xoa phan tu
st_a.pop #=> set([2, 3, 100, 5, 7]) #=> set([3, 5, 7])

#Phep lay giao
print(st_a & st_b)

#Phep lay hop
print(st_a | st_b)

#Lay gia tri co o a nhung ko co o b
print(st_a - st_b)

# Lay nhung phan tu khong phai la phan tu chung
print(st_a ^ st_b)

#---------------------------
#DICT
dict_a = {1: "MySQL", 2: "SQLServer", 3:"SQLite"} #=> {1: 'MySQL', 2: 'SQLServer', 3: 'SQLite'}
dict_b = {"a": "MySQL", "b": "SQLServer", (2, 3, 7): "SQLite"} #=> {'a': 'MySQL', 'b': 'SQLServer', (2, 3, 7): 'SQLite'}

#Lấy các keys của dict
print(dict_a.keys()) #=> [1, 2, 3]

#Lấy các values của dict
print(dict_a.values()) #=> ['MySQL', 'SQLServer', 'SQLite']

#Lấy ra các item của dict
print(dict_a.items()) #=> [(1, 'MySQL'), (2, 'SQLServer'), (3, 'SQLite')]

#Truy cập bằng key
print(dict_a[2]) #=> SQLServer

#Thêm 1 phần tử vào dict
dict_a[100] = "MongoDB"
print(dict_a) #=> {1: 'MySQL', 2: 'SQLServer', 3: 'SQLite', 100: 'MongoDB'}

#Xóa 1 phần tử dict
dict_a.pop(3)
print(dict_a) #=> {1: 'MySQL', 2: 'SQLServer', 100: 'MongoDB'}








#--------------------------------------------------
#File
obj=open("abcd.txt","w")
obj.write("Python xin chao cac ban")
obj.close()
obj1=open("abcd.txt","r")
s=obj1.read()
print(s)
obj1.close()
obj2=open("abcd.txt","r")
s1=obj2.read(20)
print(s1)
obj2.close()

#---------------------------------------
#Zipping, Unzipping file
import zipfile
# Zipping     
jungle_zip = zipfile.ZipFile(r'C:\Users\ADMIN\Desktop\BDS_moi.zip', 'w')
# Unzipping
# jungle_zip.extractall('C:\Users\ADMIN\Desktop')
 
jungle_zip.close()