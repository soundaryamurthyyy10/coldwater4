#Program to send email
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('senders mailid',"password")
msg="Hi Shalini,Are you free tomorrow"
s.sendmail('senders mailid',"reciever ids",msg)
print('success')
s.quit()
