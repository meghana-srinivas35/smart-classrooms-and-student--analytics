#!/usr/bin/env python3
"""
Add subject column to users table for teacher section assignment
"""

import pymysql
import sys

def add_subject_column():
    """Add subject column to users table"""
    try:
        # Connect to MySQL database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='smart_classrooms',
            charset='utf8mb4'
        )
        
        with connection.cursor() as cursor:
            # Check if subject column already exists
            cursor.execute("""
                SELECT COUNT(*) 
                FROM INFORMATION_SCHEMA.COLUMNS 
                WHERE TABLE_SCHEMA = 'smart_classrooms' 
                AND TABLE_NAME = 'users' 
                AND COLUMN_NAME = 'subject'
            """)
            
            column_exists = cursor.fetchone()[0]
            
            if column_exists == 0:
                # Add subject column
                cursor.execute("""
                    ALTER TABLE users 
                    ADD COLUMN subject VARCHAR(100) NULL 
                    COMMENT 'Primary subject for teachers'
                """)
                
                # Also update section column to allow longer values for multiple sections
                cursor.execute("""
                    ALTER TABLE users 
                    MODIFY COLUMN section VARCHAR(50) NULL 
                    COMMENT 'For students: single section, For teachers: comma-separated sections'
                """)
                
                connection.commit()
                print("✅ Successfully added 'subject' column to users table")
                print("✅ Updated 'section' column to support multiple sections")
            else:
                print("ℹ️  'subject' column already exists in users table")
        
        connection.close()
        print("✅ Database migration completed successfully!")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    print("🔄 Adding subject column to users table...")
    add_subject_column()