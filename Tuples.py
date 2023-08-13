#Task
"""
Given an integer, n, and n space-separated integers as input,
create a tuple, t, of those n integers. Then compute and print the result of hash(t).
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    
    print(hash(t))
"""
Step 1: First, n had taken integer type input.

Step 2: then, we created a list containing n numbers of integers.

Step 3: After this, we changed our list into a tuple.

Step 4: in the last step we used the hash module and printed it.
"""