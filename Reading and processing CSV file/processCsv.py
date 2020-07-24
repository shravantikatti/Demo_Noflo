import pandas as pd 
import sys
import io
from csv import reader
data_string = sys.argv[1]
data = io.StringIO(data_string)

df = pd.read_csv(data, sep =",") 

print("COLUMNS:")
for col in df.columns: 
    print(col) 

df.loc[20] = [21,'North View', 26000, 75]
print(df)

print("\n")
newdf=df.drop([20])
print(newdf)
#print("\nHEAD 10 \n",df.head(10)) 

#print("\nBELOW 7 data\n ", df.tail(7))

#print("\nSORTED DATA\n",df.sort_values(by=['HARDSHIP_INDEX']))


#df.loc['k'] = ['Smriti', 26, 'Bangalore', 'India']

#df.to_csv('output.csv')
