# Database Setup Instructions

## Prerequisites
1. **XAMPP** installed and running
2. **MySQL** service started in XAMPP Control Panel

## Setup Steps

### 1. Create Database
Open phpMyAdmin (http://localhost/phpmyadmin) or MySQL command line and run:

```sql
CREATE DATABASE smart_classrooms CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 2. Install Python Dependencies
Make sure all required packages are installed:

```bash
cd backend
pip install -r requirements.txt
```

### 3. Start Backend Server
The database tables will be created automatically when you start the server:

```bash
cd backend
python app.py
```

The server will:
- ✅ Connect to MySQL database
- ✅ Create all tables automatically
- ✅ Seed default users (student, teacher, admin)
- ✅ Ready to use!

### 4. Default Login Credentials

**Student Account:**
- Email: student@test.com
- Password: password123
- Role: student

**Teacher Account:**
- Email: teacher@test.com
- Password: password123
- Role: teacher

**Admin Account:**
- Email: admin@test.com
- Password: admin123
- Role: admin

## Database Configuration

The database connection is configured in `backend/config/config.py`:

```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/smart_classrooms'
```

**Format:** `mysql+pymysql://username:password@host:port/database_name`

If your MySQL has a password, update it:
```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:your_password@localhost:3306/smart_classrooms'
```

## Database Tables

The following tables will be created automatically:

1. **users** - Student, teacher, and admin accounts
2. **attendance** - Attendance records
3. **timetables** - Class schedules
4. **timetable_images** - Uploaded timetable images
5. **resources** - Study materials and resources
6. **assignments** - Assignment details
7. **assignment_submissions** - Student submissions
8. **results** - Exam results and grades
9. **support_queries** - Support tickets

## Troubleshooting

### Error: "Can't connect to MySQL server"
- Make sure XAMPP MySQL service is running
- Check if port 3306 is not blocked
- Verify MySQL credentials in config.py

### Error: "Access denied for user"
- Check MySQL username and password in config.py
- Default XAMPP MySQL has username 'root' with no password

### Error: "Unknown database 'smart_classrooms'"
- Create the database first using phpMyAdmin or MySQL command line
- Run: `CREATE DATABASE smart_classrooms;`

## Reset Database

If you need to reset the database (delete all data and recreate tables):

```python
# In Python console or create a script
from app import create_app
from core.init_db import reset_database

app = create_app()
reset_database(app)
```

## Backup Database

To backup your database:

```bash
# Using mysqldump
mysqldump -u root -p smart_classrooms > backup.sql

# Restore from backup
mysql -u root -p smart_classrooms < backup.sql
```

## Production Notes

For production deployment:

1. **Change default passwords** in seed data
2. **Use password hashing** (bcrypt or similar)
3. **Enable SSL** for database connections
4. **Set strong SECRET_KEY** in config
5. **Use environment variables** for sensitive data
6. **Enable database backups**
7. **Set up proper user permissions**

## All Set! 🎉

Your Smart Classrooms Analytics is now connected to MySQL database. All data will persist across server restarts!
