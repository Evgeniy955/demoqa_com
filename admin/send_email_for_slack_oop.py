import os
import shutil
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from cmdline_add_args.allure_report_path import CURRENT_DIRECTORY

from admin.allure_env import get_os_type
from config.env import BROWSER

folder_path = CURRENT_DIRECTORY + f'/allure-results/{BROWSER}'

if get_os_type() == "Windows":
    path = folder_path.replace("/", "\\")
else:
    path = folder_path

target_path = 'C:\\Users\\Yevhen\\Desktop\\backup_original\\Archive'
file_to_zip = 'new'

output_filename = 'archive2'
output_path = "C:\\Users\\Yevhen\\Documents\\Archives"

# Mail settings
from_email = "autouser_ukr@outlook.com"
password = "zy63Xa5pf"
to_email = "galitsyn.evgeniy955@gmail.com"
subject = "Allure report"
body = f"{BROWSER.capitalize()} report "
filename = f"{output_filename}.zip"


class SendMail:
    def __init__(self, target_path, file_to_zip):
        # Archive report
        try:
            shutil.make_archive('C:\\Users\\Yevhen\\Documents\\Archives\\archive2', 'zip', target_path, file_to_zip)
        except:
            print('pass')

    # Attaching a file
    def attaching_a_file(self):
        attachment = open(f"{output_path}\\{filename}", "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {filename}")
        return part

    # Sending email via SMTP
    def send_mail(self):
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        msg.attach(SendMail.attaching_a_file(self))
        try:
            with smtplib.SMTP('smtp.office365.com', 587) as server:
                server.starttls()
                server.login(from_email, password)
                server.sendmail(from_email, to_email, msg.as_string())

            print("Email sent successfully")
        except smtplib.SMTPAuthenticationError:
            print("\033[91mAuthentication unsuccessful, the user credentials were incorrect\033[0m")
        finally:
            archive_file = os.path.join(output_path, filename)
            os.remove(archive_file)


def send_report_to_email():
    SendMail(target_path, file_to_zip).send_mail()


if __name__ == '__main__':
    send_report_to_email()
