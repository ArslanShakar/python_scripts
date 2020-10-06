import os
import time
import json
import shlex
import platform
import subprocess
from pprint import pprint

curl = """curl -X PUT "https://api.cloudflare.com/client/v4/zones/890634ad28eddbbce499ebb8bfcbd565/dns_records/e4947868ee1961f9ebaf5f6ef15a184d" \
-H "X-Auth-Email: netstation@protonmail.com" \
-H "X-Auth-Key: 4f36106e80660df38eb3e771e2f794f05669d" \
-H "Content-Type: application/json" \
--data '{"type":"A","name":"93","content":"%s","ttl":120,"proxied":false}'"""

dns = "93.prvgroup.xyz"

ip_pool = [
    "81.30.144.94",
    "81.30.144.92",
    "81.30.144.95",
    "81.30.144.93",
]


def update_dns_with_cloudflare(ip):
    print(f'\nUpdating IP at CloudFlare {ip}')
    args = shlex.split(curl % ip)
    process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    result = json.loads(stdout)
    pprint(result)
    print("Sleeping for 5 Minutes...")
    time.sleep(60 * 5)
    return result['success']


def ping_dns(dns_ip):
    current_os = platform.system().lower()
    if current_os == "windows":
        parameter = "-n"
    else:
        parameter = "-c"

    exit_code = os.system(f"ping {parameter} 4 {dns_ip}")
    return exit_code == 0


def execute_ip_pool():
    for ip in ip_pool:
        print(f"Trying IP: {ip}")
        test = True

        while test:
            if ping_dns(dns):
                print(f"{ip} is up / ping successfully")
                test = True
                print("Sleeping for 15 seconds...")
                time.sleep(15)
            else:
                print(f"{ip} is down")
                test = False
                update_dns_with_cloudflare(ip)


if __name__ == '__main__':
    execute_ip_pool()
