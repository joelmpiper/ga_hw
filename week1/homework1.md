# Homework 1

1. Each row of the chipotle.tsv corresponds to a unique item in a unique order. Each column represents a different field (or property) associated with the row, as identified in the first (header) row, including, *order_id*, *quantity*, *item_name*, *choice_description*, and *item_price*.

2. The unique_id seems to track each of the individual orders. Also, these numbers seems to be sequential such that the unique_id of the last line identified in *tail* should contain the number of orders, **1834**.

3. *wc -l chipotle.tsv* yields **4623** lines. The first line is the header, so there would be one fewer unique order/item combination.

4.  
