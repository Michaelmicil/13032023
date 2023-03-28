import pandas as pd

# 1.Input
raw_data = pd.read_csv("AssignmentMenu1.csv")
print(raw_data)

# 2. Process
sorted_data = raw_data.sort_values("Menu",ascending=True)
total = len(raw_data)

# 3. Output
print(f'Sorted:{sorted_data}')
print(f"Total:{total}")
