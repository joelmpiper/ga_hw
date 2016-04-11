# Homework 1

1. Each row of the chipotle.tsv corresponds to a unique item in a unique order. Each column represents a different field (or property) associated with the row, as identified in the first (header) row, including *order_id*, *quantity*, *item_name*, *choice_description*, and *item_price*.

2. The *unique_id* seems to track each of the individual orders. Also, these numbers seems to be sequential such that the *unique_id* of the last line identified in *tail* should contain the number of orders, **1834**.

3. *wc -l chipotle.tsv* yields **4623** lines. The first line is the header, so there would be one fewer unique order/item combination.

4. *grep "Chicken Burrito" chipotle.tsv | cut -f2 | paste -sd+ - | bc* yields **591** total chicken burritos ordered, in a total of 553 unique order/item combinations. For the Steak Burrito, *grep "Steak Burrito" chipotle.tsv | cut -f2 | paste -sd+ - | bc* there are **386** in 368 unique order/item combinations. Therefore, the **Chicken Burrito** is the more common order. 

5. *grep "Chicken Burrito" chipotle.tsv | grep "Black Beans" | cut -f2 | paste -sd+ - | bc* yields **307** total chicken burritos with black beans ordered, in a total of 282 unique order/item combinations. For the Chicken Burrito with Pinto Beans, *grep "Chicken Burrito" chipotle.tsv | grep "Pinto Beans" | cut -f2 | paste -sd+ - | bc* there are **108** in 105 unique order/item combinations. Therefore, the **Chicken Burrito with Black Beans** is the more common order. 

6. See the list of 13 files below:  
  ../../DAT-DC-10//data/airlines.csv  
  ../../DAT-DC-10//data/bank-additional.csv  
  ../../DAT-DC-10//data/bikeshare.csv  
  ../../DAT-DC-10//data/chipotle.tsv  
  ../../DAT-DC-10//data/drinks.csv  
  ../../DAT-DC-10//data/hitters.csv  
  ../../DAT-DC-10//data/imdb_1000.csv  
  ../../DAT-DC-10//data/sms.tsv  
  ../../DAT-DC-10//data/titanic.csv  
  ../../DAT-DC-10//data/ufo.csv  
  ../../DAT-DC-10//data/vehicles_test.csv  
  ../../DAT-DC-10//data/vehicles_train.csv  
  ../../DAT-DC-10//data/yelp.csv  

  *find ../../DAT-DC-10/ -name "*.csv" -o -name "*.tsv"*

7. *grep -r -o dictionary ../../DAT-DC-10/ | wc -l* shows that there are **88** times the word *dictionary* is shown in the DAT-DC-10 files. This is the same as the number of lines that contain *dictionary*.

8. The maximum number of identical items in a single order is **15**, found by *cut -f2 chipotle.tsv | sort -n | tail -2 | head -1*. The *tail* then *head* is only to remove the header. We can then search for the item with *cut -f2,3,4 chipotle.tsv | grep 15* (not guaranteed to work if *15* is in the text) to find that the item was *Chips and Fresh Tomato Salsa*.
