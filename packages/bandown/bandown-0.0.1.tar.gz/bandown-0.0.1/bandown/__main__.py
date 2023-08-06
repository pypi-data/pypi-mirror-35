#/usr/bin/env python

from bandown import Bandown, options

def main():
    args = options.parseArgs()
    Bandown.download(args.URL, args.directory)

if __name__=='__main__':
    main()
