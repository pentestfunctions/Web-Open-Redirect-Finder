
# 🛡️ Open Redirect Finder

This Python script is designed for security enthusiasts and penetration testers to identify open redirects on websites. It processes URLs fetched from the Wayback Machine and checks for potential open redirect vulnerabilities.

## 🚀 Features

- 🕵️‍♂️ Identifies potential open redirects from archived URLs.
- 🔍 Filters URLs based on specific patterns.
- 🚦 Handles HTTP response codes relevant to redirection.
- 🛠 Deduplicates URLs based on their base paths to optimize the search.

## ⚙️ Usage

To use this script, simply run it with Python and provide a URL as input:

```bash
python open_redirect_finder.py
```

## 📚 How It Works

1. The script removes common URL prefixes (http://, https://, www) from the user input.
2. It constructs a query URL for the Wayback Machine to fetch archived URLs.
3. The script filters these URLs based on specific redirection patterns.
4. Each URL is checked for HTTP response codes indicative of open redirects.
5. URLs are deduplicated to avoid redundant checks, focusing on unique base paths. (Accounts for parameter information to avoid duplicates:\
```bash
?bannerID=1&redirectURL=https://google.com
?bannerID=2&redirectURL=http://facebook.com
```
- The script will identify that the parameters have barely changed and only target the first encounter. (Yes this could lead to missing something due to bannerID being changed but it is only in very niche cases where this would be an issue)

## 🛠️ Installation

You need Python 3.x and the `requests` library. Install the dependencies using:

```bash
pip install requests
```

## ⚠️ Disclaimer

This tool is intended for educational and ethical testing purposes only. Usage of this script for probing websites without consent is illegal and against the terms of service of many websites.
