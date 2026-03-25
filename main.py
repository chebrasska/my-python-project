from utils import greet, multiply, subtract, divide
from config import APP_NAME, VERSION

def show_menu():
    print(f"\n=== {APP_NAME} v{VERSION} ===")
    print("1. Приветствие")
    print("2. Умножение")
    print("0. Выход")

def main():
    while True:
        show_menu()
        choice = input("Выберите действие: ")
        if choice == "1":
            name = input("Введите имя: ")
            print(greet(name))
        elif choice == "2":
            a = float(input("Число a: "))
            b = float(input("Число b: "))
            print(f"Результат: {multiply(a, b)}")
        elif choice == "0":
            print("Выход")
            break

if __name__ == "__main__":
    main()