students = {
    "names" : ["Sharath", "james", "Lilly"],
    "score" : [56, 76, 98]
}
#
# for key, value in students.items():
#     print(key)
# for key, value in students.items():
#     print(value)

import pandas
studentDF = pandas.DataFrame(students)

# loop through data frame
# for key, value in studentDF.items():
#     print(key)

# for key, value in studentDF.items():
#     print(value)

# loop through rows of a data frame

# for index,row in studentDF.iterrows():
#     print(index) # just the index

# for index,row in studentDF.iterrows():
#     print(row)

#     Output:
# names    Sharath
# score         56
# Name: 0, dtype: object
# names    james
# score       76
# Name: 1, dtype: object
# names    Lilly
# score       98
# Name: 2, dtype: object

# for index,row in studentDF.iterrows():
#     print(row.names)
# output:
# Sharath
# james
# Lilly

for idx,row in studentDF.iterrows():
    if row.names == "Sharath":
        print(row.score) # 56