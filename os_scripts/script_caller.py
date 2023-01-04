import os
from subprocess import call


class CallPythonFile:
    """A class for calling a Python script file.

    Attributes:
        path (str): The path to the Python script file.
    """

    def __init__(self, file_path):
        """Initializes the `CallPythonFile` class.

        Args:
            file_path (str): The path to the Python script file.
        """
        self.path = file_path


    def is_python_script(self):
        """Checks if the file is a Python script.

        Returns:
            bool: True if the file is a Python script, False otherwise.
        """
        return self.path.endswith('.py')


    def call_python_script(self):
        """Calls the Python script file.

        Raises:
            FileNotFoundError: If the file does not exist.
            PermissionError: If the user does not have permission to execute the file.
        """
        if not self.is_python_script():
            raise ValueError("The file is not a Python script.")
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"The file {self.path} does not exist.")
        try:
            call(["py", "{}".format(self.path)])
        except PermissionError:
            print("You do not have permission to execute the file.")
