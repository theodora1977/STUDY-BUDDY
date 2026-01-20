#!/usr/bin/env python3
"""
Study Buddy Setup Script
Helps configure the application for first-time use
"""

import os
import sys
from pathlib import Path

def setup_email_config():
    """Interactive email configuration"""
    print("\n📧 Email Configuration for OTP")
    print("=" * 40)

    configure_email = input("Do you want to configure email for OTP? (y/n): ").lower().strip()

    if configure_email != 'y':
        print("✅ Skipping email configuration. OTP codes will be shown in API responses for testing.")
        return

    print("\n🔑 Gmail Setup Instructions:")
    print("1. Go to https://myaccount.google.com/apppasswords")
    print("2. Enable 2-Step Verification if not already enabled")
    print("3. Generate an app password for 'Study Buddy'")
    print("4. Copy the 16-character password\n")

    mail_username = input("Enter your Gmail address: ").strip()
    mail_password = input("Enter your Gmail app password: ").strip()

    if not mail_username or not mail_password:
        print("❌ Email configuration cancelled.")
        return

    # Update .env file
    env_path = Path(".env")
    env_content = env_path.read_text() if env_path.exists() else ""

    # Remove existing mail config
    lines = env_content.split('\n')
    lines = [line for line in lines if not line.startswith('MAIL_')]

    # Add new mail config
    lines.extend([
        f"MAIL_USERNAME={mail_username}",
        f"MAIL_PASSWORD={mail_password}",
        f"MAIL_FROM={mail_username}",
        "MAIL_PORT=587",
        "MAIL_SERVER=smtp.gmail.com",
        "MAIL_TLS=True",
        "MAIL_SSL=False"
    ])

    env_path.write_text('\n'.join(lines))
    print("✅ Email configuration saved to .env file")

def check_dependencies():
    """Check if required packages are installed"""
    print("🔍 Checking dependencies...")

    try:
        import fastapi
        import uvicorn
        import sqlalchemy
        import fastapi_mail
        print("✅ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Run: pip install -r requirements.txt")
        return False

def main():
    print("🎓 Study Buddy Setup")
    print("=" * 30)

    # Check if we're in the right directory
    if not Path("main.py").exists():
        print("❌ Please run this script from the project root directory")
        sys.exit(1)

    # Check dependencies
    if not check_dependencies():
        sys.exit(1)

    # Setup email
    setup_email_config()

    print("\n🚀 Setup Complete!")
    print("Run the server with: uvicorn main:app --reload --host localhost --port 8000")
    print("API Documentation: http://localhost:8000/docs")

if __name__ == "__main__":
    main()