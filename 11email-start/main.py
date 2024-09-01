import smtplib


myEmail = "user@noreply.com"
receiver = "reciever@noreply.me"
appPasswd =input("enter your app passwd: ")

message = """Subject: Hi there, Sample python mail

    
Please note that this code is just a sample and you may need to modify it according to your specific use case.
This message is sent from Python."""

# connection = smtplib.SMTP(host="smtp.gmail.com",port=587)
with smtplib.SMTP(host="smtp.gmail.com",port=587) as myConnection:
    myConnection.starttls() # creates a secure connection TLS
    myConnection.login(user=myEmail,password=appPasswd)

    # connection.sendmail(from_addr=myEmail,to_addrs=reciever,
    #
    #                     msg="Subject:Message from Python Code\n\n"
    #                         "This is the body of the message created by python")

    myConnection.sendmail(from_addr=myEmail, to_addrs=receiver, msg=message)

print("done")

# connection.quit()