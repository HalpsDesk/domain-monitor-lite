# Domain Monitor — Lite Edition
Local-only version of the Domain Monitor.
Checks domain expiry dates on demand, right from your computer.

## Perfect for:
Personal projects where you don’t mind running checks manually

Users who prefer local scripts over cloud automation

Quick expiry checks without extra setup

## Key Differences from the GitHub Actions Edition
Runs locally — you must run the script yourself (or schedule it)

Single alert method — Gmail email only

Manual configuration — edit the script directly

No hosting — everything runs on your machine

## Features
WHOIS-based expiry checks

Gmail alerts when expiry is near or certain statuses appear

Multiple domain support

Single Python file — easy to edit and review

## Requirements
Python 3.x

python-whois (pip install python-whois)

Gmail account + App Password (if 2FA enabled)

## Setup
Open domain_monitor_lite.py in your editor

Add your domains to DOMAINS

Set Gmail credentials (EMAIL_USERNAME, EMAIL_PASSWORD, EMAIL_RECEIVER)

## Usage
### Run:
python domain_monitor_lite.py

### To automate:

#### Windows: 
Task Scheduler

#### macOS/Linux: 
cron

## Upgrade
Want it to run automatically in the cloud, with Slack and Discord alerts included?
Upgrade to the [GitHub Actions Edition](https://halpsdesk.gumroad.com/l/DomainMonitorGAE).
