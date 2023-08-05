# Copyright (C) 2018 Ioannis Valasakis <code@wizofe.uk>
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2

import os
import sys
import filecmp
import os.path
from subprocess import Popen, PIPE

import errno
import ctypes
from ctypes import cdll
from ctypes.util import find_library
from colorama import init, Fore, Back, Style


def load_c_library():
    """
    Loads the libc from the system to use for different calls
    like mount, etc
    """
    try:
        libc_name = find_library('c')
        libc = cdll.LoadLibrary(libc_name)
        return libc
    except:
        print('Unable to load libc.')


def cmount(source, target, fs, options=''):
    """ A mount interface of the sys/mount.h from the Standard C Library
    :param source the filesystem to be attached. a path to an img, dir or a device
    :param target (pathname) the location where the source would be attached to
    :param fs the filesystem type supported by the kernel
    :param options extra options supported by the OS

    :returns 0 for Pass, -1 for Failure and sets the appropriate errno
    """
    libc = load_c_library()
    libc.mount.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_ulong, ctypes.c_char_p)

    ret = libc.mount(source, target, fs, 0, options)
    if ret < 0:
        errno = ctypes.get_errno()
        raise OSError(errno, "Error mounting {} ({}) on {} with options '{}': {}".
                      format(source, fs, target, options, os.strerror(errno)))


def mount_image(img):
    ROOT_MP = 'img/root'
    BOOT_MP = 'img/boot'
    BOOT_SUFFIX = 'p1'
    ROOT_SUFFIX = 'p2'

    try:
        device_name = Popen(["sudo", "kpartx", "-vas", img],
                              stdout=PIPE).communicate()[0].split()[2][:-2].decode('utf-8')
        os.makedirs(ROOT_MP)
        os.makedirs(BOOT_MP)

        Popen(["sudo", "mount", "/dev/mapper/{}{}".format(device_name, ROOT_SUFFIX), ROOT_MP], stdout=PIPE)
        Popen(["sudo", "mount", "/dev/mapper/{}{}".format(device_name, BOOT_SUFFIX), BOOT_MP], stdout=PIPE)

        return ROOT_MP, BOOT_MP, device_name
    except:
        raise


def mount_noobs(img):
    ROOT_NB_MP = 'noobs/root'
    BOOT_NB_MP = 'noobs/boot'
    BOOT_SUFFIX = 'p6'
    ROOT_SUFFIX = 'p7'

    try:
        device_name = Popen(["sudo", "kpartx", "-vas", img],
                              stdout=PIPE).communicate()[0].split()[2][:-2].decode('utf-8')
        os.makedirs(ROOT_NB_MP)
        os.makedirs(BOOT_NB_MP)

        Popen(["sudo", "mount", "/dev/mapper/{}{}".format(device_name, ROOT_SUFFIX), ROOT_NB_MP], stdout=PIPE)
        Popen(["sudo", "mount", "/dev/mapper/{}{}".format(device_name, BOOT_SUFFIX), BOOT_NB_MP], stdout=PIPE)

        return ROOT_NB_MP, BOOT_NB_MP, device_name
    except:
        raise


def unmount_image(img, device_name):
    try:
        Popen(["sudo", "kpartx", "-vd", img], stdout=PIPE)
        Popen(["sudo", "dmsetup", "remove", "/dev/mapper/{}*".format(device_name)], stdout=PIPE)
        Popen(["sudo", "losetup", "-d", "/dev/{}".format(device_name)], stdout=PIPE)
        return True
    except:
        print("E: Can't unmount the loopback device: {}".format(device_name))
        return False


class dircmp(filecmp.dircmp):
    """ Comparison between contents of the files of dir1 and dir2 within the same path.
    """

    def phase3(self):
        """
            Discover the differences between common files and ensure that
            we are using content comparison with shallow=False in contrast
            with the original compare phase3 implementation.

            It does an in depth comparison of contents and doesn't rely only on os.stat() attributes

            Refer to Lib/filecmp.py of cpython
            """
        fcomp = filecmp.cmpfiles(self.left, self.right, self.common_files,
                                 shallow=False)
        self.same_files, self.diff_files, self.funny_files = fcomp


def is_same(path1, path2):
    """
    Compare the content of the two directory trees.
    :param path1: Left path to compare from
    :param path2: Right path to compare with
    :rtype True is they are the same or False if they differ
    """
    compared = dircmp(path1, path2)

    if (compared.left_only or compared.right_only or compared.diff_files
            or compared.funny_files):
        # Displays a summary report if differences are found
        compared.report_full_closure()
        return False
    for subdir in compared.common_dirs:
        if not is_same(os.path.join(path1, subdir), os.path.join(path2, subdir)):
            return False
    return True


def colorp(text, foreground="black", background="white"):
    """
    :param text: the string to display to stdout
    :param foreground: color
    :param background: color
    :return:
    """
    init()  # initialize colorama
    fground = foreground.upper()
    bground = background.upper()
    style = getattr(Fore, fground) + getattr(Back, bground)
    print(style + text + Style.RESET_ALL)


def is_same_display(from_loc, to_loc):
    ret = is_same(from_loc, to_loc)
    colorp("LOCATIONS SIMILAR" if ret == True else "LOCATIONS DIFFER", "green" if ret == True else "red",
           "white")
    return ret


def main(from_loc, to_loc, image=False, extract=False, ):
    """
    The simplest user case by calling is_same()
    :param image: Boolean value; Sets an image as argument
    :param extract: Extracts a compressed image
    :param from_loc: the left side path to compare from
    :param to_loc: the right side path to compare with
    :rtype: True if they are the same, False otherwise
    """

    # Ensure that the user is root
    if os.geteuid() is not 0:
        print("E: Getting the required privileges, are you root?")
        sys.exit(1)

        # if there are images extract (if needed) and mount them
    if image:
        if extract:
            # do the gunzip here, store the file names and mount
            print('E: Currently not supported.')
            sys.exit(1)
        else:
            # store the file name and mount
            # TODO: Currently from is a normal image and to is a NOOBS one
            from_boot, from_root, img_device = mount_image(from_loc)
            to_boot, to_root, noobs_device = mount_noobs(to_loc)

            is_same_display(from_boot, to_boot)
            is_same_display(from_root, to_root)

            unmount_image(from_loc)
            unmount_image(to_loc)
            sys.exit(0)
    else:
        # and that directories/image files exist
        if not os.path.exists(from_loc) or not os.path.exists(to_loc):
            print("E: Can't find locations, misspelled?")
            sys.exit(1)

        is_same_display(from_loc, to_loc)
        sys.exit(0)
