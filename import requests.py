import requests

# Replace this list with your actual list of API endpoints
api_endpoints = [
    "https://api.example.com/endpoint1",
    "https://api.example.com/endpoint2",
    "https://api.example.com/endpoint3"
]

# Replace with your authentication cookie value
auth_cookie = "your_auth_cookie_value"

# Prepare the headers with the authentication cookie
headers = {
    "Cookie": f"auth_cookie_name={auth_cookie}"
}

# Function to extract the first name from the JSON response
def extract_first_name(json_response):
    try:
        return json_response['data'][0]['assetUsers']['data'][0]['person']['firstName']
    except (KeyError, IndexError):
        return None

# Iterate through the list of API endpoints and make a REST call for each item
for url in api_endpoints:
    response = requests.get(url, headers=headers)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        json_response = response.json()
        first_name = extract_first_name(json_response)

        if first_name:
            print(f"First name: {first_name}")
        else:
            print("Could not extract the first name from the JSON structure.")
    else:
        print(f"Error: Received status code {response.status_code} for URL {url}")
