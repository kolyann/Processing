add_library('gifAnimation')
from gifAnimation import GifMaker
import sys
import os
import re
import __main__
import datetime

class gifExport:
    def init(self):
        print("BLYAAA")
        self.__init__(locals())
    def __init__(
                 self,
                 recording = False,
                 path = os.environ['USERPROFILE']+"\\Pictures\\ProcessingResult",
                 name = re.sub('\..*','',__main__.__file__),
                 verbose = False
                 ):
        self.recording = recording
        self.verbose = verbose
        fpath = ''.join([
                         path,"\\",name,"\\",name,"_",
                         str(datetime.datetime.now().strftime('%Y%m%d_%H%M-%S')),".gif"
                         ])
        self.GM = None
        if(self.recording):
            self.GM = GifMaker(__main__.__papplet__,fpath,1)
            self.GM.setRepeat(0)
            if(self.verbose):
                print 'Start record in',fpath;
    
    def rec(self):
        if(self.recording):
            self.GM.setDelay(1000/__main__._fRate)
            self.GM.addFrame()
    
    def finish(self):
        if(self.recording):
            self.GM.finish()
            self.recording = False
            if(self.verbose):
                print('Finish record')
    
#    def __del__(self):
#        self.finish()
    
