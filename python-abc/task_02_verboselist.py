#!/usr/bin/python3
"""
This module contains the class VerboseList which is a subclass of list and it
modifies the behaviour of list
"""


class VerboseList(list):
    """VerboseList class that inherits from list class"""

    def append(self, value):
        """Notifies of an append"""
        super().append(value)
        print(f"Added [{value}] to the list.")

    def extend(self, iterable):
        """Notifies of an extend"""
        items_added = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{items_added}] items.")

    def remove(self, value):
        """Notifies of a remove"""
        print(f"Removed [{value}] from the list.")
        super().remove(value)

    def pop(self, index=-1):
        """Notifies of a pop"""
        value = self[index]
        print(f"Popped [{value}] from the list.")
        return super().pop(index)
