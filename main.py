# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



from FileOperation import FileOperation
from SalesData import SalesData
import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
    print("קראנו את ההוראות")
    print("נהנינו מהפרויקט ומהשיעורים מאד מאד מהסבלנות ומהצורה שהמורה העבירה את השיעור")
    print("החכמנו רבות ויש לנו מרץ וחשק לעבוד בפייתון")
    print("ובנוסף גם הרשנו שהמורה תרמה לנו מעבר לשפה עצמה כמו מקומות עבודה תקשורת נכונה בין גברים ונשים")
    print("יתרונות של השפה:")
    print("1 שפה קלה ונוחה לכתיבה")
    print("2 שפה מובנת ")
    print("3 יש בה הרבה פיצרים שימושיים ומגניבים")
    print("4 קל להתקין עליה ספריות ולעבוד איתם בצורה קלה ונוחה")
    print("גילינו כמה פייתון היא שפה רחבה ומלאת אפיקים")
    print("נהנינו שאפשר לשחק בה בקטע של העיצוב")
    print("אין מה לשפר!!!!!!!!!!!!!!!!!!!! נהננו מאד!!!!!!!")

    file_path = "data/YafeNof.csv"
    excel_data = pd.read_csv(file_path)
    sales_data_obj = SalesData(excel_data)

# יצירת אובייקט מסוג FileOperation
    file_operator = FileOperation("ChatGPT")

    # קריאה לפונקציה greet
    file_operator.greet()

    # קריאה לפונקציה read_csv
    file_path = 'data.csv'
    data = file_operator.read_excel(file_path)

    if data is not None:
        # הצגת הנתונים שנקראו מהקובץ
        print(data.head())

        # קריאה לפונקציה save_to_csv
        new_data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
        file_name = 'new_data.csv'
        file_operator.save_to_csv(new_data, file_name)

# 5
EX5 = sales_data_obj.calculate_total_sales()
print("ex5-calculate_total_sales", "\n", EX5)
# 6
EX6 = sales_data_obj.calculate_total_sales_per_month()
print("EX6-calculate_total_sales_per_month", "\n", EX6)
# 7
EX7 = sales_data_obj._identify_best_selling_product()
print("EX7-_identify_best_selling_product", "\n", EX7)
# 8
EX8 = sales_data_obj._identify_month_with_highest_sales()
print("EX8-_identify_month_with_highest_sales", "\n", EX8)
# 9
EX9 = sales_data_obj.analyze_sales_data()
print("EX9-analyze_sales_data", "\n", EX9)
# 10
EX10 = sales_data_obj.add_additional_values(EX9)
print("EX10-add_additional_values", "\n", EX10)
# 11
EX11 = sales_data_obj.calculate_cumulative_sales()
print("EX11-calculate_cumulative_sales", "\n", EX11)
# 13
EX13 = sales_data_obj.bar_chart_category_sum()
print("EX13-bar_chart_category_sum", "\n", EX13)
# 14
EX14 = sales_data_obj.calculate_mean_quantity()
print("EX14-calculate_mean_quantity", "\n", EX14)
# 15
EX15 = sales_data_obj.filter_by_sellings_or_and()
print("EX15-filter_by_sellings_or_and", "\n", EX15)
# 16
EX16 = sales_data_obj.divide_by_2()
print("EX16-divide_by_2", "\n", EX16)
# 17
EX17 = sales_data_obj.calculate_stats(columns='Price, Quantity')
print("EX17-calculate_stats", "\n", EX17)
# -----------------------------------------------------------
print("plot_total_sales_scatter")
sales_data_obj.plot_total_sales_scatter()

print("plot_total_sales_per_month_histogram")
sales_data_obj.plot_total_sales_per_month_histogram()

print("filter_by_sellings_or_and__")
sales_data_obj.filter_by_sellings_or_and__()

print("plot_line_chart")
sales_data_obj.plot_line_chart(excel_data)

print("plot_total_sales_scatter_")
sales_data_obj.plot_total_sales_scatter()

print("calculate_total_sales_")
sales_data_obj.calculate_total_sales_()

print("plot_total_sales_pie_chart")
sales_data_obj.plot_total_sales_pie_chart()

print("plot_cumulative_sales_area")
sales_data_obj.plot_cumulative_sales_area()

print("calculate_total_sales_and_plot")
sales_data_obj.calculate_total_sales_and_plot()

print("plot_total_sales_catplot")
sales_data_obj.plot_total_sales_catplot()

print("plot_pairplot")
sales_data_obj.plot_pairplot()

print("plot_total_sales_scatter")
sales_data_obj.plot_total_sales_scatter()

print("plot_total_sales_bar")
sales_data_obj.plot_total_sales_bar()

# Task7 3
random_sales_data = sales_data_obj.generate_random_sales("ProductA")
print("Task7 3 generate_random_sales", random_sales_data)

# Task7 4
x = sales_data_obj.print_python_version()
print("Task7 4 print_python_version ", x)

# Task7 5
x = sales_data_obj.process_parameters(name='TAG_John', age=30, score=95.5, city='New York')
print("Task7 5 process_parameters", x)
# Task7 6
sales_data_obj.print_table_data("Data/YafeNof.csv")
# Task7 7
sales_data_obj.iterate_table(excel_data)

