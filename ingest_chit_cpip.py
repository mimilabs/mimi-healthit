# Databricks notebook source
# MAGIC %run /Workspace/Repos/yubin.park@mimilabs.ai/mimi-common-utils/ingestion_utils

# COMMAND ----------

import pyspark.sql.functions as f

# COMMAND ----------

files = sorted([file for file in Path("/Volumes/mimi_ws_1/healthit/src/chit_cpip").glob("*")], reverse=True)

# COMMAND ----------

for file in files:
    mimi_src_file_date = parse(f"{file.stem[-6:-2]}-12-31").date()
    mimi_src_file_name = file.name
    mimi_dlt_load_date = datetime.today().date()
    df = spark.createDataFrame((pd.read_csv(file, dtype={'practice_size': int, 
                                                         'provider_key': str, 
                                                         'npi': str, 
                                                         'grp_key': str, 
                                                         'product_id': str,
                                                         'edition': str})))
    df = (df.withColumn("mimi_src_file_date", f.lit(mimi_src_file_date))
          .withColumn("mimi_src_file_name", f.lit(mimi_src_file_name))
          .withColumn("mimi_dlt_load_date", f.lit(mimi_dlt_load_date)))
    (df.write.format("delta")
        .mode("overwrite")
        .option('replaceWhere', f"mimi_src_file_name = '{mimi_src_file_name}'")
        .saveAsTable("mimi_ws_1.healthit.chit_cpip"))   

# COMMAND ----------


