import smtplib,ssl


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "anjushatrivedi76@gmail.com"
    password = "jydfmjoermxjbgpj"
    receiver = "ayushtrivedi92@gmail.com"
    mycontext = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=mycontext) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

