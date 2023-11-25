# DigitalHumanitiesInfographic

# Word Frequency Pie Chart with Matplotlib

This Python script generates a pie chart illustrating the word frequency analysis of commentary from the Arsenal v Manchester City FA Community Shield 2023 match using Matplotlib's `pyplot`.

## Usage

### Installation

Ensure you have Python installed. If you haven't installed Matplotlib, run:

```bash
pip install matplotlib
```

### Code

```python
import matplotlib.pyplot as plt

# Define the colors for the pie chart slices
colors = ['#8ecae6', '#219ebc', '#023047', '#ffb703', '#fb8500']

# Define the words and their corresponding counts
words = ["he", "Arsenal", "City", "they", "there"]
counts = [141, 81, 80, 73, 67]

# Create the pie chart with shadows, gradients, and other settings
slices = plt.pie(counts, colors=colors, autopct="%1.1f%%", startangle=140, shadow=True, labeldistance=0.6)
plt.legend(slices[0], words, loc="best")
plt.title("Word Frequency Analysis of\n Arsenal v Manchester City FA Community Shield 2023 Commentary")
plt.axis("equal")

# Display and save the pie chart
plt.savefig("The Language of Victory: A Word Frequency Analysis of Arsenal's Triumph over Manchester City", dpi=500)
plt.show()
```

### Running the Script

1. **Run the Script:**
   - Execute the Python script in your Python environment.

2. **Adjust Parameters:**
   - Ensure the necessary data (words, counts, and colors) are correctly defined before generating the pie chart.

3. **Output:**
   - The script generates a pie chart displaying the word frequency analysis. The chart will be saved as a high-resolution image (`*.png`) titled:
   `"The Language of Victory: A Word Frequency Analysis of Arsenal's Triumph over Manchester City"`

### Customize

Feel free to customize the code and adjust the settings according to your preferences!

---

This README provides instructions on running the code, understanding its purpose, and customizing it for specific needs.
