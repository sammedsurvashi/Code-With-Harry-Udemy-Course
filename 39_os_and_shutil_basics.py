#os_and_shutil

1. OS Module:-These modules connect Python to your computer's operating system.
              That is, through this you can do things like creating a folder, deleting files, 
               changing names, seeing things inside the folder from Python itself.

#Explanation OS Examples

getcwd() → Current folder location बताता है
chdir() → Folder change करने के लिए
listdir() → Folder में files/folders list करता है
mkdir() → नया folder बनाता है
rmdir() → Empty folder delete करता है
exists() → Path मौजूद है या नहीं check करता है
join() → Path को safely जोड़ता है
system() → Terminal command run करता है
rename() → File का नाम बदलता है
remove() → File delete करता है


# OS Module Examples -
import os

print("===== OS Module Easy Examples =====\n")

# 1️⃣ Current Working Directory
cwd = os.getcwd()
print("1. Current Folder:", cwd)
print("Explanation: अभी हम किस folder में हैं, यह दिखाता है।\n")

# 2️⃣ Change Directory (folder change करना)
# os.chdir("C:/Users/Sammed/Desktop")  # अपने path के हिसाब से uncomment करें
# print("Changed Folder:", os.getcwd())
print("2. Change Directory: Folder बदलने के लिए use होता है।\n")

# 3️⃣ List Files/Folders
files = os.listdir()
print("3. Files/Folders in Current Directory:", files)
print("Explanation: folder में मौजूद files और folders दिखाता है।\n")

# 4️⃣ Make New Folder
folder_name = "TestFolder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"4. Folder Created: {folder_name}")
else:
    print(f"Folder '{folder_name}' already exists.")
print("Explanation: नया folder बनाने के लिए use होता है।\n")

# 5️⃣ Remove Empty Folder
if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print(f"5. Folder Removed: {folder_name}")
print("Explanation: खाली folder delete करने के लिए use होता है।\n")

# 6️⃣ Check if a Path Exists
path_check = "C:/"
exists = os.path.exists(path_check)
print(f"6. Path Exists? {exists}")
print("Explanation: path मौजूद है या नहीं, यह check करता है।\n")

# 7️⃣ Join Paths
joined_path = os.path.join("C:/Users", "Sammed", "Documents")
print("7. Joined Path:", joined_path)
print("Explanation: path को safe तरीके से जोड़ने के लिए use होता है।\n")

# 8️⃣ Run System Command
os.system("echo Hello from OS module!")
print("8. Run System Command: Terminal में command चलाता है।\n")

# 9️⃣ Rename a File
with open("old_file.txt", "w") as f:
    f.write("Sample content for rename.")
os.rename("old_file.txt", "new_file.txt")
print("9. File Renamed: old_file.txt --> new_file.txt")
print("Explanation: file का नाम बदलने के लिए use होता है।\n")

# 🔟 Remove a File
if os.path.exists("new_file.txt"):
    os.remove("new_file.txt")
    print("10. File Removed: new_file.txt")
print("Explanation: file delete करने के लिए use होता है।\n")

......................................................................................

  2. shutil Module:- This module is used to copy, move, or delete files or folders.
                    This is especially useful when you need to back up a file or move a folder.

# Shutil Module Examples - Easy Version for Beginners
import shutil
import os

print("===== Shutil Module Easy Examples =====\n")

# 1️⃣ Copy a File
with open("sample.txt", "w") as f:
    f.write("This is a sample file for copy example.")

shutil.copy("sample.txt", "sample_copy.txt")
print("1. File Copied: sample.txt --> sample_copy.txt")
print("Explanation: यह file को copy करने के लिए use होता है।\n")

# 2️⃣ Move a File
shutil.move("sample_copy.txt", "moved_sample.txt")
print("2. File Moved: sample_copy.txt --> moved_sample.txt")
print("Explanation: यह file को एक location से दूसरी location में move करता है।\n")

# 3️⃣ Copy a Folder
if not os.path.exists("SourceFolder"):
    os.mkdir("SourceFolder")
    with open("SourceFolder/file1.txt", "w") as f:
        f.write("File inside folder to copy.")

shutil.copytree("SourceFolder", "CopiedFolder")
print("3. Folder Copied: SourceFolder --> CopiedFolder")
print("Explanation: यह पूरा folder और उसके contents copy करता है।\n")

# 4️⃣ Remove a Folder (with contents)
shutil.rmtree("CopiedFolder")
print("4. Folder Removed: CopiedFolder")
print("Explanation: यह folder और उसके अंदर की सभी files/folders delete करता है।\n")

# 5️⃣ Copy Only File Content
with open("source.txt", "w") as f:
    f.write("Some important text.")

shutil.copy("source.txt", "destination.txt")
print("5. File Copied: source.txt --> destination.txt")
print("Explanation: यह file content को copy करता है।\n")

# 6️⃣ Move Folder
if not os.path.exists("MoveFolder"):
    os.mkdir("MoveFolder")
shutil.move("MoveFolder", "MovedFolder")
print("6. Folder Moved: MoveFolder --> MovedFolder")
print("Explanation: यह folder को दूसरी location पर move करता है।\n")

# 7️⃣ Cleanup - remove created files and folders
os.remove("sample.txt")
os.remove("moved_sample.txt")
os.remove("source.txt")
os.remove("destination.txt")
shutil.rmtree("SourceFolder")
shutil.rmtree("MovedFolder")
print("7. Cleanup Completed: सभी sample files/folders removed")
print("Explanation: यह example cleanup के लिए है, ताकि कोई leftover न रहे।\n")

print("✅ All Shutil Module Easy Examples Completed!")





