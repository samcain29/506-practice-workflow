import pandas as pandas
import numpy as numpy
number_var = 42
my_list = [1, 2, 3, 4, 5]
my_dict = {
    "key1": "value1",
    "key2": [10, 20 30],
    "key3": {"nested_key": "nested_value"}
}
def analyze_data(a, b):
    if a > b:
        return f"{a} is greater than {b}"
    else:
        return f"{b} is greater than or equal to {a}"
result = analyze_data(10, 5)
print("Data Analyst Result:", result)
print("Number Variable:", number_var)
print("List:", my_list)
print("Dictionary:", my_dict)
git add .
git commit -m "added Python code and updated README"
git push origin main
