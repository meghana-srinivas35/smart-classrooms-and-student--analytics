# Email Notification Setup - Quick Guide

## ✅ Feature Added: Support Query Resolution Email

When an admin resolves a support query, the user automatically receives an email notification with:
- Original query details
- Resolution message
- Professional HTML template

---

## 🔧 Email Configuration

### Step 1: Update `.env` file

Add these variables to your `.env` file in the project root:

```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=your-app-password
```

### Step 2: Gmail App Password Setup

1. Go to Google Account: https://myaccount.google.com/
2. Security → 2-Step Verification (enable if not enabled)
3. Security → App passwords
4. Select app: Mail
5. Select device: Other (Custom name) → "Smart Classrooms"
6. Click Generate
7. Copy the 16-character password
8. Paste in `.env` as `SENDER_PASSWORD`

---

## 📧 Email Templates Included

### 1. Faculty Registration Email
- Sent when admin registers new faculty
- Contains login credentials
- Professional welcome message

### 2. OTP Email
- Sent for password reset
- 6-digit OTP code
- 10-minute validity

### 3. Query Resolution Email ✨ NEW
- Sent when admin resolves support query
- Shows original query
- Shows resolution message
- Professional template

---

## 🎯 How to Use

### Admin Side:
1. Login as Admin
2. Go to "Support Queries" in navbar
3. View all submitted queries
4. Click "Resolve" on any pending query
5. Enter resolution message
6. Click "Resolve & Send Email"
7. User receives email automatically!

### User Side:
1. Submit query from Login page → "Contact Administrator"
2. Wait for admin to resolve
3. Receive email notification with resolution
4. Check email for details

---

## 🧪 Testing Without Email

If you don't configure email (for testing):
- All features work normally
- Email sending fails silently
- Success message shows "email failed to send"
- No errors or crashes

---

## 📝 Email Template Preview

```
Subject: Your Support Query Has Been Resolved

Dear [User Name],

Your support query has been resolved by our team.

Your Query:
[Original query message]

Resolution:
[Admin's resolution message]

If you have any further questions, please contact us again.

Best regards,
Smart Classrooms Analytics Support Team
```

---

## ✅ What's Working

- ✅ Support query submission
- ✅ Admin can view all queries
- ✅ Admin can resolve queries
- ✅ Email sent on resolution
- ✅ Professional HTML template
- ✅ Error handling if email fails
- ✅ Status tracking (pending/resolved)

---

## 🚀 Quick Test

1. **Submit Query:**
   - Go to Login page
   - Click "Contact Administrator"
   - Fill form and submit

2. **Resolve Query:**
   - Login as Admin (admin@test.com / admin123)
   - Go to "Support Queries"
   - Click "Resolve" on the query
   - Enter resolution message
   - Submit

3. **Check Email:**
   - User receives email with resolution
   - Check spam folder if not in inbox

---

## 🔍 Troubleshooting

**Email not sending?**
- Check `.env` file has correct credentials
- Verify Gmail App Password is correct
- Check 2-Step Verification is enabled
- Try different email provider if Gmail blocks

**Query not showing?**
- Refresh the page
- Check browser console for errors
- Verify backend is running

---

## 📊 Database Fields

Support Query Object:
```javascript
{
  id: "1",
  name: "User Name",
  email: "user@email.com",
  role: "student",
  message: "Query message",
  status: "pending" | "resolved",
  resolutionMessage: "Admin's resolution",
  submittedAt: "2024-01-15T10:00:00",
  resolvedAt: "2024-01-15T11:00:00"
}
```

---

## 🎨 UI Features

- Card-based query display
- Color-coded status badges
- Modal for resolution
- Success/error alerts
- Responsive design
- Professional layout

---

**Setup Time:** 5 minutes  
**Email Provider:** Gmail (or any SMTP)  
**Cost:** Free  
**Difficulty:** Easy  

---

✅ **Feature is production-ready!**
