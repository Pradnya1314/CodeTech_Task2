from fpdf import FPDF
import csv

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Sales Report', ln=True, align='C')

    def table(self, data):
        self.set_font('Arial', '', 12)
        for row in data:
            for item in row:
                self.cell(60, 10, str(item), border=1)
            self.ln()


with open("sales_data.csv", "r") as file:
    reader = list(csv.reader(file))
    header = reader[0]
    rows = reader[1:]


summary = {}
for row in rows:
    product, sales = row[1], int(row[2])
    summary[product] = summary.get(product, 0) + sales

table_data = [["Product", "Total Sales"]]
for k, v in summary.items():
    table_data.append([k, v])


pdf = PDF()
pdf.add_page()
pdf.table(table_data)
pdf.output("simple_sales_report.pdf")

print(" PDF generated: simple_sales_report.pdf")
