import pandas as pd
import matplotlib.pyplot as plt

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# -------------------------
# LOAD DATA
# -------------------------
df = pd.read_csv("sales_data.csv")

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

# -------------------------
# ANALYSIS
# -------------------------
total_revenue = df["Revenue"].sum()
product_sales = df.groupby("Product")["Revenue"].sum()
best_product = product_sales.idxmax()
daily_sales = df.groupby("Date")["Revenue"].sum()

# -------------------------
# PRINT RESULTS
# -------------------------
print("\n===== SALES ANALYSIS REPORT =====")
print("Total Revenue:", total_revenue)
print("\nRevenue by Product:\n", product_sales)
print("\nBest Selling Product:", best_product)
print("\nDaily Sales:\n", daily_sales)

# -------------------------
# CHART 1: DAILY SALES
# -------------------------
plt.figure()
daily_sales.plot(marker="o")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.grid()
plt.savefig("daily_sales.png")   # SAVE BEFORE SHOW
plt.show()

# -------------------------
# CHART 2: PRODUCT SALES
# -------------------------
plt.figure()
product_sales.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.grid()
plt.savefig("product_sales.png")
plt.show()

# -------------------------
# CHART 3: PIE CHART
# -------------------------
plt.figure()
product_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Revenue Distribution")
plt.ylabel("")
plt.savefig("revenue_share.png")
plt.show()

# -------------------------
# PDF REPORT
# -------------------------
doc = SimpleDocTemplate("sales_report.pdf")
styles = getSampleStyleSheet()

content = []

content.append(Paragraph("Sales Data Analysis Report", styles['Title']))
content.append(Spacer(1, 12))

content.append(Paragraph(f"Total Revenue: {total_revenue}", styles['Normal']))
content.append(Spacer(1, 12))

content.append(Paragraph(f"Best Selling Product: {best_product}", styles['Normal']))
content.append(Spacer(1, 12))

content.append(Paragraph("Insights:", styles['Heading2']))
content.append(Paragraph(
    "Sales declined from Jan 1 to Jan 3 and increased sharply on Jan 4. "
    "Laptop generated the highest revenue.",
    styles['Normal']
))

doc.build(content)

print("\nPDF report generated successfully!")
