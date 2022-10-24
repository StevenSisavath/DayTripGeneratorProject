destination_list = ['Houston', 'Dallas', 'Austin', 'San Antonio']
restaurant_list = ['LongHorn Steakhouse', 'Outback Steakhouse', 'Saltgrass Steakhouse', 'Texas Roadhouse']
transportation_list = ['Hovercraft', 'Bus', 'Personal Vehicle', 'Uber']
entertainment_list = ['Amusement Park', 'Hiking', 'Circus', 'Arcade']
list_of_lists = [destination_list, restaurant_list, transportation_list, entertainment_list]
destination_updated = ''
restaurant_updated = ''
transportation_updated = ''
entertainment_updated = ''
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

#test
destination_item = generate_random_item(destination_list)
restaurant_item = generate_random_item(restaurant_list)
transportation_item = generate_random_item(transportation_list)
entertainment_item = generate_random_item(entertainment_list)
print(destination_item)

def print_full_trip(lists): #only function is to run in beginning of final function call
    destination = generate_random_item(destination_list)
    restaurant = generate_random_item(restaurant_list)
    transportation = generate_random_item(transportation_list)
    entertainment = generate_random_item(entertainment_list)
    destination = destination_updated
    restaurant = restaurant_updated
    transportation = transportation_updated
    entertainment = entertainment_updated
    for element in range(len(lists)):
            print(f'Destination: {destination}')
            print(f'Restaurant: {restaurant}')
            print(f'Transportation: {transportation}')
            print(f'Entertainment: {entertainment}')
            return

print_full_trip(list_of_lists)

def validate_item():
    valid_item = False
    user_input = ''
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
                new_destination_item = destination_updated
                print(f'New Destination: {new_destination_item}')
            elif user_input == 'destination' :
                new_restaurant_item = generate_random_item(restaurant_list)
                new_restaurant_item = restaurant_updated
                print(f'New Destination: {new_restaurant_item}')
            elif user_input == 'destination' :
                new_transportation_item = generate_random_item(transportation_list)
                new_transportation_item = transportation_updated
                print(f'New Destination: {new_transportation_item}')
            elif user_input == 'destination' :
                new_entertainment_item = generate_random_item(entertainment_list)
                new_entertainment_item = entertainment_updated
                print(f'New Destination: {new_entertainment_item}')
        elif user_input_response == 'yes' :
            valid_item = True
        elif user_input_response == 'yes' or 'no':
            valid_item = False
    return valid_item

validated_item = validate_item()
print(validated_item)

# def run_day_trip_generator():


# def run_day_trip_generator():
#     print_full_trip(list_of_lists)
#     validate_item()


# # ---------------------------------------------------------------
# print_full_trip(list_of_lists)

# def run_day_trip_generator():
#     user_input = True
#     no = True
#     yes = True
#     print_full_trip(list_of_lists)
#     input('Are you satisfied with your trip? yes/no')
#     if user_input == yes :
#         print_full_trip
    
    
# run_day_trip_generator



# def determine_satisfaction():
#     satisfied = 'yes'
#     not_satisfied = 'no'
#     input('Are you satisfied with your results? yes or no')
#     if satisfied == 'yes' :
#         print(f'''
# Great, please enjoy your day trip! Here are your final results: {print(print_full_trip(list_of_lists))}
#         ''')
#         return ()
    # elif not_satisfied == 'no' :
    #     print()
    # else :
    #     if satisfied != 'yes' and not_satisfied != 'no' :

# determine_satisfaction()