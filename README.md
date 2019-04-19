# Bulk rename PDFs


Renames all whacky PDF named files to a bit better form. 


### Install: 

```
$ sudo apt-get install build-essential libpoppler-cpp-dev pkg-config python-dev
$ pip3 install pdfs-rename --user
```

### Usage:

```
usage: pdfs-rename [-h] [--rename] [--from_text] pdfs [pdfs ...]

positional arguments:
  pdfs         list of filenames to rename

optional arguments:
  --rename     actually rename files
  --from_text  extract new name from text
```
