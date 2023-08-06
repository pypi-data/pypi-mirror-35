import smtplib
import base64

class EnviarEmail:

    def __init__(self):
        self.nome = None



def sendMail(self, params):
 
  fromaddr = params["mail_from"]
  toaddr = params["mail_to"]
  if 'mail_cc' in params:
    cc = params["mail_cc"]
  else:
    cc = ""
  if 'mail_bcc' in params:
    bcc = params["mail_bcc"]
  else:
    bcc = ""
  
  bcc = params["mail_bcc"]
  msg = MIMEMultipart()
  
  vbcc = [] if params["mail_bcc"] == "" else bcc.split(";")
  vcc = [] if params["mail_cc"] == "" else cc.split(";")
  rcpt = vbcc  + vcc + [toaddr]
  msg['From'] = fromaddr
  msg['To'] = toaddr
  msg['Cc'] = cc
  msg['Bcc'] = bcc
  msg['Subject'] = params["subject"]
   
  body = params["content"]
   
  msg.attach(MIMEText(body, params['BodyType']))
   
  if params["attach_file"]:
    filename = params["file_name"][params["file_name"].rfind("/")+1:]
    attachment = open(params["file_name"], "rb")
     
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    msg.attach(part)
  
  #169.254.8.75 
  #180.128.170.65
  server = smtplib.SMTP('180.128.170.65', 25) 
  text = msg.as_string()
  server.sendmail(fromaddr, rcpt, text)
  server.quit()
  
