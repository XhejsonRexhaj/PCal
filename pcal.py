from src import calculator

def main():
    #example
    food = calculator.Calculator("Rasin", 70, 0.2, 16.1, 0.6)
    print(food.calculateCalories())

if __name__ == "__main__":
    main()

