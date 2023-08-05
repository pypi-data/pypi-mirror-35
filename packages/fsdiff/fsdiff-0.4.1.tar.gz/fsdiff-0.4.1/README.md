# NAME 

fsdiff - A tool to compare filesystems or local disk images. It performs both a content analysis and a 
It can mount and compare two images locally or it can just compare two filesystems.

# SYNOPSIS

`fsdiff [-h] [-v --version] [-x] [-i --img] [from] [to]`

# DESCRIPTION

fsdiff is a very simple tool used to compare recursively the filesystem directory and file structure.
It does not only perform a quick (shallow) comparison using `os.stat` (stat system call), it also compares 
the contents of the files. 

In case they differ, it displays a brief summary report. It is also installed
as a Python packaged, so it can be used likewise.

Example run:
`sudo fsdiff rootfs bootfs`

For a more detailed investigation  a deep checking tool like 
diffoscope or Beyond Compare, may be used.

To install you need to run `pip3 install fsdiff`, with either super
user privileges or with the `--user` flag.

Note: Python 3.x is required, a few new language features are used, like `subprocess.run` method as well as the cache
 clearing from the directory compare library. It also needs to be run with super user privileges.

# GENERAL OPTIONS

```
-h
: Displays a help message
-v, --version
: Shows the current version
-x
: Extracts an image if it's compressed
-i, --img
: Sets the comparison type to image (img)
from
: The location of the path (image) to compare from 
to
: The location of the path (image) to compare against
```
