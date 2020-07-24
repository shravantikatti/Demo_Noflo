from pyspark.sql import functions as F
from pyspark.sql.window import Window  
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import date_format
from pyspark.sql.functions import unix_timestamp
from pyspark.sql.functions import row_number
from pyspark.sql.functions import monotonically_increasing_id
import pandas as pandas

sc = SparkContext('local')
spark = SparkSession(sc)

#Original Data
df=spark.read.csv("data.csv", header=True, inferSchema=True)
df.show()

#Changing Date format and Renaming a column
df=df.select('Input Data',date_format(unix_timestamp("Date", "yyyy-MM-dd").cast("timestamp"),"dd-MM-yyyy")
	.alias('Date'),'Type','Value').withColumnRenamed('Input Data','Output Data')
df.show()

#Displaying selected columns
df1=df.select('Output Data','Date','Type')
df1.show()

#Displaying selected columns
df2=df.select('Output Data','Date','Value')
df2.show()

#Inserting a new column with the string value 'Type' in df1
df1=df1.withColumn('Variable', F.lit('Type'))
df1.show()

#Inserting a new column with the string value 'Type' in df2
df2=df2.withColumn('Variable', F.lit('Value'))
#df2.show()

#Merging df1 with df2 with the column renamed 
df3=df1.unionAll(df2)
df3=df3.select('Output Data','Date','Variable','Type').withColumnRenamed('Type','Observations')
df3.show()

#Generate row number
df3 = df3.withColumn("OutPut Data", row_number().over(Window.orderBy(monotonically_increasing_id()))-1)
df3.show()



 
