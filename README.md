# Customer Address Retrieval Tool

This project provides a Python script designed to interact with a hypothetical API to retrieve, clean, validate, and save customer addresses. The script is designed to work directly with the API and does not include mock data.

## Features

1. **Fetch Customer Data**:
   - Retrieves the total number of customers from the API.
   - Fetches address data for each customer using individual API endpoints.

2. **Validation and Cleaning**:
   - Ensures all address fields are present and formatted correctly.
   - Handles missing fields gracefully by substituting default values.

3. **CSV Export**:
   - Saves all cleaned customer address data to a CSV file for easy access.

4. **Tabular Display**:
   - Displays the list of addresses in a readable tabular format using the `tabulate` library.

## Prerequisites

- Python 3.7+
- Required Python libraries:
  - `requests`
  - `csv` (built-in)
  - `os` (built-in)
  - `tabulate`

You can install `tabulate` using:
```bash
pip install tabulate
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/your-repo/customer-address-retrieval.git
cd customer-address-retrieval
```

2. Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Script

1. Run the script directly using:
```bash
python customer_address_retrieval.py
```

2. The script will:
   - Fetch customer data.
   - Save the results to a CSV file named `customer_addresses.csv` in the current working directory.
   - Display the data in a tabular format.

## Output

1. **CSV File**:
   - The CSV file will contain the following fields for each customer:
     - `id`, `first_name`, `last_name`, `street`, `postcode`, `state`, `country`, `lat`, `lon`
   - Default filename: `customer_addresses.csv`

2. **Tabular Data**:
   - The addresses are displayed in the terminal in a structured format.

## Code Structure

### Functions

1. `validate_request(response)`:
   - Validates API responses and extracts JSON data.

2. `validate_and_clean(address)`:
   - Ensures all required fields are present in the address and formats them.

3. `total_customer_count()`:
   - Retrieves the total number of customers from the API.

4. `fetch_all_customer_addresses()`:
   - Fetches, cleans, and aggregates addresses for all customers.

5. `write_to_csv(addresses, filename)`:
   - Writes cleaned data to a CSV file.

6. `main()`:
   - Orchestrates the execution of all functions and handles output.

## Future Enhancements

1. Enhanced validation logic for more robust data cleaning.
2. Command-line arguments for specifying output file names and formats.
3. Error handling for network issues and API errors.