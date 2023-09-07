def find_contiguous(k_input, length_N):
    '''
    Given a string k and integer N, 
    find the most occurring contiguous substring 
    of length N that exists in string k.

    Example: 
    For string k = 'abfxybfz', 
    N = 2, 
    result = 'bf'
    '''

    k_len = len(k_input) 
    i_max = k_len - length_N # setup sweep distance
    results_dict = dict() # TODO: can be optimized with better data structure

    for i in range(i_max+1):
        substring_1 = k_input[i:i+length_N]
        count = 0
        if substring_1 not in results_dict.keys(): # skip secondary instances
            for j in range(i+1,i_max,1): # don't sweep through indexes already visited

                # BUGFIX: from live implementation, replace 'i's with 'j's to fix 
                substring2 = k_input[j:j+length_N] 

                if substring_1 == substring2: # find matches
                    count += 1
            if count > 0: # reduce size for sort
                results_dict[substring_1] = count
    #print(results_dict) # print the intermediate outcomes

    # TODO: This is a potentially costly sort in large situations, can probably be optimized
    sorted_dict = dict(sorted(results_dict.items(), key=lambda item: item[1], reverse=True)) 
    return list(sorted_dict.keys())[0]

if __name__ == '__main__':
    k = 'abfxybfz'
    N = 2 #int
    result = 'bf'

    my_result = find_contiguous(k, N)

    print(my_result)
    if result == my_result:
        print('GREAT SUCCESS!')


import unittest

class Tests(unittest.TestCase):
    def test_given_result(self):
        k = 'abfxybfz'
        N = 2
        result = 'bf'
        self.assertEqual(find_contiguous(k,N), result)
    def test_alternate_input(self):
        k = 'abffxybffz'
        N = 3
        result = 'bff'
        self.assertEqual(find_contiguous(k,N), result)
