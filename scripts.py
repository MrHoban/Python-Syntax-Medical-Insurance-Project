import matplotlib.pyplot as plt
import numpy as np

# Define ranges for each factor to simulate its impact on insurance cost
ages = np.arange(20, 65, 5)  # Age from 20 to 60
bmi_values = np.arange(18, 36, 2)  # BMI from 18 to 35
children_count = np.arange(0, 5)  # 0 to 4 children

# Calculate insurance cost for different ages with fixed values for other factors
insurance_cost_age = 250 * ages - 128 * 1 + 370 * 26.2 + 425 * 2 + 24000 * 0 - 12500

# Calculate insurance cost for different BMI values with fixed values for other factors
insurance_cost_bmi = 250 * 35 - 128 * 1 + 370 * bmi_values + 425 * 2 + 24000 * 0 - 12500

# Plotting the results
plt.figure(figsize=(12, 6))

# Plot for age vs insurance cost
plt.subplot(1, 2, 1)
plt.plot(ages, insurance_cost_age, marker='o')
plt.title('Insurance Cost vs Age')
plt.xlabel('Age')
plt.ylabel('Estimated Insurance Cost ($)')
plt.grid(True)

# Plot for BMI vs insurance cost
plt.subplot(1, 2, 2)
plt.plot(bmi_values, insurance_cost_bmi, marker='o', color='orange')
plt.title('Insurance Cost vs BMI')
plt.xlabel('BMI')
plt.ylabel('Estimated Insurance Cost ($)')
plt.grid(True)

plt.tight_layout()
plt.show()
    
    # The script calculates the insurance cost for different ages and BMI values and plots the results using the  matplotlib  library. The  np.arange  function is used to create ranges for the factors, and the insurance cost is calculated based on the provided formula. The results are then plotted using two subplots to show the impact of age and BMI on insurance cost. 
    # Running the Script 
    #To run the script, you can use the following command: 
    # python scripts.py 
    # This will execute the script and display the plots showing the estimated insurance cost for different ages and BMI values. 
    # Conclusion 
    # In this tutorial, you learned how to simulate the impact of different factors on insurance costs using Python. You created a simple script that calculates insurance costs based on age and BMI values and plotted the results using the  matplotlib  library. You can further extend this script to include additional factors or more complex calculations to simulate the impact of various factors on insurance costs. 
    # If you're interested in learning more about data visualization in Python, check out our guide on  how to create a scatter plot in Python using matplotlib. 
    # About the author 
    # View full profile »
    # Hire the author ````