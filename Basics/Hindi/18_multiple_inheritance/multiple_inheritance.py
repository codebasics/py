class superMario():                                                            
    def move(self):                                             
        print('I am moving')


class jump():                                            
    def jump_above(self):
            print('I just jumped')

class mushroom():                                             
    def eat_mushroom(self):
            print('I have become big now')


class Mario(superMario, mushroom, jump):    
        pass                                                                 
play = Mario()                                           
play.move()                                                        
play.eat_mushroom() 
play.jump_above()