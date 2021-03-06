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

AAL_30min_spark_DF_newRow = StructType([StructField("AAL_date/time", StringType(), True),StructField("AAL_adjOpen", FloatType(), True),StructField("AAL_adjHigh", FloatType(), True),StructField("AAL_adjLow", FloatType(), True),StructField("AAL_adjClose", FloatType(), True),StructField("AAL_adjVolume", IntegerType(), True)])
AAL_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AAL_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AAL_30min.txt")
display(AAL_30min_spark_DF)

AAPL_30min_spark_DF_newRow = StructType([StructField("AAPL_date/time", StringType(), True),StructField("AAPL_adjOpen", FloatType(), True),StructField("AAPL_adjHigh", FloatType(), True),StructField("AAPL_adjLow", FloatType(), True),StructField("AAPL_adjClose", FloatType(), True),StructField("AAPL_adjVolume", IntegerType(), True)])
AAPL_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AAPL_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AAPL_30min.txt")
display(AAPL_30min_spark_DF)

AAP_30min_spark_DF_newRow = StructType([StructField("AAP_date/time", StringType(), True),StructField("AAP_adjOpen", FloatType(), True),StructField("AAP_adjHigh", FloatType(), True),StructField("AAP_adjLow", FloatType(), True),StructField("AAP_adjClose", FloatType(), True),StructField("AAP_adjVolume", IntegerType(), True)])
AAP_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AAP_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AAP_30min.txt")
display(AAP_30min_spark_DF)

AA_30min_spark_DF_newRow = StructType([StructField("AA_date/time", StringType(), True),StructField("AA_adjOpen", FloatType(), True),StructField("AA_adjHigh", FloatType(), True),StructField("AA_adjLow", FloatType(), True),StructField("AA_adjClose", FloatType(), True),StructField("AA_adjVolume", IntegerType(), True)])
AA_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AA_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AA_30min.txt")
display(AA_30min_spark_DF)

ABBV_30min_spark_DF_newRow = StructType([StructField("ABBV_date/time", StringType(), True),StructField("ABBV_adjOpen", FloatType(), True),StructField("ABBV_adjHigh", FloatType(), True),StructField("ABBV_adjLow", FloatType(), True),StructField("ABBV_adjClose", FloatType(), True),StructField("ABBV_adjVolume", IntegerType(), True)])
ABBV_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ABBV_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ABBV_30min.txt")
display(ABBV_30min_spark_DF)

ABC_30min_spark_DF_newRow = StructType([StructField("ABC_date/time", StringType(), True),StructField("ABC_adjOpen", FloatType(), True),StructField("ABC_adjHigh", FloatType(), True),StructField("ABC_adjLow", FloatType(), True),StructField("ABC_adjClose", FloatType(), True),StructField("ABC_adjVolume", IntegerType(), True)])
ABC_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ABC_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ABC_30min.txt")
display(ABC_30min_spark_DF)

ABMD_30min_spark_DF_newRow = StructType([StructField("ABMD_date/time", StringType(), True),StructField("ABMD_adjOpen", FloatType(), True),StructField("ABMD_adjHigh", FloatType(), True),StructField("ABMD_adjLow", FloatType(), True),StructField("ABMD_adjClose", FloatType(), True),StructField("ABMD_adjVolume", IntegerType(), True)])
ABMD_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ABMD_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ABMD_30min.txt")
display(ABMD_30min_spark_DF)

ABMD_30min_spark_DF_newRow = StructType([StructField("ABMD_date/time", StringType(), True),StructField("ABMD_adjOpen", FloatType(), True),StructField("ABMD_adjHigh", FloatType(), True),StructField("ABMD_adjLow", FloatType(), True),StructField("ABMD_adjClose", FloatType(), True),StructField("ABMD_adjVolume", IntegerType(), True)])
ABMD_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ABMD_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ABMD_30min.txt")
display(ABMD_30min_spark_DF)

ABT_30min_spark_DF_newRow = StructType([StructField("ABT_date/time", StringType(), True),StructField("ABT_adjOpen", FloatType(), True),StructField("ABT_adjHigh", FloatType(), True),StructField("ABT_adjLow", FloatType(), True),StructField("ABT_adjClose", FloatType(), True),StructField("ABT_adjVolume", IntegerType(), True)])
ABT_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ABT_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ABT_30min.txt")
display(ABT_30min_spark_DF)

ACN_30min_spark_DF_newRow = StructType([StructField("ACN_date/time", StringType(), True),StructField("ACN_adjOpen", FloatType(), True),StructField("ACN_adjHigh", FloatType(), True),StructField("ACN_adjLow", FloatType(), True),StructField("ACN_adjClose", FloatType(), True),StructField("ACN_adjVolume", IntegerType(), True)])
ACN_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ACN_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ACN_30min.txt")
display(ACN_30min_spark_DF)

ACV_30min_spark_DF_newRow = StructType([StructField("ACV_date/time", StringType(), True),StructField("ACV_adjOpen", FloatType(), True),StructField("ACV_adjHigh", FloatType(), True),StructField("ACV_adjLow", FloatType(), True),StructField("ACV_adjClose", FloatType(), True),StructField("ACV_adjVolume", IntegerType(), True)])
ACV_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ACV_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ACV_30min.txt")
display(ACV_30min_spark_DF)

ADBE_30min_spark_DF_newRow = StructType([StructField("ADBE_date/time", StringType(), True),StructField("ADBE_adjOpen", FloatType(), True),StructField("ADBE_adjHigh", FloatType(), True),StructField("ADBE_adjLow", FloatType(), True),StructField("ADBE_adjClose", FloatType(), True),StructField("ADBE_adjVolume", IntegerType(), True)])
ADBE_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ADBE_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ADBE_30min.txt")
display(ADBE_30min_spark_DF)

ADI_30min_spark_DF_newRow = StructType([StructField("ADI_date/time", StringType(), True),StructField("ADI_adjOpen", FloatType(), True),StructField("ADI_adjHigh", FloatType(), True),StructField("ADI_adjLow", FloatType(), True),StructField("ADI_adjClose", FloatType(), True),StructField("ADI_adjVolume", IntegerType(), True)])
ADI_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ADI_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ADI_30min.txt")
display(ADI_30min_spark_DF)

ADM_30min_spark_DF_newRow = StructType([StructField("ADM_date/time", StringType(), True),StructField("ADM_adjOpen", FloatType(), True),StructField("ADM_adjHigh", FloatType(), True),StructField("ADM_adjLow", FloatType(), True),StructField("ADM_adjClose", FloatType(), True),StructField("ADM_adjVolume", IntegerType(), True)])
ADM_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ADM_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ADM_30min.txt")
display(ADM_30min_spark_DF)

ADP_30min_spark_DF_newRow = StructType([StructField("ADP_date/time", StringType(), True),StructField("ADP_adjOpen", FloatType(), True),StructField("ADP_adjHigh", FloatType(), True),StructField("ADP_adjLow", FloatType(), True),StructField("ADP_adjClose", FloatType(), True),StructField("ADP_adjVolume", IntegerType(), True)])
ADP_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ADP_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ADP_30min.txt")
display(ADP_30min_spark_DF)

ADSK_30min_spark_DF_newRow = StructType([StructField("ADSK_date/time", StringType(), True),StructField("ADSK_adjOpen", FloatType(), True),StructField("ADSK_adjHigh", FloatType(), True),StructField("ADSK_adjLow", FloatType(), True),StructField("ADSK_adjClose", FloatType(), True),StructField("ADSK_adjVolume", IntegerType(), True)])
ADSK_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ADSK_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ADSK_30min.txt")
display(ADSK_30min_spark_DF)

ADS_30min_spark_DF_newRow = StructType([StructField("ADS_date/time", StringType(), True),StructField("ADS_adjOpen", FloatType(), True),StructField("ADS_adjHigh", FloatType(), True),StructField("ADS_adjLow", FloatType(), True),StructField("ADS_adjClose", FloatType(), True),StructField("ADS_adjVolume", IntegerType(), True)])
ADS_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ADS_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ADS_30min.txt")
display(ADS_30min_spark_DF)

ADT_30min_spark_DF_newRow = StructType([StructField("ADT_date/time", StringType(), True),StructField("ADT_adjOpen", FloatType(), True),StructField("ADT_adjHigh", FloatType(), True),StructField("ADT_adjLow", FloatType(), True),StructField("ADT_adjClose", FloatType(), True),StructField("ADT_adjVolume", IntegerType(), True)])
ADT_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ADT_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ADT_30min.txt")
display(ADT_30min_spark_DF)

AEE_30min_spark_DF_newRow = StructType([StructField("AEE_date/time", StringType(), True),StructField("AEE_adjOpen", FloatType(), True),StructField("AEE_adjHigh", FloatType(), True),StructField("AEE_adjLow", FloatType(), True),StructField("AEE_adjClose", FloatType(), True),StructField("AEE_adjVolume", IntegerType(), True)])
AEE_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AEE_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AEE_30min.txt")
display(AEE_30min_spark_DF)

AEP_30min_spark_DF_newRow = StructType([StructField("AEP_date/time", StringType(), True),StructField("AEP_adjOpen", FloatType(), True),StructField("AEP_adjHigh", FloatType(), True),StructField("AEP_adjLow", FloatType(), True),StructField("AEP_adjClose", FloatType(), True),StructField("AEP_adjVolume", IntegerType(), True)])
AEP_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AEP_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AEP_30min.txt")
display(AEP_30min_spark_DF)

AES_30min_spark_DF_newRow = StructType([StructField("AES_date/time", StringType(), True),StructField("AES_adjOpen", FloatType(), True),StructField("AES_adjHigh", FloatType(), True),StructField("AES_adjLow", FloatType(), True),StructField("AES_adjClose", FloatType(), True),StructField("AES_adjVolume", IntegerType(), True)])
AES_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AES_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AES_30min.txt")
display(AES_30min_spark_DF)

AFL_30min_spark_DF_newRow = StructType([StructField("AFL_date/time", StringType(), True),StructField("AFL_adjOpen", FloatType(), True),StructField("AFL_adjHigh", FloatType(), True),StructField("AFL_adjLow", FloatType(), True),StructField("AFL_adjClose", FloatType(), True),StructField("AFL_adjVolume", IntegerType(), True)])
AFL_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AFL_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AFL_30min.txt")
display(AFL_30min_spark_DF)

AIG_30min_spark_DF_newRow = StructType([StructField("AIG_date/time", StringType(), True),StructField("AIG_adjOpen", FloatType(), True),StructField("AIG_adjHigh", FloatType(), True),StructField("AIG_adjLow", FloatType(), True),StructField("AIG_adjClose", FloatType(), True),StructField("AIG_adjVolume", IntegerType(), True)])
AIG_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AIG_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AIG_30min.txt")
display(AIG_30min_spark_DF)

AINV_30min_spark_DF_newRow = StructType([StructField("AINV_date/time", StringType(), True),StructField("AINV_adjOpen", FloatType(), True),StructField("AINV_adjHigh", FloatType(), True),StructField("AINV_adjLow", FloatType(), True),StructField("AINV_adjClose", FloatType(), True),StructField("AINV_adjVolume", IntegerType(), True)])
AINV_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AINV_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AINV_30min.txt")
display(AINV_30min_spark_DF)

AIV_30min_spark_DF_newRow = StructType([StructField("AIV_date/time", StringType(), True),StructField("AIV_adjOpen", FloatType(), True),StructField("AIV_adjHigh", FloatType(), True),StructField("AIV_adjLow", FloatType(), True),StructField("AIV_adjClose", FloatType(), True),StructField("AIV_adjVolume", IntegerType(), True)])
AIV_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AIV_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AIV_30min.txt")
display(AIV_30min_spark_DF)

AIZ_30min_spark_DF_newRow = StructType([StructField("AIZ_date/time", StringType(), True),StructField("AIZ_adjOpen", FloatType(), True),StructField("AIZ_adjHigh", FloatType(), True),StructField("AIZ_adjLow", FloatType(), True),StructField("AIZ_adjClose", FloatType(), True),StructField("AIZ_adjVolume", IntegerType(), True)])
AIZ_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AIZ_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AIZ_30min.txt")
display(AIZ_30min_spark_DF)

AJG_30min_spark_DF_newRow = StructType([StructField("AJG_date/time", StringType(), True),StructField("AJG_adjOpen", FloatType(), True),StructField("AJG_adjHigh", FloatType(), True),StructField("AJG_adjLow", FloatType(), True),StructField("AJG_adjClose", FloatType(), True),StructField("AJG_adjVolume", IntegerType(), True)])
AJG_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AJG_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AJG_30min.txt")
display(AJG_30min_spark_DF)

AKAM_30min_spark_DF_newRow = StructType([StructField("AKAM_date/time", StringType(), True),StructField("AKAM_adjOpen", FloatType(), True),StructField("AKAM_adjHigh", FloatType(), True),StructField("AKAM_adjLow", FloatType(), True),StructField("AKAM_adjClose", FloatType(), True),StructField("AKAM_adjVolume", IntegerType(), True)])
AKAM_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AKAM_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AKAM_30min.txt")
display(AKAM_30min_spark_DF)

ALB_30min_spark_DF_newRow = StructType([StructField("ALB_date/time", StringType(), True),StructField("ALB_adjOpen", FloatType(), True),StructField("ALB_adjHigh", FloatType(), True),StructField("ALB_adjLow", FloatType(), True),StructField("ALB_adjClose", FloatType(), True),StructField("ALB_adjVolume", IntegerType(), True)])
ALB_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ALB_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ALB_30min.txt")
display(ALB_30min_spark_DF)

