from pathlib import Path
import os
import hashlib
import re

class Filedata:
    def __init__(self, **kwargs):
        self.filename = kwargs["filename"]
        self.sourcepath = kwargs["sourcepath"]
        self.destpath = kwargs.get("destpath", None)
        self.filetype = kwargs.get("filetype", None)
        self.hasSize = kwargs.get("hasSize", False)
        self.size = kwargs.get("size", None)
        self.hasHash = kwargs.get("hasHash", False)
        self.hash = kwargs.get("hash", None)

    @staticmethod
    def FromPath(path):
        fdata = Filedata(filename = path.name.lower(), sourcepath = str(path.resolve()).lower())
        fdata.destpath = None
        fdata.filetype = path.suffix.lower() 
        fdata.hasSize = False
        fdata.size = None
        fdata.hasHash = False
        fdata.hash = None
        return fdata

    def GetSize(self):
        if (not self.hasSize):
            statinfo = os.stat(self.sourcepath)
            self.size = statinfo.st_size
            self.hasSize = True
        return self.size

    def GetHash(self):
        if (not self.hasHash):
            self.hasHash = True
            self.hash = Filedata.HashFile(self.sourcepath)
        return self.hash

    def EqualTo(self, other):
        f1 = Path(self.sourcepath)
        f2 = Path(other.sourcepath)
        if (not(self.SimilarNames(f1, f2))):
            return False

        if (self.GetSize() != other.GetSize()):
            return False

        if (self.GetHash() != other.GetHash()):
            return False

        return True

    def SimilarNames(self, one, other):
        if (one.suffix != other.suffix):
            return False

        f1 = one.stem
        f2 = other.stem
        # Old logic
        if (f1.startswith(f2) or f2.startswith(f1)):
            return True

        # Find already numbered duplicates
        ff1 = self.RemoveStuff(f1)
        ff2 = self.RemoveStuff(f2)
        if (ff1 == ff2):
            return True
        return False

    def RemoveStuff(self, str):  
        first = str[0:5]
        second = str[5:]
        second = re.sub(r"\d", "", second)
        str = first + second
        str = str.replace("(","").replace(")","").replace("_","")
        return str

    @staticmethod
    def HashFile(filepath):
        # An implementation of MD5 from https://www.pythoncentral.io/hashing-files-with-python/
        BLOCKSIZE = 65536
        hasher = hashlib.md5()
        with open(filepath, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        return hasher.hexdigest()

# a = Filedata(filename="allan.jpg", sourcepath="C:/allan.jpg", filetype=".jpg", hasSize=True, size=4711)
# a.SimilarNames(Path(r"C:\allan_4711.jpg"), Path(r"D:\nisse\allan(14).jpg"))

# b = Filedata(filname="allan_1.jpg", sourcepath="C:/allan_1.jpg", filetype=".jpg", hasSize=True, size=4721)
# test = a.EqualTo(b)
# print(test)

# a = Filedata.HashFile(r"C:\Users\g\Pictures\Scannat\Circa 1989\2018-03-14_10.TIF")
# print(a)
