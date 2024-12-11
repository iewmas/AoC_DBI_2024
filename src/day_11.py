

def apply_rules(stone):
    if stone == 0: 
        return [1]
    elif len(str(stone)) % 2 == 0: 
        s_len_half = int( len(str(stone))/2 )
        s1 = str(stone)[:s_len_half]
        s2 = str(stone)[s_len_half:]
        return [ int(s1), int(s2)]
    else: 
        #stones_new.append( s * 2024 )
        return [stone * 2024]
    


def apply_rules_batch(stones):
    stones_new = list() 
    
    for s in stones:
        if s == 0: 
            stones_new.append(1)
        elif len(str(s)) % 2 == 0: 
            s_len_half = int( len(str(s))/2 )
            s1 = str(s)[:s_len_half]
            s2 = str(s)[s_len_half:]
            stones_new.append( int(s1) )
            stones_new.append( int(s2) )
        else: 
             stones_new.append( s * 2024 )
    return stones_new
    
