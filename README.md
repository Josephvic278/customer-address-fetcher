# Customer Address Retrieval Tool

This project provides a Python script designed to interact with a hypothetical API to retrieve, clean, validate, and save customer addresses. The script also allows for testing via mock data to simulate API responses in the absence of a live API.

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

5. **Mock Testing**:
   - Includes a mock setup to simulate API responses for testing.

## Prerequisites

- Python 3.7+
- Required Python libraries:
  - `requests`
  - `csv` (built-in)
  - `os` (built-in)
  - `tabulate`
  - `unittest.mock` (built-in)

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

### Mock Testing

To test the script without an actual API:
- The script includes mock responses to simulate:
  - Total customer count.
  - Customer address data for each customer.

The mock data assumes there are 10 customers, and their addresses are generated dynamically.

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

### Mocking API Responses

The script uses `unittest.mock.patch` to:
- Simulate a total customer count endpoint.
- Simulate address data for individual customers.

This enables testing without a live API.

## Future Enhancements

1. Integration with a real API when available.
2. Enhanced validation logic for more robust data cleaning.
3. Command-line arguments for specifying output file names and formats.