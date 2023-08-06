# photoarchive
A simple tool to copy all unique photos to an archive

## Background
I often backup phones and cameras, but to different places, using no consistent naming conventions, and more importantly, with no check for duplicates.
This tool takes such a backup location and copies all image files to a better structured archive, excluding duplicates and renaming unique files with duplicate file names.

## Usage
Select a place where you will put your archive.
Make sure that your source files will have unique paths (i.e. if you have a bunch of usb sticks that would all be called "D:\", copy the files to a hard drive first).

```
pip install photoarchive
cd <archivefolder>
python -mphotoarchive <sourcefolder>
```

## Alternative

```
git clone https://github.com/roseeng/photoarchive
cd photoarchive
python __main__.py <sourcefolder>
```

## Notes of interest
### Uniqueness
Files to be copied are checked against the files in the existing archive using the following logic:

* Are the file names similar? If they do, go to next check, if not, copy.
* Do they have the exact same size? If they do, go to next check, if not, copy.
* Do they have the same MD5 checksum? If they do, mark as duplicate, if not, copy.

All treated files are added to a list, so you can run the command against the exact same folder and only working on new files.
This is saved in `treatedfiles.txt`.
All copied files are added to a dictionary, with file size and hash value, to avoid recomputation.
This is saved in `filedict.json`.

### Name comparison
The logic for "similar names" are as follows:

* If file suffix is different, the files are different. Else remove suffix from comparison.
* Take the first 5 chars
* From the remainder, remove all digits
* From the result, remove underscores and parenthesis.

The aim is to make files like "DSC4711.jpg" and "DSC4711(1).jpg" similar, but "47122.jpg" and "47123.jpg" different.
In a future version, this should be tweakable.
It is not the end of the world if it's not perfect though, the result is just more fstat() calls and hash calculations.

## Archive structure
When copying a file, we try to get the original date from the EXIF information. If that does not succeed, we take the creation date of the file. 

That is then used to build the folder structure in the archive as: Bilder/YYYY/MM/DD.
The files keep the old name in that folder, optionally with "-n" added if there already is a file with the same name in the folder.
