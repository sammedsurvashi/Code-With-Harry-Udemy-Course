# Python File I/O Examples with Explanation

# 1. Write to a file
# "w" mode = write (overwrites existing content)
with open("myfile.txt", "w") as file:
    file.write("Hello Sammed!\n")
    file.write("Welcome to Python File I/O.\n")
  ....................................................................

# 2. Read entire file
# "r" mode = read
with open("myfile.txt", "r") as file:
    content = file.read()
    print("Reading entire file:")
    print(content)
.......................................................................

# 3. Read line by line
with open("myfile.txt", "r") as file:
    print("Reading line by line:")
    for line in file:
        print("Line:", line.strip())

.......................................................................

# 4. Append data
# "a" mode = append (adds new content at the end)
with open("myfile.txt", "a") as file:
    file.write("This is an extra line added later.\n")
.........................................................................

# 5. Binary file example (copy an image)
# "rb" = read binary, "wb" = write binary
# Note: Make sure "photo.jpg" exists in the same folder
try:
    with open("photo.jpg", "rb") as f1:
        data = f1.read()

    with open("copy_photo.jpg", "wb") as f2:
        f2.write(data)

    print("Image copied successfully!")

except FileNotFoundError:
    print("photo.jpg not found, skipping binary example.")
.............................................................................

