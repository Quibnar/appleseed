# 🍎 Appleseed v1.0 – LeadGen Mailer

Appleseed is a local-first lead generation and email outreach tool built in Python.

It scrapes real business listings using a headless browser, generates personalized messages, and emails them — all from your own machine.

> “This email wrote itself. Yours can too.” – The Johnny Appleseed of Technology

---

## ✨ Features

- 🔎 DuckDuckGo-powered business scraper (Selenium + BeautifulSoup)  
- 🧠 Email templating with Jinja2  
- 💌 Send via Gmail or Google Workspace (App Password ready)  
- 🗂 Logs all activity to a local SQLite database  
- 🔧 Runs fully offline except for scraping/email steps  
- 🌱 100% Open Source. Fork it. Plant it. Grow it.

---

## 🚀 Quickstart (Live Email Sending)

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-name/leadgen-mailer.git
   cd leadgen-mailer
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the environment**

   - PowerShell:

     ```bash
     .\venv\Scripts\Activate
     ```

   - Git Bash:

     ```bash
     source venv/Scripts/activate
     ```

4. **Install requirements**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set your Gmail/Google Workspace account**

   - Visit: [Google App Passwords](https://myaccount.google.com/apppasswords)
   - Enable 2FA
   - Generate a 16-character App Password
   - Paste it into `main.py` under `SMTP_CONFIG["password"]`

6. **Run the program**

   ```bash
   python main.py
   ```

---

## 📬 How It Works

1. You enter an industry and location (e.g., "Bakery" in "Sacramento")
2. Appleseed scrapes relevant Yelp listings
3. It extracts business names and websites
4. Each lead is used to generate a personalized email using your template
5. Emails are sent automatically from your Gmail account
6. Every send is logged in `leads.db`

---

## 📄 Email Template

Located in `templates/email_template.txt`, you can customize it with Jinja2 fields like:

```
Hi {{ business_name }},

I’d like to share Appleseed — a lead generation and outreach automation tool.

Appleseed found your business and wrote you this email. And it’s open source.

You can use it for free:
1. Clone the code: https://github.com/your-name/leadgen-mailer
2. Open in PowerShell
3. Type: python main.py

Let me know if you'd like help setting it up or want to see more tools like this.

– Dirk Stockton  
The Johnny Appleseed of Technology
```

---

## 🧠 Developer Notes

- Works best with Google Workspace (up to 2,000 emails/day)
- Can be extended with OpenAI personalization in future versions
- Logs saved in `leads.db` (can be exported as CSV later)

---

## 📜 License

MIT — see [LICENSE](./LICENSE) for details.  
You are free to use, remix, and redistribute this tool commercially or personally.

---

## 🧑‍💻 Contact

Dirk Stockton  
[on-the-metal.net](https://on-the-metal.net)  
[linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)
