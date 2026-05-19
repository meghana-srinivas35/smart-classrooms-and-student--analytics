# Smart Classrooms Analytics

## 🏗️ Feature-Based Modular Architecture with SQLite Database

A modern, scalable full-stack web application for smart classroom management with attendance tracking, timetable management, resource sharing, analytics, and AI-powered assistance. **Now with complete SQLite database integration for persistent data storage.**

## ✅ **Latest Updates (v2.0)**
- **Complete SQLite Database Integration** - All data now persists across server restarts
- **Enhanced AI Assistant (AURIX)** - Comprehensive academic knowledge base
- **Email Notification System** - Welcome emails and credential delivery
- **Profile Picture Support** - Database-stored user avatars
- **Production-Ready** - Fully functional with persistent storage

## 🗄️ **Database Status**
- **Type**: SQLite (No server setup required)
- **Location**: `backend/instance/smart_classrooms.db`
- **Tables**: 9 tables with full CRUD operations
- **Sample Data**: Admin, Teacher, and Student accounts included
- **Monitoring**: Real-time database monitoring scripts available

## 📁 Project Structure

```
smart_classrooms_Analytics/
│
├── backend/                          # Backend API (Flask)
│   ├── core/
│   │   └── database.py              # Centralized database
│   │
│   ├── features/                     # Self-contained feature modules
│   │   ├── attendance/              # Attendance management
│   │   ├── timetable/               # Timetable management
│   │   ├── resources/               # Resource management
│   │   └── analytics/               # Analytics & predictions
│   │
│   ├── config/
│   │   └── config.py                # Configuration
│   │
│   ├── app.py                        # Main entry point
│   └── requirements.txt              # Python dependencies
│
├── client/                           # Frontend (React)
│   ├── src/
│   │   ├── components/              # Reusable components
│   │   ├── pages/                   # Page components
│   │   ├── App.js                   # Main app
│   │   └── styles.css               # Global styles
│   │
│   └── package.json                 # Node dependencies
│
├── docs/                             # Documentation
│   ├── FEATURE_ARCHITECTURE.md      # Architecture guide
│   ├── FEATURE_QUICK_START.md       # Quick reference
│   ├── PROJECT_STRUCTURE.md         # Complete structure
│   ├── PROJECT_DOCUMENTATION.md     # Full documentation
│   └── UI_PRESENTATION_GUIDE.md     # UI/UX guide
│
├── start-restructured.bat            # Startup script (Windows)
├── app.py                            # Backward compatibility
└── README.md                         # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn
- **No database server required** (SQLite included)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/viswas369/Smart-Classrooms-and-Student-analytics.git
cd smart_classrooms_Analytics
```

2. **Install backend dependencies**
```bash
cd backend
pip install -r requirements.txt
```

3. **Initialize SQLite database**
```bash
cd backend
python init_sqlite.py
```

4. **Install frontend dependencies**
```bash
cd client
npm install
```

### Running the Application

**Option 1: Use startup script (Windows)**
```bash
start-restructured.bat
```

**Option 2: Manual start**

Terminal 1 - Backend:
```bash
cd backend
python app.py
```

Terminal 2 - Frontend:
```bash
cd client
npm start
```

### Access the Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000
- **Health Check**: http://localhost:5000/health
- **AI Chat**: http://localhost:5000/api/ai/health

### 🔑 **Default Login Credentials**
- **Admin**: admin@smartclassroom.com / admin123
- **Teacher**: teacher@smartclassroom.com / teacher123
- **Student**: student@smartclassroom.com / student123

### 📈 **Monitor Database**
```bash
cd backend
python monitor_db.py  # Check current data
python watch_db.py    # Live monitoring
```

## 🎯 Features

### For Students
- 📊 **Dashboard** - Academic overview, attendance graph, syllabus progress
- 📅 **Timetable** - View class schedule with teacher details
- 📚 **Resources** - Access subject-specific study materials
- 📈 **Analytics** - Track attendance and performance
- 🔔 **Notifications** - Real-time class reminders
- 🤖 **AI Assistant (AURIX)** - Academic help, study tips, assignment guidance
- 🖼️ **Profile Pictures** - Upload and manage profile photos

### For Teachers/Faculty
- 📤 **Upload Timetable** - Upload division-specific timetables
- 📁 **Manage Resources** - Share study materials via Google Drive
- 👥 **Student Management** - View student analytics
- 📊 **Reports** - Generate performance reports
- 📝 **Assignment System** - Create and grade assignments
- 📧 **Email Integration** - Automated credential delivery

### For Admins
- 👤 **User Management** - Manage students and faculty with email notifications
- 📊 **System Analytics** - Overall system statistics
- ⚙️ **Configuration** - System settings
- 📈 **Database Monitoring** - Real-time data insights
- 🤖 **AI Dashboard** - AI-powered admin insights

## 🏗️ Architecture

### Feature-Based Modular Design
Each feature is self-contained with:
- **Routes** - HTTP endpoints
- **Service** - Business logic
- **All code in one place**

Example:
```python
# backend/features/attendance/__init__.py
# Contains: Blueprint + Service + Routes
```

