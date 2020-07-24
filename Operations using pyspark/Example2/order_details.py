from pyspark.sql import functions as F
from pyspark.sql.window import Window  
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
sc = SparkContext('local')
spark = SparkSession(sc)
#Original Data
df=spark.read.csv("input_order_details.csv", header=True, inferSchema=True)
df.show()

dataframe=df.groupby(['order']).agg({'ext price':'sum'})
dataframe=df.groupby(['order']).agg({'ext price':'sum'}).withColumnRenamed('sum(ext price)','order total')
dataframe.show()

#dataframe=df.join(dataframe,df['order']==dataframe['order'])
dataframe=df.join(dataframe,df['order']==dataframe['order']).drop(dataframe['order']).withColumnRenamed('Input','Output' )
dataframe.show()

dataframe=dataframe.withColumn('Percent_of_order',dataframe['ext price']/dataframe['order total'])
dataframe.show()

dataframe=dataframe.select('Output','account','name','order','sku','quantity','unit price','ext price',F.round(dataframe['order total'],2),F.round(dataframe['Percent_of_order'],6)).withColumnRenamed("round(order total, 2)","order total").withColumnRenamed("round(Percent_of_order, 6)","Percent_of_Order")
dataframe.show()