import sys
import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from FileOperation import FileOperation


class SalesData:
    def __init__(self, data):
        self.data = data

    def eliminate_duplicates(self):
        clean_data = self.data.drop_duplicates()
        return clean_data

    def calculate_total_sales(self):
        total_sales = self.data.groupby('Product')['Total'].sum().reset_index()
        return total_sales

    def calculate_total_sales_per_month(self):
        self.data['Date'] = pd.to_datetime(self.data['Date'], errors='coerce', format='%d.%m.%Y')
        self.data['Month'] = self.data['Date'].dt.to_period('M')
        total_sales_per_month = self.data.groupby('Month')['Total'].sum().reset_index()
        total_sales_per_month.columns = ['Month', 'Total Sales']
        return total_sales_per_month

    def _identify_best_selling_product(self):
        best_selling_product = self.data.groupby('Product')['Quantity'].sum().idxmax()
        return best_selling_product

    def _identify_month_with_highest_sales(self):
        self.data['Date'] = pd.to_datetime(self.data['Date'], errors='coerce', format='%d.%m.%Y')
        self.data['Month'] = self.data['Date'].dt.to_period('M')
        total_sales_per_month = self.data.groupby('Month')['Total'].sum().reset_index()
        month_with_highest_sales = total_sales_per_month.loc[total_sales_per_month['Total'].idxmax()]['Month']
        return month_with_highest_sales.strftime('%Y-%m')

    def analyze_sales_data(self):
        best_selling_product = self._identify_best_selling_product()
        month_with_highest_sales = self._identify_month_with_highest_sales()
        analysis_results = {
            'best_selling_product': best_selling_product,
            'month_with_highest_sales': month_with_highest_sales
        }
        return analysis_results

    def add_additional_values(self, analysis_results):
        minimest_selling_product = self.data.groupby('Product')['Quantity'].sum().idxmin()
        total_sales_all_months = self.data['Total'].sum()
        num_unique_months = len(self.data['Month'].unique())
        average_sales_all_months = total_sales_all_months / num_unique_months
        analysis_results['minimest_selling_product'] = minimest_selling_product
        analysis_results['average_sales'] = average_sales_all_months

        return analysis_results

    def calculate_cumulative_sales(self):
        self.data['Date'] = pd.to_datetime(self.data['Date'], format='%d.%m.%Y')
        self.data['Month'] = self.data['Date'].dt.to_period('M')
        sales_per_product_month = self.data.groupby(['Product', 'Month'])['Total'].sum().reset_index()
        sales_per_product_month['Cumulative Sales'] = sales_per_product_month.groupby('Product')['Total'].cumsum()
        return sales_per_product_month

    def bar_chart_category_sum(self):
        product_quantities = self.data.groupby('Product')['Quantity'].sum()
        plt.figure(figsize=(10, 6))
        product_quantities.plot(kind='bar', color='skyblue')
        plt.title('Sum Of Quantities Sold For Each Product')
        plt.xlabel('Product')
        plt.ylabel('Sum Of Quantities Sold')
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    def calculate_mean_quantity(self):
        total_values = self.data['Total'].values
        mean_total = np.mean(total_values)
        median_total = np.median(total_values)
        second_max_total = np.partition(total_values, -2)[-2]
        print(f"Mean Total: {mean_total}")
        print(f"Median Total: {median_total}")
        print(f"Second Max Total: {second_max_total}")

    def filter_by_sellings_or_and(self):
        condition_1 = (self.data['Quantity'] > 5) | (self.data['Quantity'] == 0)
        condition_2 = (self.data['Price'] > 300) & (self.data['Quantity'] < 2)
        filtered_data = self.data[condition_1 | condition_2]
        return filtered_data

    def divide_by_2(self):
        if 'Quantity' in self.data.columns:
            self.data['BlackFridayPrice'] = self.data['Price'] / 2
            return self.data
        else:
            print("Column 'Quantity' does not exist in the DataFrame.")

    def calculate_stats(self, columns: str = None):
        if columns is not None:
            columns = [col.strip() for col in columns.split(",")]
        if columns is None:
            columns = self.data.columns
        stats_dict = {}
        for column in columns:
            if column in self.data.columns:
                column_data = self.data[column]
                stats_dict[column] = {
                    'max': column_data.max(),
                    'sum': column_data.sum(),
                    'abs': column_data.abs().sum(),
                    'cummax': column_data.cummax().max()
                }
        return stats_dict

    # Task 6 part one

    # 5
    def plot_total_sales_scatter(self):
        total_sales = self.calculate_total_sales()
        plt.figure(figsize=(10, 6))
        plt.scatter(total_sales['Product'], total_sales['Total'], color='pink', edgecolor='navy', alpha=0.7)
        plt.xlabel('Product', fontsize=12)
        plt.ylabel('Total Sales', fontsize=12)
        plt.title('Total Sales per Product', fontsize=16)
        plt.xticks(rotation=90, fontsize=10)
        plt.yticks(fontsize=10)
        plt.axhline(y=total_sales['Total'].mean(), color='pink', linestyle='--', label='Mean Total Sales')
        plt.legend(loc='upper right', fontsize=10)
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    # 6

    def plot_total_sales_per_month_histogram(self):
        total_sales_per_month = self.calculate_total_sales_per_month()
        plt.hist(total_sales_per_month['Total Sales'], bins=10, color='skyblue', edgecolor='black')
        plt.xlabel('Total Sales')
        plt.ylabel('Frequency')
        plt.title('Distribution of Total Sales per Month')
        plt.show()

    # 15

    def filter_by_sellings_or_and__(self):
        filtered_data = self.data[(self.data['Quantity'] > 5) | (self.data['Quantity'] == 0) |
                                  ((self.data['Price'] > 300) & (self.data['Quantity'] < 2))]
        self.plot_line_chart(filtered_data)
        return filtered_data

    def plot_line_chart(self, data):
        product_sales = data.groupby('Product')['Quantity'].sum()
        sorted_product_sales = product_sales.sort_values(ascending=False)
        plt.figure(figsize=(10, 6))
        plt.plot(sorted_product_sales.index, sorted_product_sales.values, marker='o', color='b', linestyle='-')
        plt.xlabel('Product')
        plt.ylabel('Total Quantity Sold')
        plt.title('Total Quantity Sold by Product')
        plt.xticks(rotation=45, ha='right')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    # 8
    def plot_total_sales_scatter(self):
        total_sales = self.calculate_total_sales()
        plt.scatter(total_sales['Product'], total_sales['Total'])
        plt.xlabel('Product')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Product')
        plt.xticks(rotation=90)
        plt.show()

    # מספר 5
    def calculate_total_sales_(self):
        total_sales_per_product = self.data.groupby('Product')['Total'].sum()
        plt.figure(figsize=(10, 6))
        total_sales_per_product.plot(kind='barh', color='pink')
        plt.xlabel('Total Sales')
        plt.ylabel('Product')
        plt.title('Total Sales per Product')
        plt.show()

    # מספר 6
    def plot_total_sales_pie_chart(self):
        total_sales_per_month = self.calculate_total_sales_per_month()
        plt.figure(figsize=(8, 8))
        plt.pie(total_sales_per_month['Total Sales'], labels=total_sales_per_month['Month'].astype(str),
                autopct='%1.1f%%')
        plt.title('Total Sales per Month')
        plt.axis('equal')
        plt.show()

    # מספר 11
    def plot_cumulative_sales_area(self):
        sales_per_product_month = self.calculate_cumulative_sales()
        plt.figure(figsize=(10, 6))
        for product in sales_per_product_month['Product'].unique():
            product_data = sales_per_product_month[sales_per_product_month['Product'] == product]
            plt.fill_between(product_data['Month'].astype(str), product_data['Cumulative Sales'], label=product)
        plt.xlabel('Month')
        plt.ylabel('Cumulative Sales')
        plt.title('Cumulative Sales Over Time')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

    # Task 6 part tow

    # 5 Seaborn Swarm Plot: sns.swarmplot()

    def calculate_total_sales_and_plot(self):
        total_sales = self.calculate_total_sales()
        sns.swarmplot(x='Product', y='Total', data=total_sales)
        plt.show()

    # 5 Seaborn Catplot: sns.catplot()

    def plot_total_sales_catplot(self):
        total_sales = self.calculate_total_sales()
        sns.catplot(x='Product', y='Total', kind='bar', data=total_sales)
        plt.show()

    # 5 Seaborn Pair Plot: sns.pairplot()

    def plot_pairplot(self):
        total_sales_data = self.calculate_total_sales()
        sns.pairplot(total_sales_data)
        plt.title('Pair Plot of Total Sales per Product')
        plt.show()

    # 5 Seaborn Scatter Plot: sns.scatterplot()

    def plot_total_sales_scatter(self):
        total_sales_data = self.calculate_total_sales()
        sns.scatterplot(data=total_sales_data, x='Product', y='Total', hue='Product', palette='Set1', style='Product',
                        size='Total', sizes=(50, 200))
        plt.title('Total Sales per Product')
        plt.xlabel('Product')
        plt.ylabel('Total Sales')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.show()

    # 5  Seaborn Bar Plot: sns.barplot()

    def plot_total_sales_bar(self):
        total_sales_data = self.calculate_total_sales()
        plt.figure(figsize=(10, 6))
        sns.barplot(data=total_sales_data, x='Product', y='Total')
        plt.title('Total Sales per Product')
        plt.xlabel('Product')
        plt.ylabel('Total Sales')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    # Task 7
    # תרגיל 3
    def generate_random_sales(self, product_name):
        product_sales = self.data[self.data['Product'] == product_name]
        if product_sales.empty:
            return "Product not found"

        sales_count = product_sales['Quantity'].sum()
        max_price = product_sales['Total'].max()

        if sales_count == 0 or max_price == 0:
            return "Zero sales or total price"

        start_range = min(sales_count, max_price)
        end_range = max(sales_count, max_price)

        if end_range <= 0:
            return "Invalid range"

        random_number = np.random.randint(start_range, end_range)
        random_data = [random_number, (start_range, end_range)]
        return random_data

    # תרגיל 4

    def print_python_version(self):
        print("Python version:", sys.version)

    # תרגיל 5

    def process_parameters(self, **kwargs):
        result = {}
        for key, value in kwargs.items():
            if isinstance(value, str) and value.startswith("TAG"):
                result[key] = value
            elif isinstance(value, (int, float)):
                print(f"{key}: {value}")
        return result

    # תרגיל 6
    def print_table_data(self, csv_file_path):
        try:
            sales_data = pd.read_csv(csv_file_path)
        except FileNotFoundError:
            print(f"Error: File '{csv_file_path}' not found")
            return
        print("First 3 rows:")
        print(sales_data.head(3))
        print("\nLast 2 rows:")
        print(sales_data.tail(2))
        random_row_index = random.randint(0, len(sales_data) - 1)
        random_row = sales_data.iloc[random_row_index]
        print("\nRandom row:")
        print(random_row)

        # תרגיל 7

    def iterate_table(self, table):
        for index, row in table.iterrows():
            print(row)
