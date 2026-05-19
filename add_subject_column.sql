-- Add subject column to users table for teacher section assignment
-- Run this in phpMyAdmin or MySQL command line

-- Check if subject column exists and add it if not
ALTER TABLE users 
ADD COLUMN IF NOT EXISTS subject VARCHAR(100) NULL 
COMMENT 'Primary subject for teachers';

-- Update section column to support multiple sections
ALTER TABLE users 
MODIFY COLUMN section VARCHAR(50) NULL 
COMMENT 'For students: single section, For teachers: comma-separated sections';

-- Verify the changes
DESCRIBE users;