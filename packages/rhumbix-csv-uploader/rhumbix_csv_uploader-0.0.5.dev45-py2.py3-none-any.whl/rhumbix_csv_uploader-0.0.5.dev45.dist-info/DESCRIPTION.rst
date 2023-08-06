# DataLoader

The Rhumbix DataLoader provides a basic utility to import data into your Rhumbix account.  It reads in csv files from the `csv_directory` provided in the invocation, and updates or inserts the data to the Rhumbix company identified.

There are three types of Rhumbix data that can be imported, Projects, Cost Codes, and Worker information. Each data has different required fields and identifiers that roughly follow the csv templates provided by Rhumbix.

This utility requires a Rhumbix account and access to the API. The Rhumbix company is authenticated with the `api_key`. More documentation on the Public API can be found at https://platform.rhumbix.com/public_api/v2/docs/

## Setup
```
pip install rhumbix_csv_uploader
```

## Usage
### Process CSV directory

The script can be invoked as follows:

`rhumbix_csv_uploader csv_directory api_key api_url`

This will process files matching `rhumbix_employee*.csv` as employee files, `rhumbix_project*.csv` as project files, `rhumbix_cost_code*.csv` cost code files, and `rhumbix_budget*.csv` as the budget files.

Optionally, you may provide a `config.json` in your current directory with any of the following parameters:
```json
{
  "api_key" : "YOUR_API_KEY",
  "api_url" : "YOUR_API_URL",
  "employee_filename_pattern" : "YOUR_EMPLOYEE_FILENAME_REGEX",
  "project_filename_pattern" : "YOUR_PROJECT_FILENAME_REGEX",
  "cost_code_filename_pattern" : "YOUR_COSTCODE_FILENAME_REGEX",
  "budget_filename_pattern" : "YOUR_BUDGET_FILENAME_REGEX"
}
```

### Employee CSV
#### File Format
The employee processor expects a csv file with no headers and columns formatted in the following order:

`company_supplied_id, first_name, last_name, classification-role, trade, is_active, phone, email`

### Project CSV
#### File Format
The project processor expects a csv file with no headers. The columns are formatted in the following order:

`job_number, name, is_active, address`

### Cost Code CSV
#### File Format
The cost code processor expects a csv file with no headers. The `phase` is concatenated with the `cost_code` inside the Rhumbix system.  The columns are formatted in the following order:

`job_number, name, cost_code, phase, description`

### Budget CSV
#### File Format
The budget processor expects a csv file with no headers. The columns are formatted in the following order:

`cost_code, job_number, quantities, hours`

### Direct Usage
If desired, the individual loaders can be called directly with the following format.

```python
from rhumbix_csv_uploader import employee_processor
employee_processor.process_csv("rhumbix_csv_uploader/test/exampleCSVs/rhumbix_payroll.csv", API_KEY, API_URL)
```

```python
from rhumbix_csv_uploader import project_processor
project_processor.process_csv("rhumbix_csv_uploader/test/exampleCSVs/rhumbix_wo.csv", API_KEY, API_URL)
```

```python
from rhumbix_csv_uploader import cost_code_processor
cost_code_processor.process_csv("rhumbix_csv_uploader/test/exampleCSVs/rhumbix_job_cost_2.csv", API_KEY, API_URL)
```

```python
from rhumbix_csv_uploader import budget_processor
budget_processor.process_csv("rhumbix_csv_uploader/test/exampleCSVs/rhumbix_budget.csv", API_KEY, API_URL)
```



