import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('age.csv')
ids = data['Responder_id']
ages = data['Age']

bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

plt.hist(ages, bins=bins, edgecolor='black', log=True)

median_age = 29
color = '#30fc55'

plt.axvline(median_age, color=color, label='Median Age', linewidth=2)

plt.legend()

plt.title('Ages of app users')
plt.xlabel('Ages')
plt.ylabel('Total users')

plt.tight_layout()

plt.show()