ALGN_30min_spark_DF_newRow = StructType([StructField("ALGN_date/time", StringType(), True),StructField("ALGN_adjOpen", FloatType(), True),StructField("ALGN_adjHigh", FloatType(), True),StructField("ALGN_adjLow", FloatType(), True),StructField("ALGN_adjClose", FloatType(), True),StructField("ALGN_adjVolume", IntegerType(), True)])
ALGN_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ALGN_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ALGN_30min.txt")
display(ALGN_30min_spark_DF)

ALK_30min_spark_DF_newRow = StructType([StructField("ALK_date/time", StringType(), True),StructField("ALK_adjOpen", FloatType(), True),StructField("ALK_adjHigh", FloatType(), True),StructField("ALK_adjLow", FloatType(), True),StructField("ALK_adjClose", FloatType(), True),StructField("ALK_adjVolume", IntegerType(), True)])
ALK_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ALK_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ALK_30min.txt")
display(ALK_30min_spark_DF)

ALLE_30min_spark_DF_newRow = StructType([StructField("ALLE_date/time", StringType(), True),StructField("ALLE_adjOpen", FloatType(), True),StructField("ALLE_adjHigh", FloatType(), True),StructField("ALLE_adjLow", FloatType(), True),StructField("ALLE_adjClose", FloatType(), True),StructField("ALLE_adjVolume", IntegerType(), True)])
ALLE_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ALLE_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ALLE_30min.txt")
display(ALLE_30min_spark_DF)

ALL_30min_spark_DF_newRow = StructType([StructField("ALL_date/time", StringType(), True),StructField("ALL_adjOpen", FloatType(), True),StructField("ALL_adjHigh", FloatType(), True),StructField("ALL_adjLow", FloatType(), True),StructField("ALL_adjClose", FloatType(), True),StructField("ALL_adjVolume", IntegerType(), True)])
ALL_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ALL_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ALL_30min.txt")
display(ALL_30min_spark_DF)

ALTR_30min_spark_DF_newRow = StructType([StructField("ALTR_date/time", StringType(), True),StructField("ALTR_adjOpen", FloatType(), True),StructField("ALTR_adjHigh", FloatType(), True),StructField("ALTR_adjLow", FloatType(), True),StructField("ALTR_adjClose", FloatType(), True),StructField("ALTR_adjVolume", IntegerType(), True)])
ALTR_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ALTR_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ALTR_30min.txt")
display(ALTR_30min_spark_DF)

AMAT_30min_spark_DF_newRow = StructType([StructField("AMAT_date/time", StringType(), True),StructField("AMAT_adjOpen", FloatType(), True),StructField("AMAT_adjHigh", FloatType(), True),StructField("AMAT_adjLow", FloatType(), True),StructField("AMAT_adjClose", FloatType(), True),StructField("AMAT_adjVolume", IntegerType(), True)])
AMAT_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AMAT_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AMAT_30min.txt")
display(AMAT_30min_spark_DF)

AMBC_30min_spark_DF_newRow = StructType([StructField("AMBC_date/time", StringType(), True),StructField("AMBC_adjOpen", FloatType(), True),StructField("AMBC_adjHigh", FloatType(), True),StructField("AMBC_adjLow", FloatType(), True),StructField("AMBC_adjClose", FloatType(), True),StructField("AMBC_adjVolume", IntegerType(), True)])
AMBC_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AMBC_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AMBC_30min.txt")
display(AMBC_30min_spark_DF)

AMCR_30min_spark_DF_newRow = StructType([StructField("AMCR_date/time", StringType(), True),StructField("AMCR_adjOpen", FloatType(), True),StructField("AMCR_adjHigh", FloatType(), True),StructField("AMCR_adjLow", FloatType(), True),StructField("AMCR_adjClose", FloatType(), True),StructField("AMCR_adjVolume", IntegerType(), True)])
AMCR_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AMCR_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AMCR_30min.txt")
display(AMCR_30min_spark_DF)

AMD_30min_spark_DF_newRow = StructType([StructField("AMD_date/time", StringType(), True),StructField("AMD_adjOpen", FloatType(), True),StructField("AMD_adjHigh", FloatType(), True),StructField("AMD_adjLow", FloatType(), True),StructField("AMD_adjClose", FloatType(), True),StructField("AMD_adjVolume", IntegerType(), True)])
AMD_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AMD_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AMD_30min.txt")
display(AMD_30min_spark_DF)

AME_30min_spark_DF_newRow = StructType([StructField("AME_date/time", StringType(), True),StructField("AME_adjOpen", FloatType(), True),StructField("AME_adjHigh", FloatType(), True),StructField("AME_adjLow", FloatType(), True),StructField("AME_adjClose", FloatType(), True),StructField("AME_adjVolume", IntegerType(), True)])
AME_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AME_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AME_30min.txt")
display(AME_30min_spark_DF)

AMGN_30min_spark_DF_newRow = StructType([StructField("AMGN_date/time", StringType(), True),StructField("AMGN_adjOpen", FloatType(), True),StructField("AMGN_adjHigh", FloatType(), True),StructField("AMGN_adjLow", FloatType(), True),StructField("AMGN_adjClose", FloatType(), True),StructField("AMGN_adjVolume", IntegerType(), True)])
AMGN_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AMGN_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AMGN_30min.txt")
display(AMGN_30min_spark_DF)

AMG_30min_spark_DF_newRow = StructType([StructField("AMG_date/time", StringType(), True),StructField("AMG_adjOpen", FloatType(), True),StructField("AMG_adjHigh", FloatType(), True),StructField("AMG_adjLow", FloatType(), True),StructField("AMG_adjClose", FloatType(), True),StructField("AMG_adjVolume", IntegerType(), True)])
AMG_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AMG_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AMG_30min.txt")
display(AMG_30min_spark_DF)

AMP_30min_spark_DF_newRow = StructType([StructField("AMP_date/time", StringType(), True),StructField("AMP_adjOpen", FloatType(), True),StructField("AMP_adjHigh", FloatType(), True),StructField("AMP_adjLow", FloatType(), True),StructField("AMP_adjClose", FloatType(), True),StructField("AMP_adjVolume", IntegerType(), True)])
AMP_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AMP_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AMP_30min.txt")
display(AMP_30min_spark_DF)

AMT_30min_spark_DF_newRow = StructType([StructField("AMT_date/time", StringType(), True),StructField("AMT_adjOpen", FloatType(), True),StructField("AMT_adjHigh", FloatType(), True),StructField("AMT_adjLow", FloatType(), True),StructField("AMT_adjClose", FloatType(), True),StructField("AMT_adjVolume", IntegerType(), True)])
AMT_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AMT_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AMT_30min.txt")
display(AMT_30min_spark_DF)

AMZN_30min_spark_DF_newRow = StructType([StructField("AMZN_date/time", StringType(), True),StructField("AMZN_adjOpen", FloatType(), True),StructField("AMZN_adjHigh", FloatType(), True),StructField("AMZN_adjLow", FloatType(), True),StructField("AMZN_adjClose", FloatType(), True),StructField("AMZN_adjVolume", IntegerType(), True)])
AMZN_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AMZN_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AMZN_30min.txt")
display(AMZN_30min_spark_DF)

ANET_30min_spark_DF_newRow = StructType([StructField("ANET_date/time", StringType(), True),StructField("ANET_adjOpen", FloatType(), True),StructField("ANET_adjHigh", FloatType(), True),StructField("ANET_adjLow", FloatType(), True),StructField("ANET_adjClose", FloatType(), True),StructField("ANET_adjVolume", IntegerType(), True)])
ANET_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ANET_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ANET_30min.txt")
display(ANET_30min_spark_DF)

ANF_30min_spark_DF_newRow = StructType([StructField("ANF_date/time", StringType(), True),StructField("ANF_adjOpen", FloatType(), True),StructField("ANF_adjHigh", FloatType(), True),StructField("ANF_adjLow", FloatType(), True),StructField("ANF_adjClose", FloatType(), True),StructField("ANF_adjVolume", IntegerType(), True)])
ANF_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ANF_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ANF_30min.txt")
display(ANF_30min_spark_DF)

ANSS_30min_spark_DF_newRow = StructType([StructField("ANSS_date/time", StringType(), True),StructField("ANSS_adjOpen", FloatType(), True),StructField("ANSS_adjHigh", FloatType(), True),StructField("ANSS_adjLow", FloatType(), True),StructField("ANSS_adjClose", FloatType(), True),StructField("ANSS_adjVolume", IntegerType(), True)])
ANSS_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ANSS_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ANSS_30min.txt")
display(ANSS_30min_spark_DF)

ANTM_30min_spark_DF_newRow = StructType([StructField("ANTM_date/time", StringType(), True),StructField("ANTM_adjOpen", FloatType(), True),StructField("ANTM_adjHigh", FloatType(), True),StructField("ANTM_adjLow", FloatType(), True),StructField("ANTM_adjClose", FloatType(), True),StructField("ANTM_adjVolume", IntegerType(), True)])
ANTM_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ANTM_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ANTM_30min.txt")
display(ANTM_30min_spark_DF)

AN_30min_spark_DF_newRow = StructType([StructField("AN_date/time", StringType(), True),StructField("AN_adjOpen", FloatType(), True),StructField("AN_adjHigh", FloatType(), True),StructField("AN_adjLow", FloatType(), True),StructField("AN_adjClose", FloatType(), True),StructField("AN_adjVolume", IntegerType(), True)])
AN_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AN_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AN_30min.txt")
display(AN_30min_spark_DF)

AON_30min_spark_DF_newRow = StructType([StructField("AON_date/time", StringType(), True),StructField("AON_adjOpen", FloatType(), True),StructField("AON_adjHigh", FloatType(), True),StructField("AON_adjLow", FloatType(), True),StructField("AON_adjClose", FloatType(), True),StructField("AON_adjVolume", IntegerType(), True)])
AON_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AON_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AON_30min.txt")
display(AON_30min_spark_DF)

AOS_30min_spark_DF_newRow = StructType([StructField("AOS_date/time", StringType(), True),StructField("AOS_adjOpen", FloatType(), True),StructField("AOS_adjHigh", FloatType(), True),StructField("AOS_adjLow", FloatType(), True),StructField("AOS_adjClose", FloatType(), True),StructField("AOS_adjVolume", IntegerType(), True)])
AOS_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AOS_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AOS_30min.txt")
display(AOS_30min_spark_DF)

