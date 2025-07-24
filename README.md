# Automated PDF Report Generator

This is a simple Python project that reads sales data from a CSV file, analyzes it, and generates a well-formatted PDF report using the lightweight `fpdf` library. No complex dependencies like `pandas` or `numpy` are required — perfect for beginners or constrained environments.

## Project Structure

codetech_Task2
├── sales_data.csv               
├── report_generator.py  
└── simple_sales_report.pdf     

## Requirements

- Python 3.x  
- `fpdf` library  

Install `fpdf` by running:  
`pip install fpdf`

## Features

- Reads data from a CSV file  
- Groups and summarizes sales by product  
- Outputs a clean, tabular PDF report  
- Runs without internet (after initial install)

## Sample Input (`sales_data.csv`)

Date,Product,Sales  
2025-07-01,Apples,150  
2025-07-01,Oranges,200  
2025-07-02,Apples,180  
2025-07-02,Oranges,220  
2025-07-03,Apples,160  
2025-07-03,Oranges,210

## How to Run

1. Clone this repository or download the folder  
2. Open a terminal in the project directory  
3. Run the script:  
   `python report_generator.py`  
4. The script will create a file called `simple_sales_report.pdf` in the same folder.

##  Sample Output (PDF)

| Product | Total Sales |  
|---------|-------------|  
| Apples  | 490         |  
| Oranges | 630         |

## Notes

- This script avoids heavy packages like `pandas` to ensure compatibility on systems with limited compiler support.  
- For more advanced features like filtering by date or generating charts, consider using `pandas`, `matplotlib`, and `reportlab`.

## Contributing

Feel free to fork the repo and add enhancements like:  
- Per-day reports  
- Export to Excel  
- Emailing the PDF

 
## sumbitted
 Pradnya Mhatre
