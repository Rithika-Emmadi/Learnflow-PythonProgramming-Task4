import datetime
import getpass
import smtplib
import time

smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
smtp_obj.ehlo()
smtp_obj.starttls()
msg = ""


def send_mail(from_addres, password, to_addres):

    smtp_obj.login(from_addres, password)
    print("Email logged in")

    subject = input("Subject: \n")
    message = input("Message: \n")

    print("This will be your mail:\n")
    msg = f"From: {from_addres}\nTo: {to_addres}\nSubject: {subject}\n\n{message}"
    print(msg)

    return msg


def quit_mail():
    smtp_obj.quit()


def email_sender():
    from_addres = input("Enter from address email: ")
    # password p= input("Password: ")
    password = getpass.getpass(prompt="Password: ")
    to_addres = input("Enter to address email: ")

    datetime_str = input("Enter date and time in the format YYYY-MM-DD HH:MM:SS: ")
    datetime_format = "%Y-%m-%d %H:%M:%S"

    try:
        send_time = datetime.datetime.strptime(datetime_str, datetime_format)
    except ValueError:
        print(
            "Invalid datetime format. Please enter the datetime in YYYY-MM-DD HH:MM:SS format."
        )
        return

    msg = send_mail(from_addres, password, to_addres)

    delay = (send_time - datetime.datetime.now()).total_seconds()
    if delay > 0:
        print(f"Email will be sent in {delay} seconds.")
        time.sleep(delay)
        smtp_obj.sendmail(from_addres, to_addres, msg)
        print("Email is sent")
    else:
        print("The specified time is in the past. Please enter a future time.")

    quit_mail()


email_sender()
