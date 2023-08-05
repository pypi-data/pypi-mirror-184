import os
import sys
import regex
from flatten_everything import flatten_everything


def search_in_syspath(filename, isregex=False):
    filename = filename.lower()

    if isregex:
        filename = regex.compile(filename, flags=regex.I)
    folders = sys.path
    mainfi = []
    for rootdir in folders:

        allfi = []
        for subdirs, dirs, files in os.walk(rootdir):
            if not isregex:
                allfi.append(
                    [os.path.join(subdirs, k) for k in files if k.lower() == filename]
                )
            else:
                allfi.append(
                    [
                        os.path.join(subdirs, k)
                        for k in files
                        if filename.search(k) is not None
                    ]
                )

        mainfi.extend(
            [
                os.path.normpath(os.path.join(rootdir, x))
                for x in (flatten_everything(allfi))
            ]
        )
    filesto = list(set(mainfi))
    return filesto
