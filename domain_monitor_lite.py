# domain_monitor_lite.py
# Created by Josh Halpenny (HalpsDesk)
#
# Lite Edition of Domain Monitor
# Local script — edit values below to configure
#
# Upgrade to GitHub Actions Edition: https://halpsdesk.gumroad.com/l/DomainMonitor

import whois
import time
import smtplib
from email.message import EmailMessage
from datetime import datetime

# ===== USER CONFIGURATION =====
DOMAINS = [
    "example.com",
    "example.net"
]

EMAIL_USERNAME = "youremail@gmail.com"  # Your Gmail address
EMAIL_PASSWORD = "your_app_password"   # Gmail App Password
EMAIL_RECEIVER = "recipient@gmail.com" # Where alerts are sent
# ==============================

def send_email_alert(subject, body):
    try:
        msg = EmailMessage()
        msg["From"] = EMAIL_USERNAME
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = subject
        # Force UTF-8 so emojis and non-ASCII characters work
        msg.set_content(body, subtype="plain", charset="utf-8")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"[INFO] Email sent: {subject}")
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")
def check_domain(domain):
    try:
        w = whois.whois(domain)

        expiry_date = w.expiration_date
        if isinstance(expiry_date, list):
            expiry_date = expiry_date[0]
        days_to_expiry = (expiry_date - datetime.now()).days if expiry_date else None

        status_raw = w.status
        if isinstance(status_raw, list):
            status = ", ".join(str(s) for s in status_raw)
        else:
            status = str(status_raw) if status_raw else "unknown"

        print(f"{domain}: Expiry={expiry_date.strftime('%Y-%m-%d') if expiry_date else 'unknown'} "
              f"({days_to_expiry} days) Status={status}")

        matched_keyword = None
        for keyword in ["pending delete", "redemption", "expired", "pending renewal deletion"]:
            if keyword.lower() in status.lower():
                matched_keyword = keyword
                break

        expiring_soon = days_to_expiry is not None and days_to_expiry <= 30

        if matched_keyword or expiring_soon:
            alert_message = f"⚠️ ALERT: {domain}\n"
            if expiring_soon:
                alert_message += f"🗓️ Expiry: {expiry_date.strftime('%Y-%m-%d')} ({days_to_expiry} days)\n"
            if matched_keyword:
                alert_message += f"📄 Status matched: '{matched_keyword}'\n"
            alert_message += f"📄 Status: {status}\n"
            alert_message += "🔗 More info: https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en"

            print(alert_message)
            send_email_alert(f"[Domain Alert] {domain}", alert_message)

    except Exception as e:
        print(f"[ERROR] {domain}: {e}")

if __name__ == "__main__":
    print("==== Domain Monitor Lite Edition ====")
    print("Upgrade to GitHub Actions Edition for automated cloud checks:")
    print("https://halpsdesk.gumroad.com/l/DomainMonitor\n")

    upgrade = input("Would you like to view the upgrade page now? (y/n): ").strip().lower()
    if upgrade == "y":
        import webbrowser
        webbrowser.open("https://halpsdesk.gumroad.com/l/DomainMonitor?option=3&_gl=1*1wh9avl*_ga*OTI4MjEzNzI4LjE3NTQ2ODY1ODk.*_ga_6LJN6D94N6*czE3NTQ2ODY1ODkkbzEkZzEkdDE3NTQ2ODkxNjMkajE0JGwwJGgw")

    print("\nChecking domains...\n")
    for domain in DOMAINS:
        check_domain(domain)
        time.sleep(2)
