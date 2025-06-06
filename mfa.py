import random 
import smtplib
import getpass 
import os
import webbrowser
from email.message import EmailMessage

USB_DRIVE_LETTER = "D" # USB drive letter            
EXPECTED_CODE = os.environ.get("EXPECTED_CODE")  # Set your expected code in environment variable
ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL") # Set your admin email in environment variable
APP_PASSWORD = os.environ.get("APP_PASSWORD") # Set your app password in environment variable
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD") # Set your app password in environment variable
VIDEO_URL = "https://www.youtube.com/shorts/AW2YJ9V47yI"  # YouTube Shorts URL

def check_usb_auth():
    usb_path = r"D:\otp_auth_key.txt"  
    
    if os.path.exists(usb_path):
        with open(usb_path, "r") as f:
            content = f.read().strip()
            if content == "699669": # Check if the content matches the expected code
                return True
            print(f"Invalid code: '{content}'")
    else:
        print("File not found at D:\\")
    return False

def send_otp_email(sender_email, sender_password, recipient_email):
    """Send OTP email"""
    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            msg = EmailMessage()
            msg['Subject'] = "OTP Verification" 
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg.set_content(f"Your OTP is: {otp}")
            server.send_message(msg)
            print(f"\n OTP sent to {recipient_email}")
            return otp
    except Exception as e:
        print(f"\n Email error: {e}")
        return None

def main():
    print("\n Secure OTP Sender (RyuuK32 USB Auth)")   # Initial message
    print("=====================================")
    
    # USB Authentication
    if not check_usb_auth():
        print("\n Access denied - Required:")
        print(f"- USB Drive {USB_DRIVE_LETTER}:\\")
        input("Press Enter to exit...")
        return
    
    # Password Auth
    attempts = 3
    while attempts > 0:
        if getpass.getpass("Admin password: ") == "xxxxxx": # Replace with your actual password
            break
        attempts -= 1
        print(f"{attempts} attempts left")
    
    if attempts == 0:
        print("See you")
        input("Press Enter to exit...")
        webbrowser.open(VIDEO_URL)  # This will open the YouTube Shorts in default browser
        return
    
    # OTP Process
    recipient = input("\n Recipient email: ").strip()
    if otp := send_otp_email(ADMIN_EMAIL, APP_PASSWORD, recipient):
        user_otp = input("\n Enter OTP: ").strip()
        print("\n Access granted!" if user_otp == otp else " Invalid OTP")

if __name__ == "__main__":
    main() 
