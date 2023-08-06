# Temp code writing file, keeping it separate from __init__.py to avoid users calling unusable code
# Will be moved to __init__ to keep things pythonic
# Also add support for pydoc

import os, requests
import threading
import time
import hashlib
import sys

# Main Downloading class
# Private
class _Dow:


    # Default
    def __init__(self):

        # Downloader Basics
        self.url = ""
        self.chunks = 0
        self.writeLocation = ""
        self.status = "Initialized"
        self.fileName = self.url.split('/')[-1]

        # Data Storage
        self.sizeInBytes = requests.head(self.url, headers={'Accept-Encoding': 'identity'}).headers.get('content-length', None)
        self.data = {}      # Storing in memory

        # Benchmarking
        self.startTime = ""
        self.endTime = ""
        self.elapsedTime = ""

        # Finished
        self.hash = ""

        # Creates an MD5 Hash
        # chunkSize -> chunk size of the file to load into memory

    def createHash(self, chunkSize=65000):

        # Initiate md5 check
        hasher = hashlib.md5()

        # Open file
        with open(self.fileName, 'rb') as file:
            buf = file.read(chunkSize)

            # Read
            while len(buf) > 0:
                hasher.update(buf)
                buf = file.read(chunkSize)

        # Save hash to hex digit
        self.hash = hasher.hexdigit()

    # Creates a range based on the number of splits
    def createRange(self, value, numsplits):
        ranges = []
        for i in range(numsplits):
            if i == 0:
                ranges.append(
                    '%s-%s' % (i, int(round(1 + i * value / (numsplits * 1.0) + value / (numsplits * 1.0) - 1, 0))))
            else:
                ranges.append('%s-%s' % (int(round(1 + i * value / (numsplits * 1.0), 0)), int(
                    round(1 + i * value / (numsplits * 1.0) + value / (numsplits * 1.0) - 1, 0))))
        return ranges

    # Downloads a chunk
    def downloadChunk(self, url, byteIndex, byteRange, retry=False):

        # Only send Range header if supported
        if len(self.data) != 1:
            headers = {"Range": 'bytes=%s' % byteRange}

        try:
            self.data[byteIndex] = requests.get(url, headers=headers)
        except Exception:
            if (retry == True):
                print("Error retrying chunk %d, terminating program" % byteIndex)
            else:
                print("[!] Error downloading chunk %d, retrying download.." % byteIndex)
                self.downloadChunk(url, byteIndex, byteRange, True)


    # Start a download
    def start(self):

        # Starting download
        self.status = "Downloading"
        self.startTime = time.time()

        # Check if valid URL
        if self.url == "":
            self.status = "Failed: No URL (how did you get here?)"
            return

        # Finished
        self.endTime = time.time()
        self.elapsedTime = self.endTime - self.startTime


# Single download, 1 chunk
# Public
class SingleDow(_Dow):

    def __init__(self, url=""):
        self.url = url
        self.chunks = 1




# Multi chunk download, 2+ chunks
# Public
class MutliDow(_Dow):

    def __init__(self, url="", chunks=2):
        self.url = url
        self.chunks = chunks

