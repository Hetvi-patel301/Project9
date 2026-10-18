# Data Analysis & Visualization Program

### Introduction

The **Data Analysis & Visualization Program** is a menu-driven Python application developed using Pandas, NumPy, Matplotlib, and Seaborn. It helps users load, explore, clean, manipulate, analyze, and visualize data from CSV files.

This project uses Object-Oriented Programming (OOP) to organize different data analysis functionalities into a single `SalesData` class. It also includes exception handling to manage common errors during file operations and user input.

### Features

#### 1. Load Dataset
- Load datasets from CSV files.
- Handle missing files and empty CSV files.
- Display dataset loading status.

#### 2. Explore Data
- Display the first five rows.
- Display the last five rows.
- Display column names.
- Check column data types.
- Display basic dataset information.

#### 3. Handle Missing Data
- Display rows containing missing values.
- Fill missing numeric values using the column mean.
- Remove rows containing missing values.
- Replace missing values with a user-defined value.

#### 4. Mathematical Operations
Perform mathematical operations on numeric columns:
- Addition
- Subtraction
- Multiplication
- Division

Includes numeric column validation and division-by-zero handling.

#### 5. Combine DataFrames
- Concatenate two DataFrames.
- Merge DataFrames using a common column.
- Optionally replace the current dataset with the combined result.

#### 6. Split Data
- Select a column and enter a value.
- Separate rows into two groups based on the selected value.
- Display both resulting datasets.
- Save the groups as separate CSV files.

#### 7. Search, Sort and Filter
- Search for a specific value.
- Sort data in ascending or descending order.
- Filter numeric data using a minimum value.
- Filter rows by category.

#### 8. Advanced Operations
- Create pivot tables using sum, mean, and count.
- Reset the DataFrame index.
- Calculate group-wise averages using `groupby()` and `transform()`.

#### 9. Statistical Analysis
Generate useful statistical summaries:
- Sum
- Mean
- Median
- Standard deviation
- Variance
- Minimum and maximum
- Percentiles and quartiles
- Correlation matrix
- Descriptive statistics
- Group-wise statistical analysis

#### 10. Data Visualization
Create nine types of visualizations using Matplotlib and Seaborn:

1. Bar Plot
2. Line Plot
3. Scatter Plot
4. Pie Chart
5. Histogram
6. Stack Plot
7. Multiple Subplots
8. Correlation Heatmap
9. Box Plot

#### 11. Save Visualization
- Save generated visualizations as image files.
- Export figures at 300 DPI.
- Use tight bounding boxes for better image presentation.

### Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Creating graphs and plots |
| Seaborn | Statistical data visualization |
| CSV | Dataset input and output |
| OOP | Organizing code using classes and methods |

### Requirements

- Python 3.10 or above
- Pandas
- NumPy
- Matplotlib
- Seaborn

Install all required libraries using:

```bash
pip install pandas numpy matplotlib seaborn
```

### How to Run

**Step 1: Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**Step 2: Open the project directory**

```bash
cd YOUR_PROJECT_FOLDER
```

**Step 3: Run the Python file**

```bash
python main.py
```

Replace `main.py` with the actual name of your Python file.

**Step 4: Load a dataset**

Select option `1` from the main menu and enter the path of your CSV file.

**Step 5: Analyze your data**

Choose the required options to explore, clean, manipulate, analyze, or visualize the dataset.

###  Main Menu

```text
-------Data Analysis & Visualization Program-------
Please select an option:
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
```

###  Project Structure

```text
Project_9/
│
├── Pandas_Analyzer_and_Data_Visualization.py
├── sales_data.csv
├── sales_data_2.csv
└── README.md
```


### Created by:

**Hetvi Patel**
