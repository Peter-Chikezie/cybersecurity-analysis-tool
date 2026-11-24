cat << 'EOF' > firewall_validator.py
def validate_rules(rules):
    insecure_ports = {21, 23, 3389}
    findings = []
    for rule in rules:
        if rule["src"] == "0.0.0.0/0" and rule["action"] == "ALLOW":
            if rule["port"] in insecure_ports:
                findings.append(f"[HIGH RISK] Rule {rule['id']}: Public access allowed on insecure port {rule['port']}")
    return findings

if __name__ == "__main__":
    sample_acl = [
        {"id": 101, "src": "0.0.0.0/0", "port": 23, "action": "ALLOW"},
        {"id": 102, "src": "10.0.10.0/24", "port": 443, "action": "ALLOW"},
        {"id": 103, "src": "0.0.0.0/0", "port": 21, "action": "ALLOW"},
    ]
    for alert in validate_rules(sample_acl):
        print(alert)
EOF
git add firewall_validator.py
git commit -m "feat(firewall): add firewall rule validator for insecure ports (Freshworks FW-01)"
