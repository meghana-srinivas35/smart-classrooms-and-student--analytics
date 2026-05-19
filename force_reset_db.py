"""
Force Database Reset Script
Drops and recreates the entire database
"""
import pymysql
import sys
import os

# Database configuration
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''  # Empty for default XAMPP
DB_NAME = 'smart_classrooms'

def force_reset():
    print("\n" + "="*60)
    print("  FORCE DATABASE RESET")
    print("="*60)
    
    try:
        # Connect to MySQL (without selecting database)
        print("\n🔄 Connecting to MySQL...")
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = connection.cursor()
        
        # Drop database if exists
        print(f"🗑️  Dropping database '{DB_NAME}' if exists...")
        cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME}")
        print("✅ Database dropped")
        
        # Create fresh database
        print(f"📦 Creating fresh database '{DB_NAME}'...")
        cursor.execute(f"CREATE DATABASE {DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        print("✅ Database created")
        
        cursor.close()
        connection.close()
        
        print("\n" + "="*60)
        print("✅ Database reset complete!")
        print("="*60)
        
        # Now initialize with tables
        print("\n🔄 Creating tables and seeding data...")
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))
        
        from app import create_app
        from core.models import db
        from core.init_db import seed_default_data
        
        app = create_app()
        
        with app.app_context():
            # Create all tables
            db.create_all()
            print("✅ All tables created successfully!")
            
            # Seed default data
            seed_default_data()
            print("✅ Default data seeded!")
            
            # Verify
            from core.models import User
            user_count = User.query.count()
            print(f"\n👥 Total users in database: {user_count}")
            
            if user_count > 0:
                print("\n📝 Default users:")
                users = User.query.all()
                for user in users:
                    print(f"   - {user.name} ({user.email}) - {user.role}")
        
        print("\n" + "="*60)
        print("🎉 SUCCESS! Database is ready to use!")
        print("="*60)
        print("\n📝 Default login credentials:")
        print("   Student: student@test.com / password123")
        print("   Teacher: teacher@test.com / password123")
        print("   Admin: admin@test.com / admin123")
        print("\n" + "="*60 + "\n")
        
    except pymysql.err.OperationalError as e:
        print(f"\n❌ MySQL Connection Error: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure XAMPP MySQL is running")
        print("2. Check MySQL is on port 3306")
        print("3. Verify username is 'root' with no password")
        print("\n" + "="*60 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        print(traceback.format_exc())
        print("\n" + "="*60 + "\n")

if __name__ == '__main__':
    print("\n⚠️  WARNING: This will DELETE all data in the database!")
    confirm = input("Type 'YES' to continue: ").strip()
    
    if confirm == 'YES':
        force_reset()
    else:
        print("\n❌ Reset cancelled.")
