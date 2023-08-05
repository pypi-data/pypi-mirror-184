from devjournal.constants import entries_directory
from devjournal.edit import edit_existing_file_with_editor


def amend():
    latest_file = list(entries_directory().glob("*.txt"))[-1]
    edit_existing_file_with_editor(latest_file)
