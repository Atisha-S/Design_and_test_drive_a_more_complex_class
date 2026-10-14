# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class FriendBook:
    # User-facing properties:
    #   name: string

    def __init__(self, friends_dict):
        # Parameters:
        #   _friends_dict: dictionary name: birthday  
        # Side effects:
        #   N/A
        pass # No code here yet

    def edit_date(self, name, new_date):
        # Parameters:
        #   name: string representing a friends name
        #   new_date: date
        # Returns:
        #   Nothing
        # Side-effects
        #   update friends_dict with new date
        pass # No code here yet

    def edit_name(self, name, new_name ):
        # Parameters:
        #   name: string representing a friends name
        #   new_name: string representing the new name of the friend 
        # Returns:
        #   Nothing
        # Side-effects:
        #   update friends_dict with new name
        pass # No code here yet

    def list_birthday(self):
        # Parameters:
        # None
        # Returns:
        #   list of the names and birthdays
        # Side Effects:
        # N/A

    def age_calculator(self):
        # Parameters:
        # None
        # Returns:
        #   list of the names and ages
        # Side Effects:
        # N/A
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a dictionary of names and birthday initializes friends_dict correctly
"""
friend_book = FriendBook({"Bob": "14-08-1997", "Chris": "07-04-1987", "Laura": "01-01-2000"})
friend_book._friend_dict == {"Bob": "14-08-1997", "Chris": "07-04-1987", "Laura": "01-01-2000"}

"""
Given a name and new date 
date is updated for the given namels
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
