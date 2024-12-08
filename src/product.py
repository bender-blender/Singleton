from singleton import Singleton

class Configuration(Singleton):

    def __init__(self):
        self.settings = {}
        self.load_settings()
    
    def load_settings(self):
        # Логика загрузки настроек из файла
        self.settings = {"theme": "dark", "language": "en"}

# Пример использования
config1 = Configuration()
config2 = Configuration()

print(config1.settings)  # {'theme': 'dark', 'language': 'en'}
print(config1 == config2)  # True
