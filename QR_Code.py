import qrcode

fullname = input("Please Enter Your first & last name: ")
phone_number = input("Please enter your phone number: ")
file_name ="Name: "+fullname+"\n Phone Number: "+phone_number

img_QR = qrcode.make(file_name)
img_QR.save("MyQrCode.png")