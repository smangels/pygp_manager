#!/usr/bin/env python

import sys
try:
   import gnupg
except ImportError as e:
   sys.stderr.write("failed to load module: %s" % str(e))

import pygtk
import gtk


class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()
        
        self.set_title("Python PGP Manager")
        self.set_size_request(600, 800)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", self.on_destroy)
        
        fixed = gtk.Fixed()

        quit = gtk.Button("Press here to quit")
        quit.connect("clicked", self.on_clicked)
        quit.set_size_request(150, 35)

        fixed.put(quit, 50, 50)

        self.add(fixed)
        self.show_all()
        
    def on_destroy(self, widget):
        gtk.main_quit()
        
    def on_clicked(self, widget):
        gtk.main_quit()


def main():
    print ("Successfully imported GNUPG")

    # test creating an instance of PGP
    my_gpg = gnupg.GPG()
    del my_gpg

    # Create the main window
    base = PyApp()
    gtk.main()

if __name__ == "__main__":
   main()
