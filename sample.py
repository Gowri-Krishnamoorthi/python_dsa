import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Folder path
folder_path = r"E:\Python_Code_Practice"
output_path = os.path.join(folder_path, "All_Python_Files.pdf")

# Canvas setup
c = canvas.Canvas(output_path, pagesize=A4)
width, height = A4
margin = 50
line_height = 12

# Start from top of the first page
y = height - margin

# Helper: sorting key based on numeric prefix
def extract_sort_key(filename):
    parts = filename.split('_')
    try:
        return (int(parts[0]), filename)
    except ValueError:
        return (float('inf'), filename)

# Get and sort Python files
py_files = sorted(
    [f for f in os.listdir(folder_path) if f.endswith(".py")],
    key=extract_sort_key
)

# Write lines with paging
def write_lines(lines, font_name="Courier", font_size=10):
    global y
    c.setFont(font_name, font_size)
    for line in lines:
        if y < margin:
            c.showPage()
            y = height - margin
            c.setFont(font_name, font_size)
        c.drawString(margin, y, line)
        y -= line_height

# Write each file
for filename in py_files:
    file_path = os.path.join(folder_path, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        code_lines = f.readlines()

    # Heading (file name)
    write_lines([filename], font_name="Courier-Bold", font_size=12)
    y -= line_height  # Add spacing below heading

    # Code
    clean_lines = [line.rstrip() for line in code_lines]
    write_lines(clean_lines)

    y -= line_height * 2  # Space before next file

# Save PDF
c.save()
print(f"PDF created at: {output_path}")
