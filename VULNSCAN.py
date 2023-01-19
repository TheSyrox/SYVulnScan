import requests

url = input("Enter the website URL: ")

# SQL injection test payload
payload = "' OR '1'='1"

# XSS test payload
xss_payload = "<script>alert('XSS')</script>"

# Add payload to the login form
data = {"username": "admin", "password": payload}

# Send the request
r = requests.post(url, data=data)

# Check if the response contains the error message
if "SQL syntax" in r.text:
    print("SQL injection vulnerability detected!")
else:
    print("No SQL injection vulnerability detected.")

# Add payload to the search form
data = {"query": xss_payload}

# Send the request
r = requests.post(url, data=data)

# Check if the payload is reflected in the response
if xss_payload in r.text:
    print("XSS vulnerability detected!")
else:
    print("No XSS vulnerability detected.")

# Check if the website is vulnerable to CSRF
if "csrf_token" not in r.text:
    print("CSRF vulnerability detected!")
else:
    print("CSRF protection implemented.")
