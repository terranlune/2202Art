#!/usr/local/bin/python

from PyQt4 import QtGui, QtCore
import sys
SIZE = 20

        
class Example(QtGui.QWidget):
    Size = 20
    Speed = 100

    def __init__(self, painters):
        super(Example, self).__init__()
        self.painters = painters
        for painter in self.painters:
           painter.setup()
        self.painterIndex = 0
        self.tick = 0
        self.pixelBuffer = self.painters[self.painterIndex].pixelBuffer
        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.timerUpdate)
        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 19*SIZE, 13*SIZE)
        self.setWindowTitle('MA Sim')
        self.timer.start(50)
        self.painters[self.painterIndex].draw()
        self.show()

    def timerUpdate(self):
        self.repaint()
        self.painters[self.painterIndex].draw()
        self.timer.start(50)

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawFrame(event, qp)
        qp.end()

    def drawFrame(self, event, qp):
        qp.setBrush(QtGui.QColor(0,0,0))
        qp.drawRect(0, 0, 19*SIZE, 13*SIZE)
        for x in range(0, 19):
            for y in range(0, 13):
                self.drawPixel(qp, x, y)

    def drawPixel(self, qp, x, y):
        colorT = self.pixelBuffer.getPixel(x,y)
        color = QtGui.QColor(colorT[0], colorT[1], colorT[2])
        qp.setBrush(color)
        qp.setPen(color)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)
        qp.drawRoundedRect(x*SIZE+2, y*SIZE+2, SIZE-4, SIZE-4, 10.0, 10.0)


    def timerEvent(self, event):
        if (True):
            pass
        else:
            QtGui.QFrame.timerEvent(self, event)
        
def main():        
    app = QtGui.QApplication(sys.argv)
    mod = __import__(sys.argv[1])
    cls = getattr(mod, "UserPainter")
    ex = Example([cls()])
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

