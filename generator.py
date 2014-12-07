# Sony Theakanath
# West Coast Pizza Student Special Order Random Generator
# Thank you based Denero 

import random

def get_random(lst):
	return random.randint(0, len(lst) - 1)

def pick_random(toppings):
	first_top, second_top = get_random(toppings), get_random(toppings)
	while second_top == first_top:
		second_top = get_random(toppings)
	print("\nFor your pizza you should get: ")
	print(toppings[first_top], "and", toppings[second_top])

toppings = ["pepperoni", "artichoke hearts", "mild pepper rings",
 "green bell peppers", "red bell peppers", "sausage", "spicy sausage", "mushrooms",
 "chicken", "japen", "ripe olives", "beef", "deli ham", "onions", "ricotta",
 "tomatoes", "pesto", "salami", "pineapple", "sauce", "spinach", "garlic",
 "feta cheese", "bacon", "provolone", "red onion"]

#I WANT TWO PIZZAS BITCHHHHHHHHHHH
pick_random(toppings)
pick_random(toppings)
print("And a Cheesy sticks for 21.99! Freshmen special order~")