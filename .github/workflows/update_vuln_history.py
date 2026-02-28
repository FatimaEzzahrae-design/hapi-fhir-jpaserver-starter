import json
import sys
from datetime import datetime, UTC

if len(sys.argv) != 3:
    print("Usage: python update_vuln_history.py <trivy_report.json> <vuln_history.json>")
    sys.exit(1)

trivy_json_file = sys.argv[1]
history_file = sys.argv[2]

scan_date = datetime.now(UTC).strftime("%Y-%m-%d")

# Load Trivy report
with open(trivy_json_file, "r") as f:
    trivy_data = json.load(f)

# Count vulnerabilities
vuln_count = 0
for result in trivy_data.get("Results", []):
    vuln_count += len(result.get("Vulnerabilities", []))

# Load history
try:
    with open(history_file, "r") as f:
        history = json.load(f)
except FileNotFoundError:
    history = []

# Append new scan
history.append({
    "date": scan_date,
    "vulnerabilities": vuln_count
})

# Save history
with open(history_file, "w") as f:
    json.dump(history, f, indent=2)

# Calculate MTTR
if len(history) > 1:
    deltas = []
    for i in range(1, len(history)):
        prev = history[i - 1]["vulnerabilities"]
        curr = history[i]["vulnerabilities"]
        if curr < prev:
            deltas.append(prev - curr)

    mttr = sum(deltas) / len(deltas) if deltas else 0
else:
    mttr = 0

print(f"Temps moyen de correction (MTTR) : {mttr:.2f} vulnérabilités corrigées par scan")

# Optional CSV export
with open("vuln_metrics.csv", "w") as f:
    f.write("date,vulnerabilities\n")
    for entry in history:
        f.write(f"{entry['date']},{entry['vulnerabilities']}\n")