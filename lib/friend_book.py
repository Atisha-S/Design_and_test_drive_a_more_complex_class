from datetime import date, timedelta

class FriendBook:
    def __init__(self, friends_dict):
        self._friends_dict = friends_dict

    def edit_date(self, name, new_date):
        self._friends_dict[name] = new_date

    def edit_name(self, name, new_name):
        if name in self._friends_dict:
            self._friends_dict[new_name] = self._friends_dict.pop(name)

    def list_birthdays(self):
        upcoming_birthdays = {}
        today = date.today()
        day_first_dash = today.strftime('%d-%m-%Y')
        future_date = today + timedelta(days=30)
        day_first_future = future_date.strftime('%d-%m-%Y')
        
        print(day_first_dash)
        print(day_first_future)

