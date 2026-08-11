import pandas as pd

# -------------------------------
# Create the DataFrame
# -------------------------------

data = {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Hina', 'Bilal', 'Zara'],
    'City': ['Lahore', 'Karachi', 'Lahore', 'Islamabad', 'Karachi', 'Lahore'],
    'Sales': [4500, 7200, 3800, 9100, 2500, 7800],
    'Target': [5000, 6000, 5000, 8000, 4000, 6000]
}

df = pd.DataFrame(data)

# ============================================================
# 1. Understand the Problem
# ============================================================

# Q1:
# Management wants to know which employees achieved their sales target.
# We compare the Sales column with the Target column.
# If Sales >= Target, the employee achieved the target.

# Q2:
# Compare Sales with Target for all employees.
achieved_target = df['Sales'] >= df['Target']

# ============================================================
# 2. Create a Result Column
# ============================================================

# Q3:
# Create a new column named 'Achieved Target'.
df.insert(4, 'Achieved Target', achieved_target)

print("DataFrame with Achieved Target column:\n")
print(df)

# ============================================================
# 3. Filter the Successful Employees
# ============================================================

# Q4:
# Display only the employees who achieved their target.
print("\nEmployees who achieved their target:")
print(df.loc[achieved_target,
             ['Name', 'City', 'Sales', 'Target', 'Achieved Target']])

# Q5:
# Display employees who achieved the target without using
# the 'Achieved Target' column.
achieved_without_column = df['Sales'] >= df['Target']

print("\nEmployees who achieved the target (without using the Achieved Target column):")
print(df.loc[achieved_without_column, 'Name'])

# ============================================================
# 4. Measure Performance Against Target
# ============================================================

# Q6:
# Create a Difference column showing how much each employee
# exceeded or fell short of the target.
difference = df['Sales'] - df['Target']
df.insert(5, 'Difference', difference)

print("\nDifference between Sales and Target:")
print(df)

# Q7:
# What does a positive Difference mean?
# A positive Difference means the employee exceeded the target.
#
# What does a negative Difference mean?
# A negative Difference means the employee did not achieve the target.

# ============================================================
# 5. Find the Best Performance
# ============================================================

# Q8:
# Find the largest value in the Difference column.
largest_difference = df['Difference'].max()

print("\nLargest Difference:")
print(largest_difference)

# Expected Result:
# Largest Difference = 1800

# Q9:
# Display the complete row of the employee
# who has the largest Difference.
print("\nEmployee with the Best Performance:")

best_performance_index = df['Difference'].idxmax()
print(df.loc[best_performance_index])

# Q10:
# Is the employee with the highest Sales always the employee
# who performed best against the target?

'''
Answer:

No.

Hina has the highest Sales (9100), but Zara performed best
against the target because her Difference is 1800, which is
higher than Hina's Difference of 1100.

Therefore, the employee with the highest sales is not always
the employee who performed best against the target.
Performance is measured by how much an employee exceeds
or falls short of the target, not just by total sales.
'''

# ============================================================
# 6. Identify Employees Who Need Support
# ============================================================

# Q11:
# Management defines an employee as needing support if:
# Sales < Target AND Sales < 5000

employee_support = (
    (df['Sales'] < df['Target']) &
    (df['Sales'] < 5000)
)

print("\nEmployees who need support:")
print(df.loc[employee_support,
             ['Name', 'City', 'Sales', 'Target']])

# ============================================================
# 7. Final Challenge
# ============================================================

# Q12:
# Display only employees from Lahore who achieved their target.

lahore_achieved = (
    (df['City'] == 'Lahore') &
    (df['Sales'] >= df['Target'])
)

print("\nEmployees from Lahore who achieved their target:")
print(df.loc[lahore_achieved,
             ['Name', 'City', 'Sales', 'Target', 'Difference']])

# Q13:
# Explain how you broke the problem into smaller steps.

'''
Answer:

I first created the DataFrame, then compared Sales with Target
to identify employees who achieved their targets. Next, I created
the required columns, filtered the data based on different conditions,
calculated the Difference between Sales and Target, identified the
best-performing employee, and finally solved the remaining filtering
tasks step by step.
'''