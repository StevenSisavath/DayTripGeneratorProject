destination_list = ['Houston', 'Dallas', 'Austin', 'San Antonio']
restaurant_list = ['LongHorn Steakhouse', 'Outback Steakhouse', 'Saltgrass Steakhouse', 'Texas Roadhouse']
transportation_list = ['Hovercraft', 'Bus', 'Personal Vehicle', 'Uber']
entertainment_list = ['Amusement Park', 'Hiking', 'Circus', 'Arcade']
list_of_lists = [destination_list, restaurant_list, transportation_list, entertainment_list]
import random

def generate_random_item(list): #generate a random item from a list of 4 strings
    random_item = random.randrange(len(list))
    if random_item == 0 :
        return list[0]
    elif random_item == 1 :
        return list[1]
    elif random_item == 2 :
        return list[2]
    elif random_item == 3 :
        return list[3]

def print_full_trip(lists): #generate and save random item from [list_of_lists]
    destination = generate_random_item(destination_list)
    restaurant = generate_random_item(restaurant_list)
    transportation = generate_random_item(transportation_list)
    entertainment = generate_random_item(entertainment_list)
    for element in range(len(lists)):
        return destination, restaurant, transportation, entertainment

destination, restaurant, transportation, entertainment = print_full_trip(list_of_lists)

def validate_items(): # validate and confirm items to be printed out (with user input)
    valid_item = False
    user_input = ''
    final_destination = destination
    final_restaurant = restaurant
    final_transportation = transportation
    final_entertainment = entertainment
    print('Here is a randomly generated day trip!')
    print(f'Destination: {destination}')
    print(f'Restaurant: {restaurant}')
    print(f'Transportation: {transportation}')
    print(f'Entertainment: {entertainment}')
    while valid_item == False:
        user_input_response = input('''
Are you satisfied with all your options? 
yes / no
''')
        if user_input_response == 'no':
            valid_item = False
            user_input = input('''
Which option would you like to change? 
destination
restaurant
transportation
entertainment
all
''')
            if user_input == 'destination' :
                new_destination_item = generate_random_item(destination_list)
                print(f'New Destination: {new_destination_item}')
                final_destination = new_destination_item
                valid_item = False
            elif user_input == 'restaurant' :
                new_restaurant_item = generate_random_item(restaurant_list)
                print(f'New Restaurant: {new_restaurant_item}')
                final_restaurant = new_restaurant_item
                valid_item = False
            elif user_input == 'transportation' :
                new_transportation_item = generate_random_item(transportation_list)
                print(f'New Transportation: {new_transportation_item}')
                final_transportation = new_transportation_item
                valid_item = False
            elif user_input == 'entertainment' :
                new_entertainment_item = generate_random_item(entertainment_list)
                print(f'New Entertainment: {new_entertainment_item}')
                final_entertainment = new_entertainment_item
                valid_item = False
            elif user_input == 'all' :
                new_destination_item = generate_random_item(destination_list)
                new_restaurant_item = generate_random_item(restaurant_list)
                new_transportation_item = generate_random_item(transportation_list)
                new_entertainment_item = generate_random_item(entertainment_list)
                print(f'''Newly generated list:
{new_destination_item}
{new_restaurant_item}
{new_transportation_item}
{new_entertainment_item}''')
                final_destination = new_destination_item
                final_restaurant = new_restaurant_item
                final_transportation = new_transportation_item
                final_entertainment = new_entertainment_item
                valid_item = False
            else:
                valid_item = False
        elif user_input_response == 'yes' :
            print(f'''
Great! Here is your final results:
Destination: {final_destination}
Restaurant: {final_restaurant}
Transportation: {final_transportation}
Entertainment: {final_entertainment}

Have an amazing time on your day trip!
        ''')
            valid_item = True
            return valid_item
        else:
            valid_item = False
    return destination, restaurant, transportation, entertainment

def run_day_trip_generator(): # final function to generate day trip
    print_full_trip(list_of_lists)
    validate_items()

run_day_trip_generator()