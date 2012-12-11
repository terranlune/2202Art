#!/usr/bin/python

from PyQt4 import QtGui, QtCore
import sys 

SIZE = 20

class Example(QtGui.QWidget):
    Size = 20
    Speed = 100

    def __init__(self):
        super(Example, self).__init__()
        self.pixelBuffer = []
        pixel = 0
        for x in range(19):
            for y in range(13):
                self.pixelBuffer.append((pixel, pixel, pixel))
                pixel +=1
        
        self.timer = QtCore.QBasicTimer()
        self.initUI()

    def initUI(self):      
        
        self.setGeometry(300, 300, 19*SIZE, 13*SIZE)
        self.setWindowTitle('MA Sim')
        self.show()

    def paintEvent(self, event):
        print self.pixelBuffer
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawFrame(event, qp)
        qp.end()

    def drawFrame(self, event, qp):
        for x in range(0, 19):
            for y in range(0, 13):
                self.drawPixel(qp, x, y)

    def drawPixel(self, qp, x, y):
        colorT = self.pixelBuffer[y*19+x]
        qp.setBrush(QtGui.QColor(colorT[0], colorT[1], 
                                 colorT[2]))
        qp.drawRect(x*SIZE, y*SIZE, SIZE, SIZE)


    def timerEvent(self, event):
        if (True):
            pass
        else:
            QtGui.QFrame.timerEvent(self, event)
        
def main():    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

