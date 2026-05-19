# Smart Classrooms Analytics - Updated Project Structure

## 📁 Complete Project Structure

```
smart_classrooms_Analytics/
│
├── 📂 backend/                          # Backend API (Feature-Based Architecture)
│   │
│   ├── 📂 core/                         # Core shared modules
│   │   ├── __init__.py
│   │   └── database.py                  # Centralized mock database (Singleton)
│   │
│   ├── 📂 features/                     # Feature modules (Self-contained)
│   │   ├── __init__.py
│   │   │
│   │   ├── 📂 attendance/              # 📊 Attendance Feature
│   │   │   └── __init__.py             # Routes + Service + Logic (ALL IN ONE)
│   │   │                                # - AttendanceService class
│   │   │                                # - attendance_bp Blueprint
│   │   │                                # - POST /api/attendance
│   │   │                                # - GET /api/attendance/<student_id>
│   │   │                                # - GET /api/attendance/<student_id>/rate
│   │   │
│   │   ├── 📂 timetable/               # 📅 Timetable Feature
│   │   │   └── __init__.py             # Routes + Service + Logic (ALL IN ONE)
│   │   │                                # - TimetableService class
│   │   │                                # - timetable_bp Blueprint
│   │   │                                # - GET /api/timetable/<division>
│   │   │                                # - POST /api/timetable/upload-image
│   │   │                                # - GET /api/timetable/image/<division>
│   │   │                                # - GET /api/timetable/divisions
│   │   │
│   │   ├── 📂 resources/               # 📚 Resources Feature
│   │   │   └── __init__.py             # Routes + Service + Logic (ALL IN ONE)
│   │   │                                # - ResourceService class
│   │   │                                # - resources_bp Blueprint
│   │   │                                # - GET /api/resources
│   │   │                                # - GET /api/resources/<subject>
│   │   │                                # - POST /api/resources/upload
│   │   │                                # - DELETE /api/resources/<subject>
│   │   │
│   │   └── 📂 analytics/               # 📈 Analytics Feature
│   │       └── __init__.py             # Routes + Service + Logic (ALL IN ONE)
│   │                                    # - AnalyticsService class
│   │                                    # - analytics_bp Blueprint
│   │                                    # - GET /api/analytics
│   │                                    # - GET /api/analytics/predict-performance
│   │                                    # - GET /api/analytics/student/<student_id>
│   │
│   ├── 📂 config/                       # Configuration management
│   │   ├── __init__.py
│   │   └── config.py                    # Config classes (Dev, Prod, Test)
│   │
│   ├── 📂 middleware/                   # Middleware (Legacy - not used in feature-based)
│   │   ├── __init__.py
│   │   └── error_handler.py
│   │
│   ├── 📂 routes/                       # Routes (Legacy - replaced by features)
│   │   ├── __init__.py
│   │   ├── attendance.py
│   │   ├── timetable.py
│   │   ├── resources.py
│   │   └── analytics.py
│   │
│   ├── 📂 services/                     # Services (Legacy - replaced by features)
│   │   ├── __init__.py
│   │   └── data_service.py
│   │
│   ├── 📂 models/                       # Models (Empty - for future DB integration)
│   ├── 📂 utils/                        # Utilities (Empty - for future use)
│   │
│   ├── __init__.py                      # Backend package init
│   ├── app.py                           # 🚀 Main application entry point
│   └── requirements.txt                 # Python dependencies
│
├── 📂 client/                           # Frontend (React Application)
│   │
│   ├── 📂 public/
│   │   └── index.html                   # HTML template
│   │
│   ├── 📂 src/
│   │   │
│   │   ├── 📂 components/              # Reusable React components
│   │   │   ├── FloatingParticles.js
│   │   │   ├── Icons.js                # Custom icon components
│   │   │   ├── LoginBackgroundFlow.js
│   │   │   ├── LoginFloatingHats.js
│   │   │   ├── Navbar.js               # Navigation bar
│   │   │   └── ThemeToggle.js
│   │   │
│   │   ├── 📂 pages/                   # Page components
│   │   │   ├── Assignments.js          # Assignments page
│   │   │   ├── Classes.js              # My Classes page (Timetable)
│   │   │   ├── Contact.js              # Contact page
│   │   │   ├── Dashboard.js            # Main dashboard
│   │   │   ├── Grades.js               # Grades page
│   │   │   ├── Login.js                # Login page
│   │   │   ├── Notifications.js        # Notifications page
│   │   │   ├── Performance.js          # Performance page
│   │   │   ├── Reports.js              # Reports page
│   │   │   ├── ResourceLinks.js        # Resource management (Faculty)
│   │   │   ├── Students.js             # Students page
│   │   │   ├── Subjects.js             # Subjects page
│   │   │   ├── TimetableUpload.js      # Timetable upload (Faculty)
│   │   │   └── Users.js                # Users page
│   │   │
│   │   ├── 📂 utils/                   # Utility functions
│   │   │
│   │   ├── App.js                      # Main App component
│   │   ├── App-simple.js               # Simple App version
│   │   ├── index.js                    # React entry point
│   │   └── styles.css                  # Global styles
│   │
│   ├── package.json                    # Node dependencies
│   └── package-lock.json
│
├── 📂 docs/                             # Documentation (Old structure - can be removed)
│   └── (various old files)
│
├── 📂 middleware/                       # Old middleware (can be removed)
├── 📂 models/                           # Old models (can be removed)
├── 📂 routes/                           # Old routes (can be removed)
├── 📂 static/                           # Old static files (can be removed)
├── 📂 templates/                        # Old templates (can be removed)
│
├── 📄 app.py                            # ⚠️ Backward compatibility wrapper
├── 📄 config.py                         # Old config (can be removed)
├── 📄 server.js                         # Old Node server (can be removed)
│
├── 📄 FEATURE_ARCHITECTURE.md           # ✅ Feature-based architecture guide
├── 📄 FEATURE_QUICK_START.md            # ✅ Quick start guide
├── 📄 MIGRATION_GUIDE.md                # ✅ Migration guide
├── 📄 PROJECT_DOCUMENTATION.md          # ✅ Complete project documentation
├── 📄 QUICK_START.md                    # ✅ Quick reference
├── 📄 RESTRUCTURE_README.md             # ✅ Restructure details
├── 📄 UI_PRESENTATION_GUIDE.md          # ✅ UI/UX presentation guide
│
├── 📄 start-restructured.bat            # ✅ Startup script
├── 📄 run-app.bat                       # Old startup script
├── 📄 start.bat                         # Old startup script
│
├── 📄 .env                              # Environment variables
├── 📄 .gitignore                        # Git ignore file
├── 📄 README.md                         # Main README
├── 📄 requirements.txt                  # Old requirements (use backend/requirements.txt)
├── 📄 package.json                      # Old package.json (can be removed)
└── 📄 package-lock.json                 # Old package-lock (can be removed)
```

