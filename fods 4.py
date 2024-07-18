import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature (Celsius)': [10, 12, 15, 18, 22, 25, 27, 26, 24, 20, 15, 12],
    'Rainfall (mm)': [50, 40, 60, 30, 20, 10, 5, 5, 10, 20, 30, 40]
}

df = pd.DataFrame(data)
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Temperature (Celsius)'], marker='o', linestyle='-', color='b', label='Temperature (Celsius)')
plt.title('Monthly Temperature Variation')
plt.xlabel('Month')
plt.ylabel('Temperature (Celsius)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Rainfall (mm)'], marker='s', linestyle='--', color='g', label='Rainfall (mm)')
plt.title('Monthly Rainfall Variation')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(df['Temperature (Celsius)'], df['Rainfall (mm)'], color='r', marker='o', label='Monthly Data')
plt.title('Temperature vs Rainfall')
plt.xlabel('Temperature (Celsius)')
plt.ylabel('Rainfall (mm)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
