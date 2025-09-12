# Databricks notebook source
# MAGIC %run /Workspace/Repos/yubin.park@mimilabs.ai/mimi-common-utils/ingestion_utils

# COMMAND ----------

import pyspark.sql.functions as f

# COMMAND ----------

files = sorted([file for file in Path("/Volumes/mimi_ws_1/healthit/src/hospital_tefca/").glob("*")], reverse=True)

# COMMAND ----------

pd.read_csv(files[0], dtype=str).display()

# COMMAND ----------

for file in files:
    mimi_src_file_date = parse(f"{file.stem[-7:]}-01").date()
    mimi_src_file_name = file.name
    mimi_dlt_load_date = datetime.today().date()
    pdf = pd.read_csv(file, dtype=str)
    pdf['year'] = pdf['year'].astype(int)
    pdf['mimi_src_file_date'] = mimi_src_file_date
    pdf['mimi_src_file_name'] = mimi_src_file_name
    pdf['mimi_dlt_load_date'] = mimi_dlt_load_date
    df = spark.createDataFrame(pdf)
    (
        df.write.format("delta")
        .mode("overwrite")
        .option('replaceWhere', f"mimi_src_file_name = '{mimi_src_file_name}'")
        .saveAsTable("mimi_ws_1.healthit.hospital_tefca_participation")
    )

# COMMAND ----------

# MAGIC %sql
# MAGIC COMMENT ON TABLE mimi_ws_1.healthit.hospital_tefca_participation IS '# [US Hospital Participation in Health Information Networks](https://www.healthit.gov/data/datasets/hospital-network-participation) | resolution: hospital, interval: yearly
# MAGIC
# MAGIC Hospitals’ ability to seamlessly exchange patient health information across the care continuum is critical to ensuring clinicians have access to the information they need for clinical decision-making and care coordination. Hospitals use various methods for exchange, and increasingly rely on various health information networks such as state, regional, and local health information exchange organizations (HIOs), prominent national health information exchange networks (national networks) that connect healthcare providers, HIOs, public health authorities, and payers, and electronic health record (EHR) vendor networks to support clinical information exchange. 
# MAGIC
# MAGIC Beginning in late 2023, hospitals also had the option to participate in the Trusted Exchange Framework and Common Agreement™ (TEFCA™), a nationwide interoperability framework designed to connect these various health information networks with a set of baseline policy and technical requirements to promote secure, nationwide information sharing. TEFCA enables exchange between networks to help limit the need for hospitals to join multiple networks to be able to exchange. 
# MAGIC
# MAGIC This dataset provides information on hospitals’ participation in health information networks—HIOs, national networks, and EHR vendor networks—as well as current and planned participation in TEFCA using the latest available data from the last 3 waves of the American Hospital Association (AHA) Information Technology (IT) Supplement Survey. 
# MAGIC '

# COMMAND ----------


