from email_generator import generate_email
from email_sender import send_email
import sqlite3
from datetime import datetime
from search_scraper import search_yelp

# === CONFIGURATION ===
SMTP_CONFIG = {
    "host": "smtp.gmail.com",
    "port": 465,
    "password": "your-app-password"  # Replace with your actual app password
}

SEND_EMAILS = False    # Set to True only when you're ready to send
MAX_EMAILS = 5         # Cap how many emails to process per run
USE_FAKE_LEADS = False # Use fake leads instead of scraping

FAKE_LEADS = [
    {"name": "Sunrise Creamery", "url": "https://example.com"},
    {"name": "Golden Milk Co.", "url": "https://example.com"},
    {"name": "Dallas Dairy Delight", "url": "https://example.com"},
    {"name": "Creamy Hills Farm", "url": "https://example.com"},
    {"name": "Bluebell Barn", "url": "https://example.com"}
]

# === LOGGING ===
def log_email(business_name, website, email, status):
    conn = sqlite3.connect("leads.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS email_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            business_name TEXT,
            website TEXT,
            email TEXT,
            status TEXT,
            timestamp TEXT
        )
    """)
    cursor.execute("""
        INSERT INTO email_log (business_name, website, email, status, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (business_name, website, email, status, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

# === MAIN EXECUTION ===
def main():
    industry = input("Enter industry: ")
    location = input("Enter location: ")
    sender_email = input("Your email: ")

    leads = FAKE_LEADS if USE_FAKE_LEADS else search_yelp(industry, location)
    print(f"✅ Loaded {len(leads)} real leads")

    sent_count = 0

    for lead in leads:
        if sent_count >= MAX_EMAILS:
            print(f"Reached email limit of {MAX_EMAILS}. Stopping.")
            break

        email = f"{lead['name'].lower().replace(' ', '')}@example.com"
        body = generate_email(lead['name'], industry)

        if SEND_EMAILS:
            try:
                send_email(email, "Just Sharing My Work", body, sender_email, SMTP_CONFIG)
                print(f"✅ Sent email to {email}")
                log_email(lead['name'], lead['url'], email, "sent")
            except Exception as e:
                print(f"❌ Failed to send to {email}: {e}")
                log_email(lead['name'], lead['url'], email, "failed")
        else:
            print(f"📬 [Preview] Would send to {email}:\n---\n{body}\n---")
            log_email(lead['name'], lead['url'], email, "preview")


        sent_count += 1

if __name__ == "__main__":
    main()
