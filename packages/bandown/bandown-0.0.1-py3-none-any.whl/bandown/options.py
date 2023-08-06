import argparse
import os

def parseArgs():
    parser = argparse.ArgumentParser(
        prog='bandown',
        description='Download music from Bandcamp.')

    parser.add_argument(
        'URL',
        help='download specified track/artist/album')

    parser.add_argument(
        '--output',
        dest='directory',
        default=os.getcwd(),
        help='select output directory')

    args = parser.parse_args()
    return args
