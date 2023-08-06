import piexif
import os
import datetime
import shutil
from pathlib import Path

class PhotoCopy:
    destroot = "./Bilder"

    @staticmethod
    def CopyFile(srcpath):
        dateparts = PhotoCopy.GetDateFromExif(srcpath)
        if (dateparts is None):
            dateparts = PhotoCopy.GetDateFromStat(srcpath)

        year, month, day = dateparts
        destdir = Path(PhotoCopy.destroot).resolve()
        destdir = destdir / Path(year, month, day)
        destpath = destdir / Path(srcpath).name
        print(destpath)
        if (not destdir.exists()):
            print("Creating dir: " + str(destdir))
            destdir.mkdir(parents=True, exist_ok=True)
        
        if (destpath.exists()):
            destpath = PhotoCopy.Uniquify(destpath)

        shutil.copy2(srcpath, destpath)

        return str(destpath)

    @staticmethod
    def Uniquify(path):
        i = 0
        newpath = path
        while (newpath.exists()):
            i = i+1
            file = path.stem + "_" + str(i) + path.suffix
            newpath = path.parent / file

        print("Creating unique path: " + str(newpath))
        return newpath

    @staticmethod 
    def GetDateFromExif(srcpath):
        try:
            exif_dict = piexif.load(srcpath)
        except:
            return None

        tags = [("Exif", "DateTimeOriginal", 36867),
                ("Exif", "DateTimeDigitized", 36868),
                ("0th", "DateTime", 306),
                ("1st", "DateTime", 306) ]

        for ifd, _, tag in tags:
            d1 = exif_dict.get(ifd)
            if (d1 is not None):
                datestring = exif_dict[ifd].get(tag)
                if (datestring is not None):
                    datestring = datestring.decode("utf-8", "strict") 
                    if (not datestring.startswith("0000")):
                        print("Date from exif: " + datestring)
                        return (datestring[0:4], datestring[5:7], datestring[8:10])

        return None

    @staticmethod
    def GetDateFromStat(srcpath):
        statinfo = os.stat(srcpath)
        date = datetime.datetime.fromtimestamp(statinfo.st_ctime)
        print("Date from file")
        return (str(date.year), str(date.month).zfill(2), str(date.day).zfill(2))

    @staticmethod
    def PrintExif(srcpath, all=False):
        exif_dict = piexif.load(srcpath)
        for ifd in ("0th", "Exif", "GPS", "1st"):
            for tag in exif_dict[ifd]:
                if (all or piexif.TAGS[ifd][tag]["name"].find("Date") >= 0):
                    print(ifd, piexif.TAGS[ifd][tag]["name"], exif_dict[ifd][tag])

#PrintExif(r"C:\Users\g\Pictures\Gitarr\20130506_004442.jpg")

#PhotoCopy.PrintExif(r"C:\Users\g\Documents\Python\photoarchive\photoarchive\Bilder\2006\12\15\klassfotocroppad.jpg", all=True)
#allan =  PhotoCopy.CopyFile(r"C:\Users\g\Pictures\Scannat\110-film\2018-03-14_77.TIF")
# allan = PhotoCopy.Uniquify(Path(r"C:\Users\g\Pictures\Scannat\110-film\2018-03-14_77.TIF"))
# print(allan)

#print(GetDateFromStat(r"C:\Users\g\Pictures\Scannat\110-film\2018-03-14_77.TIF"))
# for ifd in ("0th", "Exif", "GPS", "1st"):
#     for tag in piexif.TAGS[ifd]:
#         if (str(piexif.TAGS[ifd][tag]["name"]).find("DateTime") != -1):
#             print(ifd, piexif.TAGS[ifd][tag]["name"], tag)

