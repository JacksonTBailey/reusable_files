from datetime import datetime

from win32com.client import Dispatch
from ..date import DateHelper


class OutlookAttachmentDownloader:
    def __init__(self, sender_email, base_file_location, file_extension, file_folder, folder_index, time_subtraction):
        """Initializes the OutlookAttachmentDownloader instance.
        
        Args:
            sender_email (str): The email address of the sender to filter by.
            base_file_location (str): The base file path where attachments should be saved.
            file_folder (str): The name of the folder to save the attachments in.
            folder_index (int): The index of the folder to search for attachments.
            file_extension (str): The file type to be retrieved.
            time_subtraction (dict): The amount of time to subtract from the current date and time, in the format\
                                     {"days": X, "months": X, "years": X, "hours": X, "minutes": X, "seconds": X}.
        """
        self.sender_email = sender_email
        self.base_file_location = base_file_location
        self.file_extension = file_extension
        self.file_folder = file_folder
        self.folder_index = folder_index
        self.time_subtraction = time_subtraction
        self.date_helper = DateHelper()


    def download_attachments(self):
        """Downloads Outlook attachments from the specified folder that meet the specified criteria.
        
        Returns:
            list: A list of file paths for the downloaded attachments.
        """
        # Connect to Outlook
        outlook = Dispatch("Outlook.Application").GetNamespace("MAPI")

        # Connect to folder
        folder = outlook.GetDefaultFolder(self.folder_index)

        # Get the current date and time and subtract the specified amount of time
        date_helper = DateHelper()
        current_datetime = date_helper.now - datetime.timedelta(**self.time_subtraction)
        current_datetime = current_datetime.strftime('%m/%d/%Y %H:%M %p')

        # Check mail in folder and filter by sender email address and time received
        messages = folder.Items
        messages = messages.Restrict(f"[SenderEmailAddress] = '{self.sender_email}' AND [LastModificationTime] > '{current_datetime}'")

        # Get the first message that matches the criteria
        new_message = messages.GetFirst()

        # Get the attachments from the message
        attachments = new_message.Attachments

        list_of_attachments = []
        
        for attachment in attachments:
            
            file_save_path = f"{self.base_file_location}\{self.file_folder}.{self.file_extension}"
            attachment.SaveAsFile(file_save_path)
            list_of_attachments.append(file_save_path)

        return list_of_attachments
