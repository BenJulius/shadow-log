import socket
import psutil
import json
from datetime import datetime

class ShadowLog:
    def __init__(self):
        self.timestamp = datetime.now().isoformat()
        self.audit_data = {
            "meta": {"run_time": self.timestamp, "status": "complete"},
            "findings": []
        }

    def map_network_telemetry(self):
        connections = psutil.net_connections(kind='inet')
        for conn in connections:
            if conn.status in ['LISTEN', 'ESTABLISHED']:
                try:
                    proc = psutil.Process(conn.pid)
                    entry = {
                        "pid": conn.pid,
                        "process": proc.name(),
                        "local_addr": f"{conn.laddr.ip}:{conn.laddr.port}",
                        "remote_addr": f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A",
                        "status": conn.status,
                        "user": "admin"
                    }
                    self.audit_data["findings"].append(entry)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue

    def export(self, file_path="system_audit.json"):
        with open(file_path, "w") as f:
            json.dump(self.audit_data, f, indent=4)

if __name__ == "__main__":
    scanner = ShadowLog()
    scanner.map_network_telemetry()
    scanner.export()
