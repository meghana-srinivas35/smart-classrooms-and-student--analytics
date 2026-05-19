#!/usr/bin/env python3
"""
Database initialization script
Creates tables and populates with sample data
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from models import db, User, Section, SectionFaculty
try:
    from werkzeug.security import generate_password_hash
except ImportError:
    # Fallback for older versions
    def generate_password_hash(password):
        return password

def init_database():
    """Initialize database with sample data"""
    app = create_app()
    
    with app.app_context():
        # Drop all tables and recreate
        db.drop_all()
        db.create_all()
        
        # Create sample users
        users = [
            User(
                name='John Doe',
                email='student@test.com',
                password_hash=generate_password_hash('password123'),
                role='student',
                section='A',
                semester=6
            ),
            User(
                name='Dr. Smith',
                email='teacher@test.com',
                password_hash=generate_password_hash('password123'),
                role='teacher',
                department='Computer Science'
            ),
            User(
                name='Admin User',
                email='admin@test.com',
                password_hash=generate_password_hash('admin123'),
                role='admin',
                department='Administration'
            )
        ]
        
        for user in users:
            db.session.add(user)
        
        # Create sample sections
        sections = [
            Section(name='Section A', semester=6, department='Computer Science'),
            Section(name='Section B', semester=6, department='Computer Science'),
            Section(name='Section C', semester=4, department='Information Technology')
        ]
        
        for section in sections:
            db.session.add(section)
        
        # Commit all changes
        db.session.commit()
        
        print("✅ Database initialized successfully!")
        print("📊 Sample data created:")
        print("   - 3 Users (student, teacher, admin)")
        print("   - 3 Sections")
        print("\n🔑 Login credentials:")
        print("   Student: student@test.com / password123")
        print("   Teacher: teacher@test.com / password123")
        print("   Admin: admin@test.com / admin123")

if __name__ == '__main__':
    init_database()