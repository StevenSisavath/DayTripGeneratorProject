destination_list = ['Houston', 'Dallas', 'Austin', 'San Antonio']
restaurant_list = ['LongHorn Steakhouse', 'Outback Steakhouse', 'Saltgrass Steakhouse', 'Texas Roadhouse']
transportation_list = ['Hovercraft', 'Bus', 'Personal Vehicle', 'Uber']
entertainment_list = ['Amusement Park', 'Hiking', 'Circus', 'Arcade']
list_of_lists = [destination_list, restaurant_list, transportation_list, entertainment_list]
import random

# def generate_random_item(list_of_items):
#     random_item = random.randrange(len(list_of_items))
#     if random_item == 0 :
#         print(list_of_items[0])
#     elif random_item == 1 :
#         print(list_of_items[1])
#     elif random_item == 2 :
#         print(list_of_items[2])
#     elif random_item == 3 :
#         print(list_of_items[3])

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
    
print(generate_random_item(destination_list))

def print_full_trip(lists):
    destination = generate_random_item(destination_list)
    restaurant = generate_random_item(restaurant_list)
    transportation = generate_random_item(transportation_list)
    entertainment = generate_random_item(entertainment_list)
    for element in range(len(lists)) :
            print(f'Destination: {destination}')
            print(f'Restaurant: {restaurant}')
            print(f'Transportation: {transportation}')
            print(f'Entertainment: {entertainment}')
            return

print_full_trip(list_of_lists)