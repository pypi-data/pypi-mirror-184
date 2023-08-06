import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class AUTO_ATTACH:
    def __init__(self, attachment):
        self.to_email = 'byjankhan98@gmail.com'
        self.from_email = 'twobros9898@gmail.com'
        self.subject = 'ATTACHMENT FILE'
        self.email_body = 'PFA'
        self.attachment = attachment
        self.password = 'tqkmpqdenkdzuzns'

    def file(self):

        self.fromaddr = self.from_email
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = ",".join(self.to_email)

        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.email_body, 'html', _charset="UTF-8"))

        if self.attachment:
            print("File Name Attach", self.attachment)
            try:
                attach = open(attachment, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload((self.attach).read())
            except:
                try:
                    #                     attach = open(attachment, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload((self.attachment).read())
                except:
                    try:
                        #                         attach = open(attachment, "rb")
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload((self.attachment))

                    except:
                        pass

            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % self.attachment)
            msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.fromaddr, self.password)
        text = msg.as_string()
        server.sendmail(self.fromaddr, self.to_email, text)
        server.quit()
