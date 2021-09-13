from functools import reduce
if __name__ == "__main__":
    my_list = [1,2,3,4,5,6,7,8,9,10]
    #Solution using filter
    odd = list(filter(lambda x: x%2 != 0,my_list))
    print(odd)
    #Solution using map
    squares = list(map(lambda x: x**2,my_list))
    print(squares)
    #Solution using filter note: add reduce form functools at begin
    all = [2,2,2,2,2]
    all_multiplied = reduce(lambda a,b:a*b,all)
    print(all_multiplied)
