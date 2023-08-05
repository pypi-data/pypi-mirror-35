# -*- coding: utf-8 -*-

# Copyright 2018 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Convert pixiv ugoira to webm"""

from .common import PostProcessor
from .. import util
import collections
import subprocess
import tempfile
import zipfile
import os


class UgoiraPP(PostProcessor):

    def __init__(self, pathfmt, options):
        PostProcessor.__init__(self)
        self.extension = options.get("extension") or "webm"
        self.args = options.get("ffmpeg-args")
        self.twopass = options.get("ffmpeg-twopass")
        self.delete = not options.get("keep-files", False)

        ffmpeg = options.get("ffmpeg-location")
        self.ffmpeg = util.expand_path(ffmpeg) if ffmpeg else "ffmpeg"

        rate = options.get("framerate", "auto")
        if rate != "auto":
            self.calculate_framerate = lambda _: (None, rate)

    def run(self, pathfmt):
        if (pathfmt.keywords["extension"] != "zip" or
                "frames" not in pathfmt.keywords):
            return

        framelist = pathfmt.keywords["frames"]
        rate_in, rate_out = self.calculate_framerate(framelist)

        with tempfile.TemporaryDirectory() as tempdir:
            # extract frames
            with zipfile.ZipFile(pathfmt.temppath) as zfile:
                zfile.extractall(tempdir)

            # write ffconcat file
            ffconcat = tempdir + "/ffconcat.txt"
            with open(ffconcat, "w") as file:
                file.write("ffconcat version 1.0\n")
                for frame in framelist:
                    file.write("file '{}'\n".format(frame["file"]))
                    file.write("duration {}\n".format(frame["delay"] / 1000))
                if self.extension != "gif":
                    # repeat the last frame to prevent it from only being
                    # displayed for a very short amount of time
                    file.write("file '{}'\n".format(framelist[-1]["file"]))

            # collect command-line arguments
            args = [self.ffmpeg]
            if rate_in:
                args += ["-r", str(rate_in)]
            args += ["-i", ffconcat]
            if rate_out:
                args += ["-r", str(rate_out)]
            if self.args:
                args += self.args
            self.log.debug("ffmpeg args: %s", args)

            # invoke ffmpeg
            pathfmt.set_extension(self.extension)
            if self.twopass:
                if "-f" not in args:
                    args += ["-f", self.extension]
                null = "NUL" if os.name == "nt" else "/dev/null"
                args += ["-passlogfile", tempdir + "/ffmpeg2pass", "-pass"]
                subprocess.Popen(args + ["1", "-y", null]).wait()
                subprocess.Popen(args + ["2", pathfmt.realpath]).wait()
            else:
                args.append(pathfmt.realpath)
                subprocess.Popen(args).wait()

        if self.delete:
            pathfmt.delete = True
        else:
            pathfmt.set_extension("zip")

    @staticmethod
    def calculate_framerate(framelist):
        counter = collections.Counter(frame["delay"] for frame in framelist)
        fps = "1000/{}".format(min(counter))
        return (fps, None) if len(counter) == 1 else (None, fps)


__postprocessor__ = UgoiraPP
