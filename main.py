from __future__ import unicode_literals
from __future__ import print_function
import sys
from gooey import Gooey, GooeyParser
from pathlib import Path
import os

@Gooey()
def main():
    parser = GooeyParser(description="FFmpeg")
    parser.add_argument('Filename', widget="FileChooser")

    args = parser.parse_args(sys.argv[1:])

    if args.Filename:
        output_file = Path(args.Filename).stem + ".mp3"
        if os.path.exists(output_file):
            print("File already exists, ending")
            exit(0)
        else:
            os.system(f"ffmpeg -i '{args.Filename}' -ab 320k -map_metadata 0 -id3v2_version 3 '{output_file}'")

if __name__ == "__main__":
    sys.exit(main())
