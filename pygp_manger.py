#!/usr/bin/env python

import sys
try:
   import gnupg
except ImportError as e:
   sys.stderr.write("failed to load module: %s" % str(e))


def main():
   print ("Successfully imported GNUPG")
   
   my_gpg = gnupg.GPG()
   
   del my_gpg

   sys.exit(0)

if __name__ == "__main__":
   main()