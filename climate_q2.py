import matplotlib.pyplot as plt
import pandas as pd

years = []
co2 = []
temp = []

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

data = pd.read_csv('data.csv')

dates = data['Date']
values = data['Value']
plt.figure(figsize=(10, 6))
plt.plot(dates, values, marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Test Data from CSV File')
plt.grid(True)
plt.xticks(rotation=45)

plt.show()
