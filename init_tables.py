"""
Simple Database Initialization
Assumes database already exists, just creates tables
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from app import create_app
from core.models import db, User

def init_tables():
    print("\n" + "="*60)
    print("  Creating Database Tables")
    print("="*60)
    
    app = create_app()
    
    with app.app_context():
        try:
            # Drop all tables first
            print("\n🗑️  Dropping old tables...")
            db.drop_all()
            print("✅ Old tables dropped")
            
            # Create all tables
            print("\n📦 Creating new tables...")
            db.create_all()
            print("✅ All tables created successfully!")
            
            # Create default users
            print("\n👥 Creating default users...")
            
            default_users = [
                User(
                    name='John Doe',
                    email='student@test.com',
                    password='password123',
                    role='student',
                    section='A',
                    semester=6,
                    enrollment_number='CS2021001',
                    status='active'
                ),
                User(
                    name='Dr. Smith',
                    email='teacher@test.com',
                    password='password123',
                    role='teacher',
                    department='Computer Science',
                    employee_id='FAC001',
                    status='active'
                ),
                User(
                    name='Admin User',
                    email='admin@test.com',
                    password='admin123',
                    role='admin',
                    department='Administration',
                    status='active'
                )
            ]
            
            for user in default_users:
                db.session.add(user)
            
            db.session.commit()
            print("✅ Default users created!")
            
            # Verify
            user_count = User.query.count()
            print(f"\n📊 Total users in database: {user_count}")
            
            print("\n" + "="*60)
            print("🎉 SUCCESS! Database is ready!")
            print("="*60)
            print("\n📝 Default login credentials:")
            print("   Student: student@test.com / password123")
            print("   Teacher: teacher@test.com / password123")
            print("   Admin: admin@test.com / admin123")
            print("\n" + "="*60 + "\n")
            
        except Exception as e:
            print(f"\n❌ Error: {e}")
            import traceback
            print(traceback.format_exc())
            print("\nMake sure:")
            print("1. XAMPP MySQL is running")
            print("2. Database 'smart_classrooms' exists")
            print("3. Run this in phpMyAdmin first:")
            print("   DROP DATABASE IF EXISTS smart_classrooms;")
            print("   CREATE DATABASE smart_classrooms;")
            print("\n" + "="*60 + "\n")

if __name__ == '__main__':
    init_tables()
