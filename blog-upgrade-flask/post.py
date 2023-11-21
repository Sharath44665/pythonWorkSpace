
import requests,smtplib,pandas
class Post:
    def __init__(self):
        response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
        response.raise_for_status()

        self.fakeData = response.json()

    def getData(self):
        return self.fakeData


    def sendMailToUser(self,contactData={}):
        myData = pandas.read_csv(filepath_or_buffer="myPassword.csv")
        myEmail = myData.iloc[0,0]
        myPasswd = myData.iloc[0,1]


        mailSubject = "Sharath's Blog - contact"

        msgBody = (f"user: {contactData['username']}\n"
                       f"email: {contactData['email']}\n"
                       f"Phone: {contactData['phone']}\n"
                       f"message: {contactData['message']}")

        with smtplib.SMTP("smtp.gmail.com",587) as emailConnect:
            emailConnect.starttls()
            emailConnect.login(user=myEmail, password=myPasswd)
            emailConnect.sendmail(from_addr=myEmail, to_addrs= myEmail, msg=f"Subject:{mailSubject}\n\n{msgBody}")
            print("mail sent")


