# CyberShield — Real-Time Network Intrusion Detection System

CyberShield is a defensive, educational IDS for authorized/local traffic. It captures packet metadata with Scapy, applies configurable rule-based detection, stores security events in SQLite, and presents a SOC-style Flask dashboard.

## Features
- Secure registration/login with Flask-Login and Werkzeug password hashing
- CSRF protection with Flask-WTF
- Real-time metadata capture using Scapy
- Authorized PCAP/PCAPNG analysis
- Rule-based IDS: port-scan pattern, excessive connections, ICMP burst, DNS anomaly, SYN flood-like metadata
- Simple statistical anomaly detector
- Alert lifecycle: New, Investigating, Resolved, False Positive
- Demo Mode using synthetic metadata only
- Traffic and IP investigation pages
- CSV and PDF reports
- REST API
- Pytest test suite
- Structured application logging

## Safety
Use only localhost, your own computer/lab, authorized networks, and authorized PCAP files. CyberShield intentionally does not inspect/store packet payloads and does not generate real attack traffic.

## Architecture
```text
Interface / Authorized PCAP
        ↓
Packet Capture / PCAP Reader
        ↓
Packet Parser (metadata only)
        ↓
Detection Engine
   ┌────┴─────┐
 Rules     Statistics
   └────┬─────┘
        ↓
 Alert Manager
        ↓
 SQLite / SQLAlchemy
        ↓
 Flask API
        ↓
 Web Dashboard
```

## Installation — Windows
1. Install Python 3.11+.
2. Open PowerShell in the project directory.
3. `python -m venv venv`
4. `venv\Scripts\activate`
5. `pip install -r requirements.txt`
6. Copy `.env.example` to `.env` and change `SECRET_KEY`.
7. `python run.py`
8. Open `http://127.0.0.1:5000`

For live capture on Windows, Scapy commonly requires a supported packet-capture driver such as Npcap. Install it from the official Npcap distribution and select only the options appropriate to your authorized lab. If capture permission is unavailable, use Demo Mode or PCAP Analysis.

## Installation — Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python run.py
```
Live packet capture may require appropriate OS packet-capture permissions. Prefer a dedicated lab interface and avoid granting more privilege than necessary.

## Database
SQLite is created automatically as `cybershield.db` on first startup.

## Demo Mode
Register and log in, then press **Generate Demo Data**. The app creates clearly labeled SIMULATED / DEMO DATA. It does not send packets or attack any host.

## PCAP Analysis
Use `POST /api/pcap/upload` from the authenticated UI/API with an authorized `.pcap` or `.pcapng`. Maximum upload size is configurable. Payload contents are not stored.

## Project Structure
See `PROJECT_DOCUMENTATION.md` for the full module map.

## Detection Rules
- CS-001 Port Scan Pattern — unique destination ports/window
- CS-002 Excessive Connection Attempts — repeated observed connections
- CS-003 ICMP Burst — ICMP frequency
- CS-004 DNS Anomaly — DNS frequency
- CS-005 SYN Flood-like Pattern — SYN minus observed SYN-ACKs

Thresholds are stored in the DetectionRule table and are configurable.

## Testing
```bash
pytest -q
```

## Limitations
- Detection is heuristic and can create false positives/negatives.
- Live capture depends on OS interface/driver permissions.
- SQLite is intended for a small academic deployment, not a high-volume enterprise SOC.
- No payload inspection or automated blocking is performed.

## Future Enhancements
Machine-learning anomaly detection, threat-intelligence enrichment, SIEM integration, email/SMS alerts, GeoIP visualization, RBAC, PostgreSQL, Docker, cloud deployment, topology visualization, and carefully governed incident-response integrations.

## Author
BCA Final-Year Academic Project — CyberShield
