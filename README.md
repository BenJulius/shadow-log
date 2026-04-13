# Shadow-Log
A lightweight Python security auditor for mapping network telemetry to system processes.

### Functionality
- **Process Correlation:** Maps active network sockets to specific PIDs and process names.
- **User Context:** Identifies the system user associated with each network connection.
- **Forensic Export:** Generates structured JSON audit logs for security analysis.

### Getting Started
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Run the auditor:

Bash
python shadow_log.py
3. Review the findings in system_audit.json.
Project Stack
Language: Python 3.x

Libraries: psutil, json, socket
