# Import modules
import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt

# Import dataset in a variable named healthcare
healthcare = pd.read_csv("healthcare.csv")

# Output the first five rows of the dataset
print(healthcare.head())

# Print the unique entries of healthcare's "DRG Definition" column
print(healthcare["DRG Definition"].unique())

# Get rows in healthcare dataset that are about chest pain. Save the result in a variable called chest_pain
chest_pain = healthcare[healthcare["DRG Definition"] == "313 - CHEST PAIN"]

# Get every chest pain diagnosis in Alabama and store the results in a variable called alabama_chest_pain
alabama_chest_pain = chest_pain[chest_pain["Provider State"] == "AL"]

# Find the values for the average cost, related to alabama_chest_pain. Store the result in a variable called costs
costs = alabama_chest_pain[" Average Covered Charges "].values

# Output costs
print(costs)

# Make a boxplot of costs
#plt.boxplot(costs)

# Show plot
#plt.show()

# Find the unique values of chest_pain and store the result in a variable named states
states = chest_pain["Provider State"].unique()

# An empty list called datasets
datasets = []
# Loop through states
for state in states:
  # Append the values of each state's average cost to datasets
  datasets.append(chest_pain[chest_pain["Provider State"] == state][" Average Covered Charges "].values)

# Create a large room for the plots
plt.figure(figsize=(20,6))

# Draw boxplots for datasets
plt.boxplot(datasets, labels = states)

# Show the plots
plt.show()

# Get rows in healthcare dataset that are about heart failure & shock w mcc. Save the result in a variable called heart_failure_shock
heart_failure_shock = healthcare[healthcare["DRG Definition"] == "291 - HEART FAILURE & SHOCK W MCC"]

# Get every heart failure & shock w mcc diagnosis in New York and store the results in a variable called new_york_heart_failure_shock
new_york_heart_failure_shock = heart_failure_shock[heart_failure_shock["Provider State"] == "NY"]

# Find the values for the Average Medicare Payments, related to new_york_heart_failure_shock. Store the result in a variable called payments_new_york
payments_new_york = new_york_heart_failure_shock["Average Medicare Payments"].values

# Find the unique values of heart_failure_shock and store the result in a variable named states1
states1 = heart_failure_shock["Provider State"].unique()

# An empty list called datasets1
datasets1 = []
# Loop through states1
for state in states1:
  # Append the values of each state's Average Medicare Payments to datasets1
  datasets1.append(heart_failure_shock[heart_failure_shock["Provider State"] == state]["Average Medicare Payments"].values)

# Create a large room for the plots
plt.figure(figsize=(20,6))

# Draw boxplots for datasets1
plt.boxplot(datasets1, labels = states)

# Show the plots
plt.show()