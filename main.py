import sys
from pyfiglet import Figlet

custom_fig = Figlet(font='Big')
print(custom_fig.renderText('SubSync'))

FILE_NAME = 'subscriptions.txt'


def load_subscriptions():
    subscriptions = {}
    try:
        with open(FILE_NAME, 'r') as file:
            for line in file:
                name, price = line.strip().split(',')
                subscriptions[name] = float(price)
    except FileNotFoundError:
        pass
    return subscriptions


def save_subscriptions(subscriptions):
    with open(FILE_NAME, 'w') as file:
        for name, price in subscriptions.items():
            file.write(f"{name},{price}\n")


def add_subscription(subscriptions, name, price):
    if name in subscriptions:
        print(f"Subscription '{name}' already exists.")
    else:
        confirm = input(f"Are you sure you want to add subscription '{name}' with price {price}? (yes/no): ")
        if confirm.lower() == 'yes':
            subscriptions[name] = price
            save_subscriptions(subscriptions)
            print(f"Added subscription '{name}' with price {price}.")
        else:
            print("Subscription not added.")


def delete_subscription(subscriptions, name):
    if name in subscriptions:
        confirm = input(f"Are you sure you want to delete subscription '{name}'? (yes/no): ")
        if confirm.lower() == 'yes':
            del subscriptions[name]
            save_subscriptions(subscriptions)
            print(f"Deleted subscription '{name}'.")
        else:
            print("Subscription not deleted.")
    else:
        print(f"Subscription '{name}' not found.")


def edit_subscription(subscriptions, name):
    if name in subscriptions:
        try:
            new_price = float(input(f"Enter new price for subscription '{name}': "))
            confirm = input(f"Are you sure you want to edit the subscription '{name}' price to {new_price}? (yes/no): ")
            if confirm.lower() == 'yes':
                subscriptions[name] = new_price
                save_subscriptions(subscriptions)
                print(f"Updated subscription '{name}' with new price {new_price}.")
            else:
                print("Subscription not updated.")
        except ValueError:
            print("Invalid price. Please enter a number.")
    else:
        print(f"Subscription '{name}' not found.")


def view_subscriptions(subscriptions):
    if not subscriptions:
        print("No subscriptions found.")
    else:
        total_price = 0
        print("\nSubscriptions:")
        for name, price in subscriptions.items():
            print(f"- {name}: ${price:.2f}")
            total_price += price
        print(f"Total price: ${total_price:.2f}")


def about_subsync():
    print("\nAbout SubSync")
    print("-" * 30)
    print("SubSync is a subscription tracker that helps you manage and track your monthly subscriptions.")
    print("With SubSync, you can:")
    print("1. Add new subscriptions with their monthly cost.")
    print("2. Delete subscriptions you no longer need.")
    print("3. View all your subscriptions and their total monthly cost.")
    print("-" * 30)
    input("Press Enter to return to the main menu.")


def main():
    subscriptions = load_subscriptions()
    print("SubSync is a subscription tracker used to manage your active subscriptions")
    while True:
        print("\n SubSync Subscription Tracker")
        print("-" * 30)
        print("1. Add Subscription")
        print("2. Delete Subscription")
        print("3. View Subscriptions")
        print("4. Edit Subscription")
        print("5. About SubSync")
        print("6. Exit")
        print("-" * 30)
        choice = input("Enter your choice number: ")

        if choice == '1':
            name = input("Enter subscription name: ")
            try:
                price = float(input("Enter subscription price per month: "))
                add_subscription(subscriptions, name, price)
            except ValueError:
                print("Invalid price. Please enter a number.")
        elif choice == '2':
            name = input("Enter subscription name to delete: ")
            delete_subscription(subscriptions, name)
        elif choice == '3':
            view_subscriptions(subscriptions)
        elif choice == '4':
            name = input("Enter subscription name to edit: ")
            edit_subscription(subscriptions, name)
        elif choice == '5':
            about_subsync()
        elif choice == '6':
            print("Exiting program.")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == '__main__':
    main()
