# file_reader.py

def read_file(file_name):
    """
    Reads the content of a file and returns it as a string.

    Args:
    file_name (str): The name of the file to read.

    Returns:
    str: The content of the file.
    """
    try:
        with open(file_name, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
        return None
