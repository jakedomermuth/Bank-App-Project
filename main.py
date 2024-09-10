from database import add_entry, get_entries, del_entry, get_last_entry, create_table, get_dated_entries

MENU = """
Welcome to the Banking App!

1. Add Entry
2. View All Entries
3. View Entries By Date
4. Delete Last Entry
5. Exit


Selection: 
"""

# utility

def normalize(text):
    return text.strip().upper()


# prompt functions
def prompt_add_entry():
    content = input('How much money did you spend today? ')
    date = input("What is today's date(MM/DD/YY) ")
    return content, date

def prompt_get_date():
    user_selected_date = input('What day would you like to check?(MM/DD/YY) ')
    return user_selected_date

def prompt_view_entries(my_data):
    for row in my_data:
        print(f"{row[2]}: ${row[1]}\n")

def prompt_del_entry(data_to_delete):
    a = normalize(input(f'Are you sure you want to delete {last_entry[1]}: ${last_entry[0]}\nSelection (Y/N) '))
    return a


create_table()

while (user_input := input(MENU)) != '5':
    if user_input == '1':
        content, date = prompt_add_entry()
        add_entry(content, date)
    elif user_input == '2':
        my_data = get_entries()
        prompt_view_entries(my_data)
    elif user_input == '3':
        specified_date = prompt_get_date()
        my_data = get_dated_entries(specified_date)
        prompt_view_entries(my_data)
    elif user_input == '4':
        last_entry = get_last_entry()
        del_decision = prompt_del_entry(last_entry)
        if del_decision == 'Y':
            del_entry()

    else:
        print('Try Again')

