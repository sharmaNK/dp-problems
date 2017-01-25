preorder = []
arr = [21, 16, 10, 4, 15, 30, 28, 32]

def findPreOrder(left, right):
    if not len(left) and not len(right):
        return preorder 
    
    if left:
        val = min(left)
        ind = left.index(val)
        preorder.append(val)
        print val, left
        right_remaining = [] if ind == len(left)-1 else left[ind+1:  len(left)]
        findPreOrder(left[0:ind], right_remaining)
    
    if right:
        val = min(right)
        ind = right.index(val)
        preorder.append(val)
        right_remaining = [] if ind == len(right)-1 else right[ind+1: len(right)]
        findPreOrder(right[0:ind], right_remaining)        


print findPreOrder(arr, [])
print preorder
