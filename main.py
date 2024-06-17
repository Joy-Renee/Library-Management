import sys
from book_management import add_book, get_all_books, update_book_copies, delete_book
from users_management import add_user, get_all_user, delete_user
from status_management import status_book, return_book



def print_help():
    print("Usage:")
    print("  python main.py <command> <arguments>")
    print("Commands:")
    print("  book add <title> <author> <copies>")
    print("  book list")
    print("  book update <book_id> <new_copies>")
    print("  book delete <book_id>")
    print("  user add <name> <email>")
    print("  user list")
    print("  user delete <user_id>")
    print("  status <book_id> <user_id>")
    print("  return <status_id>")
    print("  help")

def main():
    if len(sys.argv) < 2:
        print_help()
        return
    
    command = sys.argv[1]

    if command == "book":
        subcommand = sys.argv[2]
        if subcommand == "add":
            title = sys.argv[3]
            author = sys.argv[4]
            copies = int(sys.argv[5])
            add_book(title, author, copies)
            print("Book added")
        elif subcommand == "list":
            books = get_all_books()
            for book in books:
                print(f"{book.id}: {book.title} by {book.author} - {book.copies} copies")
        elif subcommand == "update":
            book_id = int(sys.argv[3])
            new_copies = int(sys.argv[4])
            update_book_copies(book_id, new_copies)
            print("Book copies updated")
        elif subcommand == "delete":
            book_id = int(sys.argv[3])
            delete_book(book_id)
            print("Book deleted")

    elif command == "user":
        subcommand = sys.argv[2]
        if subcommand == "add":
            name = sys.argv[3]
            email = sys.argv[4]
            add_user(name, email)
            print("Member added")
        elif subcommand == "list":
            users = get_all_user()
            for user in users:
                print(f"{user.id}: {user.name} - Email: {user.email}")
        elif subcommand == "delete":
            user_id = int(sys.argv[3])
            delete_user(user_id)
            print("Member deleted")

    elif command == "status":
        book_id = int(sys.argv[2])
        user_id = int(sys.argv[3])
        status_book(book_id, user_id)
        print("Book borrowed ")

    elif command == "return":
        status_id = int(sys.argv[2])
        return_book(status_id)
        print("Book returned")

    else:
        print_help()

if __name__ == "__main__":
    main()