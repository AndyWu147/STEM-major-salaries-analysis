U.S. College ROI Analysis (College Scorecard Dataset)
1. Project Overview

This project analyzes the financial return on investment (ROI) of U.S. colleges using data from the U.S. Department of Education’s College Scorecard.
I measure early-career earnings relative to tuition cost, compare ROI across school types, states, and STEM dominance, and identify which institutions deliver the strongest economic value for students.

2. Key Features

Cleaned and merged College Scorecard institution and earnings datasets

Calculated in-state and out-of-state ROI metrics

Labeled schools as STEM or non-STEM using the Field-of-Study dataset

Generated eight visualizations covering ROI distribution, gender gaps, school type differences, and more

Produced actionable insights interpretable by students, parents, and policymakers

3. Data Sources

Most Recent Cohorts—Institution Data

Most Recent Cohorts—Field-of-Study Data
Both datasets from the U.S. Department of Education (College Scorecard).

These include tuition costs, student demographics, earnings outcomes, school characteristics, and program categories.

4. Methods & Workflow

Loaded institutional and earnings datasets

Cleaned missing values and converted numeric columns

Removed schools with unrealistic tuition (TUITIONFEE_IN > 3000)

Calculated ROI for in-state and out-of-state students

Extracted STEM-related programs from the field-of-study file

Tagged each school as STEM or non-STEM based on UNITID match

Created all ROI-related visualizations

Wrote insights summarizing each visualization’s conclusion

5. Visualization Insights
6.1 ROI Distribution

The distribution is heavily right-skewed. Most colleges deliver modest ROI, with a long tail of very high-performing schools. Educational value varies widely across institutions.

6.2 Top 20 In-State ROI Schools

High-ROI schools are mainly public STEM-focused universities with low tuition and strong wage outcomes. Affordability + technical programs drive high ROI.

6.3 Top 20 Out-of-State ROI Schools

ROI drops sharply for non-residents. Only a few elite public universities provide strong out-of-state ROI. Most public schools are not cost-effective for out-of-state attendance.

6.4 ROI by School Type (Control)

Public schools offer the strongest average ROI. Private nonprofits show wide variability. For-profit institutions consistently underperform with the lowest ROI across the board.

6.5 Male vs Female Earnings Gap

Male median earnings exceed female earnings at nearly all institutions. The gap is persistent and substantial, indicating structural differences in labor-market outcomes.

6.6 Family Income Group Earnings (INC1–INC3)

Students from higher-income families consistently earn more after graduation, even within the same institutions. Socioeconomic background has strong influence on outcomes.

6.7 ROI by State

States with strong technical and economic ecosystems (CA, MA, TX) show higher average ROI. States with many small private colleges tend to show weaker ROI.

6.8 STEM vs Non-STEM School Earnings

STEM-dominant schools produce significantly higher early-career earnings. The gap between STEM and non-STEM institutions is large and consistent.

6. How to Run This Project

Clone the repository

Install required Python packages:

pip install pandas numpy matplotlib


Place the College Scorecard CSV files into the /data folder

Open the Jupyter Notebook in /notebooks/

Run all cells in order to reproduce the analysis

7. Repository Structure
/data/
    Institution.csv
    FieldOfStudy.csv

/notebooks/
    ROI_Analysis.ipynb

/plots/
    roi_distribution.png
    roi_by_state.png
    gender_gap.png
    stem_vs_nonstem.png

/src/
    data_cleaning.py
    visualization.py

README.md
LICENSE (optional)

8. Future Improvements

Add mid-career (10-year) ROI analysis

Incorporate program-level earnings instead of school-level

Build an interactive dashboard (Plotly/Streamlit)

Add machine learning to predict ROI based on school features