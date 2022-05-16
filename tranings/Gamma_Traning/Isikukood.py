user_input = None
while True:
    while True:
        user_input = input(('Enter ID:'))
        try:
            int(user_input)
            if len(user_input) != 11:
                raise UserWarning
        except ValueError:
            print('Code in not nimeric')
        except UserWarning:
            if len(user_input) > 11:
                print('Code is too long')
            elif len(user_input) < 11:
                print('Code is too short')
            else:
                print(user_input)
                break

    user_choice = input('Please choose:\n'
                    '1.Get gender\n'
                    '2.Get date of birth\n'
                    '3.Get region of birth\n'
                    '4.Validate ID\n'
                    '5.Change ID\n'
                    '0.Exit\n'
                    '--> ')
    if user_choice == '1':
    elif user_choice == '2':
    elif user_choice == '3':
    elif user_choice == '4':
    elif user_choice == '5':
    elif user_choice == '0':
        print("By!e")
        break
    else:
        print('You should choose between 1-5 or press 0 to exit')