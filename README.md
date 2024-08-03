# NanoLegion Bot

This Python script automates browser interactions using Selenium WebDriver. It spins multiple browser instances attached to separate nodes on a binary tree.

Features:

Configuration Management: The data.py file handles configuration variables for each web driver, providing flexibility and ease of management.

Rumble Platform Tasks: The main directory contains Python files responsible for executing tasks on the Rumble platform.

SeleniumBase Integration: Utilizes the undetected Chrome driver from SeleniumBase in conjunction with Selenium's WebDriver for automated browser interactions.

Virtual Environment: All program dependencies are contained within an active virtual environment directory labeled env.

Usage:

Clone the repository. Download the Python3.12 interpreter from the link below. Use the [ cd ] Mac/Windows command inside of the terminal to view and interact with the contents inside of the folder. Once inside the folder, set up a virtual environment (env) with [Python3 -m venv env] command on Mac/Windows. Now activate the virtual environment with the Mac command [source env/bin/activate] or the [env\Scripts\activate] Windows command in the terminal. Install the dependencies (requirements.txt) with the [pip3 install -r requirements.txt] command. If the requirements.txt file does not work, install dependencies individually with pip3 install [____name of dependency___]. Finally run the script (root.py). All of this should be ran in the terminal (mac) or powershell (windows).

Interpreter:

Python 3.12
https://www.python.org/downloads/

Dependencies:

seleniumbase==4.23.7

selenium==4.17.2

License

This project is licensed under the MIT License - see the LICENSE file for details.
(USE THIS PROGRAM AT YOUR OWN RISK. I AM NOT RESPONSIBLE FOR COMPUTER FAILURES, PROGRAM CRASHES OR LEAGAL ISSUES)
