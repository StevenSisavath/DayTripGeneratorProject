destination_list = ['Houston', 'Dallas', 'Austin', 'San Antonio']
restaurant_list = ['LongHorn Steakhouse', 'Outback Steakhouse', 'Saltgrass Steakhouse', 'Texas Roadhouse']
transportation_list = ['Hovercraft', 'Bus', 'Personal Vehicle', 'Uber']
entertainment_list = ['Amusement Park', 'Hiking', 'Circus', 'Arcade']
list_of_lists = [destination_list, restaurant_list, transportation_list, entertainment_list]
valid_item = False
import random

def generate_random_item(list_of_items):
    random_item = random.randrange(len(list_of_items))
    if random_item == 0 :
        return list_of_items[0]
    elif random_item == 1 :
        return list_of_items[1]
    elif random_item == 2 :
        return list_of_items[2]
    elif random_item == 3 :
        return list_of_items[3]

random_destination_item = generate_random_item(destination_list)
print(random_destination_item)

def print_full_trip(lists): #only function is to run in beginning of final function call
    destination = generate_random_item(destination_list)
    restaurant = generate_random_item(restaurant_list)
    transportation = generate_random_item(transportation_list)
    entertainment = generate_random_item(entertainment_list)
    for element in range(len(lists)):
            print(f'Destination: {destination}')
            print(f'Restaurant: {restaurant}')
            print(f'Transportation: {transportation}')
            print(f'Entertainment: {entertainment}')
            return

print_full_trip(list_of_lists)


def validate_item(list):
    valid_item = False
    while valid_item == False:
        user_input_response = input('Are you satisfied with your option? yes / no')
        if user_input_response != 'yes':
            valid_item = False
        else :
            valid_item = True
    return valid_item

item_result = validate_item(destination_list)
print(item_result)

def 
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