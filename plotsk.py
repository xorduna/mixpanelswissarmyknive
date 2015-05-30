'''
Created on Jan 7, 2014

@author: xorduna
'''

class CharPlot(object):
    
    def __init__(self, height, width):
        self.plot = []
        self.height = height
        self.width = width
        for i in range(0, height):
            self.plot.append([' '] * width)
            #for j in range(0, width):
            #    self.plot.append(" ")
        pass
    
    def put(self, x, y, element):
        e = str(element)[0] #get the first element
        #check colision
        if (self.plot[self.height - y][x] != " "):
            print 'colision'
        self.plot[self.height - y][x] = e
        
    def print_chart(self):
        
        print '+' + '- ' * self.width + '+'
        for row in range(0, self.height):
            s = ""
            for c in self.plot[row]:
                s = s + c + " "
            #print '|' + "".join(self.plot[row]) + '|'
            print '|' + s + '|'
        
        print '+' + '- ' * self.width + '+'
        
if __name__ == '__main__':
    
    c = CharPlot(50, 50)
    c.put(23, 32, '1')
    c.put(8, 8, '2')
    c.print_chart()
    