# Databricks notebook source
# MAGIC %run /Workspace/Repos/yubin.park@mimilabs.ai/mimi-common-utils/download_utils

# COMMAND ----------

volumepath = "/Volumes/mimi_ws_1/healthit/src/hospital_tefca/"

# COMMAND ----------

download_file_like_browser("https://www.healthit.gov/sites/default/files/2025-08/hospital-TEFCA-Network-participation.csv", volumepath, "hospital-TEFCA-Network-participation-2025-08.csv")

# COMMAND ----------


