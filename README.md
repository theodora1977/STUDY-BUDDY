# Study Buddy - Study App

A full-stack study application with FastAPI backend and React frontend, featuring OTP authentication and progress tracking.

## 🚀 Quick Start

### Backend Setup

1. **Install Python dependencies**:
   ```bash
   pip install -r requirement.txt
   ```

2. **Configure Email (Optional)**:
   For OTP functionality, configure Gmail SMTP:

   #### Generate Gmail App Password:
   1. Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
   2. Enable 2-Step Verification if not already enabled
   3. Generate an app password for "Study Buddy"

   #### Configure via API:
   ```bash
   curl -X POST "http://localhost:8000/admin/config/email" \
     -H "Content-Type: application/json" \
     -d '{
       "mail_username": "your_email@gmail.com",
       "mail_password": "your_app_password",
       "mail_from": "your_email@gmail.com"
     }'
   ```

   Or manually edit `.env` file:
   ```
   MAIL_USERNAME=your_email@gmail.com
   MAIL_PASSWORD=your_app_password
   MAIL_FROM=your_email@gmail.com
   ```

3. **Run the Backend Server**:
   ```bash
   uvicorn main:app --reload --host localhost --port 8000
   ```

### Frontend Setup

1. **Install Node.js** (if not already installed):
   ```bash
   winget install OpenJS.NodeJS
   ```

2. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

3. **Install dependencies**:
   ```bash
   npm install
   ```

4. **Start the Frontend**:
   ```bash
   npm run dev
   ```

5. **Access the Application**:
   - **Frontend**: http://localhost:5173
   - **Backend API**: http://localhost:8000
   - **API Documentation**: http://localhost:8000/docs

## 📧 Email Configuration

### For Development/Testing:
If email is not configured, OTP codes will be returned directly in the API response for testing.

### For Production:
Configure Gmail SMTP as described above. The app will automatically send OTP emails.

### Admin Endpoints:
- `GET /admin/config` - Check current email configuration
- `POST /admin/config/email` - Update email settings

## 📧 Email Configuration

### For Development/Testing:
If email is not configured, OTP codes will be returned directly in the API response for testing.

### For Production:
Configure Gmail SMTP as described above. The app will automatically send OTP emails.

### Admin Endpoints:
- `GET /admin/config` - Check current email configuration
- `POST /admin/config/email` - Update email settings

## 🔐 Authentication Flow

1. **Send OTP**: `POST /auth/send-otp?identifier=user@email.com`
2. **Verify OTP**: `POST /auth/verify-otp` with identifier and code
3. **Access Protected Routes**: Use the returned JWT token

## 🎨 Frontend Features

The React frontend provides a complete user interface:

- **📱 Responsive Design**: Works on desktop, tablet, and mobile
- **🔐 OTP Authentication**: Secure login with email verification
- **📚 Subject Dashboard**: Browse available subjects and topics
- **❓ Interactive Quizzes**: Answer questions with real-time feedback
- **📊 Progress Tracking**: View detailed learning statistics
- **🎯 Real-time Updates**: Progress updates during quiz sessions

### Frontend Pages:
- **Login** (`/login`) - OTP-based authentication
- **Dashboard** (`/`) - Subject and topic overview
- **Quiz** (`/quiz/:topicId`) - Interactive question interface
- **Progress** (`/progress`) - Learning analytics and statistics

## 📚 API Endpoints

- `GET /` - Health check
- `GET /subjects` - List all subjects
- `GET /subjects/{id}/topics` - Get topics for a subject
- `GET /topics/{id}/questions` - Get questions for a topic
- `POST /progress` - Update user progress (requires auth)
- `GET /progress` - Get user progress (requires auth)
- `POST /auth/send-otp` - Send OTP for authentication
- `POST /auth/verify-otp` - Verify OTP and login
- `GET /admin/config` - Check email configuration
- `POST /admin/config/email` - Update email settings

## 🗄️ Database

The app uses SQLite by default. Database file is created automatically on first run.

## 🔧 Environment Variables

```env
DATABASE_URL=sqlite:///./study_app.db
SECRET_KEY=your_secret_key_here
MAIL_USERNAME=your_gmail@gmail.com
MAIL_PASSWORD=your_app_password
MAIL_FROM=your_gmail@gmail.com
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
MAIL_TLS=True
MAIL_SSL=False
```