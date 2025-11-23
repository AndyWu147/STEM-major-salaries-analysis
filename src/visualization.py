import matplotlib.pyplot as plt

def stem_boxplot(df):
    plt.figure(figsize=(8,8))
    plt.boxplot([
        df[df["STEM_SCHOOL"]==True]["MD_EARN_WNE_P10"],
        df[df["STEM_SCHOOL"]==False]["MD_EARN_WNE_P10"]
    ], tick_labels=["STEM","Non-STEM"])
    plt.savefig("plots/stem_vs_nonstem.png", dpi=300)
    plt.close()

def roi_hist(df):
    plt.figure(figsize=(8,8))
    plt.hist(df["ROI_INSTATE"], bins=40)
    plt.savefig("plots/roi_instate_hist.png", dpi=300)
    plt.close()

def tuition_vs_earnings(df):
    plt.figure(figsize=(8,8))
    plt.scatter(df["TUITIONFEE_IN"], df["MD_EARN_WNE_P10"], s=10)
    plt.savefig("plots/tuition_vs_earnings.png", dpi=300)
    plt.close()
