class Cat:
    def __init__(self, name, color = '흰색'):
        self.name = name
        self.color = color
    
    
    def meow(self):
        print('내 이름은 {}, 색깔은 {}, 야옹'.format(self.name, self.color))
    

nabi = Cat('nabi')
nabi.meow()
nero = Cat('nero', '검은색')
nero.meow()
mimi = Cat('mimi', '갈색')
mimi.meow()