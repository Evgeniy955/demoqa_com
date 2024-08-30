import os
import shutil
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from cmdline_add_args.allure_report_path import CURRENT_DIRECTORY

from admin.allure_env import get_os_type
from config.env import BROWSER, SEND_REPORT

report_path = CURRENT_DIRECTORY + f'/allure-results'

if get_os_type() == "Windows":
    path = report_path.replace("/", "\\")
else:
    path = report_path

target_path = path
file_to_zip = BROWSER
ADMIN_FOLDER = os.path.dirname(__file__)

output_filename = f'{BROWSER} report'
output_path = ADMIN_FOLDER

# Mail settings
from_email = "halitsyn.evhen@outlook.com"
password = "zy63Xa5pf"
to_email = "galitsyn.evgeniy955@gmail.com"
subject = "Allure report"
body = f"{BROWSER} report"
filename = f"{output_filename}.zip"


class SendMail:
    def __init__(self, target_path, file_to_zip):
        # Archive report
        try:
            shutil.make_archive(os.path.join(ADMIN_FOLDER, output_filename), 'zip', target_path, file_to_zip)
        except:
            print('pass')

    # Attaching a file
    def attaching_a_file(self):
        attachment_file = f"{output_path}\\{filename}"
        if get_os_type() == "Windows":
            correct_path = attachment_file
        else:
            correct_path = attachment_file.replace("\\", "/")
        try:
            with open(correct_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {filename}")
                return part
        except UnicodeDecodeError as e:
            print(f"Error reading file {correct_path}: {e}")
            return None

    # Sending email via SMTP
    def send_mail(self):
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        attachment_part = SendMail.attaching_a_file(self)
        if attachment_part:
            msg.attach(attachment_part)
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
    print("\nSend report")
    print(f"\n{BROWSER}")
    if SEND_REPORT:
        SendMail(target_path, file_to_zip).send_mail()