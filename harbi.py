#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import threading
import subprocess
import concurrent.futures
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import print as rprint

# معلومات المبرمج
AUTHOR = "Saudi Linux"
EMAIL = "SaudiCrackers@gmail.com"

class Harbi:
    def __init__(self):
        self.console = Console()
        self.tools = {
            "1": {"name": "Sherlock", "function": self.run_sherlock},
            "2": {"name": "Sublist3r", "function": self.run_sublist3r},
            "3": {"name": "WhatWeb", "function": self.run_whatweb},
            "4": {"name": "Google Dorks", "function": self.run_google_dorks},
            "5": {"name": "GHunt", "function": self.run_ghunt},
            "6": {"name": "Datasploit", "function": self.run_datasploit},
            "7": {"name": "Photon", "function": self.run_photon},
            "8": {"name": "Nexpose", "function": self.run_nexpose},
            "9": {"name": "OSRFramework", "function": self.run_osrframework},
            "10": {"name": "theHarvester", "function": self.run_theharvester},
            "11": {"name": "Shodan", "function": self.run_shodan},
            "12": {"name": "SpiderFoot", "function": self.run_spiderfoot},
            "13": {"name": "Amass", "function": self.run_amass},
            "14": {"name": "Censys", "function": self.run_censys}
        }

    def show_banner(self):
        banner = f"""
        [bold red]HARBI - أداة استخبارات مفتوحة المصدر[/bold red]
        [bold blue]المبرمج:[/bold blue] {AUTHOR}
        [bold blue]البريد الإلكتروني:[/bold blue] {EMAIL}
        """
        self.console.print(banner)

    def show_menu(self):
        table = Table(title="قائمة الأدوات المتاحة")
        table.add_column("الرقم", justify="center")
        table.add_column("اسم الأداة", justify="left")

        for key, tool in self.tools.items():
            table.add_row(key, tool["name"])

        self.console.print(table)

    def install_requirements(self):
        requirements = [
            "sherlock", "sublist3r", "whatweb", "ghunt", "datasploit", "photon",
            "nexpose-client", "osrframework", "theharvester", "shodan", "spiderfoot",
            "amass", "censys", "rich"
        ]
        
        self.console.print("[bold yellow]جاري تثبيت المتطلبات...[/bold yellow]")
        for req in requirements:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", req])
            except:
                self.console.print(f"[bold red]فشل تثبيت {req}[/bold red]")

    def run_tool(self, target, tool_function):
        try:
            return tool_function(target)
        except Exception as e:
            return f"خطأ في تنفيذ الأداة: {str(e)}"

    # تنفيذ الأدوات
    def run_sherlock(self, username):
        try:
            result = subprocess.check_output(["sherlock", username], text=True)
            return result
        except:
            return f"تنفيذ Sherlock للبحث عن {username}"

    def run_sublist3r(self, domain):
        try:
            result = subprocess.check_output(["sublist3r", "-d", domain], text=True)
            return result
        except:
            return f"تنفيذ Sublist3r للنطاق {domain}"

    def run_whatweb(self, target):
        try:
            result = subprocess.check_output(["whatweb", target], text=True)
            return result
        except:
            return f"تنفيذ WhatWeb على {target}"

    def run_google_dorks(self, query):
        return f"تنفيذ Google Dorks للبحث عن {query}"

    def run_ghunt(self, email):
        try:
            result = subprocess.check_output(["ghunt", "email", email], text=True)
            return result
        except:
            return f"تنفيذ GHunt للبريد الإلكتروني {email}"

    def run_datasploit(self, target):
        return f"تنفيذ Datasploit على {target}"

    def run_photon(self, url):
        try:
            result = subprocess.check_output(["photon", "-u", url], text=True)
            return result
        except:
            return f"تنفيذ Photon على {url}"

    def run_nexpose(self, target):
        return f"تنفيذ Nexpose على {target}"

    def run_osrframework(self, username):
        try:
            result = subprocess.check_output(["usufy", "-n", username], text=True)
            return result
        except:
            return f"تنفيذ OSRFramework للبحث عن {username}"

    def run_theharvester(self, domain):
        try:
            result = subprocess.check_output(["theHarvester", "-d", domain, "-b", "all"], text=True)
            return result
        except:
            return f"تنفيذ theHarvester على النطاق {domain}"

    def run_shodan(self, query):
        try:
            result = subprocess.check_output(["shodan", "search", query], text=True)
            return result
        except:
            return f"تنفيذ Shodan للبحث عن {query}"

    def run_spiderfoot(self, target):
        return f"تنفيذ SpiderFoot على {target}"

    def run_amass(self, domain):
        try:
            result = subprocess.check_output(["amass", "enum", "-d", domain], text=True)
            return result
        except:
            return f"تنفيذ Amass على النطاق {domain}"

    def run_censys(self, query):
        try:
            result = subprocess.check_output(["censys", "search", query], text=True)
            return result
        except:
            return f"تنفيذ Censys للبحث عن {query}"

    def run_all_tools(self, target):
        results = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_tool = {executor.submit(tool["function"], target): tool["name"] 
                             for tool in self.tools.values()}
            
            for future in concurrent.futures.as_completed(future_to_tool):
                tool_name = future_to_tool[future]
                try:
                    result = future.result()
                    results.append((tool_name, result))
                except Exception as e:
                    results.append((tool_name, f"خطأ: {str(e)}"))
        return results

    def main(self):
        self.show_banner()
        self.install_requirements()

        while True:
            self.show_menu()
            choice = Prompt.ask("\nاختر رقم الأداة (0 للخروج، 99 لتشغيل جميع الأدوات)")

            if choice == "0":
                break
            elif choice == "99":
                target = Prompt.ask("أدخل الهدف (IP/اسم المستخدم/النطاق/البريد الإلكتروني)")
                results = self.run_all_tools(target)
                for tool_name, result in results:
                    self.console.print(f"[bold blue]{tool_name}:[/bold blue] {result}")
            elif choice in self.tools:
                target = Prompt.ask("أدخل الهدف")
                result = self.tools[choice]["function"](target)
                self.console.print(f"\n[bold green]النتيجة:[/bold green] {result}")
            else:
                self.console.print("[bold red]اختيار غير صالح![/bold red]")

if __name__ == "__main__":
    harbi = Harbi()
    harbi.main()