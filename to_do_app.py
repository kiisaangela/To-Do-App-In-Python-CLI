# Simple Python to-do app Project
# Improvements: exception handling, input validation, logging, and clearer user feedback.

import logging

# Logging for important events 
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

user_input = 'random'
data = list()

logging.info("To-do app started")


def showMenu():
    print("\nMenu:")
    print("1. Add an item:")
    print("2. Mark as Done:")
    print("3. View Items:")
    print("4. Exit:\n")


def get_menu_choice():
    """Returns the user's menu choice (1-4). Raises ValueError if choice is invalid."""
    raw = input("Enter Your Choice: ").strip()
    # validate menu input; ValueError for invalid choice
    if raw not in ('1', '2', '3', '4'):
        raise ValueError(f"Invalid menu choice: {raw!r}")
    return raw


while user_input != '4':
    showMenu()
    # exception handling — invalid option, EOF, or unexpected errors
    try:
        user_input = get_menu_choice()
    except ValueError as e:
        print("Invalid menu option. Please enter 1, 2, 3, or 4.")
        logging.warning("Invalid menu option entered: %s", e)
        user_input = 'random'
        continue
    except EOFError:
        logging.warning("Input stream ended unexpectedly")
        print("Input ended. Exiting.")
        break
    except Exception:
        logging.exception("Unexpected error reading menu choice")
        print("An unexpected error occurred. Please try again.")
        user_input = 'random'
        continue

    if user_input == '1':
        try:
            item = input("\nWhat is to be done ? ").strip()
        except (EOFError, KeyboardInterrupt):
            logging.warning("Input cancelled or ended while adding task")
            print("Cancelled.")
            continue

        # reject empty tasks (input validation)
        if not item:
            print("Task cannot be empty. Please enter a non-empty description.")
            logging.warning("Attempt to add empty task rejected")
            continue

        data.append(item)
        print("Added item:", item)
        logging.info("Task added: %s", item)

    elif user_input == '2':
        try:
            item = input("What is to be marked as Done ").strip()
        except (EOFError, KeyboardInterrupt):
            logging.warning("Input cancelled or ended while marking done")
            print("Cancelled.")
            continue

        if not item:
            print("Please enter the exact task text to mark as done.")
            logging.warning("Empty task removal attempt")
            continue

        if item in data:
            data.remove(item)
            print("Removed item:", item)
            logging.info("Task removed: %s", item)
        else:
            # clear feedback + log when user tries to remove non-existent task
            print("Item does not exist in the to-do list.")
            logging.warning("Attempt to remove non-existent task: %s", item)

    elif user_input == '3':
        print("\nList of TO-DO Items: ")
        if not data:
            print("  (no items)")
        for items in data:
            print(items)

    elif user_input == '4':
        print("\nGood Bye")
        logging.info("To-do app exited")