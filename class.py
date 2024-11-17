class Motorcycle:
    is_engine_on = False
    is_headlight_on = False
    is_driving = False
    def turnEngineOn(self):
        print("Turning engine on. BROOM, BROOM")
        self.is_engine_on = True
    def turnEngineOff(self):
        print("Turning engine off")
        if self.is_driving:
            print('You tried to turn the engine off while driving '
                  'and crashed')
            return
        self.is_engine_on = False
    def turnHeadlightOn(self):
        print('Turning headlights on')
        self.is_headlight_on = True
    def turnHeadlightOff(self):
        print('Turning headlights off')
        self.is_headlight_on = False
    def startDriving(self):
        if not self.is_engine_on:
            print("You can't drive without turning the engine on!")
            return
        print("Starting to drive")
        self.is_driving = True

    def stopDriving(self):
        self.is_driving = False

    def lean(self, direction):
        if not self.is_driving:
            print("You leaned while not driving and crashed!")
            return
        print(f'Leaning {direction}')
    
    def turn_handlebars(self,direction):
        print(f'Turning handlebars {direction}')

    def turn(self, direction):
        if direction == 'left':
            self.turn_handlebars('right')
            self.lean('left')
        elif direction == 'right':
            self.turn_handlebars('left')
            self.lean('right')
        else:
            print("Didn't understand that direction")

    def __repr__(self):
        return (f'{self.make} {self.model} with engine '
                f'{"on" if self.is_engine_on ==True else "off"} '
                f'and headlight {"on" if self.is_headlight_on ==True else "off"}')
    def __init__(self, make, model):
        self.make = make
        self.model = model
moto = Motorcycle('Triumph','Harley')
print(moto)
moto.turnEngineOn()