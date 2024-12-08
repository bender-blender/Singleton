class Singleton:
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None: # Проверяем, существует ли уже экземпляр
            cls._instance = super(Singleton,cls).__new__(cls) # Создаем новый экземпляр
        return cls._instance # Возвращаем существующий экземпляр
    
    def some_business_logic(self):
        # Метод с бизнес-логикой
        print("Выполнение бизнес-логики")



#singleton1 = Singleton()
#singleton2 = Singleton()

#print(singleton1 == singleton2)  # Вывод: True, оба объекта - это один и тот же экземпляр
