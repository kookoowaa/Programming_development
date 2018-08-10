from tkinter import *  #### import tkinter와 차이는 tkinter.메서드를 사용하지 않아도 되는 점에 있음

class Table:
    def __init__(self, window, colour='black', net_colour='green', width=600, height=400, vertical_net=False, horizontal_net=False):
        self.width = width
        self.height = height
        self.colour = colour
        self.canvas = Canvas(window, bg = self.colour, height = self.height, width = self.width)
        self.canvas.pack()
        self.vertical_net = vertical_net
        self.horizontal_net = horizontal_net
        self.net_colour = net_colour
        
       #### 점수표
        font  = ('monaco', 72)
        self.scoreboard = self.canvas.create_text(300, 65, font = font, fill = 'darkgreen')
     
    
    def draw_net(self):
        if (self.vertical_net):
            self.canvas.create_line(self.width/2, 0, self.width/2,
                                   self.height, width=2, fill=self.net_colour, dash = (15,23))
        if(self.horizontal_net):
            self.canvas.create_line(0, self.height/2, self.width, 
                                    self.height/2, width=2, fill=self.net_colour, dash = (15,23))
        #### canvas.create_line([top x-coord], [top y-choord], [bottomx-coord], [botton y-choord], [width], [line colour], [dash type])
        
    def draw_rectangle(self, rectangle):
        x1 = rectangle.x_posn
        x2 = rectangle.x_posn + rectangle.width
        y1 = rectangle.y_posn
        y2 = rectangle.y_posn + rectangle.height
        c = rectangle.colour
        return self.canvas.create_rectangle(x1, y2, x2, y2, fill=c)
    
    def draw_oval(self, oval):
        x1 = oval.x_posn
        x2 = oval.x_posn + oval.width
        y1 = oval.y_posn
        y2 = oval.y_posn + oval.height
        c = oval.colour
        return self.canvas.create_oval(x1, y2, x2, y2, fill=c)
    
    def move_item(self, item, x1, y1, x2, y2):
        self.canvas.coords(item, x1, y1, x2, y2)
        
    def remove_item(self, item):
        self.canvas.delete(item)
        
    def change_item_colour(self, item, c):
        self.canvas.itemconfigure(item, fill = c)   
        
    # canvas에 점수 표시
    def draw_score(self, left, right):
        scores = str(right) + "  " + str(left)
        self.canvas.itemconfigure(self.scoreboard, text=scores)
