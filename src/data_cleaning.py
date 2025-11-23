import pandas as pd

def load_and_clean_data():
    inst = pd.read_csv("data/Most-Recent-Cohorts-Institution.csv", low_memory=False)
    major = pd.read_csv("data/Most-Recent-Cohorts-Field-of-Study.csv", low_memory=False)
    inst["UNITID"] = pd.to_numeric(inst["UNITID"], errors="coerce")
    inst["CONTROL"] = pd.to_numeric(inst["CONTROL"], errors="coerce")
    inst["TUITIONFEE_IN"] = pd.to_numeric(inst["TUITIONFEE_IN"], errors="coerce")
    inst["TUITIONFEE_OUT"] = pd.to_numeric(inst["TUITIONFEE_OUT"], errors="coerce")
    inst["MD_EARN_WNE_P10"] = pd.to_numeric(inst["MD_EARN_WNE_P10"], errors="coerce")
    inst = inst.dropna(subset=["TUITIONFEE_IN", "MD_EARN_WNE_P10"])
    inst = inst[inst["TUITIONFEE_IN"] > 3000].copy()
    major = major[major["CIPDESC"].str.contains("Engineering|Computer|Math|Biolog", case=False, na=False)]
    stem_ids = major["UNITID"].unique()
    inst["STEM_SCHOOL"] = inst["UNITID"].isin(stem_ids)
    inst["ROI_INSTATE"] = inst["MD_EARN_WNE_P10"] / inst["TUITIONFEE_IN"]
    inst["ROI_OUTSTATE"] = inst["MD_EARN_WNE_P10"] / inst["TUITIONFEE_OUT"]
    inst = inst.dropna(subset=["ROI_INSTATE", "ROI_OUTSTATE"])
    return inst
