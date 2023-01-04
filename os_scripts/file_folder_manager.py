import os, re, shutil


class FoldersInDirectory:
    """A class for manipulating files and folders in a directory.

    Attributes:
        parent_folder (str): The path to the parent folder.
    """


    def __init__(self, folder):
        """Initializes the `FoldersInDirectory` class.

        Args:
            folder (str): The path to the parent folder.
        """
        self.parent_folder = folder.replace("\\", "/")


    def exists(self, path):
        """Checks if a file or folder exists at the given path.

        Args:
            path (str): The path to the file or folder.

        Returns:
            bool: True if the file or folder exists, False otherwise.
        """
        return os.path.exists(path)


    def is_dir(self, path):
        """Checks if a path is a directory.

        Args:
            path (str): The path to check.

        Returns:
            bool: True if the path is a directory, False otherwise.
        """
        return os.path.isdir(path)


    def switch_to_parent_folder(self):
        """Switches the current working directory to the parent folder."""
        try:
            os.chdir(self.parent_folder)
            print('Changed directory to: {0}'.format(os.getcwd()))
        except FileNotFoundError:
            print("Directory: {0} does not exist".format(self.parent_folder))
        except NotADirectoryError:
            print("{0} is not a directory".format(self.parent_folder))
        except PermissionError:
            print("You do not have permissions to change to {0}".format(self.parent_folder))


    def switch_to_child_folder(self, child_folder):
        """Switches the current working directory to a child folder.

        Args:
            child_folder (str): The name of the child folder.

        Returns:
            str: The path to the child folder.
        """
        child_path = f"{self.parent_folder}/{child_folder}"
        if self.exists(child_path) and self.is_dir(child_path):
            os.chdir(child_path)
            return child_path
        else:
            print("Can't change the current working directory")


    def switch_folders(self, destination_folder):
        """Switches the current working directory to a destination folder.

        Args:
            destination_folder (str): The path to the destination folder.
        """
        if self.exists(destination_folder) and self.is_dir(destination_folder):
            os.chdir(destination_folder)
        else:
            print(f"path doesn't exist. Provided path: {destination_folder}")


    def move_folders(self, folder, destination_folder):
        """Moves a folder to a destination folder.

        Args:
            folder (str): The name of the folder to move.
            destination_folder (str): The path to the destination folder.
        """
        if self.exists(folder) and self.is_dir(folder):
            if self.exists(destination_folder) and self.is_dir(destination_folder):
                print(f"previous folder is : {destination_folder} and current folder is {folder}")
                shutil.move(folder, destination_folder)
                print(f"Moved {folder} into {destination_folder}")
            else:
                print(f"destination folder doesn't exist. Provided path: {destination_folder}")
        else:
            print(f"folder doesn't exist. Provided path: {folder}")


    def list_items_in_folder(self):
        """Lists the top-level items in the parent folder.

        Returns:
            list: A list of the names of the top-level items in the parent folder.
        """
        list_of_files = []
        files = os.listdir(self.parent_folder)

        for f in files:
            list_of_files.append(f)
        return list_of_files


    def regex_file_or_folder(self, regex_pattern, items):
        """Searches for items that match a regex pattern.

        Args:
            regex_pattern (str): The regex pattern to match.
            items (list): A list of items to search.

        Returns:
            list: A list of items that match the regex pattern.
        """
        self.switch_to_parent_folder()
        matching = []

        for item in items:
            if re.search(regex_pattern, item):
                matching.append(item)

        return matching


    def create_new_file_or_folder(self, child_dir):
        """Creates a new file or folder in the parent folder.

        Args:
            child_dir (str): The name of the file or folder to create.

        Returns:
            str: The path to the file or folder.
        """
        path = os.path.join(self.parent_folder, child_dir)
        os.mkdir(path)
        print("Directory '% s' created" % child_dir)
        return path


    def copy_items_into_folder(self, items, destination_folder):
        """Copies items into a destination folder.

        Args:
            items (list): A list of items to copy.
            destination_folder (str): The path to the destination folder.
        """
        self.switch_to_parent_folder()
        if self.exists(destination_folder) and self.is_dir(destination_folder):
            for i in items:
                shutil.copy(i, destination_folder)
            print(f"All files have been copied to {destination_folder}")
        else:
            print(f"destination folder doesn't exist. Provided path: {destination_folder}")


    def delete_item(self, path):
        """Deletes a file or folder.

        Args:
            path (str): The path to the file or folder to delete.
        """
        if self.exists(path):
            if self.is_dir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
            print(f"Deleted {path}")
        else:
            print(f"path doesn't exist. Provided path: {path}")


    def rename_item(self, path, new_name):
        """Renames a file or folder.

        Args:
            path (str): The path to the file or folder to rename.
            new_name (str): The new name for the file or folder.
        """
        if self.exists(path):
            os.rename(path, new_name)
            print(f"Renamed {path} to {new_name}")
        else:
            print(f"path doesn't exist. Provided path: {path}")


    def list_items_in_folder_recursive(self, path):
        """Lists all files and subfolders in a folder, recursively.

        Args:
            path (str): The path to the folder.

        Returns:
            list: A list of the names of the files and subfolders in the folder.
        """
        items = []
        for root, dirs, files in os.walk(path):
            for name in dirs:
                items.append(os.path.join(root, name))
            for name in files:
                items.append(os.path.join(root, name))
        return items


    def list_sizes_of_items_in_folder_recursive(self, path):
        """Lists the sizes of all files and folders in a folder, recursively.

        Args:
            path (str): The path to the folder.

        Returns:
            list: A list of tuples, where each tuple contains the name and size of a file or folder.
        """
        items = []
        for root, dirs, files in os.walk(path):
            for name in dirs:
                item_path = os.path.join(root, name)
                size = os.path.getsize(item_path)
                items.append((item_path, size))
            for name in files:
                item_path = os.path.join(root, name)
                size = os.path.getsize(item_path)
                items.append((item_path, size))
        return items


    def compress_folder(self, path, zip_file):
        """Compresses a folder into a zip file.

        Args:
            path (str): The path to the folder to compress.
            zip_file (str): The name of the zip file to create.
        """
        shutil.make_archive(zip_file, 'zip', path)
        print(f"Compressed {path} into {zip_file}.zip")


    def extract_zip_file(self, zip_file, destination_folder):
        """Extracts a zip file into a destination folder.

        Args:
            zip_file (str): The name of the zip file to extract.
            destination_folder (str): The path to the destination folder.
        """
        shutil.unpack_archive(zip_file, destination_folder)
        print(f"Extracted {zip_file} into {destination_folder}")
