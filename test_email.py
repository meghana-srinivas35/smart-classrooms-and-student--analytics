#!/usr/bin/env python3
"""
Simple email test script to debug Gmail SMTP issues
"""
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_email():
    # Get credentials from environment
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
    SENDER_EMAIL = os.getenv('SENDER_EMAIL')
    SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')
    
    print(f"Testing email with:")
    print(f"SMTP Server: {SMTP_SERVER}")
    print(f"SMTP Port: {SMTP_PORT}")
    print(f"Sender Email: {SENDER_EMAIL}")
    print(f"Password: {'*' * len(SENDER_PASSWORD) if SENDER_PASSWORD else 'NOT SET'}")
    print("-" * 50)
    
    if not SENDER_EMAIL or not SENDER_PASSWORD:
        print("ERROR: Email credentials not found in environment variables")
        return False
    
    try:
        # Create a simple test message
        message = MIMEMultipart()
        message['Subject'] = 'Test Email - Smart Classrooms Analytics'
        message['From'] = SENDER_EMAIL
        message['To'] = SENDER_EMAIL  # Send to yourself for testing
        
        # Simple text body
        body = """
        This is a test email from Smart Classrooms Analytics.
        
        If you receive this email, the SMTP configuration is working correctly!
        
        Best regards,
        Smart Classrooms Analytics Team
        """
        
        message.attach(MIMEText(body, 'plain'))
        
        print("Attempting to send test email...")
        
        # Connect and send
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            print("Connecting to SMTP server...")
            server.set_debuglevel(1)  # Enable debug output
            
            print("Starting TLS...")
            server.starttls()
            
            print("Logging in...")
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            
            print("Sending message...")
            server.send_message(message)
            
        print("SUCCESS: Test email sent successfully!")
        print(f"Check your inbox at {SENDER_EMAIL}")
        return True
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Make sure 2-Factor Authentication is enabled on your Gmail")
        print("2. Generate a new App Password from Google Account settings")
        print("3. Use the 16-character app password (not your regular Gmail password)")
        print("4. Check if 'Less secure app access' is disabled (it should be)")
        return False

if __name__ == "__main__":
    print("Smart Classrooms Analytics - Email Test")
    print("=" * 50)
    test_email()