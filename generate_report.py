
import pandas as pd
from fpdf import FPDF

df = pd.read_csv('sample_data.csv')

class PDF(FPDF):
    def header(self):
        self.image("codtech_logo.png", 10, 8, 33)
        self.set_font("Arial", "B", 14)
        self.set_text_color(0, 102, 204)
        self.cell(0, 10, "CODTECH Internship Report", ln=True, align="C")
        self.set_text_color(0, 0, 0)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(128)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_summary_table(self, df):
        self.set_fill_color(220, 220, 255)
        self.set_font("Arial", "B", 12)
        self.cell(60, 10, "Name", 1, 0, "C", True)
        self.cell(60, 10, "Tasks Completed", 1, 1, "C", True)
        self.set_font("Arial", "", 12)
        for _, row in df.iterrows():
            self.cell(60, 10, row["Name"], 1)
            self.cell(60, 10, str(row["Tasks_Completed"]), 1)
            self.ln()

    def add_certificate(self, name, end_date):
        self.add_page()
        self.set_font("Arial", "B", 18)
        self.set_text_color(0, 102, 204)
        self.cell(0, 20, "COMPLETION CERTIFICATE", ln=True, align="C")
        self.set_text_color(0, 0, 0)
        self.set_font("Arial", "", 13)
        self.ln(10)
        text = (
            f"This is to certify that {name} has successfully completed their "
            f"internship at CODTECH. The internship ended on {end_date}."
        )
        self.multi_cell(0, 10, text, align="C")
        self.ln(30)
        self.image("signature.png", x=80, w=50)
        self.set_font("Arial", "I", 11)
        self.cell(0, 10, "Authorized Signatory", ln=True, align="C")

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Intern Summary Report", ln=True)
pdf.ln(5)
pdf.add_summary_table(df)

for _, row in df.iterrows():
    pdf.add_certificate(row["Name"], row["Internship_End"])

pdf.output("internship_report.pdf")
print("PDF report generated: internship_report.pdf")
