# Email-Bombing VAPT Demo

This repository demonstrates a safe, local VAPT workflow for testing "email-bombing" (repeated forgot-password requests) using a local Flask demo and an automated Python script.

> **Important:** All tests in this repository target local demo servers only. Do **not** run automated requests against third-party systems unless you have explicit written authorization from the owner.

## Contents
- `email_bom_py` — automation script: sends up to N password-reset requests, stops on HTTP 429/403, and (by default) only writes a full `report.md` if no 429/403 was observed.
- `demo_app.py` — simple forgot-password demo (no real emails sent).
- `demo_app_token.py` — token-in-URL demo to emulate `tbtoken` style flows.
- `report_sample.md` — sanitized sample report from a local demo run.
- `requirements.txt` — Python dependencies.(Flask, requests, beautifulsoup4 if used)
- `.gitignore` — recommended to exclude `venv/` and transient report files.

## Quick start (Kali / Linux)

1. Clone the repo:
```bash
git clone https://github.com/<your-username>/email-bombing-demo.git
cd email-bombing-demo

## Create a virtual environment and install dependencies:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


## Start the demo server (terminal 1):

python3 demo_app_token.py
# runs on http://127.0.0.1:5001


## Start Burp Suite (optional) and set the proxy listener to 127.0.0.1:8080. For automation set Proxy → Intercept = OFF.

## Run the automation (terminal 2). Replace <demo_token> with a demo token (local only):

./email_bom_py --url "http://127.0.0.1:5001/password-reset?tbtoken=<demo_token>" --email "test@example.com" --burp


## Inspect report_sample.md (sanitized) or report.md if the automation produced one. Note: if the script observes a 429 or 403 the run will skip producing a full report.md (by design).

## Notes & ethics

Do not run the automation against third-party services without explicit written authorization (VDP scope + signed/email confirmation). Save any authorization offline (do not publish it).
Remove or redact any real tokens, secrets, or live-target screenshots before publishing.
Use the included demo servers for safe demonstration and testing.
