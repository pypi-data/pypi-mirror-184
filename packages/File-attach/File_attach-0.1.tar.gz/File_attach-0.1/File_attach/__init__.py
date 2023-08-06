import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def file(attachment):
    to_email = 'byjankhan98@gmail.com'
    from_email = 'twobros9898@gmail.com'
    subject = 'ATTACHMENT FILE'
    email_body = 'PFA'
    password = 'tqkmpqdenkdzuzns'

    fromaddr = from_email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = ",".join(to_email)

    msg['Subject'] = subject
    msg.attach(MIMEText(email_body, 'html', _charset="UTF-8"))

    if attachment:
        print("File Name Attach", attachment)
        try:
            attach = open(attachment, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attach).read())
        except:
            try:
                #                     attach = open(attachment, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
            except:
                try:
                    #                         attach = open(attachment, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload((attachment))

                except:
                    pass

        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % attachment)
        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, to_email, text)
    server.quit()
