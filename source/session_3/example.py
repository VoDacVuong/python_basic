
#-------------------------------------------------
import pdb
import smtplib
import os
import json
def send_email():
  print("===== Config Email Server ======")
  print("Gmail User: ")
  gmail_user=input()
  print("Gmail Password: ")
  gmail_password=input()

  sent_from = gmail_user
  to = [gmail_user, 'vuongit2905r@gmail.com']
  subject = 'Email Demo'
  body = 'Hello world'

  email_text = """\
  From: %s
  To: %s
  Subject: %s

  %s
  """ % (sent_from, ", ".join(to), subject, body)

  EMAIL_HOST_USER =os.environ.get("ALLOWED_HOSTS")
  try:
      server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
      server.ehlo()
      server.login(gmail_user, gmail_password)
      server.sendmail(sent_from, to, email_text)
      server.close()

      print ('Email sent!')
  except:
      print ('Error')

#-------------------------------------------
# Working with file: Image, PDF, CSV, Excel

# export ra file Excel
import openpyxl
def output_Excel(input_detail,output_excel_path):
  #Xác định số hàng và cột lớn nhất trong file excel cần tạo
  row = len(input_detail)
  column = len(input_detail[0])

  #Tạo một workbook mới và active nó
  wb = openpyxl.Workbook()
  ws = wb.active
  
  #Dùng vòng lặp for để ghi nội dung từ input_detail vào file Excel
  for i in range(0,row):
    for j in range(0,column):
      v=input_detail[i][j]
      ws.cell(column=j+1, row=i+1, value=v)

  #Lưu lại file Excel
  wb.save(output_excel_path)


# import file csv
import csv
def import_csv(file_import):
      with open(file_import, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

# xử lý hình ảnh
from PIL import Image, ImageEnhance
import cv2
def grayscale(file_img):
      img = Image.open(file_img)
      pixels = img.load()
      new_img = Image.new(img.mode, img.size)
      pixels_new = new_img.load()
      for i in range(new_img.size[0]):
          for j in range(new_img.size[1]):
              r, b, g = pixels[i,j]
              avg = int(round((r + b + g) / 3))
              pixels_new[i,j] = (avg, avg, avg, 0)
      new_img.show()

# Thay đổi độ tương phản
def contrast(file_img):
      img = Image.open(file_img)
      enhancer = ImageEnhance.Contrast(img)
      for i in range(1, 8):
          factor = i / 4.0
          new_img = enhancer.enhance(factor)
          new_img.show()

# Tìm cạnh
def canny_edge_detection(file_img):
      img = cv2.imread(file_img, 0)
      edges = cv2.Canny(img, 100, 200)
      cv2.imshow('image', edges)
      cv2.waitKey(0)

      cv2.destroyAllWindows()

# convert to pdf
import validators
import pdfkit
def html2pdf(html_file_name_or_url_html, pdf_file_name):
      config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\wkhtmltopdf.exe")
      # import pdb;pdb.set_trace()
      if validators.url(html_file_name_or_url_html):
            pdfkit.from_url(html_file_name_or_url_html, pdf_file_name, configuration = config)
      else:
            pdfkit.from_file(html_file_name_or_url_html, pdf_file_name, configuration = config)


