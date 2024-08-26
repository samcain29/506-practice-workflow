# 506-practice-workflow
A primer for 504/507 Fall semester classes to practice a basic development workflow.
## Variables

- **Number Variable (`number_var`)**: 
  - Type: Integer
  - Description: This variable holds an integer value. For this example, it is assigned the value `42`.

- **String Variable (`string_var`)**: 
  - Type: String
  - Description: A simple string variable containing a greeting message. The value is `"Hello, world!"`.

- **List (`my_list`)**: 
  - Type: List
  - Description: A list of integers ranging from 1 to 5. This list is used to demonstrate list operations in Python.

- **Dictionary (`my_dict`)**: 
  - Type: Dictionary
  - Description: A dictionary with three key-value pairs:
    - `"key1"`: Contains a string value `"value1"`.
    - `"key2"`: Contains a list `[10, 20, 30]`.
    - `"key3"`: Contains a nested dictionary `{"nested_key": "nested_value"}`.
## Function: `analyze_data`

- **Purpose:** This function compares two input numbers and returns a message indicating which number is greater.

- **Inputs:**
  - `a`: The first number (e.g., `10`).
  - `b`: The second number (e.g., `5`).

- **Logic:**
  - The function uses an `if/else` statement to compare the two numbers:
    - If `a` is greater than `b`, the function returns a string stating `"a is greater than b"`.
    - Otherwise, it returns `"b is greater than or equal to a"`.

- **Example Output:**
  - For inputs `10` and `5`, the function will output `"10 is greater than 5"`.
cd path/506-practice-workflow
git add .
git add intro_practice.py README.md
