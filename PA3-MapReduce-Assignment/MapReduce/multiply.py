import MapReduce
import sys

"""
Matrix Multiply in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(record):
    # YOUR CODE GOES HERE
    ori_m_name = record[0]
    i = record[1]
    j = record[2]
    val = record[3]
    if ori_m_name == "a":
        for p_i in range(5):
            mr.emit_intermediate((i, p_i), (j, val))
    elif ori_m_name=="b":
        for p_j in range(5):
            mr.emit_intermediate((p_j, j), (i, val))



# Implement the REDUCE function
def reducer(key, list_of_values):
    # YOUR CODE GOES HERE
    multiplication = 0
    init_list=[]
    for i in range(5):
        init_list.append(0)
    for ijvalue in list_of_values:
        if init_list[ijvalue[0]] != 0:
            multiplication = multiplication + ijvalue[1] * init_list[ijvalue[0]]
            init_list[ijvalue[0]] = 0
        else:
            init_list[ijvalue[0]] = ijvalue[1]

    mr.emit((key[0], key[1], multiplication))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
