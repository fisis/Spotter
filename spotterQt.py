# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 21:14:43 2012
@author: <Ronny Eichler> ronny.eichler@gmail.com

Track position LEDs and sync signal from camera or video file.

Usage:
    spotter.py --source SRC [--outfile DST] [options]
    spotter.py -h | --help

Options:
    -h --help           Show this screen
    -f --fps FPS        Fps for camera and video
    -s --source SRC     Path to file or device ID [default: 0]
    -S --Serial         Serial port to uC [default: None]
    -o --outfile DST    Path to video out file [default: None]
    -d --dims DIMS      Frame size [default: 320x200]
    -H --Headless       Run without interface
    -D --DEBUG          Verbose output

To do:
    - destination file name may consist of tokens to automatically create,
      i.e., %date%now%iterator3$fixedstring
    - track low res, but store full resolution
    - can never overwrite a file

#Example:
    --source 0 --outfile test.avi --size=320x200 --fps=30

"""

NO_EXIT_CONFIRMATION = True

import sys
import os
import platform
from PyQt4 import QtGui, QtCore
import logging

#project libraries
sys.path.append('./lib')
from spotter import Spotter
import utils

#Qt user interface files
sys.path.append('./ui')
from GLFrame import GLFrame
from mainUi import Ui_MainWindow
import TabFeatures
import TabObjects
import TabRegions

#command line handling
sys.path.append('./lib/docopt')
from docopt import docopt


__version__ = 0.01

class Main(QtGui.QMainWindow):

    led_templates = [['redLED', ( 160, 5 ), False],
                     ['blueLED', ( 105, 135 ), False],
                     ['greenLED', ( 15, 90 ), True]]


    def __init__(self, source, destination, fps, size, gui, serial):
        QtGui.QMainWindow.__init__(self)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Exit Signals
        self.ui.actionE_xit.setShortcut('Ctrl+Q')
        self.ui.actionE_xit.setStatusTip('Exit Spotter') 
        self.connect(self.ui.actionE_xit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.centerWindow()

        # About window        
        self.connect(self.ui.actionAbout, QtCore.SIGNAL('triggered()'), self.about)
        
        # Menubar items
        self.ui.actionFile.triggered.connect(self.openFile)
        

        # Spotter main class, handles Grabber, Writer, Tracker, Funker      
        self.spotter = Spotter(source, destination, fps, size, gui, serial)
        
        # OpenGL frame        
        self.frame = GLFrame()
        self.ui.frame_video.addWidget(self.frame)
        self.frame.setSizePolicy( QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding )

        # For debugging, later as standard use loader
        self.connect(self.ui.btn_load_templates, QtCore.SIGNAL('clicked()'), self.load_templates)

        # Features tab widget
        self.feature_tabs = []
        self.connect(self.ui.tab_features, QtCore.SIGNAL('currentChanged(int)'), self.tab_features_switch)
        self.connect(self.ui.btn_new_feature_tab, QtCore.SIGNAL('clicked()'), self.add_feature)

        # Objects tab widget
        self.object_tabs = []
        self.connect(self.ui.tab_objects, QtCore.SIGNAL('currentChanged(int)'), self.tab_objects_switch) 
        self.connect(self.ui.btn_new_object_tab, QtCore.SIGNAL('clicked()'), self.add_object)
        
        # Regions tab widget
        self.region_tabs = []
        self.connect(self.ui.tab_regions, QtCore.SIGNAL('currentChanged(int)'), self.tab_regions_switch) 
        self.connect(self.ui.btn_new_region_tab, QtCore.SIGNAL('clicked()'), self.add_region)


        # Starts main frame grabber loop
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.refresh)
        self.refresh()
        self.frame.resizeFrame()
        self.timer.start(30)
       

    def about(self):
        """ About message box. Credits. Links. Jokes. """
        QtGui.QMessageBox.about(self, "About",
                """<b>Spotter</b> v%s
               <p>Copyright &#169; 2012-2013 <a href=mailto:ronny.eichler@gmail.com>Ronny Eichler</a>.
               <p>This application can and will be used for funs.
               <p>Python %s -  PyQt4 version %s - on %s""" % (__version__,
                platform.python_version(), QtCore.QT_VERSION_STR, platform.system()))


    def centerWindow(self):
        """ Centers main window on screen."""
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
 
 
    def load_templates(self):
        """ Loads and creates all LEDs and Objects from templates. This will
        probably be the place later the standard set of features/objects/ROIs
        etc. will be handled on startup.
        TODO: Add Object templates
        """
        for led in self.led_templates:
            self.add_feature(led)

 
    #Feature Tab List Updates
    def tab_features_switch(self, idx_tab = 0):
        """ Switch to selected tab or create a new tab if the selected tab is
        the last, which should be the "+" tab. Switching through the tabs with
        the mousewheel can cause to create a lot of tabs unfortunately.
        TODO: Mousewheel handling.
        """
        if idx_tab == self.ui.tab_features.count() - 1:
            self.add_feature()
        else:
            self.ui.tab_features.setCurrentIndex(idx_tab)


    def add_feature(self, template = None):
        """ Create a feature from trackables and add a corresponding tab to
        the tab widget, which is linked to show and edit feature properties.
        TODO: Create new templates when running out by fitting them into
        the colorspace somehow.
        """
        if not template:
            template = self.led_templates[self.ui.tab_features.count()-2]
        feature = self.spotter.tracker.addLED(*template)
        new_tab = self.add_tab(self.ui.tab_features, TabFeatures, feature)
        self.feature_tabs.append(new_tab)

            
    # Object Tab List Updates
    def tab_objects_switch(self, idx_tab = 0):
        """ Switch to selected tab or create a new tab if the selected tab is
        the last, which should be the "+" tab. Switching through the tabs with
        the mousewheel can cause to create a lot of tabs unfortunately.
        TODO: Mousewheel handling.
        """
        if idx_tab == self.ui.tab_objects.count() - 1:
            self.add_object()
        else:
            self.ui.tab_objects.setCurrentIndex(idx_tab)

    def add_object(self, template = None):
        """ Create a new object that will be linked to LEDs and/r ROIs to
        track and trigger events.
        TODO: Create new objects even when running out of templates for example
        by randomizing offsets.
        """
        new_object = self.spotter.tracker.addOOI(self.spotter.tracker.leds[0:2], "Subject")
        self.add_tab(self.ui.tab_objects, TabObjects, new_object)
        self.object_tabs.append(new_object)


    # Object Tab List Updates
    def tab_regions_switch(self, idx_tab = 0):
        """ Switch to selected tab or create a new tab if the selected tab is
        the last, which should be the "+" tab. Switching through the tabs with
        the mousewheel can cause to create a lot of tabs unfortunately.
        TODO: Mousewheel handling.
        """
        if idx_tab == self.ui.tab_regions.count() - 1:
            self.add_region()
        else:
            self.ui.tab_regions.setCurrentIndex(idx_tab)

    def add_region(self, template = None):
        """ Create a new region of interest that will be that will be linked
        to Objects with conditions to trigger events.
        TODO: New regions created empty!
        """
        new_region = self.spotter.tracker.addROI()
        self.add_tab(self.ui.tab_regions, TabRegions, new_region)
        self.region_tabs.append(new_region)


    def add_tab(self, tabwidget, newTabClass, tab_equivalent):
        """ Add new tab with Widget newTabClass and switches to it. The
        tab_equivalent is the object that is being represented by the tab,
        for example an LED or Object.
        """
        new_tab = newTabClass.Tab(self, tab_equivalent )
        tabwidget.insertTab(tabwidget.count() - 1, new_tab, new_tab.name)
        tabwidget.setCurrentIndex(tabwidget.count()-2)
        return new_tab


    def remove_tab(self, tabwidget, tab):
        """ Removing is trickier, as it has to delete the features/objects
        from the tracker!
        """
        
    def update_current_tab(self):
        """ Currently visible tab is the only one that requires to be updated
        live when parameters of its associated object change, e.g. coordinates
        of tracked objects or LEDs. The rest should happen behind the scenes
        in the spotter sub-classes.
        """
        curr_parent_tab = self.ui.tab_parameters.tabText(self.ui.tab_parameters.currentIndex())
        if curr_parent_tab == "Features":
            self.ui.tab_features.widget(self.ui.tab_features.currentIndex()).update()
        elif curr_parent_tab == "Objects":
            self.ui.tab_objects.widget(self.ui.tab_objects.currentIndex()).update()
        elif curr_parent_tab == "ROIs":
            self.ui.tab_regions.widget(self.ui.tab_regions.currentIndex()).update()
        elif curr_parent_tab == "SerialOut":
            print "Serial"
        else:
            pass
 
    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open Video', os.getenv('HOME'))
        print filename
 
 
    def closeEvent(self, event):
        """ Exiting the interface has to kill the spotter class and subclasses
        properly, especially the writer and serial handles, otherwise division
        by zero might be imminent.
        """
        if NO_EXIT_CONFIRMATION:
            event.accept()
            return
        reply = QtGui.QMessageBox.question(self, 'Exit confirmation', 'Are you sure?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()       


    def refresh(self):
        self.spotter.update()
        self.frame.frame = self.spotter.newest_frame
        
        # Append Object tracking markers to the list of things that have 
        # to be drawn onto the GL frame
        for l in self.spotter.tracker.leds:
            if not l.pos_hist[-1] == None and l.marker_visible:
                self.frame.jobs.append([self.frame.drawCross, l.pos_hist[-1][0], l.pos_hist[-1][1], 14, l.lblcolor])
        
        for o in self.spotter.tracker.oois:
            if not o.guessed_pos == None:
                self.frame.jobs.append([self.frame.drawCross, o.guessed_pos[0], o.guessed_pos[1], 8, (1.0, 1.0, 1.0, 1.0), 7, True])
                self.frame.jobs.append([self.frame.drawTrace, o.guessed_pos[0], o.guessed_pos[1], 8, (1.0, 1.0, 1.0, 1.0), 7, True])

        self.frame.updateWorld()
        
        self.update_current_tab()



#############################################################
def main(source, destination, fps, size, gui, serial):
    app = QtGui.QApplication([])
    window = Main(source, destination, fps, size, gui, serial)
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":                                  #
#############################################################

    # Command line parsing
    ARGDICT = docopt( __doc__, version=None )
    DEBUG   = ARGDICT['--DEBUG']
    if DEBUG: print( ARGDICT )

    # Debug logging
    log = logging.getLogger('ledtrack')
    loghdl = logging.StreamHandler()#logging.FileHandler('ledtrack.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s') #
    loghdl.setFormatter( formatter )
    log.addHandler( loghdl )
    if DEBUG:
        log.setLevel( logging.INFO ) #INFOERROR
    else:
        log.setLevel( logging.ERROR ) #INFOERROR    
        
    # Frame size parameter string 'WIDTHxHEIGHT' to size tupple (WIDTH, HEIGHT)
    size = (0, 0) if not ARGDICT['--dims'] else tuple( ARGDICT['--dims'].split('x') )
        
    # no GUI, may later select GUI backend, i.e., Qt or cv2.highgui etc.
    gui = 'Qt' if not ARGDICT['--Headless'] else ARGDICT['--Headless']
            
    # Qt main window which instantiates spotter class with all parameters    
    main(source    = ARGDICT['--source'],
         destination = utils.dst_file_name( ARGDICT['--outfile'] ),
         fps         = ARGDICT['--fps'],
         size        = size,
         gui         = gui,
         serial      = ARGDICT['--Serial'])