APA_30min_spark_DF_newRow = StructType([StructField("APA_date/time", StringType(), True),StructField("APA_adjOpen", FloatType(), True),StructField("APA_adjHigh", FloatType(), True),StructField("APA_adjLow", FloatType(), True),StructField("APA_adjClose", FloatType(), True),StructField("APA_adjVolume", IntegerType(), True)])
APA_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(APA_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/APA_30min.txt")
display(APA_30min_spark_DF)

APD_30min_spark_DF_newRow = StructType([StructField("APD_date/time", StringType(), True),StructField("APD_adjOpen", FloatType(), True),StructField("APD_adjHigh", FloatType(), True),StructField("APD_adjLow", FloatType(), True),StructField("APD_adjClose", FloatType(), True),StructField("APD_adjVolume", IntegerType(), True)])
APD_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(APA_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/APD_30min.txt")
display(APD_30min_spark_DF)

APH_30min_spark_DF_newRow = StructType([StructField("APH_date/time", StringType(), True),StructField("APH_adjOpen", FloatType(), True),StructField("APH_adjHigh", FloatType(), True),StructField("APH_adjLow", FloatType(), True),StructField("APH_adjClose", FloatType(), True),StructField("APH_adjVolume", IntegerType(), True)])
APH_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(APH_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/APH_30min.txt")
display(APH_30min_spark_DF)

APTV_30min_spark_DF_newRow = StructType([StructField("APTV_date/time", StringType(), True),StructField("APTV_adjOpen", FloatType(), True),StructField("APTV_adjHigh", FloatType(), True),StructField("APTV_adjLow", FloatType(), True),StructField("APTV_adjClose", FloatType(), True),StructField("APTV_adjVolume", IntegerType(), True)])
APTV_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(APTV_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/APTV_30min.txt")
display(APTV_30min_spark_DF)

APTV_30min_spark_DF_newRow = StructType([StructField("APTV_date/time", StringType(), True),StructField("APTV_adjOpen", FloatType(), True),StructField("APTV_adjHigh", FloatType(), True),StructField("APTV_adjLow", FloatType(), True),StructField("APTV_adjClose", FloatType(), True),StructField("APTV_adjVolume", IntegerType(), True)])
APTV_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(APTV_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/APTV_30min.txt")
display(APTV_30min_spark_DF)

ARNC_30min_spark_DF_newRow = StructType([StructField("ARNC_date/time", StringType(), True),StructField("ARNC_adjOpen", FloatType(), True),StructField("ARNC_adjHigh", FloatType(), True),StructField("ARNC_adjLow", FloatType(), True),StructField("ARNC_adjClose", FloatType(), True),StructField("ARNC_adjVolume", IntegerType(), True)])
ARNC_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ARNC_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ARNC_30min.txt")
display(ARNC_30min_spark_DF)

ASH_30min_spark_DF_newRow = StructType([StructField("ASH_date/time", StringType(), True),StructField("ASH_adjOpen", FloatType(), True),StructField("ASH_adjHigh", FloatType(), True),StructField("ASH_adjLow", FloatType(), True),StructField("ASH_adjClose", FloatType(), True),StructField("ASH_adjVolume", IntegerType(), True)])
ASH_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ASH_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ASH_30min.txt")
display(ASH_30min_spark_DF)

ASO_30min_spark_DF_newRow = StructType([StructField("ASO_date/time", StringType(), True),StructField("ASO_adjOpen", FloatType(), True),StructField("ASO_adjHigh", FloatType(), True),StructField("ASO_adjLow", FloatType(), True),StructField("ASO_adjClose", FloatType(), True),StructField("ASO_adjVolume", IntegerType(), True)])
ASO_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ASO_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ASO_30min.txt")
display(ASO_30min_spark_DF)

ATGE_30min_spark_DF_newRow = StructType([StructField("ATGE_date/time", StringType(), True),StructField("ATGE_adjOpen", FloatType(), True),StructField("ATGE_adjHigh", FloatType(), True),StructField("ATGE_adjLow", FloatType(), True),StructField("ATGE_adjClose", FloatType(), True),StructField("ATGE_adjVolume", IntegerType(), True)])
ATGE_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ATGE_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ATGE_30min.txt")
display(ATGE_30min_spark_DF)

ATI_30min_spark_DF_newRow = StructType([StructField("ATI_date/time", StringType(), True),StructField("ATI_adjOpen", FloatType(), True),StructField("ATI_adjHigh", FloatType(), True),StructField("ATI_adjLow", FloatType(), True),StructField("ATI_adjClose", FloatType(), True),StructField("ATI_adjVolume", IntegerType(), True)])
ATI_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ATI_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ATI_30min.txt")
display(ATI_30min_spark_DF)

ATO_30min_spark_DF_newRow = StructType([StructField("ATO_date/time", StringType(), True),StructField("ATO_adjOpen", FloatType(), True),StructField("ATO_adjHigh", FloatType(), True),StructField("ATO_adjLow", FloatType(), True),StructField("ATO_adjClose", FloatType(), True),StructField("ATO_adjVolume", IntegerType(), True)])
ATO_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ATO_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ATO_30min.txt")
display(ATO_30min_spark_DF)

ATVI_30min_spark_DF_newRow = StructType([StructField("ATVI_date/time", StringType(), True),StructField("ATVI_adjOpen", FloatType(), True),StructField("ATVI_adjHigh", FloatType(), True),StructField("ATVI_adjLow", FloatType(), True),StructField("ATVI_adjClose", FloatType(), True),StructField("ATVI_adjVolume", IntegerType(), True)])
ATVI_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ATVI_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ATVI_30min.txt")
display(ATVI_30min_spark_DF)

AVB_30min_spark_DF_newRow = StructType([StructField("AVB_date/time", StringType(), True),StructField("AVB_adjOpen", FloatType(), True),StructField("AVB_adjHigh", FloatType(), True),StructField("AVB_adjLow", FloatType(), True),StructField("AVB_adjClose", FloatType(), True),StructField("AVB_adjVolume", IntegerType(), True)])
AVB_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AVB_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AVB_30min.txt")
display(AVB_30min_spark_DF)

AVGO_30min_spark_DF_newRow = StructType([StructField("AVGO_date/time", StringType(), True),StructField("AVGO_adjOpen", FloatType(), True),StructField("AVGO_adjHigh", FloatType(), True),StructField("AVGO_adjLow", FloatType(), True),StructField("AVGO_adjClose", FloatType(), True),StructField("AVGO_adjVolume", IntegerType(), True)])
AVGO_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AVGO_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AVGO_30min.txt")
display(AVGO_30min_spark_DF)

AVY_30min_spark_DF_newRow = StructType([StructField("AVY_date/time", StringType(), True),StructField("AVY_adjOpen", FloatType(), True),StructField("AVY_adjHigh", FloatType(), True),StructField("AVY_adjLow", FloatType(), True),StructField("AVY_adjClose", FloatType(), True),StructField("AVY_adjVolume", IntegerType(), True)])
AVY_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AVY_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AVY_30min.txt")
display(AVY_30min_spark_DF)

AWK_30min_spark_DF_newRow = StructType([StructField("AWK_date/time", StringType(), True),StructField("AWK_adjOpen", FloatType(), True),StructField("AWK_adjHigh", FloatType(), True),StructField("AWK_adjLow", FloatType(), True),StructField("AWK_adjClose", FloatType(), True),StructField("AWK_adjVolume", IntegerType(), True)])
AWK_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AWK_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AWK_30min.txt")
display(AWK_30min_spark_DF)

AXP_30min_spark_DF_newRow = StructType([StructField("AXP_date/time", StringType(), True),StructField("AXP_adjOpen", FloatType(), True),StructField("AXP_adjHigh", FloatType(), True),StructField("AXP_adjLow", FloatType(), True),StructField("AXP_adjClose", FloatType(), True),StructField("AXP_adjVolume", IntegerType(), True)])
AXP_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AXP_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AXP_30min.txt")
display(AXP_30min_spark_DF)

AYI_30min_spark_DF_newRow = StructType([StructField("AYI_date/time", StringType(), True),StructField("AYI_adjOpen", FloatType(), True),StructField("AYI_adjHigh", FloatType(), True),StructField("AYI_adjLow", FloatType(), True),StructField("AYI_adjClose", FloatType(), True),StructField("AYI_adjVolume", IntegerType(), True)])
AYI_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AYI_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AYI_30min.txt")
display(AYI_30min_spark_DF)

AZO_30min_spark_DF_newRow = StructType([StructField("AZO_date/time", StringType(), True),StructField("AZO_adjOpen", FloatType(), True),StructField("AZO_adjHigh", FloatType(), True),StructField("AZO_adjLow", FloatType(), True),StructField("AZO_adjClose", FloatType(), True),StructField("AZO_adjVolume", IntegerType(), True)])
AZO_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AZO_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AZO_30min.txt")
display(AZO_30min_spark_DF)

A_30min_spark_DF_newRow = StructType([StructField("A_date/time", StringType(), True),StructField("A_adjOpen", FloatType(), True),StructField("A_adjHigh", FloatType(), True),StructField("A_adjLow", FloatType(), True),StructField("A_adjClose", FloatType(), True),StructField("A_adjVolume", IntegerType(), True)])
A_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(A_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/A_30min.txt")
display(A_30min_spark_DF)


BAC_30min_spark_DF_newRow = StructType([StructField("BAC_date/time", StringType(), True),StructField("BAC_adjOpen", FloatType(), True),StructField("BAC_adjHigh", FloatType(), True),StructField("BAC_adjLow", FloatType(), True),StructField("BAC_adjClose", FloatType(), True),StructField("BAC_adjVolume", IntegerType(), True)])
BAC_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BAC_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BAC_30min.txt")
display(BAC_30min_spark_DF)

BAX_30min_spark_DF_newRow = StructType([StructField("BAX_date/time", StringType(), True),StructField("BAX_adjOpen", FloatType(), True),StructField("BAX_adjHigh", FloatType(), True),StructField("BAX_adjLow", FloatType(), True),StructField("BAX_adjClose", FloatType(), True),StructField("BAX_adjVolume", IntegerType(), True)])
BAX_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BAX_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BAX_30min.txt")
display(BAX_30min_spark_DF)

BA_30min_spark_DF_newRow = StructType([StructField("BA_date/time", StringType(), True),StructField("BA_adjOpen", FloatType(), True),StructField("BA_adjHigh", FloatType(), True),StructField("BA_adjLow", FloatType(), True),StructField("BA_adjClose", FloatType(), True),StructField("BA_adjVolume", IntegerType(), True)])
BA_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BA_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BA_30min.txt")
display(BA_30min_spark_DF)

BBBY_30min_spark_DF_newRow = StructType([StructField("BBBY_date/time", StringType(), True),StructField("BBBY_adjOpen", FloatType(), True),StructField("BBBY_adjHigh", FloatType(), True),StructField("BBBY_adjLow", FloatType(), True),StructField("BBBY_adjClose", FloatType(), True),StructField("BBBY_adjVolume", IntegerType(), True)])
BBBY_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BBBY_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BBBY_30min.txt")
display(BBBY_30min_spark_DF)

BBY_30min_spark_DF_newRow = StructType([StructField("BBY_date/time", StringType(), True),StructField("BBY_adjOpen", FloatType(), True),StructField("BBY_adjHigh", FloatType(), True),StructField("BBY_adjLow", FloatType(), True),StructField("BBY_adjClose", FloatType(), True),StructField("BBY_adjVolume", IntegerType(), True)])
BBY_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BBY_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BBY_30min.txt")
display(BBY_30min_spark_DF)

BC_30min_spark_DF_newRow = StructType([StructField("BC_date/time", StringType(), True),StructField("BC_adjOpen", FloatType(), True),StructField("BC_adjHigh", FloatType(), True),StructField("BC_adjLow", FloatType(), True),StructField("BC_adjClose", FloatType(), True),StructField("BC_adjVolume", IntegerType(), True)])
BC_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BC_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BC_30min.txt")
display(BC_30min_spark_DF)

BDX_30min_spark_DF_newRow = StructType([StructField("BDX_date/time", StringType(), True),StructField("BDX_adjOpen", FloatType(), True),StructField("BDX_adjHigh", FloatType(), True),StructField("BDX_adjLow", FloatType(), True),StructField("BDX_adjClose", FloatType(), True),StructField("BDX_adjVolume", IntegerType(), True)])
BDX_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BDX_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BDX_30min.txt")
display(BDX_30min_spark_DF)

BEN_30min_spark_DF_newRow = StructType([StructField("BEN_date/time", StringType(), True),StructField("BEN_adjOpen", FloatType(), True),StructField("BEN_adjHigh", FloatType(), True),StructField("BEN_adjLow", FloatType(), True),StructField("BEN_adjClose", FloatType(), True),StructField("BEN_adjVolume", IntegerType(), True)])
BEN_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BEN_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BEN_30min.txt")
display(BEN_30min_spark_DF)

BF_B_30min_spark_DF_newRow = StructType([StructField("BF_B_date/time", StringType(), True),StructField("BF_B_adjOpen", FloatType(), True),StructField("BF_B_adjHigh", FloatType(), True),StructField("BF_B_adjLow", FloatType(), True),StructField("BF_B_adjClose", FloatType(), True),StructField("BF_B_adjVolume", IntegerType(), True)])
BF_B_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BF_B_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BF_B_30min.txt")
display(BF_B_30min_spark_DF)

BIDU_30min_spark_DF_newRow = StructType([StructField("BIDU_date/time", StringType(), True),StructField("BIDU_adjOpen", FloatType(), True),StructField("BIDU_adjHigh", FloatType(), True),StructField("BIDU_adjLow", FloatType(), True),StructField("BIDU_adjClose", FloatType(), True),StructField("BIDU_adjVolume", IntegerType(), True)])
BIDU_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BIDU_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BIDU_30min.txt")
display(BIDU_30min_spark_DF)

BIG_30min_spark_DF_newRow = StructType([StructField("BIG_date/time", StringType(), True),StructField("BIG_adjOpen", FloatType(), True),StructField("BIG_adjHigh", FloatType(), True),StructField("BIG_adjLow", FloatType(), True),StructField("BIG_adjClose", FloatType(), True),StructField("BIG_adjVolume", IntegerType(), True)])
BIG_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BIG_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BIG_30min.txt")
display(BIG_30min_spark_DF)

BIIB_30min_spark_DF_newRow = StructType([StructField("BIIB_date/time", StringType(), True),StructField("BIIB_adjOpen", FloatType(), True),StructField("BIIB_adjHigh", FloatType(), True),StructField("BIIB_adjLow", FloatType(), True),StructField("BIIB_adjClose", FloatType(), True),StructField("BIIB_adjVolume", IntegerType(), True)])
BIIB_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BIIB_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BIIB_30min.txt")
display(BIIB_30min_spark_DF)

BIO_30min_spark_DF_newRow = StructType([StructField("BIO_date/time", StringType(), True),StructField("BIO_adjOpen", FloatType(), True),StructField("BIO_adjHigh", FloatType(), True),StructField("BIO_adjLow", FloatType(), True),StructField("BIO_adjClose", FloatType(), True),StructField("BIO_adjVolume", IntegerType(), True)])
BIO_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BIO_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BIO_30min.txt")
display(BIO_30min_spark_DF)

BKNG_30min_spark_DF_newRow = StructType([StructField("BKNG_date/time", StringType(), True),StructField("BKNG_adjOpen", FloatType(), True),StructField("BKNG_adjHigh", FloatType(), True),StructField("BKNG_adjLow", FloatType(), True),StructField("BKNG_adjClose", FloatType(), True),StructField("BKNG_adjVolume", IntegerType(), True)])
BKNG_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BKNG_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BKNG_30min.txt")
display(BKNG_30min_spark_DF)

BK_30min_spark_DF_newRow = StructType([StructField("BK_date/time", StringType(), True),StructField("BK_adjOpen", FloatType(), True),StructField("BK_adjHigh", FloatType(), True),StructField("BK_adjLow", FloatType(), True),StructField("BK_adjClose", FloatType(), True),StructField("BK_adjVolume", IntegerType(), True)])
BK_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BK_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BK_30min.txt")
display(BK_30min_spark_DF)

BLK_30min_spark_DF_newRow = StructType([StructField("BLK_date/time", StringType(), True),StructField("BLK_adjOpen", FloatType(), True),StructField("BLK_adjHigh", FloatType(), True),StructField("BLK_adjLow", FloatType(), True),StructField("BLK_adjClose", FloatType(), True),StructField("BLK_adjVolume", IntegerType(), True)])
BLK_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BLK_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BLK_30min.txt")
display(BLK_30min_spark_DF)

BLL_30min_spark_DF_newRow = StructType([StructField("BLL_date/time", StringType(), True),StructField("BLL_adjOpen", FloatType(), True),StructField("BLL_adjHigh", FloatType(), True),StructField("BLL_adjLow", FloatType(), True),StructField("BLL_adjClose", FloatType(), True),StructField("BLL_adjVolume", IntegerType(), True)])
BLL_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BLL_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BLL_30min.txt")
display(BLL_30min_spark_DF)

BMRN_30min_spark_DF_newRow = StructType([StructField("BMRN_date/time", StringType(), True),StructField("BMRN_adjOpen", FloatType(), True),StructField("BMRN_adjHigh", FloatType(), True),StructField("BMRN_adjLow", FloatType(), True),StructField("BMRN_adjClose", FloatType(), True),StructField("BMRN_adjVolume", IntegerType(), True)])
BMRN_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BMRN_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BMRN_30min.txt")
display(BMRN_30min_spark_DF)

BMY_30min_spark_DF_newRow = StructType([StructField("BMY_date/time", StringType(), True),StructField("BMY_adjOpen", FloatType(), True),StructField("BMY_adjHigh", FloatType(), True),StructField("BMY_adjLow", FloatType(), True),StructField("BMY_adjClose", FloatType(), True),StructField("BMY_adjVolume", IntegerType(), True)])
BMY_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BMY_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BMY_30min.txt")
display(BMY_30min_spark_DF)

BRK_B_30min_spark_DF_newRow = StructType([StructField("BRK_B_date/time", StringType(), True),StructField("BRK_B_adjOpen", FloatType(), True),StructField("BRK_B_adjHigh", FloatType(), True),StructField("BRK_B_adjLow", FloatType(), True),StructField("BRK_B_adjClose", FloatType(), True),StructField("BRK_B_adjVolume", IntegerType(), True)])
BRK_B_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BRK_B_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BRK_B_30min.txt")
display(BRK_B_30min_spark_DF)

BRO_30min_spark_DF_newRow = StructType([StructField("BRO_date/time", StringType(), True),StructField("BRO_adjOpen", FloatType(), True),StructField("BRO_adjHigh", FloatType(), True),StructField("BRO_adjLow", FloatType(), True),StructField("BRO_adjClose", FloatType(), True),StructField("BRO_adjVolume", IntegerType(), True)])
BRO_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BRK_B_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BRO_30min.txt")
display(BRO_30min_spark_DF)

BR_30min_spark_DF_newRow = StructType([StructField("BR_date/time", StringType(), True),StructField("BR_adjOpen", FloatType(), True),StructField("BR_adjHigh", FloatType(), True),StructField("BR_adjLow", FloatType(), True),StructField("BR_adjClose", FloatType(), True),StructField("BR_adjVolume", IntegerType(), True)])
BR_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BR_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BR_30min.txt")
display(BR_30min_spark_DF)

BSX_30min_spark_DF_newRow = StructType([StructField("BSX_date/time", StringType(), True),StructField("BSX_adjOpen", FloatType(), True),StructField("BSX_adjHigh", FloatType(), True),StructField("BSX_adjLow", FloatType(), True),StructField("BSX_adjClose", FloatType(), True),StructField("BSX_adjVolume", IntegerType(), True)])
BSX_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BSX_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BSX_30min.txt")
display(BSX_30min_spark_DF)

BTU_30min_spark_DF_newRow = StructType([StructField("BTU_date/time", StringType(), True),StructField("BTU_adjOpen", FloatType(), True),StructField("BTU_adjHigh", FloatType(), True),StructField("BTU_adjLow", FloatType(), True),StructField("BTU_adjClose", FloatType(), True),StructField("BTU_adjVolume", IntegerType(), True)])
BTU_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BTU_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BTU_30min.txt")
display(BTU_30min_spark_DF)

BUD_30min_spark_DF_newRow = StructType([StructField("BUD_date/time", StringType(), True),StructField("BUD_adjOpen", FloatType(), True),StructField("BUD_adjHigh", FloatType(), True),StructField("BUD_adjLow", FloatType(), True),StructField("BUD_adjClose", FloatType(), True),StructField("BUD_adjVolume", IntegerType(), True)])
BUD_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BUD_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BUD_30min.txt")
display(BUD_30min_spark_DF)

BWA_30min_spark_DF_newRow = StructType([StructField("BUD_date/time", StringType(), True),StructField("BUD_adjOpen", FloatType(), True),StructField("BUD_adjHigh", FloatType(), True),StructField("BUD_adjLow", FloatType(), True),StructField("BUD_adjClose", FloatType(), True),StructField("BUD_adjVolume", IntegerType(), True)])
BUD_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BUD_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BUD_30min.txt")
display(BUD_30min_spark_DF)

BXP_30min_spark_DF_newRow = StructType([StructField("BXP_date/time", StringType(), True),StructField("BXP_adjOpen", FloatType(), True),StructField("BXP_adjHigh", FloatType(), True),StructField("BXP_adjLow", FloatType(), True),StructField("BXP_adjClose", FloatType(), True),StructField("BXP_adjVolume", IntegerType(), True)])
BXP_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(BXP_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/BXP_30min.txt")
display(BXP_30min_spark_DF)


CAG_30min_spark_DF_newRow = StructType([StructField("CAG_date/time", StringType(), True),StructField("CAG_adjOpen", FloatType(), True),StructField("CAG_adjHigh", FloatType(), True),StructField("CAG_adjLow", FloatType(), True),StructField("CAG_adjClose", FloatType(), True),StructField("CAG_adjVolume", IntegerType(), True)])
CAG_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CAG_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CAG_30min.txt")
display(CAG_30min_spark_DF)

CAH_30min_spark_DF_newRow = StructType([StructField("CAH_date/time", StringType(), True),StructField("CAH_adjOpen", FloatType(), True),StructField("CAH_adjHigh", FloatType(), True),StructField("CAH_adjLow", FloatType(), True),StructField("CAH_adjClose", FloatType(), True),StructField("CAH_adjVolume", IntegerType(), True)])
CAH_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CAH_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CAH_30min.txt")
display(CAH_30min_spark_DF)

CARR_30min_spark_DF_newRow = StructType([StructField("CARR_date/time", StringType(), True),StructField("CARR_adjOpen", FloatType(), True),StructField("CARR_adjHigh", FloatType(), True),StructField("CARR_adjLow", FloatType(), True),StructField("CARR_adjClose", FloatType(), True),StructField("CARR_adjVolume", IntegerType(), True)])
CARR_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CARR_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CARR_30min.txt")
display(CARR_30min_spark_DF)

CAR_30min_spark_DF_newRow = StructType([StructField("CAR_date/time", StringType(), True),StructField("CAR_adjOpen", FloatType(), True),StructField("CAR_adjHigh", FloatType(), True),StructField("CAR_adjLow", FloatType(), True),StructField("CAR_adjClose", FloatType(), True),StructField("CAR_adjVolume", IntegerType(), True)])
CAR_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CAR_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CAR_30min.txt")
display(CAR_30min_spark_DF)

CAT_30min_spark_DF_newRow = StructType([StructField("CAT_date/time", StringType(), True),StructField("CAT_adjOpen", FloatType(), True),StructField("CAT_adjHigh", FloatType(), True),StructField("CAT_adjLow", FloatType(), True),StructField("CAT_adjClose", FloatType(), True),StructField("CAT_adjVolume", IntegerType(), True)])
CAT_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CAT_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CAT_30min.txt")
display(CAT_30min_spark_DF)

CBH_30min_spark_DF_newRow = StructType([StructField("CBH_date/time", StringType(), True),StructField("CBH_adjOpen", FloatType(), True),StructField("CBH_adjHigh", FloatType(), True),StructField("CBH_adjLow", FloatType(), True),StructField("CBH_adjClose", FloatType(), True),StructField("CBH_adjVolume", IntegerType(), True)])
CBH_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CBH_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CBH_30min.txt")
display(CBH_30min_spark_DF)

CBOE_30min_spark_DF_newRow = StructType([StructField("CBOE_date/time", StringType(), True),StructField("CBOE_adjOpen", FloatType(), True),StructField("CBOE_adjHigh", FloatType(), True),StructField("CBOE_adjLow", FloatType(), True),StructField("CBOE_adjClose", FloatType(), True),StructField("CBOE_adjVolume", IntegerType(), True)])
CBOE_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CBOE_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CBOE_30min.txt")
display(CBOE_30min_spark_DF)

CBRE_30min_spark_DF_newRow = StructType([StructField("CBRE_date/time", StringType(), True),StructField("CBRE_adjOpen", FloatType(), True),StructField("CBRE_adjHigh", FloatType(), True),StructField("CBRE_adjLow", FloatType(), True),StructField("CBRE_adjClose", FloatType(), True),StructField("CBRE_adjVolume", IntegerType(), True)])
CBRE_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CBRE_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CBRE_30min.txt")
display(CBRE_30min_spark_DF)

CB_30min_spark_DF_newRow = StructType([StructField("CB_date/time", StringType(), True),StructField("CB_adjOpen", FloatType(), True),StructField("CB_adjHigh", FloatType(), True),StructField("CB_adjLow", FloatType(), True),StructField("CB_adjClose", FloatType(), True),StructField("CB_adjVolume", IntegerType(), True)])
CB_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CB_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CB_30min.txt")
display(CB_30min_spark_DF)

CCI_30min_spark_DF_newRow = StructType([StructField("CCI_date/time", StringType(), True),StructField("CCI_adjOpen", FloatType(), True),StructField("CCI_adjHigh", FloatType(), True),StructField("CCI_adjLow", FloatType(), True),StructField("CCI_adjClose", FloatType(), True),StructField("CCI_adjVolume", IntegerType(), True)])
CCI_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CCI_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CCI_30min.txt")
display(CCI_30min_spark_DF)

CCK_30min_spark_DF_newRow = StructType([StructField("CCK_date/time", StringType(), True),StructField("CCK_adjOpen", FloatType(), True),StructField("CCK_adjHigh", FloatType(), True),StructField("CCK_adjLow", FloatType(), True),StructField("CCK_adjClose", FloatType(), True),StructField("CCK_adjVolume", IntegerType(), True)])
CCK_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CCK_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CCK_30min.txt")
display(CCK_30min_spark_DF)

CCL_30min_spark_DF_newRow = StructType([StructField("CCL_date/time", StringType(), True),StructField("CCL_adjOpen", FloatType(), True),StructField("CCL_adjHigh", FloatType(), True),StructField("CCL_adjLow", FloatType(), True),StructField("CCL_adjClose", FloatType(), True),StructField("CCL_adjVolume", IntegerType(), True)])
CCL_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CCL_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CCL_30min.txt")
display(CCL_30min_spark_DF)

CCU_30min_spark_DF_newRow = StructType([StructField("CCU_date/time", StringType(), True),StructField("CCU_adjOpen", FloatType(), True),StructField("CCU_adjHigh", FloatType(), True),StructField("CCU_adjLow", FloatType(), True),StructField("CCU_adjClose", FloatType(), True),StructField("CCU_adjVolume", IntegerType(), True)])
CCU_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CCU_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CCU_30min.txt")
display(CCU_30min_spark_DF)

CC_30min_spark_DF_newRow = StructType([StructField("CC_date/time", StringType(), True),StructField("CC_adjOpen", FloatType(), True),StructField("CC_adjHigh", FloatType(), True),StructField("CC_adjLow", FloatType(), True),StructField("CC_adjClose", FloatType(), True),StructField("CC_adjVolume", IntegerType(), True)])
CC_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CC_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CC_30min.txt")
display(CC_30min_spark_DF)

CDAY_30min_spark_DF_newRow = StructType([StructField("CDAY_date/time", StringType(), True),StructField("CDAY_adjOpen", FloatType(), True),StructField("CDAY_adjHigh", FloatType(), True),StructField("CDAY_adjLow", FloatType(), True),StructField("CDAY_adjClose", FloatType(), True),StructField("CDAY_adjVolume", IntegerType(), True)])
CDAY_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CDAY_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CDAY_30min.txt")
display(CDAY_30min_spark_DF)

CDNS_30min_spark_DF_newRow = StructType([StructField("CDNS_date/time", StringType(), True),StructField("CDNS_adjOpen", FloatType(), True),StructField("CDNS_adjHigh", FloatType(), True),StructField("CDNS_adjLow", FloatType(), True),StructField("CDNS_adjClose", FloatType(), True),StructField("CDNS_adjVolume", IntegerType(), True)])
CDNS_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CDNS_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CDNS_30min.txt")
display(CDNS_30min_spark_DF)

CDW_30min_spark_DF_newRow = StructType([StructField("CDW_date/time", StringType(), True),StructField("CDW_adjOpen", FloatType(), True),StructField("CDW_adjHigh", FloatType(), True),StructField("CDW_adjLow", FloatType(), True),StructField("CDW_adjClose", FloatType(), True),StructField("CDW_adjVolume", IntegerType(), True)])
CDW_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CDW_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CDW_30min.txt")
display(CDW_30min_spark_DF)

CERN_30min_spark_DF_newRow = StructType([StructField("CERN_date/time", StringType(), True),StructField("CERN_adjOpen", FloatType(), True),StructField("CERN_adjHigh", FloatType(), True),StructField("CERN_adjLow", FloatType(), True),StructField("CERN_adjClose", FloatType(), True),StructField("CERN_adjVolume", IntegerType(), True)])
CERN_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CERN_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CERN_30min.txt")
display(CERN_30min_spark_DF)

CE_30min_spark_DF_newRow = StructType([StructField("CE_date/time", StringType(), True),StructField("CE_adjOpen", FloatType(), True),StructField("CE_adjHigh", FloatType(), True),StructField("CE_adjLow", FloatType(), True),StructField("CE_adjClose", FloatType(), True),StructField("CE_adjVolume", IntegerType(), True)])
CE_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CE_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CE_30min.txt")
display(CE_30min_spark_DF)

CFG_30min_spark_DF_newRow = StructType([StructField("CFG_date/time", StringType(), True),StructField("CFG_adjOpen", FloatType(), True),StructField("CFG_adjHigh", FloatType(), True),StructField("CFG_adjLow", FloatType(), True),StructField("CFG_adjClose", FloatType(), True),StructField("CFG_adjVolume", IntegerType(), True)])
CFG_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CFG_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CFG_30min.txt")
display(CFG_30min_spark_DF)

CF_30min_spark_DF_newRow = StructType([StructField("CF_date/time", StringType(), True),StructField("CF_adjOpen", FloatType(), True),StructField("CF_adjHigh", FloatType(), True),StructField("CF_adjLow", FloatType(), True),StructField("CF_adjClose", FloatType(), True),StructField("CF_adjVolume", IntegerType(), True)])
CF_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CF_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CF_30min.txt")
display(CF_30min_spark_DF)

CHD_30min_spark_DF_newRow = StructType([StructField("CHD_date/time", StringType(), True),StructField("CHD_adjOpen", FloatType(), True),StructField("CHD_adjHigh", FloatType(), True),StructField("CHD_adjLow", FloatType(), True),StructField("CHD_adjClose", FloatType(), True),StructField("CHD_adjVolume", IntegerType(), True)])
CHD_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CHD_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CHD_30min.txt")
display(CHD_30min_spark_DF)

CHIR_30min_spark_DF_newRow = StructType([StructField("CHIR_date/time", StringType(), True),StructField("CHIR_adjOpen", FloatType(), True),StructField("CHIR_adjHigh", FloatType(), True),StructField("CHIR_adjLow", FloatType(), True),StructField("CHIR_adjClose", FloatType(), True),StructField("CHIR_adjVolume", IntegerType(), True)])
CHIR_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CHIR_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CHIR_30min.txt")
display(CHIR_30min_spark_DF)

CHKP_30min_spark_DF_newRow = StructType([StructField("CHKP_date/time", StringType(), True),StructField("CHKP_adjOpen", FloatType(), True),StructField("CHKP_adjHigh", FloatType(), True),StructField("CHKP_adjLow", FloatType(), True),StructField("CHKP_adjClose", FloatType(), True),StructField("CHKP_adjVolume", IntegerType(), True)])
CHKP_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CHKP_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CHKP_30min.txt")
display(CHKP_30min_spark_DF)

CHK_30min_spark_DF_newRow = StructType([StructField("CHK_date/time", StringType(), True),StructField("CHK_adjOpen", FloatType(), True),StructField("CHK_adjHigh", FloatType(), True),StructField("CHK_adjLow", FloatType(), True),StructField("CHK_adjClose", FloatType(), True),StructField("CHK_adjVolume", IntegerType(), True)])
CHK_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CHK_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CHK_30min.txt")
display(CHK_30min_spark_DF)

CHRW_30min_spark_DF_newRow = StructType([StructField("CHRW_date/time", StringType(), True),StructField("CHRW_adjOpen", FloatType(), True),StructField("CHRW_adjHigh", FloatType(), True),StructField("CHRW_adjLow", FloatType(), True),StructField("CHRW_adjClose", FloatType(), True),StructField("CHRW_adjVolume", IntegerType(), True)])
CHRW_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CHRW_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CHRW_30min.txt")
display(CHRW_30min_spark_DF)

CHTR_30min_spark_DF_newRow = StructType([StructField("CHTR_date/time", StringType(), True),StructField("CHTR_adjOpen", FloatType(), True),StructField("CHTR_adjHigh", FloatType(), True),StructField("CHTR_adjLow", FloatType(), True),StructField("CHTR_adjClose", FloatType(), True),StructField("CHTR_adjVolume", IntegerType(), True)])
CHTR_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CHTR_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CHTR_30min.txt")
display(CHTR_30min_spark_DF)

CIEN_30min_spark_DF_newRow = StructType([StructField("CIEN_date/time", StringType(), True),StructField("CIEN_adjOpen", FloatType(), True),StructField("CIEN_adjHigh", FloatType(), True),StructField("CIEN_adjLow", FloatType(), True),StructField("CIEN_adjClose", FloatType(), True),StructField("CIEN_adjVolume", IntegerType(), True)])
CIEN_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CIEN_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CIEN_30min.txt")
display(CIEN_30min_spark_DF)

CINF_30min_spark_DF_newRow = StructType([StructField("CINF_date/time", StringType(), True),StructField("CINF_adjOpen", FloatType(), True),StructField("CINF_adjHigh", FloatType(), True),StructField("CINF_adjLow", FloatType(), True),StructField("CINF_adjClose", FloatType(), True),StructField("CINF_adjVolume", IntegerType(), True)])
CINF_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CINF_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CINF_30min.txt")
display(CINF_30min_spark_DF)

CIT_30min_spark_DF_newRow = StructType([StructField("CIT_date/time", StringType(), True),StructField("CIT_adjOpen", FloatType(), True),StructField("CIT_adjHigh", FloatType(), True),StructField("CIT_adjLow", FloatType(), True),StructField("CIT_adjClose", FloatType(), True),StructField("CIT_adjVolume", IntegerType(), True)])
CIT_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CIT_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CIT_30min.txt")
display(CIT_30min_spark_DF)

CI_30min_spark_DF_newRow = StructType([StructField("CI_date/time", StringType(), True),StructField("CI_adjOpen", FloatType(), True),StructField("CI_adjHigh", FloatType(), True),StructField("CI_adjLow", FloatType(), True),StructField("CI_adjClose", FloatType(), True),StructField("CI_adjVolume", IntegerType(), True)])
CI_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CI_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CI_30min.txt")
display(CI_30min_spark_DF)

CLF_30min_spark_DF_newRow = StructType([StructField("CLF_date/time", StringType(), True),StructField("CLF_adjOpen", FloatType(), True),StructField("CLF_adjHigh", FloatType(), True),StructField("CLF_adjLow", FloatType(), True),StructField("CLF_adjClose", FloatType(), True),StructField("CLF_adjVolume", IntegerType(), True)])
CLF_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CLF_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CLF_30min.txt")
display(CLF_30min_spark_DF)

CLX_30min_spark_DF_newRow = StructType([StructField("CLX_date/time", StringType(), True),StructField("CLX_adjOpen", FloatType(), True),StructField("CLX_adjHigh", FloatType(), True),StructField("CLX_adjLow", FloatType(), True),StructField("CLX_adjClose", FloatType(), True),StructField("CLX_adjVolume", IntegerType(), True)])
CLX_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CLX_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CLX_30min.txt")
display(CLX_30min_spark_DF)

CL_30min_spark_DF_newRow = StructType([StructField("CL_date/time", StringType(), True),StructField("CL_adjOpen", FloatType(), True),StructField("CL_adjHigh", FloatType(), True),StructField("CL_adjLow", FloatType(), True),StructField("CL_adjClose", FloatType(), True),StructField("CL_adjVolume", IntegerType(), True)])
CL_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CL_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CL_30min.txt")
display(CL_30min_spark_DF)

CMA_30min_spark_DF_newRow = StructType([StructField("CMA_date/time", StringType(), True),StructField("CMA_adjOpen", FloatType(), True),StructField("CMA_adjHigh", FloatType(), True),StructField("CMA_adjLow", FloatType(), True),StructField("CMA_adjClose", FloatType(), True),StructField("CMA_adjVolume", IntegerType(), True)])
CMA_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CMA_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CMA_30min.txt")
display(CMA_30min_spark_DF)

CMCSA_30min_spark_DF_newRow = StructType([StructField("CMCSA_date/time", StringType(), True),StructField("CMCSA_adjOpen", FloatType(), True),StructField("CMCSA_adjHigh", FloatType(), True),StructField("CMCSA_adjLow", FloatType(), True),StructField("CMCSA_adjClose", FloatType(), True),StructField("CMCSA_adjVolume", IntegerType(), True)])
CMCSA_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CMCSA_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CMCSA_30min.txt")
display(CMCSA_30min_spark_DF)

CME_30min_spark_DF_newRow = StructType([StructField("CME_date/time", StringType(), True),StructField("CME_adjOpen", FloatType(), True),StructField("CME_adjHigh", FloatType(), True),StructField("CME_adjLow", FloatType(), True),StructField("CME_adjClose", FloatType(), True),StructField("CME_adjVolume", IntegerType(), True)])
CME_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CME_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CME_30min.txt")
display(CME_30min_spark_DF)

CMG_30min_spark_DF_newRow = StructType([StructField("CMG_date/time", StringType(), True),StructField("CMG_adjOpen", FloatType(), True),StructField("CMG_adjHigh", FloatType(), True),StructField("CMG_adjLow", FloatType(), True),StructField("CMG_adjClose", FloatType(), True),StructField("CMG_adjVolume", IntegerType(), True)])
CMG_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CMG_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CMG_30min.txt")
display(CMG_30min_spark_DF)

CMI_30min_spark_DF_newRow = StructType([StructField("CMI_date/time", StringType(), True),StructField("CMI_adjOpen", FloatType(), True),StructField("CMI_adjHigh", FloatType(), True),StructField("CMI_adjLow", FloatType(), True),StructField("CMI_adjClose", FloatType(), True),StructField("CMI_adjVolume", IntegerType(), True)])
CMI_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CMI_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CMI_30min.txt")
display(CMI_30min_spark_DF)

CMS_30min_spark_DF_newRow = StructType([StructField("CMS_date/time", StringType(), True),StructField("CMS_adjOpen", FloatType(), True),StructField("CMS_adjHigh", FloatType(), True),StructField("CMS_adjLow", FloatType(), True),StructField("CMS_adjClose", FloatType(), True),StructField("CMS_adjVolume", IntegerType(), True)])
CMS_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CMS_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CMS_30min.txt")
display(CMS_30min_spark_DF)

CNC_30min_spark_DF_newRow = StructType([StructField("CNC_date/time", StringType(), True),StructField("CNC_adjOpen", FloatType(), True),StructField("CNC_adjHigh", FloatType(), True),StructField("CNC_adjLow", FloatType(), True),StructField("CNC_adjClose", FloatType(), True),StructField("CNC_adjVolume", IntegerType(), True)])
CNC_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CNC_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CNC_30min.txt")
display(CNC_30min_spark_DF)

CNP_30min_spark_DF_newRow = StructType([StructField("CNP_date/time", StringType(), True),StructField("CNP_adjOpen", FloatType(), True),StructField("CNP_adjHigh", FloatType(), True),StructField("CNP_adjLow", FloatType(), True),StructField("CNP_adjClose", FloatType(), True),StructField("CNP_adjVolume", IntegerType(), True)])
CNP_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CNP_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CNP_30min.txt")
display(CNP_30min_spark_DF)

CNX_30min_spark_DF_newRow = StructType([StructField("CNX_date/time", StringType(), True),StructField("CNX_adjOpen", FloatType(), True),StructField("CNX_adjHigh", FloatType(), True),StructField("CNX_adjLow", FloatType(), True),StructField("CNX_adjClose", FloatType(), True),StructField("CNX_adjVolume", IntegerType(), True)])
CNX_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CNX_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CNX_30min.txt")
display(CNX_30min_spark_DF)

COF_30min_spark_DF_newRow = StructType([StructField("COF_date/time", StringType(), True),StructField("COF_adjOpen", FloatType(), True),StructField("COF_adjHigh", FloatType(), True),StructField("COF_adjLow", FloatType(), True),StructField("COF_adjClose", FloatType(), True),StructField("COF_adjVolume", IntegerType(), True)])
COF_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(COF_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/COF_30min.txt")
display(COF_30min_spark_DF)

COOP_30min_spark_DF_newRow = StructType([StructField("COOP_date/time", StringType(), True),StructField("COOP_adjOpen", FloatType(), True),StructField("COOP_adjHigh", FloatType(), True),StructField("COOP_adjLow", FloatType(), True),StructField("COOP_adjClose", FloatType(), True),StructField("COOP_adjVolume", IntegerType(), True)])
COOP_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(COOP_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/COOP_30min.txt")
display(COOP_30min_spark_DF)

COO_30min_spark_DF_newRow = StructType([StructField("COO_date/time", StringType(), True),StructField("COO_adjOpen", FloatType(), True),StructField("COO_adjHigh", FloatType(), True),StructField("COO_adjLow", FloatType(), True),StructField("COO_adjClose", FloatType(), True),StructField("COO_adjVolume", IntegerType(), True)])
COO_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(COO_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/COO_30min.txt")
display(COO_30min_spark_DF)

COP_30min_spark_DF_newRow = StructType([StructField("COP_date/time", StringType(), True),StructField("COP_adjOpen", FloatType(), True),StructField("COP_adjHigh", FloatType(), True),StructField("COP_adjLow", FloatType(), True),StructField("COP_adjClose", FloatType(), True),StructField("COP_adjVolume", IntegerType(), True)])
COP_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(COP_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/COP_30min.txt")
display(COP_30min_spark_DF)

COST_30min_spark_DF_newRow = StructType([StructField("COST_date/time", StringType(), True),StructField("COST_adjOpen", FloatType(), True),StructField("COST_adjHigh", FloatType(), True),StructField("COST_adjLow", FloatType(), True),StructField("COST_adjClose", FloatType(), True),StructField("COST_adjVolume", IntegerType(), True)])
COST_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(COST_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/COST_30min.txt")
display(COST_30min_spark_DF)

COTY_30min_spark_DF_newRow = StructType([StructField("COTY_date/time", StringType(), True),StructField("COTY_adjOpen", FloatType(), True),StructField("COTY_adjHigh", FloatType(), True),StructField("COTY_adjLow", FloatType(), True),StructField("COTY_adjClose", FloatType(), True),StructField("COTY_adjVolume", IntegerType(), True)])
COTY_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(COTY_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/COTY_30min.txt")
display(COTY_30min_spark_DF)

CPB_30min_spark_DF_newRow = StructType([StructField("CPB_date/time", StringType(), True),StructField("CPB_adjOpen", FloatType(), True),StructField("CPB_adjHigh", FloatType(), True),StructField("CPB_adjLow", FloatType(), True),StructField("CPB_adjClose", FloatType(), True),StructField("CPB_adjVolume", IntegerType(), True)])
CPB_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CPB_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CPB_30min.txt")
display(CPB_30min_spark_DF)

CPRI_30min_spark_DF_newRow = StructType([StructField("CPRI_date/time", StringType(), True),StructField("CPRI_adjOpen", FloatType(), True),StructField("CPRI_adjHigh", FloatType(), True),StructField("CPRI_adjLow", FloatType(), True),StructField("CPRI_adjClose", FloatType(), True),StructField("CPRI_adjVolume", IntegerType(), True)])
CPRI_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CPRI_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CPRI_30min.txt")
display(CPRI_30min_spark_DF)

CPRT_30min_spark_DF_newRow = StructType([StructField("CPRT_date/time", StringType(), True),StructField("CPRT_adjOpen", FloatType(), True),StructField("CPRT_adjHigh", FloatType(), True),StructField("CPRT_adjLow", FloatType(), True),StructField("CPRT_adjClose", FloatType(), True),StructField("CPRT_adjVolume", IntegerType(), True)])
CPRT_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CPRT_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CPRT_30min.txt")
display(CPRT_30min_spark_DF)

CRM_30min_spark_DF_newRow = StructType([StructField("CRM_date/time", StringType(), True),StructField("CRM_adjOpen", FloatType(), True),StructField("CRM_adjHigh", FloatType(), True),StructField("CRM_adjLow", FloatType(), True),StructField("CRM_adjClose", FloatType(), True),StructField("CRM_adjVolume", IntegerType(), True)])
CRM_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CRM_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CRM_30min.txt")
display(CRM_30min_spark_DF)

CSCO_30min_spark_DF_newRow = StructType([StructField("CSCO_date/time", StringType(), True),StructField("CSCO_adjOpen", FloatType(), True),StructField("CSCO_adjHigh", FloatType(), True),StructField("CSCO_adjLow", FloatType(), True),StructField("CSCO_adjClose", FloatType(), True),StructField("CSCO_adjVolume", IntegerType(), True)])
CSCO_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CSCO_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CSCO_30min.txt")
display(CSCO_30min_spark_DF)

CSX_30min_spark_DF_newRow = StructType([StructField("CSX_date/time", StringType(), True),StructField("CSX_adjOpen", FloatType(), True),StructField("CSX_adjHigh", FloatType(), True),StructField("CSX_adjLow", FloatType(), True),StructField("CSX_adjClose", FloatType(), True),StructField("CSX_adjVolume", IntegerType(), True)])
CSX_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CSX_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CSX_30min.txt")
display(CSX_30min_spark_DF)

CTAS_30min_spark_DF_newRow = StructType([StructField("CTAS_date/time", StringType(), True),StructField("CTAS_adjOpen", FloatType(), True),StructField("CTAS_adjHigh", FloatType(), True),StructField("CTAS_adjLow", FloatType(), True),StructField("CTAS_adjClose", FloatType(), True),StructField("CTAS_adjVolume", IntegerType(), True)])
CTAS_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CTAS_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CTAS_30min.txt")
display(CTAS_30min_spark_DF)

CTLT_30min_spark_DF_newRow = StructType([StructField("CTLT_date/time", StringType(), True),StructField("CTLT_adjOpen", FloatType(), True),StructField("CTLT_adjHigh", FloatType(), True),StructField("CTLT_adjLow", FloatType(), True),StructField("CTLT_adjClose", FloatType(), True),StructField("CTLT_adjVolume", IntegerType(), True)])
CTLT_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CTLT_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CTLT_30min.txt")
display(CTLT_30min_spark_DF)

CTSH_30min_spark_DF_newRow = StructType([StructField("CTSH_date/time", StringType(), True),StructField("CTSH_adjOpen", FloatType(), True),StructField("CTSH_adjHigh", FloatType(), True),StructField("CTSH_adjLow", FloatType(), True),StructField("CTSH_adjClose", FloatType(), True),StructField("CTSH_adjVolume", IntegerType(), True)])
CTSH_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CTSH_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CTSH_30min.txt")
display(CTSH_30min_spark_DF)

CTVA_30min_spark_DF_newRow = StructType([StructField("CTVA_date/time", StringType(), True),StructField("CTVA_adjOpen", FloatType(), True),StructField("CTVA_adjHigh", FloatType(), True),StructField("CTVA_adjLow", FloatType(), True),StructField("CTVA_adjClose", FloatType(), True),StructField("CTVA_adjVolume", IntegerType(), True)])
CTVA_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CTVA_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CTVA_30min.txt")
display(CTVA_30min_spark_DF)

CTXS_30min_spark_DF_newRow = StructType([StructField("CTXS_date/time", StringType(), True),StructField("CTXS_adjOpen", FloatType(), True),StructField("CTXS_adjHigh", FloatType(), True),StructField("CTXS_adjLow", FloatType(), True),StructField("CTXS_adjClose", FloatType(), True),StructField("CTXS_adjVolume", IntegerType(), True)])
CTXS_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CTXS_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CTXS_30min.txt")
display(CTXS_30min_spark_DF)

CVS_30min_spark_DF_newRow = StructType([StructField("CVS_date/time", StringType(), True),StructField("CVS_adjOpen", FloatType(), True),StructField("CVS_adjHigh", FloatType(), True),StructField("CVS_adjLow", FloatType(), True),StructField("CVS_adjClose", FloatType(), True),StructField("CVS_adjVolume", IntegerType(), True)])
CVS_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CVS_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CVS_30min.txt")
display(CVS_30min_spark_DF)

CVX_30min_spark_DF_newRow = StructType([StructField("CVX_date/time", StringType(), True),StructField("CVX_adjOpen", FloatType(), True),StructField("CVX_adjHigh", FloatType(), True),StructField("CVX_adjLow", FloatType(), True),StructField("CVX_adjClose", FloatType(), True),StructField("CVX_adjVolume", IntegerType(), True)])
CVX_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CVX_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CVX_30min.txt")
display(CVX_30min_spark_DF)

CZR_30min_spark_DF_newRow = StructType([StructField("CZR_date/time", StringType(), True),StructField("CZR_adjOpen", FloatType(), True),StructField("CZR_adjHigh", FloatType(), True),StructField("CZR_adjLow", FloatType(), True),StructField("CZR_adjClose", FloatType(), True),StructField("CZR_adjVolume", IntegerType(), True)])
CZR_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(CZR_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/CZR_30min.txt")
display(CZR_30min_spark_DF)

C_30min_spark_DF_newRow = StructType([StructField("C_date/time", StringType(), True),StructField("C_adjOpen", FloatType(), True),StructField("C_adjHigh", FloatType(), True),StructField("C_adjLow", FloatType(), True),StructField("C_adjClose", FloatType(), True),StructField("C_adjVolume", IntegerType(), True)])
C_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(C_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/C_30min.txt")
display(C_30min_spark_DF)


DAL_30min_spark_DF_newRow = StructType([StructField("DAL_date/time", StringType(), True),StructField("DAL_adjOpen", FloatType(), True),StructField("DAL_adjHigh", FloatType(), True),StructField("DAL_adjLow", FloatType(), True),StructField("DAL_adjClose", FloatType(), True),StructField("DAL_adjVolume", IntegerType(), True)])
DAL_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DAL_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DAL_30min.txt")
display(DAL_30min_spark_DF)

DAN_30min_spark_DF_newRow = StructType([StructField("DAN_date/time", StringType(), True),StructField("DAN_adjOpen", FloatType(), True),StructField("DAN_adjHigh", FloatType(), True),StructField("DAN_adjLow", FloatType(), True),StructField("DAN_adjClose", FloatType(), True),StructField("DAN_adjVolume", IntegerType(), True)])
DAN_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DAN_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DAN_30min.txt")
display(DAN_30min_spark_DF)

DDS_30min_spark_DF_newRow = StructType([StructField("DDS_date/time", StringType(), True),StructField("DDS_adjOpen", FloatType(), True),StructField("DDS_adjHigh", FloatType(), True),StructField("DDS_adjLow", FloatType(), True),StructField("DDS_adjClose", FloatType(), True),StructField("DDS_adjVolume", IntegerType(), True)])
DDS_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DDS_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DDS_30min.txt")
display(DDS_30min_spark_DF)

DD_30min_spark_DF_newRow = StructType([StructField("DD_date/time", StringType(), True),StructField("DD_adjOpen", FloatType(), True),StructField("DD_adjHigh", FloatType(), True),StructField("DD_adjLow", FloatType(), True),StructField("DD_adjClose", FloatType(), True),StructField("DD_adjVolume", IntegerType(), True)])
DD_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DD_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DD_30min.txt")
display(DD_30min_spark_DF)

DELL_30min_spark_DF_newRow = StructType([StructField("DELL_date/time", StringType(), True),StructField("DELL_adjOpen", FloatType(), True),StructField("DELL_adjHigh", FloatType(), True),StructField("DELL_adjLow", FloatType(), True),StructField("DELL_adjClose", FloatType(), True),StructField("DELL_adjVolume", IntegerType(), True)])
DELL_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DELL_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DELL_30min.txt")
display(DELL_30min_spark_DF)

DE_30min_spark_DF_newRow = StructType([StructField("DE_date/time", StringType(), True),StructField("DE_adjOpen", FloatType(), True),StructField("DE_adjHigh", FloatType(), True),StructField("DE_adjLow", FloatType(), True),StructField("DE_adjClose", FloatType(), True),StructField("DE_adjVolume", IntegerType(), True)])
DE_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DE_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DE_30min.txt")
display(DE_30min_spark_DF)

DFS_30min_spark_DF_newRow = StructType([StructField("DFS_date/time", StringType(), True),StructField("DFS_adjOpen", FloatType(), True),StructField("DFS_adjHigh", FloatType(), True),StructField("DFS_adjLow", FloatType(), True),StructField("DFS_adjClose", FloatType(), True),StructField("DFS_adjVolume", IntegerType(), True)])
DFS_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DFS_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DFS_30min.txt")
display(DFS_30min_spark_DF)

DGX_30min_spark_DF_newRow = StructType([StructField("DGX_date/time", StringType(), True),StructField("DGX_adjOpen", FloatType(), True),StructField("DGX_adjHigh", FloatType(), True),StructField("DGX_adjLow", FloatType(), True),StructField("DGX_adjClose", FloatType(), True),StructField("DGX_adjVolume", IntegerType(), True)])
DGX_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DGX_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DGX_30min.txt")
display(DGX_30min_spark_DF)

DG_30min_spark_DF_newRow = StructType([StructField("DG_date/time", StringType(), True),StructField("DG_adjOpen", FloatType(), True),StructField("DG_adjHigh", FloatType(), True),StructField("DG_adjLow", FloatType(), True),StructField("DG_adjClose", FloatType(), True),StructField("DG_adjVolume", IntegerType(), True)])
DG_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DG_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DG_30min.txt")
display(DG_30min_spark_DF)

DHI_30min_spark_DF_newRow = StructType([StructField("DHI_date/time", StringType(), True),StructField("DHI_adjOpen", FloatType(), True),StructField("DHI_adjHigh", FloatType(), True),StructField("DHI_adjLow", FloatType(), True),StructField("DHI_adjClose", FloatType(), True),StructField("DHI_adjVolume", IntegerType(), True)])
DHI_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DHI_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DHI_30min.txt")
display(DHI_30min_spark_DF)

DHR_30min_spark_DF_newRow = StructType([StructField("DHR_date/time", StringType(), True),StructField("DHR_adjOpen", FloatType(), True),StructField("DHR_adjHigh", FloatType(), True),StructField("DHR_adjLow", FloatType(), True),StructField("DHR_adjClose", FloatType(), True),StructField("DHR_adjVolume", IntegerType(), True)])
DHR_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DHR_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DHR_30min.txt")
display(DHR_30min_spark_DF)

DISCA_30min_spark_DF_newRow = StructType([StructField("DISCA_date/time", StringType(), True),StructField("DISCA_adjOpen", FloatType(), True),StructField("DISCA_adjHigh", FloatType(), True),StructField("DISCA_adjLow", FloatType(), True),StructField("DISCA_adjClose", FloatType(), True),StructField("DISCA_adjVolume", IntegerType(), True)])
DISCA_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DISCA_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DISCA_30min.txt")
display(DISCA_30min_spark_DF)

DISCK_30min_spark_DF_newRow = StructType([StructField("DISCK_date/time", StringType(), True),StructField("DISCK_adjOpen", FloatType(), True),StructField("DISCK_adjHigh", FloatType(), True),StructField("DISCK_adjLow", FloatType(), True),StructField("DISCK_adjClose", FloatType(), True),StructField("DISCK_adjVolume", IntegerType(), True)])
DISCK_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DISCK_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DISCK_30min.txt")
display(DISCK_30min_spark_DF)

DISH_30min_spark_DF_newRow = StructType([StructField("DISH_date/time", StringType(), True),StructField("DISH_adjOpen", FloatType(), True),StructField("DISH_adjHigh", FloatType(), True),StructField("DISH_adjLow", FloatType(), True),StructField("DISH_adjClose", FloatType(), True),StructField("DISH_adjVolume", IntegerType(), True)])
DISH_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DISH_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DISH_30min.txt")
display(DISH_30min_spark_DF)

DIS_30min_spark_DF_newRow = StructType([StructField("DIS_date/time", StringType(), True),StructField("DIS_adjOpen", FloatType(), True),StructField("DIS_adjHigh", FloatType(), True),StructField("DIS_adjLow", FloatType(), True),StructField("DIS_adjClose", FloatType(), True),StructField("DIS_adjVolume", IntegerType(), True)])
DIS_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DIS_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DIS_30min.txt")
display(DIS_30min_spark_DF)

DLR_30min_spark_DF_newRow = StructType([StructField("DLR_date/time", StringType(), True),StructField("DLR_adjOpen", FloatType(), True),StructField("DLR_adjHigh", FloatType(), True),StructField("DLR_adjLow", FloatType(), True),StructField("DLR_adjClose", FloatType(), True),StructField("DLR_adjVolume", IntegerType(), True)])
DLR_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DLR_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DLR_30min.txt")
display(DLR_30min_spark_DF)

DLTR_30min_spark_DF_newRow = StructType([StructField("DLTR_date/time", StringType(), True),StructField("DLTR_adjOpen", FloatType(), True),StructField("DLTR_adjHigh", FloatType(), True),StructField("DLTR_adjLow", FloatType(), True),StructField("DLTR_adjClose", FloatType(), True),StructField("DLTR_adjVolume", IntegerType(), True)])
DLTR_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DLTR_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DLTR_30min.txt")
display(DLTR_30min_spark_DF)

DLX_30min_spark_DF_newRow = StructType([StructField("DLX_date/time", StringType(), True),StructField("DLX_adjOpen", FloatType(), True),StructField("DLX_adjHigh", FloatType(), True),StructField("DLX_adjLow", FloatType(), True),StructField("DLX_adjClose", FloatType(), True),StructField("DLX_adjVolume", IntegerType(), True)])
DLX_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DLX_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DLX_30min.txt")
display(DLX_30min_spark_DF)

DNB_30min_spark_DF_newRow = StructType([StructField("DNB_date/time", StringType(), True),StructField("DNB_adjOpen", FloatType(), True),StructField("DNB_adjHigh", FloatType(), True),StructField("DNB_adjLow", FloatType(), True),StructField("DNB_adjClose", FloatType(), True),StructField("DNB_adjVolume", IntegerType(), True)])
DNB_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DNB_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DNB_30min.txt")
display(DNB_30min_spark_DF)

DOV_30min_spark_DF_newRow = StructType([StructField("DOV_date/time", StringType(), True),StructField("DOV_adjOpen", FloatType(), True),StructField("DOV_adjHigh", FloatType(), True),StructField("DOV_adjLow", FloatType(), True),StructField("DOV_adjClose", FloatType(), True),StructField("DOV_adjVolume", IntegerType(), True)])
DOV_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DOV_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DOV_30min.txt")
display(DOV_30min_spark_DF)

DOW_30min_spark_DF_newRow = StructType([StructField("DOW_date/time", StringType(), True),StructField("DOW_adjOpen", FloatType(), True),StructField("DOW_adjHigh", FloatType(), True),StructField("DOW_adjLow", FloatType(), True),StructField("DOW_adjClose", FloatType(), True),StructField("DOW_adjVolume", IntegerType(), True)])
DOW_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DOW_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DOW_30min.txt")
display(DOW_30min_spark_DF)

DPZ_30min_spark_DF_newRow = StructType([StructField("DPZ_date/time", StringType(), True),StructField("DPZ_adjOpen", FloatType(), True),StructField("DPZ_adjHigh", FloatType(), True),StructField("DPZ_adjLow", FloatType(), True),StructField("DPZ_adjClose", FloatType(), True),StructField("DPZ_adjVolume", IntegerType(), True)])
DPZ_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DPZ_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DPZ_30min.txt")
display(DPZ_30min_spark_DF)

DRE_30min_spark_DF_newRow = StructType([StructField("DRE_date/time", StringType(), True),StructField("DRE_adjOpen", FloatType(), True),StructField("DRE_adjHigh", FloatType(), True),StructField("DRE_adjLow", FloatType(), True),StructField("DRE_adjClose", FloatType(), True),StructField("DRE_adjVolume", IntegerType(), True)])
DRE_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DRE_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DRE_30min.txt")
display(DRE_30min_spark_DF)

DRI_30min_spark_DF_newRow = StructType([StructField("DRI_date/time", StringType(), True),StructField("DRI_adjOpen", FloatType(), True),StructField("DRI_adjHigh", FloatType(), True),StructField("DRI_adjLow", FloatType(), True),StructField("DRI_adjClose", FloatType(), True),StructField("DRI_adjVolume", IntegerType(), True)])
DRI_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DRI_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DRI_30min.txt")
display(DRI_30min_spark_DF)

DTE_30min_spark_DF_newRow = StructType([StructField("DTE_date/time", StringType(), True),StructField("DTE_adjOpen", FloatType(), True),StructField("DTE_adjHigh", FloatType(), True),StructField("DTE_adjLow", FloatType(), True),StructField("DTE_adjClose", FloatType(), True),StructField("DTE_adjVolume", IntegerType(), True)])
DTE_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DTE_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DTE_30min.txt")
display(DTE_30min_spark_DF)

DUK_30min_spark_DF_newRow = StructType([StructField("DUK_date/time", StringType(), True),StructField("DUK_adjOpen", FloatType(), True),StructField("DUK_adjHigh", FloatType(), True),StructField("DUK_adjLow", FloatType(), True),StructField("DUK_adjClose", FloatType(), True),StructField("DUK_adjVolume", IntegerType(), True)])
DUK_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DUK_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DUK_30min.txt")
display(DUK_30min_spark_DF)

DVA_30min_spark_DF_newRow = StructType([StructField("DVA_date/time", StringType(), True),StructField("DVA_adjOpen", FloatType(), True),StructField("DVA_adjHigh", FloatType(), True),StructField("DVA_adjLow", FloatType(), True),StructField("DVA_adjClose", FloatType(), True),StructField("DVA_adjVolume", IntegerType(), True)])
DVA_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DVA_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DVA_30min.txt")
display(DVA_30min_spark_DF)

DVN_30min_spark_DF_newRow = StructType([StructField("DVN_date/time", StringType(), True),StructField("DVN_adjOpen", FloatType(), True),StructField("DVN_adjHigh", FloatType(), True),StructField("DVN_adjLow", FloatType(), True),StructField("DVN_adjClose", FloatType(), True),StructField("DVN_adjVolume", IntegerType(), True)])
DVN_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DVN_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DVN_30min.txt")
display(DVN_30min_spark_DF)

DXCM_30min_spark_DF_newRow = StructType([StructField("DXCM_date/time", StringType(), True),StructField("DXCM_adjOpen", FloatType(), True),StructField("DXCM_adjHigh", FloatType(), True),StructField("DXCM_adjLow", FloatType(), True),StructField("DXCM_adjClose", FloatType(), True),StructField("DXCM_adjVolume", IntegerType(), True)])
DXCM_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DXCM_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DXCM_30min.txt")
display(DXCM_30min_spark_DF)

DXC_30min_spark_DF_newRow = StructType([StructField("DXC_date/time", StringType(), True),StructField("DXC_adjOpen", FloatType(), True),StructField("DXC_adjHigh", FloatType(), True),StructField("DXC_adjLow", FloatType(), True),StructField("DXC_adjClose", FloatType(), True),StructField("DXC_adjVolume", IntegerType(), True)])
DXC_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(DXC_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/DXC_30min.txt")
display(DXC_30min_spark_DF)

D_30min_spark_DF_newRow = StructType([StructField("D_date/time", StringType(), True),StructField("D_adjOpen", FloatType(), True),StructField("D_adjHigh", FloatType(), True),StructField("D_adjLow", FloatType(), True),StructField("D_adjClose", FloatType(), True),StructField("D_adjVolume", IntegerType(), True)])
D_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(D_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/D_30min.txt")
display(D_30min_spark_DF)



EA_30min_spark_DF_newRow = StructType([StructField("EA_date/time", StringType(), True),StructField("EA_adjOpen", FloatType(), True),StructField("EA_adjHigh", FloatType(), True),StructField("EA_adjLow", FloatType(), True),StructField("EA_adjClose", FloatType(), True),StructField("EA_adjVolume", IntegerType(), True)])
EA_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(EA_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/EA_30min.txt")
display(EA_30min_spark_DF)

EBAY_30min_spark_DF_newRow = StructType([StructField("EBAY_date/time", StringType(), True),StructField("EBAY_adjOpen", FloatType(), True),StructField("EBAY_adjHigh", FloatType(), True),StructField("EBAY_adjLow", FloatType(), True),StructField("EBAY_adjClose", FloatType(), True),StructField("EBAY_adjVolume", IntegerType(), True)])
EBAY_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(EBAY_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/EBAY_30min.txt")
display(EBAY_30min_spark_DF)

ECL_30min_spark_DF_newRow = StructType([StructField("ECL_date/time", StringType(), True),StructField("ECL_adjOpen", FloatType(), True),StructField("ECL_adjHigh", FloatType(), True),StructField("ECL_adjLow", FloatType(), True),StructField("ECL_adjClose", FloatType(), True),StructField("ECL_adjVolume", IntegerType(), True)])
ECL_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ECL_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ECL_30min.txt")
display(ECL_30min_spark_DF)

ED_30min_spark_DF_newRow = StructType([StructField("ED_date/time", StringType(), True),StructField("ED_adjOpen", FloatType(), True),StructField("ED_adjHigh", FloatType(), True),StructField("ED_adjLow", FloatType(), True),StructField("ED_adjClose", FloatType(), True),StructField("ED_adjVolume", IntegerType(), True)])
ED_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ED_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ED_30min.txt")
display(ED_30min_spark_DF)

EFX_30min_spark_DF_newRow = StructType([StructField("EFX_date/time", StringType(), True),StructField("EFX_adjOpen", FloatType(), True),StructField("EFX_adjHigh", FloatType(), True),StructField("EFX_adjLow", FloatType(), True),StructField("EFX_adjClose", FloatType(), True),StructField("EFX_adjVolume", IntegerType(), True)])
EFX_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(EFX_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/EFX_30min.txt")
display(EFX_30min_spark_DF)

EIX_30min_spark_DF_newRow = StructType([StructField("EIX_date/time", StringType(), True),StructField("EIX_adjOpen", FloatType(), True),StructField("EIX_adjHigh", FloatType(), True),StructField("EIX_adjLow", FloatType(), True),StructField("EIX_adjClose", FloatType(), True),StructField("EIX_adjVolume", IntegerType(), True)])
EIX_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(EIX_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/EIX_30min.txt")
display(EIX_30min_spark_DF)

EL_30min_spark_DF_newRow = StructType([StructField("EL_date/time", StringType(), True),StructField("EL_adjOpen", FloatType(), True),StructField("EL_adjHigh", FloatType(), True),StructField("EL_adjLow", FloatType(), True),StructField("EL_adjClose", FloatType(), True),StructField("EL_adjVolume", IntegerType(), True)])
EL_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(EL_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/EL_30min.txt")
display(EL_30min_spark_DF)

EMN_30min_spark_DF_newRow = StructType([StructField("EMN_date/time", StringType(), True),StructField("EMN_adjOpen", FloatType(), True),StructField("EMN_adjHigh", FloatType(), True),StructField("EMN_adjLow", FloatType(), True),StructField("EMN_adjClose", FloatType(), True),StructField("EMN_adjVolume", IntegerType(), True)])
EMN_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(EMN_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/EMN_30min.txt")
display(EMN_30min_spark_DF)

EMR_30min_spark_DF_newRow = StructType([StructField("EMR_date/time", StringType(), True),StructField("EMR_adjOpen", FloatType(), True),StructField("EMR_adjHigh", FloatType(), True),StructField("EMR_adjLow", FloatType(), True),StructField("EMR_adjClose", FloatType(), True),StructField("EMR_adjVolume", IntegerType(), True)])
EMR_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(EMR_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/EMR_30min.txt")
display(EMR_30min_spark_DF)

ENDP_30min_spark_DF_newRow = StructType([StructField("ENDP_date/time", StringType(), True),StructField("ENDP_adjOpen", FloatType(), True),StructField("ENDP_adjHigh", FloatType(), True),StructField("ENDP_adjLow", FloatType(), True),StructField("ENDP_adjClose", FloatType(), True),StructField("ENDP_adjVolume", IntegerType(), True)])
ENDP_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ENDP_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ENDP_30min.txt")
display(ENDP_30min_spark_DF)

ENPH_30min_spark_DF_newRow = StructType([StructField("ENPH_date/time", StringType(), True),StructField("ENPH_adjOpen", FloatType(), True),StructField("ENPH_adjHigh", FloatType(), True),StructField("ENPH_adjLow", FloatType(), True),StructField("ENPH_adjClose", FloatType(), True),StructField("ENPH_adjVolume", IntegerType(), True)])
ENPH_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ENPH_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ENPH_30min.txt")
display(ENPH_30min_spark_DF)

EOG_30min_spark_DF_newRow = StructType([StructField("EOG_date/time", StringType(), True),StructField("EOG_adjOpen", FloatType(), True),StructField("EOG_adjHigh", FloatType(), True),StructField("EOG_adjLow", FloatType(), True),StructField("EOG_adjClose", FloatType(), True),StructField("EOG_adjVolume", IntegerType(), True)])
EOG_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(EOG_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/EOG_30min.txt")
display(EOG_30min_spark_DF)

EPAM_30min_spark_DF_newRow = StructType([StructField("EPAM_date/time", StringType(), True),StructField("EPAM_adjOpen", FloatType(), True),StructField("EPAM_adjHigh", FloatType(), True),StructField("EPAM_adjLow", FloatType(), True),StructField("EPAM_adjClose", FloatType(), True),StructField("EPAM_adjVolume", IntegerType(), True)])
EPAM_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(EPAM_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/EPAM_30min.txt")
display(EPAM_30min_spark_DF)

EQIX_30min_spark_DF_newRow = StructType([StructField("EQIX_date/time", StringType(), True),StructField("EQIX_adjOpen", FloatType(), True),StructField("EQIX_adjHigh", FloatType(), True),StructField("EQIX_adjLow", FloatType(), True),StructField("EQIX_adjClose", FloatType(), True),StructField("EQIX_adjVolume", IntegerType(), True)])
EQIX_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(EQIX_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/EQIX_30min.txt")
display(EQIX_30min_spark_DF)

EQR_30min_spark_DF_newRow = StructType([StructField("EQR_date/time", StringType(), True),StructField("EQR_adjOpen", FloatType(), True),StructField("EQR_adjHigh", FloatType(), True),StructField("EQR_adjLow", FloatType(), True),StructField("EQR_adjClose", FloatType(), True),StructField("EQR_adjVolume", IntegerType(), True)])
EQR_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(EQR_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/EQR_30min.txt")
display(EQR_30min_spark_DF)

EQT_30min_spark_DF_newRow = StructType([StructField("EQT_date/time", StringType(), True),StructField("EQT_adjOpen", FloatType(), True),StructField("EQT_adjHigh", FloatType(), True),StructField("EQT_adjLow", FloatType(), True),StructField("EQT_adjClose", FloatType(), True),StructField("EQT_adjVolume", IntegerType(), True)])
EQT_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(EQT_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/EQT_30min.txt")
display(EQT_30min_spark_DF)

EQ_30min_spark_DF_newRow = StructType([StructField("EQ_date/time", StringType(), True),StructField("EQ_adjOpen", FloatType(), True),StructField("EQ_adjHigh", FloatType(), True),StructField("EQ_adjLow", FloatType(), True),StructField("EQ_adjClose", FloatType(), True),StructField("EQ_adjVolume", IntegerType(), True)])
EQ_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(EQ_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/EQ_30min.txt")
display(EQ_30min_spark_DF)

ESS_30min_spark_DF_newRow = StructType([StructField("ESS_date/time", StringType(), True),StructField("ESS_adjOpen", FloatType(), True),StructField("ESS_adjHigh", FloatType(), True),StructField("ESS_adjLow", FloatType(), True),StructField("ESS_adjClose", FloatType(), True),StructField("ESS_adjVolume", IntegerType(), True)])
ESS_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ESS_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ESS_30min.txt")
display(ESS_30min_spark_DF)

ES_30min_spark_DF_newRow = StructType([StructField("ES_date/time", StringType(), True),StructField("ES_adjOpen", FloatType(), True),StructField("ES_adjHigh", FloatType(), True),StructField("ES_adjLow", FloatType(), True),StructField("ES_adjClose", FloatType(), True),StructField("ES_adjVolume", IntegerType(), True)])
ES_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ES_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ES_30min.txt")
display(ES_30min_spark_DF)

ETN_30min_spark_DF_newRow = StructType([StructField("ETN_date/time", StringType(), True),StructField("ETN_adjOpen", FloatType(), True),StructField("ETN_adjHigh", FloatType(), True),StructField("ETN_adjLow", FloatType(), True),StructField("ETN_adjClose", FloatType(), True),StructField("ETN_adjVolume", IntegerType(), True)])
ETN_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ETN_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ETN_30min.txt")
display(ETN_30min_spark_DF)

ETR_30min_spark_DF_newRow = StructType([StructField("ETR_date/time", StringType(), True),StructField("ETR_adjOpen", FloatType(), True),StructField("ETR_adjHigh", FloatType(), True),StructField("ETR_adjLow", FloatType(), True),StructField("ETR_adjClose", FloatType(), True),StructField("ETR_adjVolume", IntegerType(), True)])
ETR_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ETR_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ETR_30min.txt")
display(ETR_30min_spark_DF)

ETSY_30min_spark_DF_newRow = StructType([StructField("ETSY_date/time", StringType(), True),StructField("ETSY_adjOpen", FloatType(), True),StructField("ETSY_adjHigh", FloatType(), True),StructField("ETSY_adjLow", FloatType(), True),StructField("ETSY_adjClose", FloatType(), True),StructField("ETSY_adjVolume", IntegerType(), True)])
ETSY_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ETSY_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/ETSY_30min.txt")
display(ETSY_30min_spark_DF)

EVRG_30min_spark_DF_newRow = StructType([StructField("EVRG_date/time", StringType(), True),StructField("EVRG_adjOpen", FloatType(), True),StructField("EVRG_adjHigh", FloatType(), True),StructField("EVRG_adjLow", FloatType(), True),StructField("EVRG_adjClose", FloatType(), True),StructField("EVRG_adjVolume", IntegerType(), True)])
EVRG_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(EVRG_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/EVRG_30min.txt")
display(EVRG_30min_spark_DF)

EW_30min_spark_DF_newRow = StructType([StructField("EW_date/time", StringType(), True),StructField("EW_adjOpen", FloatType(), True),StructField("EW_adjHigh", FloatType(), True),StructField("EW_adjLow", FloatType(), True),StructField("EW_adjClose", FloatType(), True),StructField("EW_adjVolume", IntegerType(), True)])
EW_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(EW_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/EW_30min.txt")
display(EW_30min_spark_DF)

EXC_30min_spark_DF_newRow = StructType([StructField("EXC_date/time", StringType(), True),StructField("EXC_adjOpen", FloatType(), True),StructField("EXC_adjHigh", FloatType(), True),StructField("EXC_adjLow", FloatType(), True),StructField("EXC_adjClose", FloatType(), True),StructField("EXC_adjVolume", IntegerType(), True)])
EXC_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(EXC_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/EXC_30min.txt")
display(EXC_30min_spark_DF)

EXPD_30min_spark_DF_newRow = StructType([StructField("EXPD_date/time", StringType(), True),StructField("EXPD_adjOpen", FloatType(), True),StructField("EXPD_adjHigh", FloatType(), True),StructField("EXPD_adjLow", FloatType(), True),StructField("EXPD_adjClose", FloatType(), True),StructField("EXPD_adjVolume", IntegerType(), True)])
EXPD_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(EXPD_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/EXPD_30min.txt")
display(EXPD_30min_spark_DF)

EXPE_30min_spark_DF_newRow = StructType([StructField("EXPE_date/time", StringType(), True),StructField("EXPE_adjOpen", FloatType(), True),StructField("EXPE_adjHigh", FloatType(), True),StructField("EXPE_adjLow", FloatType(), True),StructField("EXPE_adjClose", FloatType(), True),StructField("EXPE_adjVolume", IntegerType(), True)])
EXPE_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(EXPE_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/EXPE_30min.txt")
display(EXPE_30min_spark_DF)

EXR_30min_spark_DF_newRow = StructType([StructField("EXR_date/time", StringType(), True),StructField("EXR_adjOpen", FloatType(), True),StructField("EXR_adjHigh", FloatType(), True),StructField("EXR_adjLow", FloatType(), True),StructField("EXR_adjClose", FloatType(), True),StructField("EXR_adjVolume", IntegerType(), True)])
EXR_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(EXR_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/EXR_30min.txt")
display(EXR_30min_spark_DF)

FANG_30min_spark_DF_newRow = StructType([StructField("FANG_date/time", StringType(), True),StructField("FANG_adjOpen", FloatType(), True),StructField("FANG_adjHigh", FloatType(), True),StructField("FANG_adjLow", FloatType(), True),StructField("FANG_adjClose", FloatType(), True),StructField("FANG_adjVolume", IntegerType(), True)])
FANG_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(FANG_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/FANG_30min.txt")
display(FANG_30min_spark_DF)

FAST_30min_spark_DF_newRow = StructType([StructField("FAST_date/time", StringType(), True),StructField("FAST_adjOpen", FloatType(), True),StructField("FAST_adjHigh", FloatType(), True),StructField("FAST_adjLow", FloatType(), True),StructField("FAST_adjClose", FloatType(), True),StructField("FAST_adjVolume", IntegerType(), True)])
FAST_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(FAST_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/FAST_30min.txt")
display(FAST_30min_spark_DF)

FBHS_30min_spark_DF_newRow = StructType([StructField("FBHS_date/time", StringType(), True),StructField("FBHS_adjOpen", FloatType(), True),StructField("FBHS_adjHigh", FloatType(), True),StructField("FBHS_adjLow", FloatType(), True),StructField("FBHS_adjClose", FloatType(), True),StructField("FBHS_adjVolume", IntegerType(), True)])
FBHS_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(FBHS_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/FBHS_30min.txt")
display(FBHS_30min_spark_DF)

FB_30min_spark_DF_newRow = StructType([StructField("FB_date/time", StringType(), True),StructField("FB_adjOpen", FloatType(), True),StructField("FB_adjHigh", FloatType(), True),StructField("FB_adjLow", FloatType(), True),StructField("FB_adjClose", FloatType(), True),StructField("FB_adjVolume", IntegerType(), True)])
FB_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(FB_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/FB_30min.txt")
display(FB_30min_spark_DF)

FCX_30min_spark_DF_newRow = StructType([StructField("FCX_date/time", StringType(), True),StructField("FCX_adjOpen", FloatType(), True),StructField("FCX_adjHigh", FloatType(), True),StructField("FCX_adjLow", FloatType(), True),StructField("FCX_adjClose", FloatType(), True),StructField("FCX_adjVolume", IntegerType(), True)])
FCX_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(FCX_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/FCX_30min.txt")
display(FCX_30min_spark_DF)

FDS_30min_spark_DF_newRow = StructType([StructField("FDS_date/time", StringType(), True),StructField("FDS_adjOpen", FloatType(), True),StructField("FDS_adjHigh", FloatType(), True),StructField("FDS_adjLow", FloatType(), True),StructField("FDS_adjClose", FloatType(), True),StructField("FDS_adjVolume", IntegerType(), True)])
FDS_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(FDS_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/FDS_30min.txt")
display(FDS_30min_spark_DF)

FDX_30min_spark_DF_newRow = StructType([StructField("FDX_date/time", StringType(), True),StructField("FDX_adjOpen", FloatType(), True),StructField("FDX_adjHigh", FloatType(), True),StructField("FDX_adjLow", FloatType(), True),StructField("FDX_adjClose", FloatType(), True),StructField("FDX_adjVolume", IntegerType(), True)])
FDX_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(FDX_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/FDX_30min.txt")
display(FDX_30min_spark_DF)

FE_30min_spark_DF_newRow = StructType([StructField("FE_date/time", StringType(), True),StructField("FE_adjOpen", FloatType(), True),StructField("FE_adjHigh", FloatType(), True),StructField("FE_adjLow", FloatType(), True),StructField("FE_adjClose", FloatType(), True),StructField("FE_adjVolume", IntegerType(), True)])
FE_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(FE_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/FE_30min.txt")
display(FE_30min_spark_DF)

FFIV_30min_spark_DF_newRow = StructType([StructField("FFIV_date/time", StringType(), True),StructField("FFIV_adjOpen", FloatType(), True),StructField("FFIV_adjHigh", FloatType(), True),StructField("FFIV_adjLow", FloatType(), True),StructField("FFIV_adjClose", FloatType(), True),StructField("FFIV_adjVolume", IntegerType(), True)])
FFIV_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(FFIV_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/FFIV_30min.txt")
display(FFIV_30min_spark_DF)

FHN_30min_spark_DF_newRow = StructType([StructField("FHN_date/time", StringType(), True),StructField("FHN_adjOpen", FloatType(), True),StructField("FHN_adjHigh", FloatType(), True),StructField("FHN_adjLow", FloatType(), True),StructField("FHN_adjClose", FloatType(), True),StructField("FHN_adjVolume", IntegerType(), True)])
FHN_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(FHN_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/FHN_30min.txt")
display(FHN_30min_spark_DF)

FISV_30min_spark_DF_newRow = StructType([StructField("FISV_date/time", StringType(), True),StructField("FISV_adjOpen", FloatType(), True),StructField("FISV_adjHigh", FloatType(), True),StructField("FISV_adjLow", FloatType(), True),StructField("FISV_adjClose", FloatType(), True),StructField("FISV_adjVolume", IntegerType(), True)])
FISV_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(FISV_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/FISV_30min.txt")
display(FISV_30min_spark_DF)

FIS_30min_spark_DF_newRow = StructType([StructField("FIS_date/time", StringType(), True),StructField("FIS_adjOpen", FloatType(), True),StructField("FIS_adjHigh", FloatType(), True),StructField("FIS_adjLow", FloatType(), True),StructField("FIS_adjClose", FloatType(), True),StructField("FIS_adjVolume", IntegerType(), True)])
FIS_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(FIS_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/FIS_30min.txt")
display(FIS_30min_spark_DF)

FITB_30min_spark_DF_newRow = StructType([StructField("FITB_date/time", StringType(), True),StructField("FITB_adjOpen", FloatType(), True),StructField("FITB_adjHigh", FloatType(), True),StructField("FITB_adjLow", FloatType(), True),StructField("FITB_adjClose", FloatType(), True),StructField("FITB_adjVolume", IntegerType(), True)])
FITB_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(FITB_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/FITB_30min.txt")
display(FITB_30min_spark_DF)

FLEX_30min_spark_DF_newRow = StructType([StructField("FLEX_date/time", StringType(), True),StructField("FLEX_adjOpen", FloatType(), True),StructField("FLEX_adjHigh", FloatType(), True),StructField("FLEX_adjLow", FloatType(), True),StructField("FLEX_adjClose", FloatType(), True),StructField("FLEX_adjVolume", IntegerType(), True)])
FLEX_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(FLEX_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/FLEX_30min.txt")
display(FLEX_30min_spark_DF)

FLR_30min_spark_DF_newRow = StructType([StructField("FITB_date/time", StringType(), True),StructField("FITB_adjOpen", FloatType(), True),StructField("FITB_adjHigh", FloatType(), True),StructField("FITB_adjLow", FloatType(), True),StructField("FITB_adjClose", FloatType(), True),StructField("FITB_adjVolume", IntegerType(), True)])
FITB_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(FITB_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/FITB_30min.txt")
display(FITB_30min_spark_DF)

FLS_30min_spark_DF_newRow = StructType([StructField("FLS_date/time", StringType(), True),StructField("FLS_adjOpen", FloatType(), True),StructField("FLS_adjHigh", FloatType(), True),StructField("FLS_adjLow", FloatType(), True),StructField("FLS_adjClose", FloatType(), True),StructField("FLS_adjVolume", IntegerType(), True)])
FLS_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(FLS_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/FLS_30min.txt")
display(FLS_30min_spark_DF)
