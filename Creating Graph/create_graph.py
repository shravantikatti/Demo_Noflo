import matplotlib.pyplot as plt
import pandas as pd
import sys
import io
from csv import reader
data_string = sys.argv[1]
data = io.StringIO(data_string)
df = pd.read_csv(data, sep =",") 

fig = plt.figure()

# Divide the figure into a 1x2 grid, and give me the first section
ax1 = fig.add_subplot(121)

# Divide the figure into a 1x2 grid, and give me the second section
ax2 = fig.add_subplot(122)


df.plot(kind='scatter',x='age',y='bmi',color='red',ax=ax1)
df['sex'].value_counts().plot(y='age',kind='bar',ax=ax2);
plt.show()

