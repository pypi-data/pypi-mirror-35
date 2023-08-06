import sys

from photoarchive.persist import ReadDictionary, ReadTreatedFiles, SaveDictionary, SaveTreatedFiles
#import photoarchive.persist
from photoarchive.archive import Manage

folder = r"C:\Users\g\Pictures\Scannat"
#print(photoarchive.filetypes)
if (len(sys.argv) > 1):
    folder = sys.argv[1]

filedict = ReadDictionary()
print("Read {} files from db".format(len(filedict)))

treatedfiles = ReadTreatedFiles()
print("Read {} treated files".format(len(treatedfiles)))
newtreatedfiles = list()

try:
    Manage(folder, treatedfiles, filedict, newtreatedfiles)
except KeyboardInterrupt:
    print("aborted by user")
except Exception as ex:
    print("Error: " + str(ex))

SaveDictionary(filedict)
SaveTreatedFiles(newtreatedfiles)
