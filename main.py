import matplotlib.pyplot as plt

# Define the colors for the pie chart slices
colors = ['#8ecae6', '#219ebc', '#023047','#ffb703', '#fb8500']

# Define the words and their corresponding counts
words = ["he", "Arsenal", "City", "they", "there"]
counts = [141, 81, 80, 73, 67]

# Create the pie chart with shadows and gradients
slices = plt.pie(counts, colors=colors, autopct="%1.1f%%", startangle=140, shadow=True, labeldistance=0.6)

# Create a legend
plt.legend(slices[0], words, loc="best")

# Set the title of the pie chart
plt.title("Word Frequency Analysis of\n Arsenal v Manchester City FA Community Shield 2023 Commentary")

# Make sure the aspect ratio of the plot is equal
plt.axis("equal")

# Display the pie chart
plt.savefig("The Language of Victory: A Word Frequency Analysis of Arsenal's Triumph over Manchester City", dpi = 500)
plt.show()
