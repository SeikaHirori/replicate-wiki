import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from django.http import HttpRequest
import random


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))
    """
    ### PERSONAL NOTE:
        - It looks like the list is storing the titles as str[strings].
    """    


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def random_entry(request:HttpRequest) -> str: # My implementation
    random_entry = None

    while True:
        current_entries = list_entries()
        random_page = random.choice(current_entries)
        random_entry = str(random_page)

        url_check = f'/wiki/{random_entry}' 

        # if url_check not in request.get_full_path(): # RFER 7 ### Original
        #     break

        if url_check != request.get_full_path(): # RFER 7 ### Revison
            break
        """
        Potential problem:
            - Not sure if substring would disqualify entries if it contains ONLY a part of the string.
        """

    return random_entry

class filter_class:

    def __init__(self, title:str) -> None:
        self.existence:bool = False
        self.current_entry:str = None # This is used to return the files' proper name.
        self.filtered_list:list[str] = None

        # Run immediately
        self.check_if_exists_in_list(title)

    def check_if_exists_in_list(self, title:str):
        """
        - Filter current database asap # Verison_1
            - Keep the entries in its original format; DO NOT AUTOMATICALLY LOWERCASE/UPPERCASE THEM.
                -  Reason: The list will be used to display to the user.
        """
        filtered_list:list[str] = [entry for entry in list_entries() if title.lower() in entry.lower()] # RFER 11

        # # # Verison_2
        # filtered_list:list[str] = []
        # for entry in list_entries():
        #     if title.lower() in entry.lower():
        #         filtered_list.append(entry)

        for entry in filtered_list:
            lowercase_entry:str = entry.lower()
            lowercase_request_get_q:str = title.lower()

            if lowercase_request_get_q == lowercase_entry:
                # If entry exists in database.
                self.existence = True
                self.current_entry = entry
                break

        self.filtered_list = filtered_list


