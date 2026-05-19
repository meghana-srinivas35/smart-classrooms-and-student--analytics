import sqlite3
import os
from datetime import datetime

def check_database():
    db_path = 'instance/smart_classrooms.db'
    
    if not os.path.exists(db_path):
        print("❌ Database file not found!")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("=" * 60)
    print(f"DATABASE STATUS CHECK - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Check Users
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]
    print(f"USERS: {user_count} records")
    
    if user_count > 0:
        cursor.execute("SELECT name, email, role FROM users ORDER BY id DESC LIMIT 3")
        recent_users = cursor.fetchall()
        print("   Recent users:")
        for user in recent_users:
            print(f"   - {user[0]} ({user[1]}) - {user[2]}")
    
    # Check Attendance
    cursor.execute("SELECT COUNT(*) FROM attendance")
    attendance_count = cursor.fetchone()[0]
    print(f"ATTENDANCE: {attendance_count} records")
    
    if attendance_count > 0:
        cursor.execute("SELECT student_id, subject, date, status FROM attendance ORDER BY id DESC LIMIT 3")
        recent_attendance = cursor.fetchall()
        print("   Recent attendance:")
        for att in recent_attendance:
            print(f"   - Student {att[0]}: {att[1]} on {att[2]} - {att[3]}")
    
    # Check Resources
    cursor.execute("SELECT COUNT(*) FROM resources")
    resource_count = cursor.fetchone()[0]
    print(f"RESOURCES: {resource_count} records")
    
    if resource_count > 0:
        cursor.execute("SELECT title, subject, uploaded_by FROM resources ORDER BY id DESC LIMIT 3")
        recent_resources = cursor.fetchall()
        print("   Recent resources:")
        for res in recent_resources:
            print(f"   - {res[0]} ({res[1]}) by {res[2]}")
    
    # Check Assignments
    cursor.execute("SELECT COUNT(*) FROM assignments")
    assignment_count = cursor.fetchone()[0]
    print(f"ASSIGNMENTS: {assignment_count} records")
    
    if assignment_count > 0:
        cursor.execute("SELECT title, subject, created_by FROM assignments ORDER BY id DESC LIMIT 3")
        recent_assignments = cursor.fetchall()
        print("   Recent assignments:")
        for ass in recent_assignments:
            print(f"   - {ass[0]} ({ass[1]}) by {ass[2]}")
    
    # Check Assignment Submissions
    cursor.execute("SELECT COUNT(*) FROM assignment_submissions")
    submission_count = cursor.fetchone()[0]
    print(f"SUBMISSIONS: {submission_count} records")
    
    # Check Timetables
    cursor.execute("SELECT COUNT(*) FROM timetables")
    timetable_count = cursor.fetchone()[0]
    print(f"TIMETABLES: {timetable_count} records")
    
    # Check Results
    cursor.execute("SELECT COUNT(*) FROM results")
    result_count = cursor.fetchone()[0]
    print(f"RESULTS: {result_count} records")
    
    print("=" * 60)
    total_records = user_count + attendance_count + resource_count + assignment_count + submission_count + timetable_count + result_count
    print(f"TOTAL RECORDS: {total_records}")
    print("=" * 60)
    
    conn.close()

if __name__ == "__main__":
    check_database()