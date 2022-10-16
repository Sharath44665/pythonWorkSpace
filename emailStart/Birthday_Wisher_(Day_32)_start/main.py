import smtplib

myEmail="someone@noreply.com"
myPasswd="bleh bleh" #app password of gmail or yahoo
recieverMail="reciever@noreply.com"

# connection=smtplib.SMTP("smtp.gmail.com")
# connection.starttls() # make TLS connection->meaning secure
# connection.login(user=myEmail, password=myPasswd)
# connection.sendmail(from_addr=myEmail, to_addrs=recieverMail,
#                     msg="Subject:Hello world!\n\n This is some text msg")
# connection.close()
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # make TLS connection->meaning secure
    connection.login(user=myEmail, password=myPasswd)
    connection.sendmail(from_addr=myEmail, to_addrs=recieverMail,
                        msg="Subject:Hello world!\n\n This is some text msg for body")
