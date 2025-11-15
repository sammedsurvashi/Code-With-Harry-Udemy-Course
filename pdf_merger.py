#How It Works

#User enters how many PDF files they want to merge.
#Script asks for each PDF file name.
#All entered PDF files are combined into a new file named merged-pdf.pdf.

#Install required library:
#pip install PyPDF2


from PyPDF2 import PdfWriter       # Import PDF writing/merging tool

merger = PdfWriter()               # Create merger object

pdfs = []                          # Empty list to store PDF names
n = int(input("How many pdfs do you want to merge?\n"))  # Ask how many PDFs

for i in range(0, n):              # Loop for each PDF
    name = input(f"Enter the name of pdf {i + 1}: ")  # Get PDF file name
    pdfs.append(name)              # Add file name to list

for pdf in pdfs:                   # Loop through collected names
    merger.append(pdf)             # Add each PDF to merger

merger.write("merged-pdf.pdf")     # Save merged output file
merger.close()                     # Close merger
