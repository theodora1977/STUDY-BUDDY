# Study Buddy Frontend

A modern React frontend for the Study Buddy study application.

## 🚀 Features

- **Authentication**: OTP-based login system
- **Dashboard**: Browse subjects and topics
- **Quiz Interface**: Interactive question answering
- **Progress Tracking**: View learning statistics and progress
- **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Tech Stack

- **React 18** with TypeScript
- **Vite** for build tooling
- **Tailwind CSS** for styling
- **React Router** for navigation
- **Axios** for API calls

## 📦 Installation

1. **Install Node.js** (if not already installed):
   ```bash
   winget install OpenJS.NodeJS
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm run dev
   ```

4. **Open your browser** and navigate to `http://localhost:5173`

## 🔧 Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## 🌐 API Integration

The frontend connects to the FastAPI backend running on `http://localhost:8000`. Make sure the backend is running before using the frontend.

### Key API Endpoints Used:

- `POST /auth/send-otp` - Send OTP for authentication
- `POST /auth/verify-otp` - Verify OTP and login
- `GET /subjects` - Get all subjects
- `GET /subjects/{id}/topics` - Get topics for a subject
- `GET /topics/{id}/questions` - Get questions for a topic
- `POST /progress` - Update user progress
- `GET /progress` - Get user progress

## 🎨 UI Components

The application includes the following main pages:

1. **Login** (`/login`) - OTP authentication
2. **Dashboard** (`/`) - Subject and topic overview
3. **Quiz** (`/quiz/:topicId`) - Question answering interface
4. **Progress** (`/progress`) - Learning statistics

## 🔐 Authentication Flow

1. User enters email address
2. OTP is sent to email (or returned in response for testing)
3. User enters OTP to verify
4. JWT token is stored for subsequent requests
5. Protected routes require valid authentication

## 📱 Responsive Design

The application is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones

## 🐛 Development Notes

- The frontend uses a proxy configuration to forward API calls to the backend
- Authentication state is managed with React Context
- Progress is tracked in real-time during quiz sessions
- Error handling is implemented for network requests

## 🎨 Customization

### Branding Colors
To change the application's color scheme, modify the `tailwind.config.js` file. You can update the `theme.extend.colors` section to use your preferred brand colors.

### Logo & Images
To update the logo, replace the image file in `src/assets/` or `public/`. You may also need to update the import path in the main layout component (typically `src/components/Layout.tsx` or `src/components/Navbar.tsx`).

## 🚀 Production Deployment

To build for production:

```bash
npm run build
```

The built files will be in the `dist` directory and can be served by any static file server.