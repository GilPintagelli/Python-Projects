import os
import re
from typing import Match

PATH = '../MySql__course__1/'

sql_scripts = os.listdir(PATH)
print(sql_scripts)

# ORDER NUMBERS
lowest_script_number = int(sorted(sql_scripts[0].split('__'))[0])
ordered_sql_scripts = []

# BUG 2 lies here because ordered_items (28) ends up having more elements than sql_scripts (25)
while len(ordered_sql_scripts) < len(sql_scripts):
    for old_title in sql_scripts:
        n = 0
        script_number = int(sorted(old_title.split('__'))[0])
        if script_number < lowest_script_number:
            ordered_sql_scripts.append(old_title)
        else:
            lowest_script_number = script_number
            # n += 1

print(ordered_sql_scripts)

# while len(ordered_sql_scripts) < len(sql_scripts):
#     for old_title in sql_scripts:
#         n = 0
#         if int(sorted(old_title.split('__'))[n]) < lowest_script_number:
#             ordered_sql_scripts.append(old_title)
#         else:
#             lowest_script_number = int(sorted(old_title.split('__'))[n])
#             n += 1

x = '122 lol 33'
first_number = re.search(pattern='(\d+)', string=x)
replace_first_number = re.sub(pattern=first_number.group(), string=x, repl='7')
print(replace_first_number)
