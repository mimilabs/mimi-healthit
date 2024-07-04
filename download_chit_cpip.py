# Databricks notebook source
# MAGIC %run /Workspace/Repos/yubin.park@mimilabs.ai/mimi-common-utils/download_utils

# COMMAND ----------

urls = [
    "https://media.githubusercontent.com/media/onc-healthit/onc-open-data/main/puf/2019/clinician-certified-technology-pi-2019-1.csv",
    "https://media.githubusercontent.com/media/onc-healthit/onc-open-data/main/puf/2019/clinician-certified-technology-pi-2019-2.csv",
    "https://media.githubusercontent.com/media/onc-healthit/onc-open-data/main/puf/2019/clinician-certified-technology-pi-2019-3.csv",
    "https://media.githubusercontent.com/media/onc-healthit/onc-open-data/main/puf/2020/clinician-certified-technology-pi-2020-1.csv",
    "https://media.githubusercontent.com/media/onc-healthit/onc-open-data/main/puf/2020/clinician-certified-technology-pi-2020-2.csv",
    "https://media.githubusercontent.com/media/onc-healthit/onc-open-data/main/puf/2020/clinician-certified-technology-pi-2020-3.csv",
    "https://media.githubusercontent.com/media/onc-healthit/onc-open-data/main/puf/2021/clinician-certified-technology-pi-2021-1.csv",
    "https://media.githubusercontent.com/media/onc-healthit/onc-open-data/main/puf/2021/clinician-certified-technology-pi-2021-2.csv",
    "https://media.githubusercontent.com/media/onc-healthit/onc-open-data/main/puf/2021/clinician-certified-technology-pi-2021-3.csv",
    "https://media.githubusercontent.com/media/onc-healthit/onc-open-data/main/puf/2021/clinician-certified-technology-pi-2021-4.csv",
    "https://media.githubusercontent.com/media/onc-healthit/onc-open-data/main/puf/2022/clinician-certified-technology-pi-2022-1.csv",
    "https://media.githubusercontent.com/media/onc-healthit/onc-open-data/main/puf/2022/clinician-certified-technology-pi-2022-2.csv",
    "https://media.githubusercontent.com/media/onc-healthit/onc-open-data/main/puf/2022/clinician-certified-technology-pi-2022-3.csv",
    "https://media.githubusercontent.com/media/onc-healthit/onc-open-data/main/puf/2022/clinician-certified-technology-pi-2022-4.csv",    
]

# COMMAND ----------

download_files(urls, "/Volumes/mimi_ws_1/healthit/src/chit_cpip/")
