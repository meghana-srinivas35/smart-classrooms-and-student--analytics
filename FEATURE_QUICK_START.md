# Quick Start - Feature-Based Architecture

## 🚀 Start Application

```bash
python backend/app.py
```

## 📁 Project Structure

```
backend/
├── core/
│   └── database.py          # Shared database
│
├── features/                # Self-contained features
│   ├── attendance/
│   │   └── __init__.py     # Routes + Service + Logic
│   ├── timetable/
│   │   └── __init__.py     # Routes + Service + Logic
│   ├── resources/
│   │   └── __init__.py     # Routes + Service + Logic
│   └── analytics/
│       └── __init__.py     # Routes + Service + Logic
│
└── app.py                   # Main entry point
```

## 🎯 Key Concept

**Each feature = ONE file with everything**
- Routes (HTTP endpoints)
- Service (business logic)
- All related code together

## 📊 Features

### Attendance
```
GET  /api/attendance/<student_id>
POST /api/attendance
GET  /api/attendance/<student_id>/rate
```

### Timetable
```
GET  /api/timetable/<division>
POST /api/timetable/upload-image
GET  /api/timetable/image/<division>
GET  /api/timetable/divisions
```

### Resources
```
GET    /api/resources
GET    /api/resources/<subject>
POST   /api/resources/upload
DELETE /api/resources/<subject>
```

### Analytics
```
GET /api/analytics
GET /api/analytics/predict-performance
GET /api/analytics/student/<student_id>
```

## ➕ Add New Feature

1. Create folder: `backend/features/new_feature/`
2. Create file: `__init__.py`
3. Add code:
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
4. Register in `app.py`:
```python
from backend.features.new_feature import new_feature_bp
app.register_blueprint(new_feature_bp)
```

Done! ✅

## 🔍 Find Code

Want to modify attendance? → `backend/features/attendance/__init__.py`  
Want to modify timetable? → `backend/features/timetable/__init__.py`  
Want to modify resources? → `backend/features/resources/__init__.py`  

**Everything for a feature in ONE place!**

## ✅ Benefits

- ✅ Easy to find code
- ✅ Easy to add features
- ✅ Easy to test
- ✅ Easy to maintain
- ✅ Scalable

## 📚 Full Documentation

See: `FEATURE_ARCHITECTURE.md`
