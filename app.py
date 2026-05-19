"""DEPRECATED - This file has been moved to backend/app.py
Please use: python backend/app.py
"""
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from backend.app import create_app

if __name__ == '__main__':
    print("⚠️  WARNING: Running from old location")
    print("✅ Please use: python backend/app.py")
    print("")
    app = create_app()
    app.run(debug=True)