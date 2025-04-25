import requests
import pprint

# Replace <your-credentials> with your actual credentials
creds = <your-credentials>
url = <your-url>


def main():
    print("Hello from courier-connect!")
    headers = {
        "Authorization": f"Basic {creds}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Request was successful!")
        pprint.pprint(response.json())
    else:
        print(f"Request failed with status code {response.status_code}")

    return response.json()

if __name__ == "__main__":
    respone=main()



