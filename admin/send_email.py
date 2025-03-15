import os
import shutil
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from cmdline_add_args.allure_report_path import CURRENT_DIRECTORY
from dotenv import load_dotenv

from admin.logger import logger
from config.env import BROWSER, SEND_REPORT

load_dotenv()

report_path = os.path.join(CURRENT_DIRECTORY, 'allure-results')
target_path = os.path.normpath(report_path)
file_to_zip = 'IPAD 10.6.0'

output_filename = f'{BROWSER} report'
output_path = os.path.dirname(__file__)
filename = f"{output_filename}.zip"

# Mail settings
from_email = os.getenv('FROM_EMAIL')
password = os.getenv('PASSWORD')
to_email = os.getenv('TO_EMAIL')
subject = "Allure report"
body = f"{BROWSER} report"


class SendMail:
    def __init__(self, target_path, file_to_zip):
        self.target_path = target_path
        self.file_to_zip = file_to_zip
        self.archive_report()

    def archive_report(self):
        try:
            shutil.make_archive(os.path.join(output_path, output_filename), 'zip', self.target_path, self.file_to_zip)
        except Exception as e:
            print(f"Error creating archive: {e}")

    # Attaching a file
    def attaching_a_file(self):
        attachment_file = os.path.join(output_path, filename)
        correct_path = os.path.normpath(attachment_file)
        try:
            with open(correct_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename={filename}")
                return part
        except Exception as e:
            print(f"Error reading file {correct_path}: {e}")
            return None

    # Sending email via SMTP
    def send_mail(self):
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        attachment_part = self.attaching_a_file()
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
        except Exception as e:
            print(f"Error sending email: {e}")
        finally:
            archive_file = os.path.join(output_path, filename)
            if os.path.exists(archive_file):
                os.remove(archive_file)


def send_report_to_email():
    logger.info(f"SEND REPORT: {SEND_REPORT}")
    if SEND_REPORT:
        print("\nSend report")
        print("Slack zip: ", filename)
        SendMail(target_path, filename).send_mail()


if __name__ == '__main__':
    send_report_to_email()
