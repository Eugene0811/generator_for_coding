from docx import Document
import csv

def extract_column(csv_reader, column_index):            
    # Skip header if present
    next(csv_reader, None)

    # Extract the specified column
    column_data = [row[column_index] for row in csv_reader]
    return column_data

def extract_data_from_csv(csv_filename, column_index):
    try:
        with open(csv_filename, 'r', newline='', encoding='utf-8') as csv_file:
            # Create a CSV reader
            csv_reader = csv.reader(csv_file)

            # Skip header if present
            next(csv_reader, None)

            # Extract the specified column
            column_data = [row[column_index] for row in csv_reader]
            return column_data

    except Exception as e:
        print(f'Error: {e}')     

def create_docx(filename, column_data):
    # Create a new Document
    doc = Document()

    # Add content to the document
    # Write the extracted column data to a text file
    for data_point in column_data:
        # text_file.write(f'{data_point}\n')
        doc.add_paragraph(data_point)

    # Save the document
    doc.save(filename)
    print(f'DOCX file "{filename}" created successfully.')

# Example usage
csv_filename = '../data.csv'
column_index_to_extract = 3  # Replace with the index of the column you want (0-indexed)
docx_filename = 'driver_doc.docx'

data_list = extract_data_from_csv(csv_filename, column_index_to_extract)
create_docx(docx_filename, data_list)