### Benefits
✅ Easy to find code  
✅ Easy to add features  
✅ Easy to test  
✅ Easy to maintain  
✅ Scalable  

## 📡 API Endpoints

### Admin & User Management
- `GET /api/admin/users` - Get all users
- `POST /api/admin/users` - Create new user
- `PUT /api/admin/users/<id>` - Update user (including profile pictures)
- `DELETE /api/admin/users/<id>` - Delete user
- `POST /api/admin/faculty/register` - Register faculty with email

### Attendance
- `POST /api/attendance` - Record attendance
- `GET /api/attendance/<student_id>` - Get student attendance
- `GET /api/attendance/<student_id>/rate` - Get attendance rate

### Resources
- `GET /api/resources` - Get all resources
- `GET /api/resources/<subject>` - Get resource by subject
- `POST /api/resources/upload` - Upload resource
- `DELETE /api/resources/<subject>` - Delete resource

### Assignments
- `GET /api/assignments` - Get assignments
- `POST /api/assignments` - Create assignment
- `POST /api/assignments/<id>/submit` - Submit assignment
- `PUT /api/assignments/<id>/grade` - Grade assignment

### AI Assistant (AURIX)
- `POST /api/ai/chat` - Enhanced AI chatbot
- `POST /api/ai/student-analysis` - Student performance analysis
- `POST /api/ai/class-insights` - Teacher class insights
- `GET /api/ai/admin-dashboard` - AI admin dashboard
- `POST /api/ai/smart-resources` - Resource recommendations
- `POST /api/ai/study-suggestions` - Study suggestions
- `POST /api/ai/assignment-help` - Assignment assistance
- `GET /api/ai/health` - AI service health check

### Timetable
- `GET /api/timetable/<division>` - Get timetable
- `POST /api/timetable/upload-image` - Upload timetable image
- `GET /api/timetable/image/<division>` - Get timetable image
- `GET /api/timetable/divisions` - Get all divisions

### Analytics
- `GET /api/analytics` - Get overall analytics
- `GET /api/analytics/predict-performance` - Predict performance
- `GET /api/analytics/student/<student_id>` - Get student analytics

## 🛠️ Technology Stack

### Backend
- **Flask** - Python web framework
- **SQLAlchemy** - Database ORM
- **SQLite** - Embedded database (no server required)
- **Flask-CORS** - Cross-origin resource sharing
- **Python 3.8+** - Programming language
- **Email Service** - SMTP integration for notifications

### Frontend
- **React 18** - UI library
- **React Bootstrap** - UI components
- **React Router** - Client-side routing
- **Axios** - HTTP client for API calls
- **CSS3** - Styling

### AI & Intelligence
- **AURIX AI Assistant** - Comprehensive academic knowledge base
- **Fallback AI Service** - Works without external APIs
- **Multi-subject Support** - Math, Science, Programming, and more

### Database
- **SQLite Database** - `backend/instance/smart_classrooms.db`
- **9 Tables** - Users, Attendance, Resources, Assignments, etc.
- **Full CRUD Operations** - Create, Read, Update, Delete
- **Persistent Storage** - Data survives server restarts

### Architecture
- **Feature-Based Modular** - Self-contained features
- **RESTful API** - Standard HTTP methods
- **Database Integration** - Persistent data storage

## 📚 Documentation

- **FEATURE_ARCHITECTURE.md** - Complete architecture explanation
- **FEATURE_QUICK_START.md** - Quick reference guide
- **PROJECT_STRUCTURE.md** - Detailed structure breakdown
- **PROJECT_DOCUMENTATION.md** - Full project documentation
- **UI_PRESENTATION_GUIDE.md** - UI/UX implementation guide

## 🔧 Development

### Adding a New Feature

1. Create feature folder:
```bash
mkdir backend/features/new_feature
```

2. Create `__init__.py`:
```python
from flask import Blueprint
from backend.core.database import db

new_feature_bp = Blueprint('new_feature', __name__, url_prefix='/api/new-feature')

class NewFeatureService:
    @staticmethod
    def do_something():
        return db.get_all('something')

@new_feature_bp.route('', methods=['GET'])
def get_something():
    data = NewFeatureService.do_something()
    return {'success': True, 'data': data}
```

3. Register in `backend/app.py`:
```python
from backend.features.new_feature import new_feature_bp
app.register_blueprint(new_feature_bp)
```

Done! ✅

## 🧪 Testing

```bash
# Backend tests
cd backend
python -m pytest

# Frontend tests
cd client
npm test
```

## 📦 Deployment

### Backend
```bash
cd backend
gunicorn app:app
```

### Frontend
```bash
cd client
npm run build
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request.

## 👥 Authors

- **Your Name** - VENKATA SAI VISWAS PATNALA

## 🙏 Acknowledgments

- React Bootstrap for UI components
- Flask for backend framework
- All contributors and testers

## 📞 Support

For support, email your- VISHWASPATNALA@GMAIL.COM or open an issue.

---

**Built with ❤️ using Feature-Based Modular Architecture**
