class auto:

    def __init__(self):
        self._sebesseg = 0

    @property
    def v(self):
        print('Ez a getter')
        return(self._sebesseg)

    @v.setter
    def v(self, ujseb):
        print('Ez a setter')
        if ujseb < 0:
            print('Ne már...')
            
        else:
            self._sebesseg=ujseb


kocsim = auto()

kocsim.v = 500

print(kocsim.v)