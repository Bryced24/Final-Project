# Event Management System

## Description

This Event Management System is a command-line interface (CLI) application that allows users to manage events efficiently. Built with Python, it leverages MongoDB for data storage and offers a range of functionalities, including creating, reading, updating, and deleting (CRUD) event information.

## Features

- **Create Event**: Add new events with details such as title, date, location, and description.
- **List Events**: View all the events stored in the database.
- **Update Event**: Modify details of existing events.
- **Delete Event**: Remove events from the system.

## Technical Stack

- **Language**: Python
- **Database**: MongoDB
- **Other Tools**: Docker, GitHub, Makefile, flake8, mypy, unittest

## Installation

1. **Clone the Repository** 
~~~
git clone [https://github.com/Bryced24/Final-Project]
~~~
2. **Set Up a Virtual Environment (optional)**
~~~
python -m venv venv
~~~
~~~
source venv/bin/activate # For Unix or MacOS
venv\Scripts\activate # For Windows
~~~
3. **Install Dependencies**
~~~
pip install -r requirements.txt
~~~

## Usage

To start the application, run: 
~~~
python cli.py
~~~

Follow the on-screen prompts to interact with the system.

## Testing

To run the tests, use the following command: 
~~~
make test
~~~

## Linting

To run flake8 for linting, use:
~~~
make lint
~~~

## Type Checking

To perform type checks with mypy, run:
~~~
make type-check
~~~

## Continuous Integration

The project is configured with GitHub Actions for continuous integration, which runs tests, linting, and type checking on every push.

## Contributing

Contributions to this project are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a new Pull Request.










