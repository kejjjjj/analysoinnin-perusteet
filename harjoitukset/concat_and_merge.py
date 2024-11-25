import pandas as pd

# Create Orders DataFrame
portions_data1 = {'order_id': [2, 1, 3], 'item_name': ['Burger', 'Pizza', 'Salad'], 'quantity': [2, 1, 3]}
orders_df = pd.DataFrame(portions_data1)

# Create Portions Dataframe
portions_data2 = {'order_id': [4, 6, 5], 'item_name': ['Soup', 'Burger', 'Wok'], 'quantity': [1, 3, 4]}
portions_df = pd.DataFrame(portions_data2)

# Combine using concat
combined_df = pd.concat([orders_df, portions_df], ignore_index=True)
print(combined_df)

########################################################################################################################################
########################################################################################################################################
########################################################################################################################################

# Data Orders DataFrame
orders_data = {'order_id': [1, 2, 3], 'customer_name': ['Alice', 'Bob', 'Charlie'], 'total_amount': [25.5, 30.2, 15.75]}
orders_df = pd.DataFrame(orders_data)

# Create Portions DataFrame
portions_data = {'order_id': [2, 1, 3], 'item_name': ['Burger', 'Pizza', 'Salad'], 'quantity': [2, 1, 3]}
portions_df = pd.DataFrame(portions_data)

# Combine using merge
merged_df = pd.merge(orders_df, portions_df, on='order_id')
print(merged_df)