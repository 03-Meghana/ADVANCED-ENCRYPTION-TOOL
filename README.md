# ADVANCED-ENCRYPTION-TOOL

## COMPANY : Codtech IT Solutions

## NAME : Alla Meghana Reddy

## INTERN ID : CT06DG1638

## DOMAIN : Cyber Security & Ethical Hacking

## DURATION : 6 weeks

## MENTOR : Neela Santhosh

## DESCRIPTION OF TASK :

TASK NAME - Advanced Encryption Tool

GOAL - The goal of this task is to develop a command-line based, modular penetration testing toolkit using Python. It is designed for cybersecurity enthusiasts and professionals to simulate and automate common reconnaissance and exploitation techniques in a controlled, ethical environment. This toolkit streamlines initial phases of penetration testing such as port scanning, brute force attacks, banner grabbing, vulnerability detection, and WHOIS lookups—each encapsulated within a dedicated module.

OBJECTIVE - - Create a menu-driven interface for interacting with various pentesting modules - Implement lightweight and functional modules to perform tasks such as SSH brute-forcing and port scanning - Promote reusability and clarity through well-separated components - Emphasize basic automation of reconnaissance techniques and integrate external data sources like WHOIS services - Serve as an educational and practical foundation for future toolkit expansion

PLATFORMS USED - - Development Environment: The toolkit was developed using Visual Studio Code, a versatile and extensible code editor that offers features like integrated terminal, and Git integration for efficient debugging and development. - Version Control & Collaboration: Source code and version history were managed using GitHub, providing a centralized platform for code backup, revision tracking, and optional open-source sharing. - Supported Operating Systems: While the toolkit is cross-platform, it was primarily tested on Windows, with compatibility for Linux and macOS as well. - Python Version: Developed and tested using Python 3.8+

HOW IT WORKS - The user runs main.py, which presents a numbered menu corresponding to each tool: - Port Scanner: Uses Python's socket library to iterate through ports 1 to 1024 on a given IP address, reporting open ports. - SSH Brute Forcer: Reads from a user-provided password list to attempt logging into an SSH service using paramiko. It tests credentials until it finds a match or exhausts the list. - Banner Grabber: Connects to a specified port on a target machine (default 80), sends a request, and prints any service response banners—often useful in identifying software. - Vulnerability Checker (Basic): Checks for keywords related to commonly vulnerable technologies in a domain input. It suggests manual CVE lookup but can later be enhanced with API integration. - WHOIS Lookup: Retrieves domain registration info such as registrar, expiration date, and contact details using the whois library.

TOOLS & LIBRARIES - The toolkit is built using Python due to its readability, platform independence, and extensive third-party support. Libraries may include: - socket: For low-level TCP port communication and banner grabbing - paramiko: To attempt SSH connections using password-based brute force - requests: For HTTP-based tasks (planned for future modules) - whois: To perform domain lookup and fetch WHOIS records - argparse, input() and print(): For user interaction via CLI - Custom wordlists and external files: Used in brute-force operations

APPLICATIONS - - Cybersecurity Education: Demonstrates basic pentest workflows for students and self-learners. - Ethical Hacking Practice: A safe platform to simulate and practice reconnaissance tasks. - CTF Training: Useful for introductory CTF challenges involving brute force, port discovery, and OSINT. - Automation Base: Provides a Python framework for integrating more advanced tools like CVE scanning, DNS fuzzing, or packet sniffing in the future. - Portfolio Project: Showcases Python development, modular architecture, and cybersecurity knowledge in practical form.

OUTPUT -
