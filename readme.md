# Stock Data Analysis and Trading Strategy

This project loads stock data from a Google Sheet, inserts it into a MySQL database, and then performs a trading strategy analysis. It calculates short and long moving averages (SMA), generates buy/sell signals, and compares the performance of the strategy with the market.

## Features

- **Data Insertion**: Pulls data from a Google Spreadsheet in CSV format and inserts it into a MySQL database.
- **Moving Average Strategy**: Calculates short and long Simple Moving Averages (SMA) to generate trading signals.
- **Performance Analysis**: Compares the strategy’s performance with the market returns.

## Requirements

Before running the project, ensure that you have the following installed:

- Python 3.x
- MySQL Server
- Libraries:
  - `mysql-connector`
  - `pandas`
  - `sqlalchemy`
  - `unittest`

You can install the necessary Python libraries by running:

```bash
pip install mysql-connector pandas sqlalchemy
```

## Database Setup

Ensure you have a MySQL database named `Analysis`. The following table is required for the data insertion:

```sql
CREATE TABLE ticker_data (
    datetime DATETIME,
    instrument VARCHAR(10),
    open DECIMAL(10, 2),
    high DECIMAL(10, 2),
    low DECIMAL(10, 2),
    close DECIMAL(10, 2),
    volume INT
);
```

## How to Use

### 1. Add Data to the Database

Run the following script to fetch stock data from the Google Sheet and insert it into the MySQL database:

```bash
python main.py
```

Select option `1` to add data to the database.

### 2. Perform Analysis

After loading the data, select option `2` to analyze the stock data. The analysis will calculate short and long moving averages and generate buy/sell signals based on their crossover.

### Example Output

```bash
Strategy Performance:
1210    0.601602
1211    0.618119
1212    0.615991
1213    0.610355
1214    0.602331
```

### Test Cases

The `test_case.py` file contains unit tests to validate data integrity and ensure correct data types. You can run the tests with:

```bash
python test_case.py
```

### Unit Test Methods:

- **test_datetime**: Ensures that the `datetime` column contains valid date/time values.
- **test_instrument**: Verifies that the `instrument` column contains only string values.
- **test_numericData**: Confirms that the `open`, `high`, `low`, and `close` columns contain numeric values.
- **test_volume**: Ensures that the `volume` column contains integer values.

## Project Structure

```
.
├── main.py          # Main script for data loading and analysis
├── test_case.py     # Unit tests for data validation
└── README.md        # Project documentation
```
## Image 
![Screenshot 2025-01-19 173536](https://github.com/user-attachments/assets/90af3a85-1d3d-453c-b426-2dfbab55e8ba)
![Screenshot 2025-01-19 174737](https://github.com/user-attachments/assets/8d0a46ac-a28b-4aac-98da-79b91ad1f528)
