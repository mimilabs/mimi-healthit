# Databricks notebook source
# MAGIC %run /Workspace/Repos/yubin.park@mimilabs.ai/mimi-common-utils/download_utils

# COMMAND ----------

volumepath = "/Volumes/mimi_ws_1/healthit/src/chit_hpip/"

# COMMAND ----------

download_file_like_browser("https://www.healthit.gov/sites/default/files/2025-05/hospital-promoting-interoperability-2023-chpl-linkage.csv", volumepath, "hospital-promoting-interoperability-2023-chpl-linkage-2025-05.csv")

# COMMAND ----------


