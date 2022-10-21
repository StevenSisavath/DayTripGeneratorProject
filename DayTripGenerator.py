destinations = ['Houston', 'Dallas', 'Austin', 'San Antonio']
restaurants = ['LongHorn Steakhouse', 'Outback Steakhouse', 'Saltgrass Steakhouse', 'Texas Roadhouse']
transportation = ['fly', 'bus', 'personal car', 'uber']
entertainment = ['Amusement Park', 'Hiking', 'Circus', 'Arcade']
list_of_lists = [destinations, restaurants, transportation, entertainment]
import random

def generate_random_item(list_of_items):
    random_item = random.randrange(len(list_of_items))
    if random_item == 0 :
        print(list_of_items[0])
    elif random_item == 1 :
        print(list_of_items[1])
    elif random_item == 2 :
        print(list_of_items[2])
    elif random_item == 3 :
        print(list_of_items[3])

generate_random_item(destinations)