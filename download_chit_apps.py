# Databricks notebook source
# MAGIC %run /Workspace/Repos/yubin.park@mimilabs.ai/mimi-common-utils/download_utils

# COMMAND ----------

volumepath = "/Volumes/mimi_ws_1/healthit/src/chit_apps/"

# COMMAND ----------

download_file_like_browser("https://www.healthit.gov/sites/default/files/2025-08/ecosystem-apps-software-marketplace-history.csv", volumepath, "ecosystem-apps-software-marketplace-history-2025-08.csv")

# COMMAND ----------


