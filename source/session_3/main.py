# unit test
import test_unit
# test = test_unit.TestStringMethods()
# test.test_isupper()
# test.test_upper()
# test.test_islower()
# test.test_split()

#-------------------------------------
# Send Email
import example
# example.send_email()

#-------------------------------------
# export ra file Excel
input_detail =[['Sản phẩm', 'Mã', 'Số lượng' , 'Giá tiền'],['Áo sơ mi', '1S25H', 1, 23000],['Quần bò', '3325H', 7, 50000],['Áo phông', '16G5H', 45, 70000]]
output_excel_path= 'C:\\Users\\ADMIN\Desktop\\TPS_soft\\user.xlsx'
example.output_Excel(input_detail, output_excel_path)

#------------------------------------
#import file csv
example.import_csv('C:\\Users\\ADMIN\Desktop\\TPS_soft\\user.csv')

#------------------------------------
#Xử lý hình ảnh
# example.grayscale('C:\\Users\\ADMIN\Desktop\\TPS_soft\\download.jpg')
# example.contrast('C:\\Users\\ADMIN\Desktop\\TPS_soft\\download.jpg')
# example.canny_edge_detection('C:\\Users\\ADMIN\Desktop\\TPS_soft\\download.jpg')