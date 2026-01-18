# CLI Calculator

A simple command-line calculator implemented in Python.
Supports addition, subtraction, multiplication, and division with input validation and error handling.

Built to demonstrate clean separation of logic and input/output, along with unit testing.

## Features
- Addition, subtraction, multiplication, division
- Handles invalid input safely
- Graceful division by zero handling
- Unit tests included with pytest

## Requirements
- Python 3.10+
- pytest (for running tests)

## Installation
Clone the repository:
```
git clone <repo_url>
cd cli-calculator
```
(Optional) Install pytest if not already installed:
```
pip install pytest
```

## Usage
Run the CLI calculator:
```
python main.py
```
Enter calculations in the format:
```
<number> <operator> <number>
```
Examples:
```
2 + 3
10 / 2
exit    # to quit
```

## Testing
Run unit tests using pytest:
```
pytest
```
This will test all calculator functions and validate error handling.

## Author
Muhammad Ahmer

## License
MIT

