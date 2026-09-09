import logging
from pathlib import Path
from flask import Flask
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from config import Config
from database.db import db
from database.models import User
from capture.packet_capture import capture_service
from detection.detection_engine import DetectionEngine

login_manager = LoginManager()
csrf = CSRFProtect()
detection_engine = DetectionEngine()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    for folder in (
        app.config["UPLOAD_FOLDER"],
        app.config["REPORT_FOLDER"],
        app.config["LOG_FOLDER"],
    ):
        Path(folder).mkdir(parents=True, exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to continue."

    from routes.auth import auth_bp
    from routes.dashboard import dashboard_bp
    from routes.alerts import alerts_bp
    from routes.reports import reports_bp
    from routes.api import api_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(alerts_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(api_bp)

    configure_logging(app)

    with app.app_context():
        db.create_all()
        seed_detection_rules()

    @app.errorhandler(413)
    def too_large(_):
        return "File size exceeds the allowed limit.", 413

    @app.errorhandler(404)
    def not_found(_):
        return "Page not found.", 404

    @app.errorhandler(500)
    def server_error(_):
        app.logger.exception("Unhandled application error")
        return "An internal application error occurred.", 500

    return app

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

def configure_logging(app):
    level = getattr(logging, app.config["LOG_LEVEL"].upper(), logging.INFO)
    log_file = Path(app.config["LOG_FOLDER"]) / "cybershield.log"
    handler = logging.FileHandler(log_file, encoding="utf-8")
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s"
    ))
    app.logger.setLevel(level)
    app.logger.addHandler(handler)

def seed_detection_rules():
    from database.models import DetectionRule
    defaults = [
        ("CS-001", "Port Scan Pattern", "Many unique destination ports from one source in a short window.", "HIGH", 20),
        ("CS-002", "Excessive Connection Attempts", "Repeated connections from one source.", "MEDIUM", 50),
        ("CS-003", "ICMP Burst", "Unusually high ICMP packet frequency.", "MEDIUM", 30),
        ("CS-004", "DNS Anomaly", "Unusually high DNS query frequency.", "MEDIUM", 60),
        ("CS-005", "SYN Flood-like Pattern", "High SYN count with few observed SYN-ACK responses.", "HIGH", 40),
    ]
    for rule_id, name, description, severity, threshold in defaults:
        if not DetectionRule.query.filter_by(rule_id=rule_id).first():
            db.session.add(DetectionRule(
                rule_id=rule_id, name=name, description=description,
                severity=severity, threshold=threshold, enabled=True
            ))
    db.session.commit()

if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=5000, debug=False)
