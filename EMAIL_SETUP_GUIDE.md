# Email Configuration Guide

## Overview
When admin registers a new faculty member, the system automatically sends login credentials to the faculty's email address.

## Setup Instructions

### 1. Configure Environment Variables

Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

### 2. Gmail Setup (Recommended)

**Step 1: Enable 2-Factor Authentication**
1. Go to your Google Account: https://myaccount.google.com
2. Navigate to Security
3. Enable 2-Step Verification

**Step 2: Generate App Password**
1. Go to: https://myaccount.google.com/apppasswords
2. Select "Mail" and "Windows Computer" (or Other)
3. Click "Generate"
4. Copy the 16-character password

**Step 3: Update .env File**
```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=xxxx-xxxx-xxxx-xxxx  # Your 16-char app password
```

### 3. Alternative Email Providers

**Outlook/Hotmail:**
```env
SMTP_SERVER=smtp-mail.outlook.com
SMTP_PORT=587
SENDER_EMAIL=your-email@outlook.com
SENDER_PASSWORD=your-password
```

**Yahoo Mail:**
```env
SMTP_SERVER=smtp.mail.yahoo.com
SMTP_PORT=587
SENDER_EMAIL=your-email@yahoo.com
SENDER_PASSWORD=your-app-password
```

**Custom SMTP Server:**
```env
SMTP_SERVER=smtp.yourcompany.com
SMTP_PORT=587
SENDER_EMAIL=noreply@yourcompany.com
SENDER_PASSWORD=your-password
```

### 4. Install Required Python Package

```bash
cd backend
pip install python-dotenv
```

### 5. Load Environment Variables

Update `backend/app.py` to load environment variables:
```python
from dotenv import load_dotenv
load_dotenv()
```

## Email Template

The system sends a professional HTML email containing:
- Welcome message
- Login credentials (email and password)
- Security notice to change password
- Direct login link
- Contact information

## Testing

1. Register a test faculty member with your own email
2. Check inbox (and spam folder)
3. Verify credentials are correct
4. Test login with received credentials

## Troubleshooting

**Email not received:**
- Check spam/junk folder
- Verify SMTP credentials in .env
- Check if 2FA is enabled (Gmail)
- Verify app password is correct
- Check firewall/antivirus settings

**Authentication failed:**
- Gmail: Use App Password, not regular password
- Outlook: Enable "Less secure app access"
- Yahoo: Generate app-specific password

**Connection timeout:**
- Check SMTP_SERVER and SMTP_PORT
- Verify internet connection
- Check if port 587 is blocked by firewall

## Security Best Practices

1. **Never commit .env file to Git**
   - Already in .gitignore
   
2. **Use App Passwords**
   - Never use your main email password
   
3. **Rotate Credentials**
   - Change app passwords periodically
   
4. **Monitor Email Logs**
   - Check for suspicious activity
   
5. **Production Setup**
   - Use dedicated email service (SendGrid, AWS SES, Mailgun)
   - Implement rate limiting
   - Add email queue system

## Production Recommendations

For production environments, consider using:
- **SendGrid** (Free tier: 100 emails/day)
- **AWS SES** (Pay as you go)
- **Mailgun** (Free tier: 5,000 emails/month)
- **Postmark** (Free tier: 100 emails/month)

These services provide:
- Better deliverability
- Email analytics
- Template management
- Bounce handling
- Spam protection
