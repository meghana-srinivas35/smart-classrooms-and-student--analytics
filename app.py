"""
Smart Classrooms Analytics - Feature-Based Modular Architecture
Main application entry point
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, jsonify
from flask_cors import CORS
from config.config import config
from core.models import db
from core.init_db import init_database
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import feature modules
from features.attendance import attendance_bp
from features.timetable import timetable_bp
from features.resources import resources_bp
from features.analytics import analytics_bp
from features.admin import admin_bp
from features.auth import auth_bp
from features.results import results_bp
from features.support import support_bp
from features.ai import ai_bp
from features.assignments import assignments_bp

def create_app(config_name='development'):
    """Application factory with feature-based architecture"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize database
    db.init_app(app)
    
    # Enable CORS
    CORS(app)
    
    # Initialize database tables and seed data
    init_database(app)
    
    # Register feature modules
    app.register_blueprint(attendance_bp)
    app.register_blueprint(timetable_bp)
    app.register_blueprint(resources_bp)
    app.register_blueprint(analytics_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(results_bp)
    app.register_blueprint(support_bp)
    app.register_blueprint(ai_bp)
    app.register_blueprint(assignments_bp)
    
    # Health check endpoint
    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({
            'status': 'healthy',
            'service': 'Smart Classrooms Analytics API',
            'architecture': 'Feature-Based Modular',
            'features': ['attendance', 'timetable', 'resources', 'analytics', 'admin', 'auth', 'results', 'support', 'ai']
        }), 200
    
    # Root endpoint
    @app.route('/', methods=['GET'])
    def root():
        return jsonify({
            'message': 'Smart Classrooms Analytics API',
            'version': '2.0',
            'architecture': 'Feature-Based Modular',
            'endpoints': {
                'health': '/health',
                'attendance': '/api/attendance',
                'timetable': '/api/timetable',
                'resources': '/api/resources',
                'analytics': '/api/analytics',
                'admin': '/api/admin',
                'auth': '/api/auth',
                'results': '/api/results',
                'support': '/api/support',
                'ai': '/api/ai'
            }
        }), 200
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'success': False, 'error': 'Resource not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'success': False, 'error': 'Internal server error'}), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    print("\n" + "="*60)
    print("  Smart Classrooms Analytics API")
    print("  Feature-Based Modular Architecture")
    print("  AURIX AI Integration - Full Platform Access")
    print("="*60)
    print("  Server: http://localhost:5000")
    print("  Health: http://localhost:5000/health")
    print("="*60)
    print("\n  Core Features:")
    print("     - Attendance  -> /api/attendance")
    print("     - Timetable   -> /api/timetable")
    print("     - Resources   -> /api/resources")
    print("     - Analytics   -> /api/analytics")
    print("     - Admin       -> /api/admin")
    print("     - Auth        -> /api/auth")
    print("     - Results     -> /api/results")
    print("     - Support     -> /api/support")
    print("\n  AURIX AI Services (Platform Integrated):")
    print("     - Enhanced Chat        -> /api/ai/chat")
    print("     - Student Analysis     -> /api/ai/student-analysis")
    print("     - Class Insights       -> /api/ai/class-insights")
    print("     - Admin Dashboard      -> /api/ai/admin-dashboard")
    print("     - Smart Resources      -> /api/ai/smart-resources")
    print("     - Study Suggestions    -> /api/ai/study-suggestions")
    print("     - Assignment Help      -> /api/ai/assignment-help")
    print("     - AI Health Check      -> /api/ai/health")
    print("\n  AI Capabilities:")
    print("     - Full platform data access")
    print("     - Personalized responses by role")
    print("     - Real-time analytics integration")
    print("     - Performance predictions")
    print("     - Risk assessment & early warnings")
    print("     - Smart resource recommendations")
    print("     - Contextual assignment assistance")
    print("="*60 + "\n")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
