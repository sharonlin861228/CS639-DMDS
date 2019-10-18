import MapReduce
import sys

"""
JOIN in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(record):
    # YOUR CODE GOES HERE
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)


# Implement the REDUCE function
def reducer(key, list_of_values):
    # YOUR CODE GOES HERE
    Order_order_id=0
    Item_order_id_list=[]
    for select_key_id,record in enumerate(list_of_values):
        if(len(record[0]) == 5 or record[0]==  "order"):
            Order_order_id=select_key_id
        elif(len(record[0]) == 9 or record[0] == "line_item"):
            Item_order_id_list.append(select_key_id)

    for select_result_item_id in Item_order_id_list:
        select_result = []
        per_order_line = list_of_values[Order_order_id]
        for i in range(len(per_order_line)):
            select_result.append(per_order_line[i])
        per_item_line = list_of_values[select_result_item_id]
        for i in range(len(per_item_line)):
            select_result.append(per_item_line[i])
        mr.emit(select_result)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
