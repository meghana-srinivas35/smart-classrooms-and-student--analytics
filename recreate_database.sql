-- Complete database recreation script for Smart Classrooms Analytics
-- Run this in phpMyAdmin after MySQL reset

CREATE DATABASE IF NOT EXISTS smart_classrooms;
USE smart_classrooms;

-- Users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL COMMENT 'student, teacher, admin',
    section VARCHAR(50) NULL COMMENT 'For students: single section, For teachers: comma-separated sections',
    semester INT NULL,
    enrollment_number VARCHAR(50) NULL,
    department VARCHAR(100) NULL,
    employee_id VARCHAR(50) NULL,
    subject VARCHAR(100) NULL COMMENT 'Primary subject for teachers',
    status VARCHAR(20) DEFAULT 'active',
    profile_picture TEXT NULL COMMENT 'Base64 encoded image',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Attendance table
CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(50) NOT NULL,
    subject VARCHAR(100) NOT NULL,
    date DATE NOT NULL,
    status VARCHAR(20) NOT NULL COMMENT 'present, absent, late',
    marked_by VARCHAR(50) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Assignments table
CREATE TABLE assignments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT NULL,
    subject VARCHAR(100) NOT NULL,
    section VARCHAR(10) NULL,
    semester INT NULL,
    due_date DATETIME NULL,
    total_marks INT NULL,
    created_by VARCHAR(50) NULL,
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Assignment submissions table
CREATE TABLE assignment_submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    assignment_id INT NOT NULL,
    student_id VARCHAR(50) NOT NULL,
    submission_text TEXT NULL,
    file_url VARCHAR(500) NULL,
    marks_obtained INT NULL,
    feedback TEXT NULL,
    status VARCHAR(20) DEFAULT 'submitted',
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    graded_at TIMESTAMP NULL,
    FOREIGN KEY (assignment_id) REFERENCES assignments(id) ON DELETE CASCADE
);

-- Resources table
CREATE TABLE resources (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subject VARCHAR(100) NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT NULL,
    file_url VARCHAR(500) NOT NULL,
    file_type VARCHAR(50) NULL,
    uploaded_by VARCHAR(50) NULL,
    section VARCHAR(10) NULL,
    semester INT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Timetables table
CREATE TABLE timetables (
    id INT AUTO_INCREMENT PRIMARY KEY,
    division VARCHAR(50) NOT NULL,
    day VARCHAR(20) NOT NULL,
    time_slot VARCHAR(50) NOT NULL,
    subject VARCHAR(100) NOT NULL,
    teacher VARCHAR(100) NULL,
    room VARCHAR(50) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Timetable images table
CREATE TABLE timetable_images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    division VARCHAR(50) UNIQUE NOT NULL,
    image_data TEXT NOT NULL COMMENT 'Base64 encoded',
    uploaded_by VARCHAR(50) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Results table
CREATE TABLE results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(50) NOT NULL,
    subject VARCHAR(100) NOT NULL,
    exam_type VARCHAR(50) NULL COMMENT 'midterm, final, quiz',
    marks_obtained INT NULL,
    total_marks INT NULL,
    grade VARCHAR(5) NULL,
    semester INT NULL,
    academic_year VARCHAR(20) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Support queries table
CREATE TABLE support_queries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    subject VARCHAR(200) NOT NULL,
    message TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'open' COMMENT 'open, in_progress, resolved',
    priority VARCHAR(20) DEFAULT 'medium',
    response TEXT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMP NULL
);

-- Insert default admin user
INSERT INTO users (name, email, password, role, department, status) VALUES 
('Admin User', 'admin@school.edu', 'admin123', 'admin', 'Administration', 'active');

-- Insert sample teacher
INSERT INTO users (name, email, password, role, department, section, subject, status) VALUES 
('John Smith', 'john.smith@school.edu', 'teacher123', 'teacher', 'Mathematics', 'A,B', 'Mathematics', 'active');

-- Insert sample students
INSERT INTO users (name, email, password, role, department, section, semester, enrollment_number, status) VALUES 
('Alice Johnson', 'alice@student.edu', 'student123', 'student', 'Computer Science', 'A', 6, 'STU2024001', 'active'),
('Bob Wilson', 'bob@student.edu', 'student123', 'student', 'Computer Science', 'A', 6, 'STU2024002', 'active'),
('Carol Davis', 'carol@student.edu', 'student123', 'student', 'Computer Science', 'B', 6, 'STU2024003', 'active');

SELECT 'Database recreated successfully!' as Status;