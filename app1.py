import requests
import config

# API endpoint and access key
url = "https://app.mojohelpdesk.com/api/v2/tickets"
access_key = config.ACCESS_KEY_ID

# Headers and payload
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = {
    "title": "Commissions",
    "description": f"Please send me monthly reports so I can run commissions",
    "ticket_queue_id": "4",
    "priority_id": "30",
}

# Send POST request
response = requests.post(f"{url}?access_key={access_key}", headers=headers, data=payload)

# Handle response
if response.status_code == 200 or response.status_code == 201:
    print("Ticket created successfully.")
    print(response.json())
else:
    print(f"Failed to create ticket. Status Code: {response.status_code}")
    print(response.text)
