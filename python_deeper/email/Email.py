#smtp 사용을 도와주는 library
import smtplib
from email.message import EmailMessage
import imghdr
import re

def sendEmail(addr):
    # 정규표현식으로 이메일 형식 유효성 검사
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg, addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

message = EmailMessage()
#헤더 부분에 접근하기 위해선 배열로 접근한다.
message["Subject"] = "SMTP 실습"
message["From"] = "seojo8625@gmail.com"
message["To"] = "lio8625@hufs.ac.kr"
message.set_content("코드라이언 SMTP 실습 중 입니다.")

with open("codelionImg.png", 'rb') as image:
    image_file = image.read()
image_type = imghdr.what('codelion', image_file)
message.add_attachment(image_file, maintype="image", subtype=image_type)

#Gmail에서 지정한 port 번호(465)를 사용해야한다.
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = "465"

#Gmail은 ssl이라는 암호화 과정을 거쳐야만 connect 가능하다.
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login("seojo8625@gmail.com", "seojo1919@")
sendEmail(message["To"])
smtp.quit()