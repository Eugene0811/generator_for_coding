from docx import Document

def create_docx(filename, content):
    # Create a new Document
    doc = Document()

    # Add content to the document
    doc.add_paragraph(content)

    # Save the document
    doc.save(filename)
    print(f'DOCX file "{filename}" created successfully.')

# Example usage
docx_filename = 'example.docx'
document_content = 'Hello, this is a sample document created with Python.'

create_docx(docx_filename, document_content)

