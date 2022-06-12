import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase

# Permet d'envoyer un mail avec un sujet, un message et une pièce jointe
def sendMail(subject, body, filename):
    # ===============================================
    # Informations générales
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "mrssniperxd@gmail.com"  # Enter your address
    receiver_email = "lucjager67@gmail.com"  # Enter receiver address
    # Mot de passe d'application
    password = "ppwbssxhvmtuoqno"

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Bcc"] = receiver_email

    message.attach(MIMEText(body, "plain"))

    # Pour attacher l'image en pièce jointe
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
