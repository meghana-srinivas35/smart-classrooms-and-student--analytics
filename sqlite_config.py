# Quick SQLite Alternative Configuration
# Update your backend/config/config.py with this if MySQL keeps failing

import os

class Config:
    # SQLite Database (no server needed)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///smart_classrooms.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Keep other settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # CORS settings
    CORS_ORIGINS = ["http://localhost:3000"]

# This creates a local file database instead of requiring MySQL server