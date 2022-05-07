import gi

# Import GTK 3.0
gi.require_version("Gtk", "3.0")
gi.require_version('Notify', '0.7')

from gi.repository import Gtk
from gi.repository import Notify

# Init Window
class IslandGenerator(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Island Generator")
        Gtk.Window.set_default_size(self, 640, 480)

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)
       
        # Set Button
        self.button = Gtk.Button(label="Generate")
        self.button.set_halign(Gtk.Align.LEFT)
        self.button.set_valign(Gtk.Align.HIGH)
        # Uncomment when algo is added
        #self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)

    #def on_button_clicked(self, widget):
        # Insert algo here

# Do not touch
win = IslandGenerator()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()