MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = get_choice()
    convert_temperature(choice)


def get_choice():
    choice = input(">>> ").upper()
    return choice


def convert_temperature(choice):
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
            # print("Result:", fahrenheit, "Fahrenheit")
        elif choice == "F":
            fahrenheit = float(input("fahrenheit: "))
            celsius = 5 / 9 * (fahrenheit - 32)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = get_choice()


def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
