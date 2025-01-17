import pandas as pd
import matplotlib.pyplot as plt

# create a dataframe
data = {'fruit': ['apple', 'banana', 'cherry', 'date', 'elderberry'],
        'quantity': [30, 20, 15, 10, 5]}

df = pd.DataFrame(data)

# create a pie chart
fig, ax = plt.subplots(figsize=(10, 6))

# explode the largest slice
explode = (0.1, 0, 0, 0, 0)

# plot the pie chart
ax.pie(df['quantity'], labels=df['fruit'], autopct='%1.1f%%', startangle=90, explode=explode)

# add a title
ax.set_title('Fruit Quantity')

# Save the plot to a file instead of showing it
plt.savefig('fruit_quantity_pie_chart.png')