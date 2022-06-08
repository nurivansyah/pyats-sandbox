# PyATS Network Automation Sandbox

## What Is This?

This is a simple Python/PyATS application intended to provide a working example of Network Automation script. The goal of these repo is to be simple, well-documented and to provide a base framework for network engineer to develop other automations off of.

## How To Use This

1. Fill in the relevant information in the `.env` file in the root folder to configure the app. You can simply copy and rename from the provided `.env.example` file and make sure you've created folder for exported script matched to your config file.
2. Run `pip install -r requirements.txt` to install dependencies. If you want to separate python environment for this project, you might need to setup a virtualenv like `virtualenv venv` or anything similar and activate the env `source ./venv/bin/activate` before you install the required python packages.
3. Run `python main.py`
4. Enter the Task Number you want to run
5. Enter the hostname of the device that need to run the Task
