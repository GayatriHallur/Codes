#Importing libraries
import itertools


def unq_pair_lst(lst,k):
    """This function is used to get different combination from list for K values"""
    try:
        if k<0:
            raise Exception('Invalid value of K')
        if len(lst)<k:
            raise Exception('Invalid list')
        result=[]
        for l in range(0, len(lst)+1):
            for subset in itertools.combinations(lst,l):
                if len(subset)==k:
                    result.append(subset)
        return result
    finally : 
            print('Function is executed.')


if '__main__'==__name__:
    lst =[int(item) for item in input("Enter the list items : ").split(',')] 
    k= int(input())
    result = unq_pair_lst(lst,k)
    print(result)

