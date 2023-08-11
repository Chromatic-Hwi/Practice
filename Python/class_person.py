class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print('안녕하세요. {0}세의 {1}, {2} 라고 합니다.'.format(self.age, self.gender, self.name))
              
