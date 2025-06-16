yYإ#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Harbi - Multi-Tool OSINT Framework
Developed by: Saudi Linux
Email: SaudiCrackers@gmail.com
'''

import os
import sys
import time
import subprocess
import pkg_resources
import concurrent.futures
from colorama import init, Fore, Style

# Initialize colorama
init()

required_packages = {
    'sherlock': 'sherlock-osint',
    'sublist3r': 'Sublist3r',
    'whatweb': 'whatweb',
    'ghunt': 'ghunt',
    'datasploit': 'datasploit',
    'twint': 'twint',
    'photon': 'photon-runner',
    'nexpose': 'nexpose',
    'osrframework': 'osrframework',
    'theharvester': 'theharvester',
    'shodan': 'shodan',
    'spiderfoot': 'spiderfoot',
    'amass': 'amass',
    'censys': 'censys'
}

def print_banner():
    banner = f'''{Fore.GREEN}
    ╔═╗╔═╗╦ ╦╔╦╗╦  ╦╔╗╔╦ ╦═╗ ╦
    ╚═╗╠═╣║ ║ ║║║  ║║║║║ ║╔╩╦╝
    ╚═╝╩ ╩╚═╝═╩╝╩═╝╩╝╚╝╚═╝╩ ╚═
    {Style.RESET_ALL}
    Developed by: Saudi Linux
    Email: SaudiCrackers@gmail.com
    '''
    print(banner)

def check_dependencies():
    print(f"{Fore.YELLOW}[*] Checking dependencies...{Style.RESET_ALL}")
    missing_packages = []
    
    for package in required_packages.values():
        try:
            pkg_resources.require(package)
        except (pkg_resources.DistributionNotFound, pkg_resources.VersionConflict):
            missing_packages.append(package)
    
    if missing_packages:
        print(f"{Fore.RED}[!] Missing packages: {', '.join(missing_packages)}{Style.RESET_ALL}")
        install = input(f"{Fore.YELLOW}[?] Would you like to install them now? (y/n): {Style.RESET_ALL}")
        if install.lower() == 'y':
            for package in missing_packages:
                print(f"{Fore.CYAN}[+] Installing {package}...{Style.RESET_ALL}")
                subprocess.run([sys.executable, "-m", "pip", "install", package])
        else:
            print(f"{Fore.RED}[!] Please install missing packages to use all features.{Style.RESET_ALL}")
            sys.exit(1)

def run_tool(tool_name, target):
    try:
        if tool_name == 'sherlock':
            subprocess.run(['sherlock', target])
        elif tool_name == 'sublist3r':
            subprocess.run(['sublist3r', '-d', target])
        elif tool_name == 'whatweb':
            subprocess.run(['whatweb', target])
        elif tool_name == 'ghunt':
            subprocess.run(['ghunt', 'email', target])
        elif tool_name == 'twint':
            subprocess.run(['twint', '-u', target])
        elif tool_name == 'photon':
            subprocess.run(['photon', '-u', target])
        elif tool_name == 'theharvester':
            subprocess.run(['theharvester', '-d', target, '-b', 'all'])
        # Add more tools as needed
        return f"{Fore.GREEN}[+] {tool_name} completed successfully{Style.RESET_ALL}"
    except Exception as e:
        return f"{Fore.RED}[!] Error running {tool_name}: {str(e)}{Style.RESET_ALL}"

def main():
    print_banner()
    check_dependencies()
    
    while True:
        print(f"""{Fore.CYAN}
Available Tools:
1. Sherlock - Hunt down social media accounts
2. Sublist3r - Subdomain enumeration
3. WhatWeb - Web scanner
4. GHunt - Google account investigation
5. Twint - Twitter intelligence tool
6. Photon - Web crawler and recon tool
7. TheHarvester - E-mail and subdomain gathering
8. Run All Tools
9. Exit
{Style.RESET_ALL}""")
        
        choice = input(f"{Fore.YELLOW}[?] Select an option (1-9): {Style.RESET_ALL}")
        
        if choice == '9':
            print(f"{Fore.GREEN}[+] Thank you for using Harbi!{Style.RESET_ALL}")
            break
            
        if choice == '8':
            target = input(f"{Fore.YELLOW}[?] Enter target: {Style.RESET_ALL}")
            print(f"{Fore.CYAN}[*] Running all tools...{Style.RESET_ALL}")
            
            with concurrent.futures.ThreadPoolExecutor() as executor:
                tools = ['sherlock', 'sublist3r', 'whatweb', 'ghunt', 'twint', 'photon', 'theharvester']
                futures = [executor.submit(run_tool, tool, target) for tool in tools]
                
                for future in concurrent.futures.as_completed(futures):
                    print(future.result())
        
        elif choice in ['1', '2', '3', '4', '5', '6', '7']:
            tool_map = {
                '1': 'sherlock',
                '2': 'sublist3r',
                '3': 'whatweb',
                '4': 'ghunt',
                '5': 'twint',
                '6': 'photon',
                '7': 'theharvester'
            }
            
            target = input(f"{Fore.YELLOW}[?] Enter target: {Style.RESET_ALL}")
            print(run_tool(tool_map[choice], target))
        
        else:
            print(f"{Fore.RED}[!] Invalid option{Style.RESET_ALL}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Exiting...{Style.RESET_ALL}")
        sys.exit(0)