import cv2
import filters
from managers import WindowManager,CaptureManager
import os
os.chdir(r'F:\Python练习\Opencv练习\OK')
class Cameo(object):
    def __init__(self):
        self._windowManager=WindowManager('Cameo',self.onKeypress)
        self._captureManager=CaptureManager(cv2.VideoCapture(0),self._windowManager,True)
        self._curveFilter=filters.BlurFilter()
    def run(self):
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame=self._captureManager.frame
            #add additional function here
            filters.strokeEdges(frame,frame)
            self._curveFilter.apply(frame,frame)
            
            self._captureManager.exitFrame()
            self._windowManager.processEvents()
        self._captureManager._capture.release()
    def onKeypress(self,keycode):
        if keycode==32:#space
            self._captureManager.writeImage('./data/pictures/screenshot.png')
        elif keycode==9: #tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo(r'F:/screen_cast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode==27: #exit
            self._windowManager.destroyWindow()
if __name__=='__main__':
    Cameo().run()
    

