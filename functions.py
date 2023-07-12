FILEPATH = "todos.txt"


def get_todos(filename =FILEPATH):  #finename todos.txt as a default arg.
    """
        Read a text file and return the list of
        to-do items.
    """
    with open(filename, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos( todos_arg, filename =FILEPATH):
    """Write the to-do item list in the text file. """
    with open(filename, 'w') as file:
        file.writelines(todos_arg)  #no return type needed coz this prog. is perforoming a function own its own and return value is not nedded

if __name__ == "__main__":  # to avoid the code below from being executed in main.py
    print("Hello")
    print(get_todos())