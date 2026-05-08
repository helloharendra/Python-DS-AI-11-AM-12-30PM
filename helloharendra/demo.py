import pandas as pd
from ydata_profiling import ProfileReport

# Load your dataset
df = pd.read_csv("industry.csv")   # replace with your file

# Generate full profiling report
profile = ProfileReport(df, title="Industry Report")

# Save report
profile.to_file("report.html")

print("Report Generated Successfully ✅")