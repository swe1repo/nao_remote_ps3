'''
Created on Oct 20, 2011

@author: patrick
'''

from nao_remote_ps3.JoystickController import JoystickController

class NaoWalkController(JoystickController):
    '''
    This class executes movement commands based on gamepad input.
    '''

    def __init__(self):
        JoystickController.__init__(self)
        pass
    
    def didReceiveUp(self):
        print 'UP'
        
    def didReceiveDown(self):
        print 'DOWN'
        
    def didReceiveLeft(self):
        print 'LEFT'
        
    def didReceiveRight(self):
        print 'RIGHT'
    
    def didReceiveX(self):
        print 'X BUTTON'
        
    def didReceiveVector(self, x, y):
        print 'vector: x: %f, y: %f' %(x, y)
        
if __name__ == '__main__':
    wc = NaoWalkController()
    wc.run()
    pass