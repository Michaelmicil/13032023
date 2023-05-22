
import pandas as pd
import matplotlib.pyplot as plt


raw_data = pd.read_csv("CarPingtung.csv")
print(raw_data)
print(raw_data.info())

x_values = raw_data['District']
y_values = raw_data['Casualities']


plt.bar(x_values, y_values)
plt.xlabel('District')
plt.ylabel('Casualties')

plt.title('Number of Traffic Accidents in Pingtung')

plt.show()

