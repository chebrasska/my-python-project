from utils import greet
from config import APP_NAME, VERSION

def main():
    print(f"Запуск {APP_NAME} v{VERSION}")
    print(greet("Мир"))

if __name__ == "__main__":
    main()
