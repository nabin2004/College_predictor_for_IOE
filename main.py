import pandas as pd
import camelot

def pdf_to_csv(pdf_path, csv_path):
    tables = camelot.read_pdf(pdf_path, flavor='stream', pages='all')
    df_list = [table.df for table in tables]
    df = pd.concat(df_list)
    df.to_csv(csv_path, index=False)
    
    
if __name__ == "__main__":
    pdf_path = 'score.pdf'
    csv_path = 'score.csv'

    pdf_to_csv(pdf_path, csv_path)
