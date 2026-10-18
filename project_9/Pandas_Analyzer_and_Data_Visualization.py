import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
class SalesData:
    def __init__(self):
        self.data = None
        self.fig = None
    def load_data(self,file_path):
        try:
            self.data=pd.read_csv(file_path)
            print("Dataset loaded successfully!")
        except FileNotFoundError:
            print("CSV file not found.")
        except pd.errors.EmptyDataError:
            print("The CSV file is empty.")
        except Exception as e:
            print("Error:",e)
    def check_data(self):
        if self.data is None:
            print("\nPlease load a dataset first.")
            return False
        return True
    def explore_data(self):
        if not self.check_data():
            return
        print("---- Explore Data ----")
        print("1.Display the first 5 rows")
        print("2.Display the last 5 rows")
        print("3.Display column names")
        print("4.Display data types")
        print("5.Display basic information")
        choice = int(input("Enter your choice:"))
        match choice:
            case 1:
                print(self.data.head(5))
            case 2:
                print(self.data.tail(5))
            case 3:
                print(self.data.columns.to_list())
            case 4:
                print(self.data.dtypes)
            case 5:
                self.data.info()
            case _:
                print("Invalid choice!!")
    def clean_data(self):
        if not self.check_data():
            return
        print("---Handle Missing Data---")
        print("1.Display rows with missing values")
        print("2.Fill missing values with mean")
        print("3.Drop rows with missing values")
        print("4.Replace missing value with a specific value")
        choice = int(input("Enter your choice:"))
        match choice:
            case 1:
                missing = self.data[self.data.isna().any(axis=1)]
                print(missing)
            case 2:
                numeric_cols = self.data.select_dtypes(include=np.number).columns
                self.data[numeric_cols]=self.data[numeric_cols].fillna(self.data[numeric_cols].mean())
                print("Numeric missing value filled with mean")
            case 3:
                self.data.dropna(inplace =True)
                print("missing values removed.")
            case 4:
                value = input("Enter replacement value:")
                self.data.fillna(value,inplace=True)
                print("Missing value replaced.")
            case _:
                print("Invalid choice!!")
    def mathematical_operations(self):
        if not self.check_data():
            return
        numeric_cols = self.data.select_dtypes(include=np.number).columns.to_list()
        if len(numeric_cols) == 0:
            print("No numeric columns available.")
            return
        print("Numeric Columns:",numeric_cols)
        column = input("Enter column name:")
        if column not in numeric_cols:
            print("Invalid numeric column!")
            return
        try:
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            n =float(input("Enter a number:"))
            choice = int(input("Enter your choice:"))
            values = self.data[column]
            match choice:
                case 1:
                    answer = values + n
                case 2:
                    answer = values - n
                case 3:
                    answer = values *n
                case 4:
                    if n==0:
                        print("Cannot divide by zero.")
                        return
                    answer = values/n
                case _:
                    print("Invalid choice!")
                    return
            print("Original values and answer:")
            print(pd.DataFrame({"Original":values,"Answer":answer}))
        except ValueError:
            print("Please enter a valid number.")
    def combine_data(self):
        if not self.check_data():
            return
        print("\n--- Combine DataFrames ---")
        print("1. Concatenate DataFrames")
        print("2. Merge DataFrames using a common column")
        try:
            choice = int(input("Enter your choice:"))
            file_path = input("Enter your second CSV file path:")
            second_data = pd.read_csv(file_path)
            match choice:
                case 1:
                    result = pd.concat([self.data,second_data])
                    print(result)
                case 2:
                    print("Common columns:",list(set(self.data.columns)&set(second_data.columns)))
                    key = input("Enter common column name:")
                    if (key not in self.data.columns or key not in second_data.columns):
                        print("Column not found in both datasets.")
                        return
                    result = pd.merge(self.data,second_data,on = key,how = "inner")
                    print(result) 
                case _:
                    print("Invalid choice!")
                    return
            save = input("Replace current dataset?(y/n)").lower()
            if save == "y":
                self.data =result
                print("Current dataset updated.")
        except FileNotFoundError:
            print("Second CSV file not found.")
        except Exception as e:
            print("Error combining datasets:",e)
    
           
    def split_data(self):
        if not self.check_data():
            return
        print("---Split Data---")
        print("Enter columns:",list(self.data.columns))
        column = input("Enter column name to split by:")
        if column not in self.data.columns:
            print("Invalid Column Name!!")
            return
        value = input("Enter value to split:")
        first = self.data[self.data[column].astype(str)==value]
        second = self.data[self.data[column].astype(str)!=value]
        print("First Dataset after splitting")
        print(first)
        print("second Dataset after splitting")
        print(second)
        save = input("Save both groups as CSV files? (y/n): ").lower()
        if save == "y":
            first.to_csv("sales_group_1.csv", index=False)
            second.to_csv("sales_group_2.csv", index=False)
            print("Both groups saved successfully.")
    def search_sort_filter(self):
            if not self.check_data():
                return
            print("----- Search, Sort and Filter -----")
            print("1. Search for a value")
            print("2. Sort data")
            print("3. Filter numeric data")
            print("4. Filter by category")
            try:
                choice = int(input("Enter your choice:"))
                match choice:
                    case 1:
                        column = input("Enter column name: ")
                        if column not in self.data.columns:
                            print("Invalid column!")
                            return                
                        value = input("Enter value to search: ")
                        result = self.data[self.data[column].astype(str) == value]
                        print(result)
                    case 2:
                        column = input("Enter column name to sort: ")
                        if column not in self.data.columns:
                            print("Invalid column!")
                            return                
                        order = input("Ascending order? (y/n): ").lower() == "y"
                        print(self.data.sort_values(by=column, ascending=order))
                    case 3:
                        numeric_cols = self.data.select_dtypes(include=np.number).columns.tolist()
                        print("Numeric columns:", numeric_cols)
                        column = input("Enter numeric column: ")
                        if column not in numeric_cols:
                            print("Invalid numeric column!")
                            return
                        value = float(input("Enter minimum value: "))
                        print(self.data[self.data[column] > value])
                    case 4:
                        column = input("Enter category column: ")
                        if column not in self.data.columns:
                            print("Invalid column!")
                            return
                        value = input("Enter category value: ")
                        print(self.data[self.data[column].astype(str) == value])
                    case _:
                        print("Invalid choice!")
            except ValueError:
                print("Please Enter a valid number.")
    def advanced_operations(self):
        if not self.check_data():
            return
        print("--- Advanced Operations ---")
        print("1. Create a pivot table")
        print("2. Re-index DataFrame")
        print("3. Display transformed group averages")
        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    print("Available columns:", list(self.data.columns))
                    index_col = input("Enter index/group column: ")
                    value_col = input("Enter numeric values column: ")
                    if index_col not in self.data.columns:
                        print("Invalid index column!")
                        return
                    if value_col not in self.data.columns:
                        print("Invalid values column!")
                        return
                    print(pd.pivot_table(self.data,index=index_col,values=value_col,aggfunc=["sum", "mean", "count"]))
                case 2:
                    print(self.data.reset_index())
                case 3:
                    group_col = input("Enter group column: ")
                    value_col = input("Enter numeric column: ")
                    if group_col not in self.data.columns:
                        print("Invalid group column!")
                        return
                    if value_col not in self.data.columns:
                        print("Invalid numeric column!")
                        return
                    if value_col not in self.data.select_dtypes(include=np.number).columns:
                        print("Invalid numeric column!")
                        return
                    print(self.data.assign(Group_Average=self.data.groupby(group_col)[value_col].transform("mean")))
    
                case _:
                    print("Invalid choice!")
    
        except ValueError:
            print("Please enter a valid number.")
    
                    
    def statistical(self):
        if not self.check_data():
            return
        numeric = self.data.select_dtypes(include=np.number)
        if numeric.empty:
            print("No numeric data available.")
            return
        print("\n--- Statistical Analysis ---")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard deviation")
        print("5. Variance")
        print("6. Minimum and maximum")
        print("7. Percentiles")
        print("8. Correlation")
        print("9. Full descriptive statistics")
        print("10. Group-wise analysis")
        try:
            choice = int(input("Enter your choice: "))        
            match choice:
                case 1:
                    print(numeric.sum())
                case 2:
                    print(numeric.mean())        
                case 3:
                    print(numeric.median())
                case 4:
                    print(numeric.std())
                case 5:
                    print(numeric.var())
                case 6:
                    print("Minimum:\n", numeric.min())
                    print("Maximum:\n", numeric.max())
                case 7:
                    print("25th percentile:\n", numeric.quantile(0.25))
                    print("50th percentile:\n", numeric.quantile(0.50))
                    print("75th percentile:\n", numeric.quantile(0.75))
                case 8:
                    print(numeric.corr())
                case 9:
                    print(numeric.describe())
                    print("\nStandard deviation:\n", numeric.std())
                    print("\nVariance:\n", numeric.var())
                    print("\nQuartiles:\n", numeric.quantile([0.25, 0.50, 0.75]))
                case 10:
                    column = input("Enter group column: ")
                    metric = input("Enter numeric column to analyze: ")
                    if column not in self.data.columns:
                        print("Invalid group column!")
                        return
        
                    if metric not in numeric.columns:
                        print("Invalid numeric column!")
                        return
        
                    print(self.data.groupby(column)[metric].agg(["sum", "mean", "count", "min", "max"]))
        
                case _:
                    print("Invalid choice!")
        
        except ValueError:
            print("Please enter a valid number.")
    def visualize_data(self):
        if not self.check_data():
            return
        numeric_cols = self.data.select_dtypes(include=np.number).columns.tolist()
        
        if not numeric_cols:
            print("No numeric columns available for plotting.")
            return
        
        print("\n--- Matplotlib Visualization ---")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")
        print("7. Multiple Subplots")
        print("8. Seaborn Heatmap")
        print("9. Seaborn Box Plot")
        try:
            choice = int(input("Enter your choice: "))
            self.fig, ax = plt.subplots()        
            if choice in [1, 2, 3, 6, 7]:
                print("Numeric columns:", numeric_cols)
        
            if choice == 1:
                column = input("Enter column for bar plot: ")
                if column not in numeric_cols:
                    print("Invalid numeric column!")
                    plt.close(self.fig)
                    return
                self.data[column].plot(kind="bar", ax=ax)
                ax.set_ylabel(column)
                ax.set_title("Bar Plot")
                ax.legend()
                ax.grid()
        
            elif choice == 2:
                column = input("Enter column for line plot: ")
                if column not in numeric_cols:
                    print("Invalid numeric column!")
                    plt.close(self.fig)
                    return
                self.data[column].plot(kind="line", marker="o", ax=ax)
                ax.set_title("Line Plot")
                ax.set_ylabel(column)
                ax.grid()
            elif choice == 3:
                x_col = input("Enter X-axis column: ")
                y_col = input("Enter Y-axis column: ")
                if x_col not in numeric_cols or y_col not in numeric_cols:
                    print("Please select numeric columns.")
                    plt.close(self.fig)
                    return
                ax.scatter(self.data[x_col], self.data[y_col])
                ax.set_xlabel(x_col)
                ax.set_ylabel(y_col)
                ax.set_title("Scatter Plot")    
            elif choice == 4:
                column = input("Enter column for pie chart: ")
                if column not in numeric_cols:
                    print("Invalid numeric column!")
                    plt.close(self.fig)
                    return
                values = self.data[column].dropna()
                labels = values.index.astype(str)
                ax.pie(values, labels=labels, autopct="%1.1f%%")
                ax.set_title("Pie Chart")        
            elif choice == 5:
                column = input("Enter column for histogram: ")
                if column not in numeric_cols:
                    print("Invalid numeric column!")
                    plt.close(self.fig)
                    return
                ax.hist(self.data[column].dropna(), bins=10)
                ax.set_xlabel(column)
                ax.set_ylabel("Frequency")
                ax.set_title("Histogram")
            elif choice == 6:
                x_col = input("Enter X-axis column: ")
                y_col = input("Enter Y-axis column: ")
                if x_col not in numeric_cols or y_col not in numeric_cols:
                    print("Please select numeric columns.")
                    plt.close(self.fig)
                    return
                x = self.data[x_col].to_numpy()
                y = self.data[y_col].to_numpy()
                ax.stackplot(np.arange(len(x)),x, y,labels=[x_col, y_col])
                ax.legend()
                ax.set_title("Stack Plot")
                ax.set_xlabel("Row Index")
                ax.set_ylabel("Value")
        
            elif choice == 7:
                columns = numeric_cols[:4]
                if len(columns) < 2:
                    print("At least two numeric columns are required.")
                    plt.close(self.fig)
                    return
                plt.close(self.fig)
                self.fig, axes = plt.subplots(len(columns), 1, figsize=(8, 3 * len(columns)))
                if len(columns) == 1:
                    axes = [axes]
                for axis, column in zip(axes, columns):
                    self.data[column].plot(ax=axis)
                    axis.set_title(column)
        
            elif choice == 8:
                plt.close(self.fig)
                self.fig, ax = plt.subplots()
                sns.heatmap(self.data[numeric_cols].corr(),annot=True,cmap="coolwarm",ax=ax)
                ax.set_title("Correlation Heatmap")
        
            elif choice == 9:
                column = input("Enter numeric column: ")
                if column not in numeric_cols:
                    print("Invalid numeric column!")
                    plt.close(self.fig)
                    return
                sns.boxplot(data=self.data, x=column, ax=ax)
                ax.set_title("Box Plot")
            else:
                print("Invalid choice!")
                plt.close(self.fig)
                return
            self.fig.tight_layout()
            plt.show()
        
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print("Visualization error:", e)
    def save_visualization(self):
        if self.fig is None:
            print("Please generate a visualization first.")
            return
        file_name = input("Enter file name:").strip()
        if not file_name:
            print("File name cannot be empty.")
            return
        try:
            self.fig.savefig(file_name, dpi=300, bbox_inches="tight")
            print("Visualization saved successfully:", file_name)
    
        except Exception as e:
            print("Error saving visualization:", e)

    def main(self):
        while True:
            print("-------Data Analysis & Visualization Program-------")
            print("Please select an option:")
            print("1.Load Dataset")
            print("2.Explore Data")
            print("3.Perform DataFrame Operations")
            print("4.Handle Missing Data")
            print("5.Generate Descriptive Statistics")
            print("6.Data Visualization")
            print("7.Save Visualization")
            print("8.Exit")
            print("---------------------------------------------------------")
            try:
                choice = int(input("Enter your choice:"))
                print()
                match choice:
                    case 1:
                        file_path = input("Enter the path of the dataset (CSV file):")
                        self.load_data(file_path)
                    case 2:
                        self.explore_data()
                    case 3:
                        print("1.Mathematical Operations")
                        print("2.Combine DataFrames")
                        print("3.Split Data")
                        print("4.Search, Sort and Filter")
                        print("5.Advanced Operations")
                        choice1 = int(input("Enter your choice:"))
                        match choice1:
                            case 1:
                                self.mathematical_operations()
                            case 2:
                                self.combine_data()
                            case 3:
                                self.split_data()
                            case 4:
                                self.search_sort_filter()
                            case 5:
                                self.advanced_operations() 
                    case 4:
                        self.clean_data()
                    case 5:
                        self.statistical()
                    case 6:
                        self.visualize_data()
                    case 7:
                        self.save_visualization()
                    case 8:
                        print()
                        print("Exiting the program. Goodbye!")
                        break
                    case _:
                        print("Invalid choice!")
            except ValueError:
                print("Please enter valid number.")
if __name__ =="__main__":
    analyzer = SalesData()
    analyzer.main()

                