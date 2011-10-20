'''
Created on Oct 20, 2011

@author: patrick
'''

import sys
import pygame

class JoystickController:
    '''
    This class handles joystick input (from a ps3 controller) 
    using pygame as its libsdl wrapper.
    '''

    def __init__(self):
        print 'init joystickctrl'
        self.x = 0.0
        self.y = 0.0
        
        pygame.display.init()
        pygame.joystick.init()
        self.j = pygame.joystick.Joystick(0) 
        self.j.init() 
        
        if self.j.get_init() == True:
            print "Joystick has successfully been initialized."
        else:
            print "Failed to initialize joystick."
            sys.exit()
        
        #Get and print joystick ID 
        print "Joystick ID: ", self.j.get_id()
        
        #Get and print joystick name 
        print "Joystick Name: ", self.j.get_name() 
        
        #Get and print number of axes 
        print "No. of axes: ", self.j.get_numaxes() 
        
        #Get and print number of trackballs 
        print "No. of trackballs: ", self.j.get_numballs() 
        
        #Get and print number of buttons 
        print "No. of buttons: ", self.j.get_numbuttons() 
        
        #Get and print number of hat controls
        print "No. of hat controls: ", self.j.get_numhats() 
            
    def run(self):
        '''
        This is the event-receiving main loop
        Events are delegated to the subclass
        '''
        #Setup event information and print data from joystick 
        while 1:
            e = pygame.event.wait()
            
            if e.type == pygame.JOYAXISMOTION or e.type == pygame.JOYBUTTONDOWN:
                self.handleJoyEvent(e)
    
    def handleJoyEvent(self, e):
        if e.type == pygame.JOYBUTTONDOWN:
            #print '%s: %s' % (pygame.event.event_name(e.type), e.dict)
        
            if 'button' in e.dict:
                val = e.dict['button']
                
                if val == 4:
                    self.didReceiveUp()
                elif val == 7:
                    self.didReceiveLeft()
                elif val == 5:
                    self.didReceiveRight()
                elif val == 6:
                    self.didReceiveDown()
                elif val == 14:
                    self.didReceiveX()
                elif val == 16:
                    print 'Good bye!'
                    self.j.quit()
                    pygame.joystick.quit()
                    sys.exit()
                else:
                    pass
        elif e.type == pygame.JOYAXISMOTION:
            if e.dict['axis'] == 0:
                self.y = e.dict['value']
            elif e.dict['axis'] == 1:
                self.x = e.dict['value']

            self.didReceiveVector(self.x, self.y)
        else:
            pass
