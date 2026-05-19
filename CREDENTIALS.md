# Login Credentials

## 🔐 Test Accounts

### Student Account
- **Email:** `student@test.com`
- **Password:** `password123`
- **Role:** Student
- **Section:** A
- **Semester:** 6th

### Faculty/Teacher Account
- **Email:** `teacher@test.com`
- **Password:** `password123`
- **Role:** Faculty
- **Department:** Computer Science
- **Employee ID:** FAC001

### Admin Account
- **Email:** `admin@test.com`
- **Password:** `admin123`
- **Role:** Admin
- **Department:** Administration

---

## 📋 How to Use

1. **Go to Login Page:** http://localhost:3000/login
2. **Enter credentials** from above based on the role you want to test
3. **Select the correct role** from the dropdown
4. **Click "Sign In"**

---

## 🎯 Faculty Features

### For Faculty (teacher@test.com):

1. **Login** with faculty credentials
2. **Go to Classes** page
3. **View assigned sections** - Initially, you need admin to assign you to a section
4. **Once assigned:**
   - View "My Sections" dashboard
   - Click on your section to manage it
   - Add students to your section
   - View student list
   - Remove students if needed

### For Admin to Assign Faculty:

1. **Login** as admin (admin@test.com)
2. **Go to Classes** page
3. **Select a section** (e.g., Section A)
4. **Click "+ Add Faculty"**
5. **Enter faculty details:**
   - Name: Dr. Smith
   - Email: `teacher@test.com` (must match the faculty login email)
   - Phone: +1 (555) 123-4567
   - Subject: Computer Science
   - Office: Room 101
6. **Click "Add Faculty"**
7. **Now faculty can access this section!**

---

## 🔄 Testing the Complete Flow

### Step 1: Admin Assigns Faculty to Section
```
1. Login as admin@test.com / admin123
2. Navigate to Classes
3. Click on "Section A"
4. Click "+ Add Faculty"
5. Fill in:
   - Name: Dr. Smith
   - Email: teacher@test.com
   - Subject: Computer Science
6. Click "Add Faculty"
```

### Step 2: Faculty Accesses Their Section
```
1. Logout and login as teacher@test.com / password123
2. Navigate to Classes
3. See "My Sections" with Section A listed
4. Click on Section A
```

### Step 3: Faculty Adds Students
```
1. In Section A details page
2. Click "+ Add Student"
3. Fill in:
   - Roll Number: CS001
   - Name: Alice Johnson
   - Email: alice@student.edu
   - Phone: +1 (555) 111-1111
4. Click "Add Student"
5. Student appears in the table
```

---

## 💾 Data Persistence

- All section assignments, faculty, and students are saved in **localStorage**
- Data persists across page refreshes
- To reset data, clear browser localStorage

---

## 🚀 Quick Test Commands

### Start Backend
```bash
cd backend
python app.py
```

### Start Frontend
```bash
cd client
npm start
```

### Access Application
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000
- Health Check: http://localhost:5000/health

---

## 📝 Notes

- **Faculty email must match** the email used during admin assignment
- Faculty can only see sections they're assigned to
- Admin can see and manage all sections
- Students see their own section's timetable and resources
- All passwords are stored in plain text (for demo purposes only)

---

## 🔒 Security Note

⚠️ **For Development/Testing Only**
- Passwords are stored in plain text
- No real authentication tokens
- No encryption
- **DO NOT use in production without proper security implementation**

---

**Last Updated:** 2024
**Version:** 2.0
