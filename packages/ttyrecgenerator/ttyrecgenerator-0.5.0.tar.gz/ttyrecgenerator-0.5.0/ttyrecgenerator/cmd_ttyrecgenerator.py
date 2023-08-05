## @namespace ttyrecgenerator.cmd_ttyrecgenerator
## @brief Program that generate gifs and video from console output
import argparse
import time
import colorama
import datetime
import gettext
import os
import pkg_resources
import platform
import subprocess

from .__init__ import __version__, __versiondate__
from .libttyrecgenerator import platform_incompatibility

try:
    t = gettext.translation('ttyrecgenerator', pkg_resources.resource_filename('ttyrecgenerator', "locale"))
    _ = t.gettext
except:
    print("Error loading translation")
    _ = str

def main():
    parser=argparse.ArgumentParser(prog='ttyrecgenerator', 
                                   description=_('Create an animated gif/video from the output of the program passed as parameter'), 
                                   epilog=_("Developed by Mariano Muñoz 2018-{} under GNU General Public License 3.0".format(__versiondate__.year)), 
                                   formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('program',  help=_("Path to program"))
    parser.add_argument('--output', help=_("Ttyrec output path"), action="store", default="ttyrecord.rec")
    parser.add_argument('--video', help=_("Makes a simulation and doesn't remove files"), action="store_true", default=False)
    args=parser.parse_args()

    if platform.system()!="Linux":
        print(platform_incompatibility())
    else:
        subprocess.run(["xterm", "-hold", "-bg", "black", "-geometry", "140x400", "-fa", "monaco", "-fs", "18", "-fg", "white", "-e", "ttyrec -e '{0}' {1}; ttygif {1}".format(args.program, args.output)])
        os.system("mv tty.gif {}.gif".format(args.output))
        if args.video==True:
            subprocess.run(["ffmpeg", "-i", "{}.gif".format(args.output), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "{}.mp4".format(args.output)])

if __name__ == "__main__":
    main()