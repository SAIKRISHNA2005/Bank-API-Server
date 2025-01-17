# Bank API with Flask

## Overview

This repository contains a simple RESTful API built using Flask, SQLAlchemy, and PostgreSQL. The API is designed to interact with two entities: `Bank` and `Branch`. The application allows users to fetch details of banks and branches, search branches with autocomplete, and get specific branch details using various filters.

The application uses the `bank.csv` and `bank_branches.csv` files for importing bank and branch data, respectively.

## Setup

To run the application, follow the instructions below:

### Prerequisites
- Python 3.x
- PostgreSQL database
- Flask
- Flask-SQLAlchemy
- Marshmallow-SQLAlchemy
- PostgreSQL database with the necessary schema (described below).

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/bank-api.git
   cd bank-api

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

3. Create and configure a PostgreSQL database:
- Set up a PostgreSQL database called bankdb (or modify the SQLALCHEMY_DATABASE_URI in app.py to use a different database).
- Ensure the database contains the necessary tables, or run the app to let SQLAlchemy create them automatically.

4. Load data from the bank.csv and bank_branches.csv files:
- The bank.csv file contains the following fields: name, id.
- The bank_branches.csv file contains the following fields: ifsc, bank_id, branch, address, city, district, and state.

5. Set up environment variables for the database connection in app.py:

python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/bankdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

### Running the Application
Run the Flask application by executing:


    ```bash
    python app.py

This will start the Flask server on http://127.0.0.1:5000/.

### Available Endpoints

1. GET /
Returns a welcome message.
Example response:
json
{
    "message": "Welcome to the Bank API!"
}

2. GET /api/branches
- Fetches all branches.
- Optionally accepts a q query parameter to search for branches by various fields like branch, address, city, district, or state.

3. GET /api/branches/autocomplete
- Fetches branches with autocomplete functionality for branch names.

4. GET /api/banks
- Fetches all banks.

5. GET /api/branches/branch
- Fetches details of a branch based on provided filters like ifsc, bank_id, or branch name.
- Example request:

http
GET /api/branches/branch?ifsc=SBIN0001

### Testing
The application includes unit tests using Python's unittest framework. These tests check the functionality of the endpoints and ensure that the API behaves correctly.
To run the tests:

    ```bash
    python -m unittest test_app.py

### Performance and Duration
- The code includes middleware that tracks the duration of each request and adds an X-Duration header to the response. This is useful for monitoring the performance of the API.
- The before_request and after_request methods in app.py are responsible for calculating the time taken by each request.

### Time Taken for Development
The following is an estimate of the time taken to complete the assignment:
- API Design and Implementation: 2 hours
- Database Schema Setup: 1 hour
- CSV Data Integration: 2 hours
- Testing and Debugging: 1 hours
- Total Time Taken: 6 hours

### Code Explanation
## app.py
- Flask Application: The core of the API, initialized with Flask(__name__).
- Database Setup: SQLAlchemy is used to connect to the PostgreSQL database.
- Middleware: The before_request and after_request functions are used to track the duration of each API request.
- Error Handling: Custom error handling for HTTPExceptions using @app.errorhandler(HTTPException).
- Routes: Routes to fetch and filter bank and branch data.

## models.py
- SQLAlchemy Models: Defines two models, Bank and Branch, with appropriate fields and relationships.
- Bank has a simple id and name.
- Branch has fields like ifsc, bank_id, branch, address, city, district, and state, with a foreign key linking to Bank.

## test_app.py
- Unit Tests: Tests the main functionality of the API, including basic routes like the home route, branch retrieval, and error handling when a branch is not found.

### Conclusion
This repository implements a fully functional Bank API with capabilities for managing bank and branch information. It includes search and autocomplete features, error handling, and performance tracking, all of which provide a robust backend for working with bank and branch data.
yaml
This `README.md` file explains the setup, running instructions, endpoints, testing, performance tracking, time estimates, and a brief code overview for the repository.
