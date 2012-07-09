# -*- coding: utf-8 -*-
"""
Created on Mon Jul 09 00:29:00 2012

@author: Ronny
"""
import cv
import cv2

class Writer:
    config = None
    _filedst = None
    _codecs = (('X','V','I','D'), ('D','I','V','X'), ('I','Y','U','V'))
    _writer = None
    _size = None
    _alive = True
    
    def __init__(self, args):
        self.config = args
        self._filedst = self.config.outfile
        self._size = self.config.size
        cc = self._codecs[0]
        self._writer = cv2.VideoWriter(self._filedst, cv.CV_FOURCC(cc[0], cc[1], cc[2], cc[3]), 30.0, self._size, 1)
  
    def opendst(self):
        print self._filedst
        
    def write(self, frame):
        self._writer.write( frame )
        
    def write_thread(self, fb, ev):
        nleave_frames = 1
        while self._alive:
            ev.wait()
            if not self._alive:
                print 'Flushing remaining frames from  buffer to file...'
                nleave_frames = 0

            frames_written = 0
            while len(fb) > nleave_frames:
                self._writer.write( fb.pop() )
                frames_written += 1
                if frames_written > 1:                
                    print str(frames_written) + ' frames written!'
        
    def close( self ):
        del( self._writer )