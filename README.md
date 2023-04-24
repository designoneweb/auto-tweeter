# Auto Tweeter

A simple Python program that uses ChatGPT to create a Tweet based on a user selected subject

## Requirements
* Python 3 or greater
* Flask
* openai
* tweepy
* Pillow
* python-dotenv

The repository has the necessary file to automatically install all the requirements and run the program in Windows (run_app.bat), MacOS (run_app.command), and Linux (run_app.sh). The app will run in a Python virtual environment (venv). Here are the instructions for installing venv (Python's virtual environment) for each operating system:

1. Linux and macOS:
    On Linux and macOS, Python 3 is usually pre-installed, and the venv module is bundled with it. To check if Python 3 is installed, you can open a terminal and type the following command:

    'python --version'
    
    If you get a version number as output, Python 3 is installed. If not, you can install Python 3 using the package manager for your Linux distribution or download it from the official website (https://www.python.org/downloads/) for macOS.
2. Windows:
    On Windows, you need to install Python 3 manually. You can download the installer from the official website (https://www.python.org/downloads/).

    While installing, make sure to check the option "Add Python to PATH" before proceeding with the installation. This ensures that the python command will be available in the command prompt, and the venv module will be installed alongside Python 3.

Once you have Python 3 and the venv module installed, you can create and use virtual environments on all operating systems using the following commands:

To create a virtual environment:

* Linux and macOS: 'python3 -m venv venv'
* Windows: 'python -m venv venv'

To activate the virtual environment:

* Linux and macOS: 'source venv/bin/activate'
* Windows: 'venv\Scripts\activate.bat'

To deactivate the virtual environment:

* All platforms: 'deactivate'

With these commands, you can create, activate, and deactivate virtual environments on Linux, macOS, and Windows.
