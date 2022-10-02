import os
import re

# get folder's path
PATH = '../MySql__course__1/'

# we can use listdir to list all the sql_scripts in a directory/folder
sql_scripts = os.listdir(PATH)

# ORDER NUMBERS
ordered_sql_scripts = []

# EXTRACT NUMBERS FROM SQL EXERCISE
sql_scripts_numbers = []
for script in sql_scripts:
    script_number = sorted(script.split('__'))[0]
    sql_scripts_numbers.append(int(script_number))

sql_scripts_list = list(zip(sql_scripts, sql_scripts_numbers))

ordered_sql_scripts = []
for script_number in sorted(sql_scripts_numbers):
    for script_tuple in sql_scripts_list:
        if script_number in script_tuple and script_tuple[0] not in ordered_sql_scripts:
            ordered_sql_scripts.append(script_tuple[0])


# CHANGE NUMBER
index = 0
starting_number = 1

for old_title in ordered_sql_scripts:
    # EXPECTED BEHAVIOR: it should only change the first one
    get_script_first_number = re.search(pattern='(\d+)', string=old_title)
    new_title = re.sub(pattern=get_script_first_number.group(), string=old_title, repl=str(starting_number))  # old pattern: "\d+"
    starting_number += 1

    ordered_sql_scripts[index] = {"new": new_title, "old": old_title}
    index += 1

# '../MySql__course__1/MySql__exercise__8__CRUD__SQL__COURSE.sql'
for index in range(0, len(ordered_sql_scripts)):

    # this variable contains the current item, which is a dictionary
    current_item_list = ordered_sql_scripts[index]

    # these two variables contain two different paths
    file_to_remove = PATH + current_item_list['old']
    file_to_keep = PATH + current_item_list['new']

    with open(file_to_remove, mode="r") as old_file:
        content = old_file.read()

        with open(file_to_keep, mode='w') as file:
            new_file = file.write(content)

    os.remove(file_to_remove)
