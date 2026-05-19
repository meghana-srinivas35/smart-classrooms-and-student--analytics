import sqlite3
import time
import os
from datetime import datetime

def watch_database():
    db_path = 'instance/smart_classrooms.db'
    
    if not os.path.exists(db_path):
        print("Database file not found!")
        return
    
    print("=== LIVE DATABASE WATCHER ===")
    print("Monitoring database changes... (Press Ctrl+C to stop)")
    print("=" * 50)
    
    # Store previous counts
    prev_counts = {}
    
    try:
        while True:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Get current counts
            tables = ['users', 'attendance', 'resources', 'assignments', 'assignment_submissions', 'timetables', 'results']
            current_counts = {}
            
            for table in tables:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                current_counts[table] = cursor.fetchone()[0]
            
            # Check for changes
            changes_detected = False
            for table, count in current_counts.items():
                if table in prev_counts and prev_counts[table] != count:
                    change = count - prev_counts[table]
                    timestamp = datetime.now().strftime('%H:%M:%S')
                    print(f"[{timestamp}] {table.upper()}: {prev_counts[table]} -> {count} ({'+' if change > 0 else ''}{change})")
                    changes_detected = True
            
            if changes_detected:
                # Show recent data from changed tables
                for table, count in current_counts.items():
                    if table in prev_counts and prev_counts[table] != count:
                        if table == 'users':
                            cursor.execute("SELECT name, email, role FROM users ORDER BY id DESC LIMIT 1")
                            user = cursor.fetchone()
                            if user:
                                print(f"   Latest user: {user[0]} ({user[1]}) - {user[2]}")
                        elif table == 'attendance':
                            cursor.execute("SELECT student_id, subject, status FROM attendance ORDER BY id DESC LIMIT 1")
                            att = cursor.fetchone()
                            if att:
                                print(f"   Latest attendance: Student {att[0]} - {att[1]} - {att[2]}")
                        elif table == 'resources':
                            cursor.execute("SELECT title, subject FROM resources ORDER BY id DESC LIMIT 1")
                            res = cursor.fetchone()
                            if res:
                                print(f"   Latest resource: {res[0]} ({res[1]})")
                print("-" * 50)
            
            prev_counts = current_counts.copy()
            conn.close()
            
            time.sleep(2)  # Check every 2 seconds
            
    except KeyboardInterrupt:
        print("\nDatabase monitoring stopped.")

if __name__ == "__main__":
    watch_database()