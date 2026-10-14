from lib.friend_book import *

"""
Given a dictionary of names and birthday initializes friends_dict correctly
"""
def test_friends_dict_initializes_correctly():
    friend_book = FriendBook({"Bob": "14-08-1997", "Chris": "07-04-1987", "Laura": "01-01-2000"})
    assert friend_book._friends_dict == {"Bob": "14-08-1997", "Chris": "07-04-1987", "Laura": "01-01-2000"}

# Given a name and new date, date is updated for given name. 

def test_edit_date_updates_birthday_for_given_name():
    friend_book = FriendBook({"Bob": "14-08-1997", "Chris": "07-04-1987", "Laura": "01-01-2000"})    
    friend_book.edit_date("Bob", "15-08-1997")
    assert friend_book._friends_dict == {"Bob": "15-08-1997", "Chris": "07-04-1987", "Laura": "01-01-2000"} 

# Given a name and new name, name is updated for given name. 

def test_edit_name_with_new_name():
    friend_book = FriendBook({"Bob": "14-08-1997", "Chris": "07-04-1987", "Laura": "01-01-2000"})    
    friend_book.edit_name("Bob", "Robert")
    assert friend_book._friends_dict == {"Robert": "14-08-1997", "Chris": "07-04-1987", "Laura": "01-01-2000"} 

# List birthdays that are coming up soon
def test_birthday_is_in_current_month_add_to_list():
    friend_book = FriendBook({"Bob": "14-08-1997", "Chris": "15-10-1987", "Laura": "20-10-2000"})  
    assert friend_book.list_birthdays() == {"Chris": "15-10-1987", "Laura": "20-10-2000"}