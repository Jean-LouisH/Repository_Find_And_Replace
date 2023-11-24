import os, fnmatch
import shutil
from distutils.dir_util import copy_tree

# Enter your inputs.

directory_location = ""
copy_location = ""
find_and_replace_mapping = {"example_from":"example_to"}
file_patterns = ["*.c", "*.h", "*.cpp", "*.hpp"]

def find_and_replace(directory, find_and_replace_mapping, file_patterns):
    #Modifications of David Sulpy's code, StackOverflow https://stackoverflow.com/posts/6257321/revisions
    
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for i in file_patterns:
            for filename in fnmatch.filter(files, i):
                filepath = os.path.join(path, filename)
                with open(filepath) as f:
                    s = f.read()
                for find in find_and_replace_mapping:
                    replace = find_and_replace_mapping[find]
                    s = s.replace(find, replace)
                with open(filepath, "w") as f:
                    f.write(s)

def main():
    print("Copying from '" + directory_location + "' ...")
    copy_tree(copy_location, copy_location + "_0")
    shutil.rmtree(copy_location)
    copy_tree(directory_location, copy_location)
    print("Done.\n")
    print("Finding and replacing in '" + copy_location + "'...")
    find_and_replace(copy_location, find_and_replace_mapping, file_patterns)
    print("Done.\n")
    input("Press any key to exit.")

if __name__ == "__main__":
    main()
