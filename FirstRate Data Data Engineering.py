# Databricks notebook source
import os
import numpy as np
import pandas as pd

from pyspark import SparkFiles
from pyspark import SparkContext
from pyspark.sql import functions
import pyspark.sql.functions #import avg, col, udf
from pyspark.sql import SQLContext
from pyspark.sql import DataFrame
from pyspark.sql.types import *
import json

#LIST, RENAME, AND SAVE ALL FILES AS DELTA LAKE AUTOMATICALLY
path = '/dbfs/FileStore/tables/FirstRate30mins'
filename_lists = os.listdir(path)

df_30mins_ = {}
_delta ={}

for filename in os.listdir(path):
    #split file name
    name = filename.split('_')[0]
    #create clolumn header names
    temp = StructType([StructField(name+"_date/time", StringType(), True),StructField(name+"_adjOpen", FloatType(), True),StructField(name+"_adjHigh", FloatType(), True),StructField(name+"_adjLow", FloatType(), True),StructField(name+"_adjClose", FloatType(), True),StructField(name+"_adjVolume", IntegerType(), True)])
    
    #list and create csv dataframes
    temp_df = spark.read.format("csv").option("header", "false").schema(temp).load("/FileStore/tables/FirstRate30mins/"+filename)
    
    #name each dataframes
    df_30mins_[name] = temp_df
    
    #name each table
    table_name = name+'_30mins_delta'

# COMMAND ----------

#create delta lake for each dataframes
df_30mins_[name].write.format("delta").mode("overwrite").saveAsTable(table_name)

# COMMAND ----------

display(df_30mins_['AAL'])
display(df_30mins_['AAPL'])
display(df_30mins_['AA'])
display(df_30mins_['A'])

display(spark.sql('SELECT * FROM aal_30mins_delta'))
display(spark.sql('SELECT * FROM aa_30mins_delta'))
display(spark.sql('SELECT * FROM aapl_30mins_delta'))
display(spark.sql('SELECT * FROM a_30mins_delta'))