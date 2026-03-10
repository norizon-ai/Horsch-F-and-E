#!/usr/bin/env python3
"""
Filter subdomains to find actual public websites vs infrastructure servers
"""
import re
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
import sys
from tqdm import tqdm

# Patterns that typically indicate infrastructure/non-public servers
INFRASTRUCTURE_PATTERNS = [
    r'^cip\d+',           # CIP pools
    r'^faui\d+',          # Infrastructure servers
    r'vc\.rrze',          # Virtual machines
    r'^tc\d+',            # Technical servers
    r'-surveys',          # Survey tools
    r'^mail\.',           # Mail servers
    r'^smtp\.',
    r'^imap\.',
    r'^pop\.',
    r'^ftp\.',            # File transfer
    r'^sftp\.',
    r'^vpn\.',            # VPN
    r'^git\.',            # Version control
    r'^gitlab\.',
    r'^github\.',
    r'^jenkins\.',        # CI/CD
    r'^ci\.',
    r'^build\.',
    r'^test\d+',          # Test servers
    r'^dev\d+',           # Dev servers
    r'^staging\d+',
    r'^backup\.',         # Backup servers
    r'^db\d*\.',          # Database servers
    r'^sql\.',
    r'^mysql\.',
    r'^postgres\.',
    r'^mongo\.',
    r'^redis\.',
    r'^ldap\.',           # Directory services
    r'^ad\.',
    r'^ns\d*\.',          # Name servers
    r'^dns\.',
    r'^ntp\.',            # Time servers
    r'^monitoring\.',     # Monitoring
    r'^nagios\.',
    r'^zabbix\.',
    r'^grafana\.',
    r'^prometheus\.',
]

def is_infrastructure(subdomain):
    """Check if subdomain matches infrastructure patterns"""
    for pattern in INFRASTRUCTURE_PATTERNS:
        if re.search(pattern, subdomain, re.IGNORECASE):
            return True
    return False

def normalize_subdomain(subdomain):
    """Normalize subdomain by removing www. prefix"""
    if subdomain.startswith('www.'):
        return subdomain[4:]
    return subdomain

def check_subdomain(subdomain, timeout=5):
    """Check if subdomain serves HTML content"""
    subdomain = subdomain.strip()

    # Normalize subdomain (remove www.)
    subdomain = normalize_subdomain(subdomain)

    # Skip if matches infrastructure pattern
    if is_infrastructure(subdomain):
        return None, f"Infrastructure pattern: {subdomain}"

    # Try HTTPS first, then HTTP
    for protocol in ['https', 'http']:
        url = f"{protocol}://{subdomain}"
        try:
            response = requests.head(
                url,
                timeout=timeout,
                allow_redirects=True,
                headers={'User-Agent': 'Mozilla/5.0'}
            )

            # Check if successful and serves HTML
            if response.status_code == 200:
                content_type = response.headers.get('content-type', '').lower()

                if 'text/html' in content_type:
                    return subdomain, f"✓ {protocol.upper()} - HTML website"
                else:
                    return None, f"✗ {subdomain} - Non-HTML ({content_type})"

        except requests.exceptions.RequestException:
            continue

    return None, f"✗ {subdomain} - No response"

def main():
    # Read subdomains from file or stdin
    if len(sys.argv) > 1:
        subdomain_files = sys.argv[1].split(',')  # Support multiple files: file1.txt,file2.txt
        subdomains = []

        for filename in subdomain_files:
            filename = filename.strip()
            try:
                with open(filename, 'r') as f:
                    file_subdomains = [line.strip() for line in f if line.strip()]
                    subdomains.extend(file_subdomains)
                    print(f"Loaded {len(file_subdomains)} subdomains from {filename}")
            except FileNotFoundError:
                print(f"Warning: File {filename} not found, skipping...")

    else:
        print("Usage: python filter_subdomains.py subdomains.txt")
        print("       python filter_subdomains.py subdomains_de.txt,subdomains_eu.txt")
        sys.exit(1)

    # Deduplicate input subdomains
    original_count = len(subdomains)
    subdomains = list(set(subdomains))

    if original_count != len(subdomains):
        print(f"Removed {original_count - len(subdomains)} duplicate entries from input")

    print(f"Checking {len(subdomains)} unique subdomains...")
    print("=" * 60)

    valid_websites = []

    # Check subdomains in parallel with progress bar
    with ThreadPoolExecutor(max_workers=20) as executor:
        future_to_subdomain = {
            executor.submit(check_subdomain, subdomain): subdomain
            for subdomain in subdomains
        }

        # Use tqdm for progress bar
        with tqdm(total=len(subdomains), desc="Checking subdomains", unit="site") as pbar:
            for future in as_completed(future_to_subdomain):
                subdomain, message = future.result()

                if subdomain:
                    tqdm.write(message)  # Write without breaking progress bar
                    valid_websites.append(subdomain)
                else:
                    # Optionally print rejections (commented out to reduce noise)
                    # tqdm.write(message)
                    pass

                pbar.update(1)  # Update progress bar

    print("\n" + "=" * 60)

    # Deduplicate output (just in case)
    valid_websites = list(set(valid_websites))

    print(f"\nFound {len(valid_websites)} valid websites:\n")

    # Save to file
    with open('valid_websites.txt', 'w') as f:
        for site in sorted(valid_websites):
            print(f"  https://{site}")
            f.write(f"https://{site}\n")

    print(f"\nSaved to: valid_websites.txt")

if __name__ == "__main__":
    main()
