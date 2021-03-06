# This calendar program allows the user to view, add, update, or delete events and terminates upon user's command.

from time import sleep, strftime

USER_NAME = 'Jordan'
calendar = {}


def welcome():
    print 'Welcome, ' + USER_NAME + '!'
    print 'Your calendar is opening.'
    sleep(1)
    print 'Today is: ' + strftime('%A %B %d, %Y')
    print 'The time is: ' + strftime('%H:%M:%S')
    sleep(1)
    print 'What would you like to do? '


def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = raw_input('Enter A to Add, U to Update, V to View, D to Delete, X to Exit: ')
        user_choice = user_choice.upper()

        if user_choice == 'V':
            if len(calendar.keys()) < 1:
                print 'Currently, there is nothing scheduled on you calendar. '
            else:
                print calendar

        elif user_choice == 'U':
            date = raw_input('Update which date? ')
            update = raw_input('What has changed? ')
            calendar[date] = update
            print 'Update successful! '
            print calendar

        elif user_choice == 'A':
            event = raw_input('What\'s new? ')
            date = raw_input('When is this happening? (MM-DD-YYYY) ')
            if len(date) > 10 or int(date[6:]) < int(strftime('%Y')):
                print 'We cannot currently go back in time, ' + USER_NAME + '!'
                try_again = raw_input('Would you like to schedule something for a future time? Y or N')
                try_again = try_again.upper()
                if try_again == 'Y':
                    continue
                else:
                    print 'Goodbye, ' + USER_NAME + '.'
                    start = False
            else:
                calendar[date] = event
                print event + ' has been scheduled. '
                print calendar

        elif user_choice == 'D':
            if len(calendar.keys()) < 1:
                print 'Your calendar is empty. '
            else:
                event = raw_input('Delete which event? ')
                for date in calendar.keys():
                    if event == calendar[date]:
                        del calendar[date]
                        print event + ' has been deleted from your calendar. '
                        print calendar
                    else:
                        print 'Your calendar has no such event scheduled. '

        elif user_choice == 'X':
            print 'Goodbye, ' + USER_NAME + '.'
            start = False

        else:
            print 'My brain hurts. I must rest. '
            print 'Goodbye, ' + USER_NAME + '.'
            start = False


start_calendar()
