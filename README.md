# Worker Generation Script

## Overview
This Python script dynamically generates worker records with attributes including ID, name, hourly rate, hours worked, salary calculation, and employment level classification.

## Features
- **Dynamic Worker Generation**: Creates worker objects with calculated attributes
- **Salary Calculation**: Automatically computes weekly salary based on hourly rate and hours worked
- **Level Classification**: Assigns employment levels (A1, A5-F) based on salary ranges
- **Error Handling**: Includes try-except blocks to gracefully handle potential data errors
- **Formatted Output**: Displays worker information in an easy-to-read format

## How It Works

### Worker Attributes
Each worker object contains the following attributes:
- **id**: Unique identifier (W1, W2, W3, W4)
- **name**: Worker name (Worker_1, Worker_2, etc.)
- **rate**: Hourly rate (ranges from $10 to $14)
- **hours**: Hours worked per week (fixed at 40 hours)
- **salary**: Calculated weekly salary (rate × hours)
- **level**: Employment level based on salary thresholds

### Level Classification Logic
The script assigns employment levels based on the following salary ranges:
- **A1**: Salary between $10,000 and $20,000
- **A5-F**: Salary between $7,500 and $30,000
- **None**: Default level if salary doesn't meet any criteria

**Note**: A worker can have multiple levels assigned if they meet multiple salary ranges.

## Usage
Simply run the script:
```bash
python workers.py