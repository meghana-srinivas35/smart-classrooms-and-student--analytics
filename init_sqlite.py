#!/usr/bin/env python3
"""
Initialize SQLite database with sample data
Run this after switching to SQLite
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.app import app
from backend.core.models import db, User

def init_sqlite_db():
    """Initialize SQLite database with sample data"""
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Check if admin already exists
        admin = User.query.filter_by(email='admin@school.edu').first()
        if not admin:
            # Create admin user
            admin = User(
                name='Admin User',
                email='admin@school.edu',
                password='admin123',
                role='admin',
                department='Administration',
                status='active'
            )
            db.session.add(admin)
        
        # Create sample teacher
        teacher = User.query.filter_by(email='john.smith@school.edu').first()
        if not teacher:
            teacher = User(
                name='John Smith',
                email='john.smith@school.edu',
                password='teacher123',
                role='teacher',
                department='Mathematics',
                section='A,B',
                subject='Mathematics',
                status='active'
            )
            db.session.add(teacher)
        
        # Create sample students
        students_data = [
            ('Alice Johnson', 'alice@student.edu', 'A'),
            ('Bob Wilson', 'bob@student.edu', 'A'),
            ('Carol Davis', 'carol@student.edu', 'B'),
            ('David Brown', 'david@student.edu', 'B'),
        ]
        
        for name, email, section in students_data:
            student = User.query.filter_by(email=email).first()
            if not student:
                student = User(
                    name=name,
                    email=email,
                    password='student123',
                    role='student',
                    department='Computer Science',
                    section=section,
                    semester=6,
                    enrollment_number=f'STU{hash(email) % 10000:04d}',
                    status='active'
                )
                db.session.add(student)
        
        db.session.commit()
        print("✅ SQLite database initialized successfully!")
        print("📊 Sample data created:")
        print("   👤 Admin: admin@school.edu / admin123")
        print("   👨‍🏫 Teacher: john.smith@school.edu / teacher123 (Sections: A,B)")
        print("   👨‍🎓 Students: alice@student.edu, bob@student.edu, etc. / student123")

if __name__ == "__main__":
    init_sqlite_db()