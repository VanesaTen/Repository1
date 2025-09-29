# using two lists

current_users = ['Admin', 'Josh', 'Jim', 'Amy', 'Ruby']

new_users = ['Bob', 'Jose', 'Becky', 'Rob', 'Ruby']




for new_user in new_users:
    if new_user in current_users:
        print(f"Username {new_user} already taken.")
    else:
        print(f"Username {new_user} available")


