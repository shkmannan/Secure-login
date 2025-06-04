#  Secure OTP Sender (RyuuK32 USB Auth)

A Python script for sending OTPs (One-Time Passwords) via email, protected by **USB-based authentication** and an **admin password**.

---

##  Features

*  **Multi-factor authentication**: Requires both a USB drive with a secret file and an admin password.
*  **OTP delivery**: Sends a randomly generated OTP to any email via Gmail SMTP.
*  **Credential security**: Uses environment variables to store sensitive data safely.
*  **User-friendly**: Clear CLI prompts and helpful error messages.
*  **Fun denial**: Opens a YouTube short if authentication fails (because why not?).

---

##  Requirements

* Python **3.7+**
* Gmail account with **App Passwords** enabled
* A USB drive (default `D:`) with a file `otp_auth_key.txt` containing your secret code

---

## 🛠️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/shkmannan/secure-login.git
cd secure-login
```

### 2. Install Dependencies

No external libraries are needed — uses only Python's standard library.

If you want to use `.env` files, install:

```bash
pip install python-dotenv
```

### 3. Set Environment Variables

Create a `.env` file (and **never** commit it):

```env
GMAIL_USER=your_email@gmail.com
APP_PASSWORD=your_generated_app_password
ADMIN_PASSWORD=your_admin_password
```

Or set them directly in your shell environment.

### 4. Prepare USB Authentication

* Insert your USB drive (default `D:` — change in script if needed)
* On that drive, create a file named: `otp_auth_key.txt`
* Add your **secret code** (no spaces or newlines) to that file

---

##  How to Enable Google SMTP (App Passwords)

1. Enable 2-Step Verification on your Google account:
    [Google 2-Step Verification](https://myaccount.google.com/security)

2. Generate an App Password:
    [App Passwords Setup](https://myaccount.google.com/apppasswords)

   * Choose “Mail” as the app
   * Choose “Other” for the device (name it however you want)
   * Copy the **16-character** password and use it in your `.env`

---

## Usage

Run the script:

```bash
python otp_sender.py
```

Then follow the prompts for:

* USB authentication
* Admin password
* Recipient email

---

## Security Notes

*  Never commit `.env` files or real credentials.
*  Change the admin password from the default in the code.
*  For more safety, consider encrypting `otp_auth_key.txt`.
