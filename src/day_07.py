

def eval_recursive(v, nums, result, ops, verbose=False):
    if len(nums) == 1:
        if   result + nums[0] == v: 
            ops.append('+')
            if verbose: print( (ops) )
            return True
        elif result * nums[0] == v: 
            ops.append('*')
            if verbose: print( (ops) )
            return True
        else: return False 
    else: 
        if eval_recursive(v, nums[1:], result+nums[0], ops + ['+'], verbose): return True 
        if eval_recursive(v, nums[1:], result*nums[0], ops + ['*'], verbose): return True 
        else: return False 
    return False 


def eval_recursive_concat(v, nums, result, ops, verbose=False):
    if len(nums) == 1:
        if   result + nums[0] == v: 
            ops.append('+')
            if verbose: print( (ops) )
            return True
        elif result * nums[0] == v: 
            ops.append('*')
            if verbose: print( (ops) )
            return True
        elif int( str(result) + str(nums[0]) ) == v:
            ops.append('||')
            if verbose: print(ops) 
            return True
        else: return False 
    else: 
        if eval_recursive_concat(v, nums[1:], result+nums[0], ops + ['+']): return True 
        if eval_recursive_concat(v, nums[1:], result*nums[0], ops + ['*']): return True 
        if eval_recursive_concat(v, nums[1:], int( str(result) + str(nums[0]) ), ops + ['||']): return True 
        else: return False 
    return False 