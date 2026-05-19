"""
Database Setup Script
Run this to initialize the MySQL database
"""
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from app import create_app
from core.models import db
from core.init_db import init_database, reset_database

def main():
    print("\n" + "="*60)
    print("  Smart Classrooms Analytics - Database Setup")
    print("="*60)
    
    print("\nOptions:")
    print("1. Initialize database (create tables and seed data)")
    print("2. Reset database (drop all tables and recreate)")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    app = create_app()
    
    if choice == '1':
        print("\n🔄 Initializing database...")
        init_database(app)
        print("\n✅ Database initialized successfully!")
        print("\n📝 Default login credentials:")
        print("   Student: student@test.com / password123")
        print("   Teacher: teacher@test.com / password123")
        print("   Admin: admin@test.com / admin123")
        
    elif choice == '2':
        confirm = input("\n⚠️  This will delete ALL data. Are you sure? (yes/no): ").strip().lower()
        if confirm == 'yes':
            print("\n🔄 Resetting database...")
            reset_database(app)
            print("\n✅ Database reset successfully!")
        else:
            print("\n❌ Reset cancelled.")
            
    elif choice == '3':
        print("\n👋 Goodbye!")
        return
    else:
        print("\n❌ Invalid choice!")
    
    print("\n" + "="*60 + "\n")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure:")
        print("1. XAMPP MySQL is running")
        print("2. Database 'smart_classrooms' exists")
        print("3. MySQL credentials are correct in config.py")