## 🎯 Key Directories

### Active Backend (Feature-Based)
```
backend/
├── core/database.py          ← Shared database
├── features/                 ← All features here
│   ├── attendance/
│   ├── timetable/
│   ├── resources/
│   └── analytics/
├── config/config.py          ← Configuration
└── app.py                    ← Main entry point
```

### Active Frontend
```
client/
├── src/
│   ├── components/           ← Reusable components
│   ├── pages/                ← Page components
│   ├── App.js                ← Main app
│   └── styles.css            ← Global styles
└── package.json              ← Dependencies
```

## 📊 Feature Breakdown

### Each Feature Contains:
1. **Blueprint** - Flask routing
2. **Service Class** - Business logic
3. **Routes** - HTTP endpoints

### Example: Attendance Feature
```python
# backend/features/attendance/__init__.py

# 1. Blueprint
attendance_bp = Blueprint('attendance', __name__, url_prefix='/api/attendance')

# 2. Service
class AttendanceService:
    @staticmethod
    def record_attendance(...):
        # Business logic
        pass

# 3. Routes
@attendance_bp.route('', methods=['POST'])
def record_attendance():
    # HTTP handler
    pass
```

## 🚀 How to Run

### Backend
```bash
python backend/app.py
```
Runs on: http://localhost:5000

### Frontend
```bash
cd client
npm start
```
Runs on: http://localhost:3000

### Both (Windows)
```bash
start-restructured.bat
```

## 📝 API Endpoints

### Attendance
- `POST /api/attendance` - Record attendance
- `GET /api/attendance/<student_id>` - Get student attendance
- `GET /api/attendance/<student_id>/rate` - Get attendance rate

### Timetable
- `GET /api/timetable/<division>` - Get timetable
- `POST /api/timetable/upload-image` - Upload timetable image
- `GET /api/timetable/image/<division>` - Get timetable image
- `GET /api/timetable/divisions` - Get all divisions

### Resources
- `GET /api/resources` - Get all resources
- `GET /api/resources/<subject>` - Get resource by subject
- `POST /api/resources/upload` - Upload resource
- `DELETE /api/resources/<subject>` - Delete resource

### Analytics
- `GET /api/analytics` - Get overall analytics
- `GET /api/analytics/predict-performance` - Predict performance
- `GET /api/analytics/student/<student_id>` - Get student analytics

### System
- `GET /health` - Health check
- `GET /` - API info

## 🗑️ Files That Can Be Removed

### Old Backend Structure (No longer used)
- `backend/routes/` (replaced by features)
- `backend/services/` (replaced by features)
- `backend/middleware/` (not used in feature-based)

### Old Root Files
- `middleware/` folder
- `models/` folder (old Node.js models)
- `routes/` folder (old Node.js routes)
- `static/` folder
- `templates/` folder
- `config.py` (use backend/config/config.py)
- `server.js` (old Node.js server)
- `requirements.txt` (use backend/requirements.txt)
- `package.json` (root level)
- `run.bat`, `run-app.bat` (use start-restructured.bat)

### Keep These
- ✅ `backend/` - New feature-based backend
- ✅ `client/` - React frontend
- ✅ `app.py` - Backward compatibility
- ✅ All `.md` documentation files
- ✅ `start-restructured.bat`
- ✅ `.env`, `.gitignore`

## 📚 Documentation Files

1. **FEATURE_ARCHITECTURE.md** - Complete architecture explanation
2. **FEATURE_QUICK_START.md** - Quick reference guide
3. **MIGRATION_GUIDE.md** - Migration from old structure
4. **PROJECT_DOCUMENTATION.md** - Full project documentation
5. **UI_PRESENTATION_GUIDE.md** - UI/UX presentation guide
6. **QUICK_START.md** - Quick start commands
7. **RESTRUCTURE_README.md** - Restructure details

## ✅ Summary

**Active Structure:**
- ✅ `backend/` - Feature-based modular architecture
- ✅ `client/` - React frontend
- ✅ Documentation files

**Legacy (Can Remove):**
- ❌ Old routes, services, middleware folders
- ❌ Old Node.js files (server.js, root package.json)
- ❌ Old static/templates folders

**Architecture:**
- ✅ Feature-Based Modular
- ✅ Self-contained features
- ✅ Easy to maintain and scale
- ✅ Production-ready

---

**Current Status:** ✅ Fully restructured with feature-based modular architecture
