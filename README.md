
# 📝 Automated Internship Report Generator

This project automatically generates formatted **PDF reports** for interns using data from a CSV file. It includes a summary table and personalized certificates with a logo and signature using **Python** and **FPDF**.

---

## 📁 Project Structure

```
automated-report/
├── sample_data.csv           # Input CSV with intern data
├── generate_report.py        # Python script to generate PDF
├── codtech_logo.png          # Logo for the report
├── signature.png             # Signature for the certificate
└── internship_report.pdf     # Output PDF (generated)
```

---

## 🧰 Libraries Used

- `pandas` – for reading and processing CSV data.
- `fpdf` – for generating PDF documents.
- `Pillow` – (only used to generate placeholder images).

Install required packages:
```bash
pip install pandas fpdf pillow
```

---

## 📑 Input Format (CSV)

`sample_data.csv` should contain the following columns:

```csv
Name,Internship_Start,Internship_End,Tasks_Completed
Alice Johnson,2025-04-01,2025-05-25,15
Bob Smith,2025-03-15,2025-05-20,18
...
```

---

## 🚀 How to Run

1. Open the folder in **VS Code**.
2. Make sure Python is installed.
3. Run the script from terminal:

```bash
python generate_report.py
```

4. The file `internship_report.pdf` will be generated.

---

## 📄 Output

The generated PDF includes:
- A summary table of all interns and tasks completed.
- Individual completion certificates for each intern.
- Logo and signature embedded on each certificate.

---

## 📌 Notes

- Replace `codtech_logo.png` and `signature.png` with your actual files for branding.
- To email PDFs or add charts, extend the script using `smtplib` and `matplotlib`.

---
