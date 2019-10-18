import MapReduce
import sys

"""
Assymetric Relationships in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(record):
    # YOUR CODE GOES HERE
    ori_record=record[:]
    record.sort()
    key = "{} {}".format(str(record[0]),str(record[1]))
    value = ori_record
    mr.emit_intermediate(key, value)

# Implement the REDUCE function
def reducer(key, list_of_values):
    # YOUR CODE GOES HERE
    if len(list_of_values) == 1:
      mr.emit((list_of_values[0][1], list_of_values[0][0]))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
