# Netflix Data Analysis - Assignment 4

## Project Overview
This project performs data preparation, cleaning, and exploratory data analysis on a Netflix dataset containing information about movies and TV shows. The analysis includes handling missing values, data exploration, and statistical summarization.

## Dataset Description
- **File**: Netflix_shows_movies.csv
- **Records**: 6,224 entries (after data cleaning)
- **Columns**: 12 features
- **Column Names**: show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description

## Data Preparation & Cleaning

### Steps Performed:
1. **File Renaming**: Renamed `netflix_data.csv` to `Netflix_shows_movies.csv`
2. **Missing Value Analysis**: Identified missing values across all columns
3. **Missing Value Handling**:
   - `director`: Filled with 'no director' (1,969 missing values)
   - `cast`: Filled with 'not listed' (570 missing values)
   - `country`: Filled with 'not known' (476 missing values)
   - `date_added`: Filled with 'not listed' (11 missing values)
   - `rating`: Dropped 10 rows with missing values

### Result:
After cleaning, the dataset contains **6,224 complete records** with no missing values.

## Data Exploration

### Dataset Statistics
- **Total Records**: 6,224
- **Total Columns**: 12
- **Release Year Range**: 1925 - 2020
- **Mean Release Year**: 2013
- **Show ID Range**: 247,747 - 81,235,729

### Data Types
- **Integer**: show_id, release_year
- **Object (String)**: type, title, director, cast, country, date_added, rating, duration, listed_in, description

## Key Findings
- Dataset contains both Movies and TV Shows
- Most content was released between 2013-2018
- Significant portion of data had missing director information
- Dataset is comprehensive with 12 detailed attributes per entry

## Files Included
- `assignment4.ipynb`: Jupyter notebook containing all analysis code and visualizations
- `Netflix_shows_movies.csv`: Cleaned and processed dataset
- `README.md`: Project documentation (this file)

## Libraries Used
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib**: Data visualization
- **seaborn**: Statistical data visualization
- **os**: File operations

## Analysis Workflow

### 1. Data Preparation (Cell 1-3)
- Import required libraries
- Rename data file
- Load dataset into pandas DataFrame

### 2. Data Cleaning (Cell 4-9)
- Check for missing values
- Handle missing values strategically
- Drop rows with critical missing data
- Verify data integrity

### 3. Data Exploration (Cell 10+)
- Explore dataset shape and structure
- Review data types and non-null counts
- Generate statistical summaries
- Display cleaned dataset

## How to Use

1. Ensure you have the required libraries installed:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```

2. Open `assignment4.ipynb` in Jupyter Notebook:
   ```bash
   jupyter notebook assignment4.ipynb
   ```

3. Run the cells sequentially to perform data preparation, cleaning, and analysis

## Author
akugizibwe93

## Date
March 2026

## License
This project is part of an educational assignment at Nexford University.