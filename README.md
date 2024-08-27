Workstatus.io Python Desktop Agent
Overview

A Python-based desktop agent that tracks user activity, captures screenshots, and uploads them to AWS S3. It features a web interface for viewing screenshots and a Tkinter GUI for controlling the agent.
Features

    Activity Monitoring: Tracks mouse and keyboard activity.
    Screenshot Capture: Configurable intervals for screenshots.
    AWS S3 Upload: Automatically uploads screenshots to S3.
    Web Interface: View screenshots via a local web server.
    GUI Control: Start/stop the agent and download screenshots.

Installation

    Clone the Repository:

    bash

git clone https://github.com/yourusername/workstatus-agent.git
cd workstatus-agent

Install Dependencies:

bash

    pip install -r requirements.txt

    Configure AWS: Update config/settings.ini with your S3 bucket details and credentials.

Usage

    Run the Agent: Use the Tkinter GUI or command line:

    bash

    python gui.py  # or python main.py

    Web Interface: Access at http://localhost:5000.

Dependencies

    Python 3.6+
    boto3, Flask, pynput, Pillow, Tkinter