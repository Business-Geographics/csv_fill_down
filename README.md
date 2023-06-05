# csv_fill_down
Fill empty CSV cells with data from previous row.

Useful for preparing CSV data for input into a database or Excel PowerQuery.
Developed for processing Australian Bureau of Statistics (ABS) TableBuilder data, where only the first row in flat tables contains the value for that section.

### Usage
input.csv:

| Building   | Floor   | Name |
|------------|---------|------|
| Building A | Floor 1 | Bob  |
|            |         | John |
|            | Floor 2 | Jane |
|            |         | Tim  |


````
python csv_fill_down.py "/path/to/input.csv" "path/to/output.csv"
````
output.csv

| Building   | Floor   | Name |
|------------|---------|------|
| Building A | Floor 1 | Bob  |
| Building A | Floor 1 | John |
| Building A | Floor 2 | Jane |
| Building A | Floor 2 | Tim  |
