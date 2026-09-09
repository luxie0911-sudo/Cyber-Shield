import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-change-me")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", f"sqlite:///{BASE_DIR / 'cybershield.db'}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH", 10 * 1024 * 1024))
    DASHBOARD_REFRESH_MS = int(os.getenv("DASHBOARD_REFRESH_MS", 3000))
    CAPTURE_INTERFACE = os.getenv("CAPTURE_INTERFACE", "")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    UPLOAD_FOLDER = BASE_DIR / "uploads"
    REPORT_FOLDER = BASE_DIR / "reports"
    LOG_FOLDER = BASE_DIR / "logs"
    ALLOWED_PCAP_EXTENSIONS = {".pcap", ".pcapng"}

class DevelopmentConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
