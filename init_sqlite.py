from flask import Flask
from config.config import Config
from werkzeug.security import generate_password_hash

# Create Flask app and configure database
app = Flask(__name__)
app.config.from_object(Config)

# Import models and db
from core.models import db, User

# Initialize db with app
db.init_app(app)

with app.app_context():
    # Initialize database
    db.create_all()
    
    # Create admin user
    admin = User(
        name='System Administrator',
        email='admin@smartclassroom.com',
        password=generate_password_hash('admin123'),
        role='admin'
    )
    
    # Create teacher
    teacher = User(
        name='John Teacher',
        email='teacher@smartclassroom.com',
        password=generate_password_hash('teacher123'),
        role='teacher',
        section='A,B',
        subject='Mathematics'
    )
    
    # Create student
    student = User(
        name='Jane Student',
        email='student@smartclassroom.com',
        password=generate_password_hash('student123'),
        role='student',
        section='A'
    )
    
    db.session.add_all([admin, teacher, student])
    db.session.commit()
    
    print("SQLite database initialized successfully!")
    print("Admin: admin@smartclassroom.com/admin123")
    print("Teacher: teacher@smartclassroom.com/teacher123")
    print("Student: student@smartclassroom.com/student123")