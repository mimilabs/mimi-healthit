# Databricks notebook source
# MAGIC %run /Workspace/Repos/yubin.park@mimilabs.ai/mimi-common-utils/ingestion_utils

# COMMAND ----------

import pyspark.sql.functions as f

# COMMAND ----------

files = sorted([file for file in Path("/Volumes/mimi_ws_1/healthit/src/chit_hpip/").glob("*")], reverse=True)

# COMMAND ----------

for file in files:
    mimi_src_file_date = parse(f"{file.stem[-7:]}-01").date()
    mimi_src_file_name = file.name
    mimi_dlt_load_date = datetime.today().date()
    pdf = pd.read_csv(file, dtype=str)
    pdf.columns = change_header(pdf.columns)
    pdf.rename(columns={'meetscriteriaforpromotinginteroperabilityofeh_rs':
        'meet_criteria_for_promoting_interoperability_of_ehrs'},
            inplace=True)
    pdf['start_date'] = pd.to_datetime(pdf['start_date'], format='%m/%d/%Y').dt.date
    pdf['end_date'] = pd.to_datetime(pdf['end_date'], format='%m/%d/%Y').dt.date
    pdf['mimi_src_file_date'] = mimi_src_file_date
    pdf['mimi_src_file_name'] = mimi_src_file_name
    pdf['mimi_dlt_load_date'] = mimi_dlt_load_date
    df = spark.createDataFrame(pdf)
    (
        df.write.format("delta")
        .mode("overwrite")
        .option('replaceWhere', f"mimi_src_file_name = '{mimi_src_file_name}'")
        .saveAsTable("mimi_ws_1.healthit.chit_hpip")
    )

# COMMAND ----------

# MAGIC %sql
# MAGIC COMMENT ON TABLE mimi_ws_1.healthit.chit_hpip IS '# [Certified Health Information Technology Reported by Hospitals for Promoting Interoperability Performance](https://www.healthit.gov/data/datasets/certified-health-information-technology-reported-hospitals-promoting-interoperability) | resolution: hospital, interval: yearly
# MAGIC
# MAGIC In 2011, the Centers for Medicare and Medicaid Services (CMS) established the Medicare and Medicaid Electronic Health Record (EHR) Incentive Programs to encourage eligible professionals (EPs), eligible hospitals, and critical access hospitals (CAHs) to adopt, implement, upgrade, and demonstrate meaningful use of certified electronic health record technology (CEHRT).
# MAGIC
# MAGIC To continue a commitment to promoting and prioritizing interoperability and exchange of health care data, CMS renamed the EHR Incentive Programs to the Medicare and Medicaid Promoting Interoperability Programs in April 2018. This change moved the programs beyond the existing requirements of meaningful use to a new phase of EHR measurement with an increased focus on interoperability and improving patient access to health information.
# MAGIC
# MAGIC The “Certified Health Information Technology Reported by Hospitals for Promoting Interoperability Performance” datasets combine CMS Hospital Promoting Interoperability (PI) participation data with the ONC Certified Health IT Product List (CHPL). The Hospital PI datasets provide the certified EHR technology (CEHRT) reported by all hospitals who reported for Promoting Interoperability, beginning in program year 2023. This data field can be merged with the CHPL data to provide specific certified product details.
# MAGIC
# MAGIC These datasets provide a minimum set of data fields to further combine these data with CMS hospital datasets, the full CHPL dataset, and other datasets. The documentation and notes describe those data fields necessary for linking to other data. See Methods and Notes for further details on dataset construction and data linkages.
# MAGIC '

# COMMAND ----------


