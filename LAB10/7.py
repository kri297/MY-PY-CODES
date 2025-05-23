import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.arange(1, 6)
y = np.array([10, 15, 7, 12, 5])
categories = ['A', 'B', 'C', 'D', 'E']

# Line Plot
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)
plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")

# Bar Chart
plt.subplot(2, 2, 2)
plt.bar(categories, y, color='skyblue')
plt.title("Bar Chart")

# Scatter Plot
plt.subplot(2, 2, 3)
plt.scatter(x, y, color='red')
plt.title("Scatter Plot")

# Pie Chart
plt.subplot(2, 2, 4)
plt.pie(y, labels=categories, autopct='%1.1f%%')
plt.title("Pie Chart")

plt.tight_layout()
plt.show()
