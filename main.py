from icrawler.builtin import GoogleImageCrawler
import os
from pathlib import Path
import zipfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email_with_attachment(receiver_email, attachment_path):
    sender_email = "add mail"
    sender_password = "from your gmail"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Your Requested Images"

    with open(attachment_path, 'rb') as file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
        msg.attach(part)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        return True
    except Exception as e:
        return str(e)

def download_and_send_images(keyword, num_images, user_email):
    downloads_dir = str(Path.home() / "Downloads")
    save_dir = os.path.join(downloads_dir, 'downloaded_images')

    try:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        google_crawler = GoogleImageCrawler(storage={'root_dir': save_dir})

        print(f"Downloading {num_images} images for '{keyword}'...")
        google_crawler.crawl(keyword=keyword, max_num=num_images)

        zip_file_path = os.path.join(downloads_dir, 'images.zip')
        with zipfile.ZipFile(zip_file_path, 'w') as zipf:
            for foldername, subfolders, filenames in os.walk(save_dir):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    zipf.write(file_path, os.path.basename(file_path))

        print("Sending email...")
        email_status = send_email_with_attachment(user_email, zip_file_path)

        if email_status is True:
            print(f"Successfully downloaded {num_images} images and sent them to {user_email}.")
        else:
            print(f"Failed to send email: {email_status}")

    except Exception as ex:
        print(f"An unexpected error occurred: {str(ex)}")

if __name__ == "__main__":
    keyword = input("Enter the keyword to search for images: ")
    num_images = int(input("Enter the number of images to download: "))
    user_email = input("Enter your email address: ")
    download_and_send_images(keyword, num_images, user_email)
