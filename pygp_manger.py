#!/usr/bin/env python

import sys
try:
   import gnupg
except ImportError as e:
   sys.stderr.write("failed to load module: %s" % str(e))

import pygtk
import gtk


class Base:
   def __init__(self):
      self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
      self.window.set_title('Py GPG Manager')
      self.window.set_size_request(400, 400)
      self.window.show()
      
      # remember to never show it
      self.menu = gtk.Menu()
      items = []
      
      # create a number of sub menues
      for i in range(1,3):
         buf = 'option_%d' % i
         
         item = gtk.MenuItem(buf)
         item.connect("activate", self.menuitem_response, buf)
         
         item.show()
         
         # append the item to a list, being attached to root menu
         self.menu.append(item)
         
      
      # create a root menue and append the submenue
      root_menu = gtk.MenuItem('File')
      root_menu.show()
      root_menu.set_submenu(self.menu)
      vbox = gtk.VBox(False, 0)
      self.window.add(vbox)
      vbox.show()
      self.menu.append(item)
      
      # Create a menu-bar to hold menus and add it to the main windows
      menu_bar = gtk.MenuBar()
      vbox.pack_start(menu_bar, False, False, 2)
      menu_bar.show()
      
      button = gtk.Button("press me")
      button.connect_object("event", self.button_press, self.menu)
      vbox.pack_end(button, True, True, 2)
      button.show()
      
      menu_bar.append(root_menu)
      
      
   def main(self):
      gtk.main()
      
   def menuitem_response(self, widget, string):
      '''print the string when a menu item is selected'''
      print "%s" % string
      
   def button_press(self, widget, event):
      pass


def main():
   print ("Successfully imported GNUPG")
   
   my_gpg = gnupg.GPG()
   
   del my_gpg
   
   base = Base()
   base.main()
   sys.exit()

if __name__ == "__main__":
   main()