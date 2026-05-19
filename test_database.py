"""
Test Database Connection
Quick script to verify MySQL connection and tables
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from app import create_app
from core.models import db, User

def test_connection():
    print("\n" + "="*60)
    print("  Testing Database Connection")
    print("="*60 + "\n")
    
    app = create_app()
    
    with app.app_context():
        try:
            # Test connection
            db.engine.connect()
            print("✅ Database connection successful!")
            
            # Check if tables exist
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            
            print(f"\n📊 Found {len(tables)} tables:")
            for table in tables:
                print(f"   - {table}")
            
            # Check users table
            if 'users' in tables:
                user_count = User.query.count()
                print(f"\n👥 Users in database: {user_count}")
                
                if user_count > 0:
                    print("\n📝 Sample users:")
                    users = User.query.limit(5).all()
                    for user in users:
                        print(f"   - {user.name} ({user.email}) - {user.role}")
            else:
                print("\n⚠️  'users' table not found!")
                print("   Run: python setup_database.py")
            
            print("\n" + "="*60)
            print("✅ Database is ready to use!")
            print("="*60 + "\n")
            
        except Exception as e:
            print(f"\n❌ Database connection failed!")
            print(f"Error: {str(e)}")
            print("\nTroubleshooting:")
            print("1. Make sure XAMPP MySQL is running")
            print("2. Create database: CREATE DATABASE smart_classrooms;")
            print("3. Check credentials in backend/config/config.py")
            print("4. Run: python setup_database.py")
            print("\n" + "="*60 + "\n")

if __name__ == '__main__':
    test_connection()
