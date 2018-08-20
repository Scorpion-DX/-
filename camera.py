import cv2
from managers import WindowManager, CaptureManager
import filters


class Cameo(object):
    def __init__(self):
        self._windowManger = WindowManager('Cameo', self.onKeypress)
        self._captureManger = CaptureManager(cv2.VideoCapture(0), self._windowManger, True)
        #self._curveFilter=filters.Blur()

    def run(self):
        """Run the main loop"""
        self._windowManger.createdWindow()
        while self._windowManger.isWindowCreated:
            self._captureManger.enterFrame()
            frame = self._captureManger.frame

            #filters.strokeEdges(frame,frame)
            #self._curveFilter.apply(frame,frame)

            self._captureManger.exitFrame()
            self._windowManger.processEvents()

    def onKeypress(self, keycode):
        """Handle a keypress.
        space   -> Take a screenshot
        tab     -> Start/stop recoding a screenshot
        escape  -> Quit
        """
        if keycode == 32:  # space
            self._captureManger.writeImage("./screenshot.png")
        elif keycode == 9:  # tab
            if not self._captureManger.isWritingVideo:
                self._captureManger.startWritingVideo('./screenshot.avi')
            else:
                self._captureManger.stopWritingVideo()
        elif keycode == 27:  # escape
            self._windowManger.destroyWindow()


if __name__ == '__main__':
    Cameo().run()
