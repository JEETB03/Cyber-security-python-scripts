import requests

# Prompt user for the target URL and the file containing directories
target_url = input('[*] Enter Target URL: ')
file_name = input('[*] Enter Name Of The File Containing Directories: ')

def request(url):
    """
    Sends an HTTP GET request to the specified URL.
    
    Args:
        url (str): The URL to send the request to.
    
    Returns:
        Response object if the request is successful, None otherwise.
    """
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass  # Handle connection errors silently

# Open the file containing directories
file = open(file_name, 'r')

# Iterate through each line in the file
for line in file:
    directory = line.strip()  # Remove any leading/trailing whitespace
    full_url = target_url + '/' + directory  # Construct the full URL
    response = request(full_url)  # Send a request to the constructed URL
    if response:  # Check if the response is not None
        print('[*] Discovered Directory At This Path: ' + full_url)
