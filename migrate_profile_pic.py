"""
Database Migration - Add Profile Picture Column
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from app import create_app
from core.models import db

def migrate():
    print("\n" + "="*60)
    print("  Database Migration - Add Profile Picture")
    print("="*60)
    
    app = create_app()
    
    with app.app_context():
        try:
            # Add profile_picture column to users table
            print("\n🔄 Adding profile_picture column to users table...")
            
            db.engine.execute("""
                ALTER TABLE users 
                ADD COLUMN IF NOT EXISTS profile_picture TEXT
            """)
            
            print("✅ Profile picture column added successfully!")
            print("\n" + "="*60)
            print("✅ Migration complete!")
            print("="*60 + "\n")
            
        except Exception as e:
            print(f"\n❌ Migration error: {e}")
            print("\nNote: If column already exists, this is normal.")
            print("="*60 + "\n")

if __name__ == '__main__':
    migrate()
