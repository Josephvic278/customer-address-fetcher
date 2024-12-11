import requests
import csv
import os
from tabulate import tabulate

# API key and headers for authentication
API_KEY = 'ssfdsjfksjdhfgjfgvjdshgvkjsdlgvkjsdgjkl'
HEADERS = {
    'X-API-KEY': API_KEY,
}

# Base URL for the API
BASE_URL = 'https://pysoftware.com/v1'


def validate_request(response):
    """
    Validates the HTTP response.
    :param response: Response object from the requests library
    :return: Parsed JSON data if status code is 200, else raises an exception
    """
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")


def validate_and_clean(address):
    """
    Validates and cleans a single address record.
    :param address: Dictionary containing the address data
    :return: Cleaned and validated address dictionary
    """
    required_fields = {"id", "first_name", "last_name", "street", "postcode", "state", "country", "lat", "lon"}
    cleaned_address = {key: address.get(key, "") for key in required_fields}

    # Additional validation logic can be added here (e.g., type checks, trimming whitespace)
    return cleaned_address


def total_customer_count():
    """
    Fetches the total number of customers.
    :return: Total number of customers as an integer
    """
    endpoint = f'{BASE_URL}/customer_numbers'
    response = requests.get(url=endpoint, headers=HEADERS)
    data = validate_request(response)
    return int(data)


def fetch_all_customer_addresses():
    """
    Fetches and cleans the addresses of all customers.
    :return: List of cleaned customer address dictionaries
    """
    number_of_customers = total_customer_count()
    addresses = []

    for customer_number in range(1, number_of_customers + 1):
        endpoint = f'{BASE_URL}/address_inventory/{customer_number}'
        response = requests.get(url=endpoint, headers=HEADERS)

        try:
            data = validate_request(response)
            cleaned_data = validate_and_clean(data)
            addresses.append(cleaned_data)
        except Exception as e:
            print(f"Failed to fetch address for customer {customer_number}: {e}")

    return addresses


def write_to_csv(addresses, filename="customer_addresses.csv"):
    """
    Writes the list of customer addresses to a CSV file.
    :param addresses: List of cleaned customer address dictionaries
    :param filename: Name of the CSV file to save the data
    :return: Full file path of the saved CSV
    """
    filepath = os.path.join(os.getcwd(), filename)
    with open(filepath, "w", newline="") as csvfile:
        if addresses:
            writer = csv.DictWriter(csvfile, fieldnames=addresses[0].keys())
            writer.writeheader()
            writer.writerows(addresses)
        else:
            print("No addresses to write to CSV.")
    return filepath


def main():
    """
    Main function to fetch, clean, save, and display customer addresses.
    """
    print("Fetching customer addresses...")
    addresses = fetch_all_customer_addresses()

    if not addresses:
        print("No customer addresses found.")
        return

    # Write addresses to CSV file
    csv_path = write_to_csv(addresses)
    print(f"CSV file saved at: {csv_path}")

    # Display addresses in tabular form
    print("\nCustomer Addresses:")
    print(tabulate(addresses, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()