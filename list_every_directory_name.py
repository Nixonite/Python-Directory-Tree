import os

path = "/Users/nixonite/Documents/School/"

for library in os.listdir(path):

    if not ("." in library):
        newPath = path+library
        for root, dirs, files in os.walk(newPath):
            level = root.replace(newPath,'').count(os.sep)
            indent = ' '*4*(level)
            print(indent+ os.path.basename(root))
            #subindent = ' ' * 4 * (level + 1)
            #for file in files:
                #print(subindent+file)           
