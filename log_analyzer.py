git checkout feature/log-analysis
cat << 'EOF' > log_analyzer.py
from collections import Counter

def detect_bruteforce(log_lines, threshold=3):
    failed_ips = [line.split()[-1] for line in log_lines if "Failed password" in line]
    counts = Counter(failed_ips)
    return {ip: count for ip, count in counts.items() if count >= threshold}

if __name__ == "__main__":
    sample_logs = [
        "Failed password for root from 192.168.1.55",
        "Failed password for admin from 192.168.1.55",
        "Failed password for user from 192.168.1.55",
        "Accepted password for ops from 10.0.0.12",
    ]
    print("Flagged IPs:", detect_bruteforce(sample_logs))
EOF
git add log_analyzer.py
git commit -m "feat(logs): implement brute-force login detection parser (Freshworks LOG-02)"
git push -u origin feature/log-analysis
