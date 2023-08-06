from pathlib import Path

from .filedata import Filedata
from .persist import FindInDict
from .photocopy import PhotoCopy

filetypes = { ".png", ".gif", ".jpg", ".jpeg", ".tif", ".tiff"}

def Manage(foldername, treatedfiles, filedict, newtreatedfiles):
    startpath = Path(foldername)
    for path in startpath.glob("**/*"):
        if (path.is_file()):
            fdata = Filedata.FromPath(path)
            if (fdata.sourcepath in treatedfiles):
                print(fdata.sourcepath + " - already treated")
                continue

            if (fdata.filetype in filetypes):
                if (FindInDict(fdata, filedict)):
                    print(fdata.sourcepath + " - duplicate")
                    newtreatedfiles.append(fdata.sourcepath + ", duplicate")
                else:
                    print(fdata.sourcepath + " - new file")
                    fdata.GetSize()
                    fdata.GetHash()
                    fdata.destpath = PhotoCopy.CopyFile(fdata.sourcepath)
                    filedict[fdata.GetHash()] = fdata 
                    newtreatedfiles.append(fdata.sourcepath + ", added")
                
            else:
                print("Not an image: " + path.name)
                newtreatedfiles.append(fdata.sourcepath + ", not an image")

