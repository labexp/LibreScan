__author__ = 'diugalde'

import smtplib


class MailService:

    server = "localhost"

    def getEmailReceiver(self):
        return "librescan@gmail.com"

    #Formats the mail msg with the sender information and the body msg.
    def prepareMSG(self, pName, pMsg, pPhone, pFrom):
        msg = """\
        Enviado por: %s <%s>
        Tel: %s
        Cuerpo del mensaje: %s
        """ % (pName, pFrom, pPhone, pMsg)
        print(msg)
        return msg

    def send(self, mail):
        s = smtplib.SMTP(self.server)
        sender = mail.sender
        to = self.getEmailReceiver()
        msg = self.prepareMSG(mail.name, mail.msg, mail.phone, mail.sender)
        try:
            s.sendmail(sender, to, msg)
            print("Email was sent successfully.")
        except Exception as exc:
            print("Mail failed: {}".format(exc))
        finally:
            s.quit()
