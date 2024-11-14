from fpdf import FPDF
import pandas as pd

def dataframe_to_pdf(df, pdf_path="output.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=10)
    
    # Column widths (auto-calculated based on max width of data)
    col_widths = [pdf.get_string_width(str(col)) + 2 for col in df.columns]
    for i, col in enumerate(df.columns):
        max_width = max(pdf.get_string_width(str(value)) for value in df[col]) + 2
        if max_width > col_widths[i]:
            col_widths[i] = max_width
    
    # Add header
    for i, col in enumerate(df.columns):
        pdf.cell(col_widths[i], 10, str(col), border=1, align='C')
    pdf.ln()
    
    # Add rows
    for index, row in df.iterrows():
        for i, col in enumerate(df.columns):
            pdf.cell(col_widths[i], 10, str(row[col]), border=1, align='C')
        pdf.ln()
    
    # Save the pdf
    pdf.output(pdf_path)
    print(f"PDF saved as {pdf_path}")

