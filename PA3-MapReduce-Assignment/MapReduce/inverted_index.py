import MapReduce
import sys

"""
Inverted Index Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(doc_list):
    # YOUR CODE GOES HERE
    document_id = doc_list[0]
    text = doc_list[1]
    words  = text.split()
    for w in words:
      mr.emit_intermediate(w, document_id)

# Implement the REDUCE function
def reducer(key, list_of_values):
    # YOUR CODE GOES HERE
    document_list=[]
    for per_document in  list_of_values:
        if per_document not in document_list:
            document_list.append(per_document)
    mr.emit([key,document_list])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
