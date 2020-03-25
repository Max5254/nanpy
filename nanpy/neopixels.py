from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)


class NeoPixel(ArduinoObject):

    def __init__(self, port, length, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new', port, length)

    @arduinoobjectmethod
    def setPixel(self, index, red, green, blue):
        pass

    @arduinoobjectmethod
    def show(self):
        pass