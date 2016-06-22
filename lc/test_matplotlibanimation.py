import sys
import numpy as np
from PyQt4 import QtGui

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.path as path
import matplotlib.patches as patches
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

from functools import partial 


class Histo_Anim(QtGui.QWidget):
    def __init__(self):
        super(Histo_Anim, self).__init__()
        self.start()

    def start(self):
        self.setWindowTitle('Game of life')
        gridLayout = QtGui.QGridLayout()
        self.setLayout(gridLayout)

 # histogram our data with numpy
        #Figure and subplot
        self.figure = plt.figure()
        canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(2,1, 2)
        self.ax2 = self.figure.add_subplot(2,1, 1)
        plt.xlabel('Source')
        canvas.draw()
        #win = self.figure.canvas.manager.window
        #win.after(100, self.update)
        #plt.show()
        #self.mat = ax.matshow(self.grid)
        ani = animation.FuncAnimation(self.figure, self.update, interval=10)

        gridLayout.addWidget(canvas,0,0)
        # get the corners of the rectangles for the histogram
        self.show()

    def update(self, data):
        for subplot in [self.ax, self.ax2]:
            subplot.clear()
            mu, sigma = 100, 15
            N = 4
            x = mu + sigma*np.random.randn(N)
            rects = subplot.bar(range(N), x,  align = 'center')
            for i in range(50):
                x = mu + sigma*np.random.randn(N)
                for rect, h in zip(rects, x):
                    rect.set_height(h)
                #self.figure.canvas.draw()

class Game_of_life(QtGui.QWidget):
    def __init__(self, N, ON, OFF):
        super(Game_of_life, self).__init__()
        self.N = N
        self.ON = ON
        self.OFF = OFF
        self.vals = [ON, OFF]
        self.grid = np.random.choice(self.vals, N*N, p=[0.2, 0.8]).reshape(N, N)        
        self.start()

    def start(self):
        self.setWindowTitle('Game of life')
        gridLayout = QtGui.QGridLayout()    
        self.setLayout(gridLayout)

        #Figure and subplot
        figure = plt.figure()
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot(111)
        canvas.draw()

        self.mat = ax.matshow(self.grid)
        ani = animation.FuncAnimation(figure, self.update, interval=50, save_count=50)

        #button
        restart = QtGui.QPushButton("Restart game of life")
        restart.clicked.connect(partial(self.restart_animation, ax=ax, figure=figure))

        gridLayout.addWidget(canvas,0,0)
        gridLayout.addWidget(restart, 1,0)

        self.show()
    def update(self, data):
        newGrid = self.grid.copy()
        for i in range(self.N):
            for j in range(self.N):
                total = (self.grid[i, (j-1)%self.N] + self.grid[i, (j+1)%self.N] + 
                        self.grid[(i-1)%self.N, j] + self.grid[(i+1)%self.N, j] + 
                        self.grid[(i-1)%self.N, (j-1)%self.N] + self.grid[(i-1)%self.N, (j+1)%self.N] + 
                        self.grid[(i+1)%self.N, (j-1)%self.N] + self.grid[(i+1)%self.N, (j+1)%self.N])/255
                if self.grid[i, j]  == self.ON:
                    if (total < 2) or (total > 3):
                        newGrid[i, j] = self.OFF
                else:
                    if total == 3:
                        newGrid[i, j] = self.ON
        self.mat.set_data(newGrid)
        self.grid = newGrid

    #simply restarts game data
    def restart_animation(self, ax, figure):
        self.grid = np.random.choice(self.vals, self.N*self.N, p=[0.2, 0.8]).reshape(self.N, self.N)
        self.mat = ax.matshow(self.grid)


def main():
    app = QtGui.QApplication(sys.argv)
    #widget = Game_of_life(100, 255, 0)
    widget = Histo_Anim()
    #widget can be implement in other layout
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()