'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''


'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''


'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''

# count the number of unique order_id's
# note: you could assume this is 1834 since that's the maximum order_id, but it's best to check


# create a list of prices
# note: ignore the 'quantity' column because the 'item_price' takes quantity into account


# calculate the average price of an order and round to 2 digits



'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''

# use a for loop to get a list of all the sodas
sodas = []
for row in data:
    if 'Canned' in row[2]:
        sodas.append(row[3][1:-1])      # strip the brackets

# for practice, use a list comprehension  to do the same
sodas = [row[3][1:-1] for row in data if 'Canned' in row[2]]

# now use the set() function to get just the unique elements of the list
unique_sodas = set(sodas)


'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''

# keep a running total of burritos and toppings, so initalize some counter variables


# calculate number of toppings by counting the commas and adding 1
# note: x += 1 is equivalent to x = x + 1
# loop over the data and update the counters in this way

# calculate the average topping count and round to 2 digits



'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''

# start with an empty dictionary


# loop over the data rows and do the following - 
# if chip order is not in dictionary, then add a new key/value pair
# if chip order is already in dictionary, then update the value for that key

# let's learn about a new way to do this
# defaultdict saves you the trouble of checking whether a key already exists
from collections import defaultdict
dchips = defaultdict(int)
for row in data:
    if 'Chips' in row[2]:
        dchips[row[2]] += int(row[1])


'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''
