import plotext as plt

# Test with mixed positive and negative values
labels = ["A", "B", "C", "D", "E"]
values = [10, -15, 0, 20, -25]

plt.simple_bar(labels, values, width=80, title="Test Chart")
plt.show() 