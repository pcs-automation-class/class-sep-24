# #simple calculator with operations
#
# a = float(input("Please enter a value: "))
# b = float(input("Please enter b value: "))
# operation = input("Please enter operation type (+ , - , *, /): ")
#
#
# def calculator(a, b, operation):
#     if operation == '+':
#         return a + b
#     elif operation == '-':
#         return a - b
#     elif operation == '*':
#         return a * b
#     elif operation == '/':
#         if b != 0:
#             return a / b
#         else:
#             return "Cannot divide by zero"
#
#
# result = calculator(a, b, operation)
#
# print("Answer is: ", result)

#__________________________________________________


# List of authors, each author will have a list of books
authors = []

# Function to add a new author
def add_author(name):
    author = {
        "name": name,
        "books": []
    }
    authors.append(author)

# Function to add book to an author
def add_book(name, book):
    for author in authors:
        if author["name"] == name:
            author["books"].append(book)
            break
    else:
        print(f"author {name} not found!")

# Function to display authors and their books
def display_authors():
    for author in authors:
        print(f"Author: {author['name']}, Books: {author['books']}")

# Main program
def main():
    while True:
        print("\n1. Add an Author")
        print("2. Add a Book to an author")
        print("3. Display all authors")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter author's name: ")
            add_author(name)
        elif choice == '2':
            name = input("Enter author's name: ")
            book = str(input("Enter Book: "))
            add_book(name, book)
        elif choice == '3':
            display_authors()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose again.")

main()

