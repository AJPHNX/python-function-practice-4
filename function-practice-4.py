def max_num(a,b,c):
     return max((a,b,c))

def mult_list(list):
    amt = 1
    for item in list:
        amt *= item 
    return amt

def rev_string(str):
    return str[::-1]

def num_within(num,low,high):
    if num >= low and num <= high:
        return "TRuE!"
    else:
        return "..False.."

def pascal(num):
    triangle = [[]]#[[1],[1,1]]
    prev_row = triangle[0]
    row = []
    i = 0
    if num < 1:
        print("Invalid Input  -|😳|-")
    elif num == 1:
        prev_row = triangle[0]
    elif num == 2:
        prev_row = triangle[1]

    else:
        for i in range(num):

            for c in range(len(str(prev_row))):
                if (c == 0) or (c == i):
                    row.append(1)
                if ((c)>0) and (c<i):
                    row.append(prev_row[c-1] + prev_row[c])
            prev_row = row
            row = []
            triangle.append(prev_row)
            print(triangle[i])
    # return triangle

print(max_num(1,4,5))
print(mult_list([1,4,5,3]))
print(rev_string("1,4,5"))
print(num_within(1,2,3))
print(num_within(3,2,4))
# print(pascal(0))
print(pascal(5))
print(pascal(20))



 