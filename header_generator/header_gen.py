import csv

def extract_column_and_write_to_text(csv_filename, column_index, text_filename):
    try:
        with open(csv_filename, 'r', newline='', encoding='utf-8') as csv_file:
            # Create a CSV reader
            csv_reader = csv.reader(csv_file)
            
            # Skip header if present
            next(csv_reader, None)

            # Extract the specified column
            column_data = [row[column_index] for row in csv_reader]

        # Write the extracted column data to a text file
        with open(text_filename, 'w', encoding='utf-8') as text_file:
            for data_point in column_data:
                text_file.write(f'{data_point}\n')

        print(f'Data from column {column_index} in {csv_filename} written to {text_filename} successfully.')

    except Exception as e:
        print(f'Error: {e}')

# Example usage
csv_filename = 'data.csv'
column_index_to_extract = 3  # Replace with the index of the column you want (0-indexed)
text_filename = 'output.txt'

extract_column_and_write_to_text(csv_filename, column_index_to_extract, text_filename)

