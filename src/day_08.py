from itertools import combinations


def check_within_bound(x, y, map):
    if x < 0 or x >= len(map[0]): return False 
    if y < 0 or y >= len(map):    return False
    return True 


def find_antinodes(map, ant_coords, verbose=False):
    antinodes = list() 

    for ant in ant_coords:
        coords = ant_coords[ant]
        if len(coords) <= 1: continue
        
        for ant1, ant2 in combinations(ant_coords[ant], 2):    
            ant1_x, ant1_y = ant1 
            ant2_x, ant2_y = ant2
            ant_x_diff = ant1_x - ant2_x
            ant_y_diff = ant1_y - ant2_y 
            ant_slope = ant_x_diff / ant_y_diff
            
            ant1_node_1 = (ant1_x + ant_x_diff, ant1_y + ant_y_diff )
            ant1_node_2 = (ant1_x - ant_x_diff, ant1_y - ant_y_diff )
            ant2_node_1 = (ant2_x + ant_x_diff, ant2_y + ant_y_diff)
            ant2_node_2 = (ant2_x - ant_x_diff, ant2_y - ant_y_diff)
            
            if ant1_node_1 != ant2 and check_within_bound(ant1_node_1[0], ant1_node_1[1], map): antinodes.append( (ant, ant1_node_1, ant1, ant2) )
            if ant1_node_2 != ant2 and check_within_bound(ant1_node_2[0], ant1_node_2[1], map): antinodes.append( (ant, ant1_node_2, ant1, ant2) )
            if ant2_node_1 != ant1 and check_within_bound(ant2_node_1[0], ant2_node_1[1], map): antinodes.append( (ant, ant2_node_1, ant1, ant2) )
            if ant2_node_2 != ant1 and check_within_bound(ant2_node_2[0], ant2_node_2[1], map): antinodes.append( (ant, ant2_node_2, ant1, ant2) )
            
            if verbose: print(ant, ant1, ant2, ant_x_diff, ant_y_diff, ant_slope, '||', ant1_node_1, ant1_node_2, check_within_bound(ant1_node_1[0], ant1_node_1[1], map)) 
            if verbose: print('\t||', ant1_node_1, ant1_node_2, ant2_node_1, ant2_node_2,)
            
    return antinodes


def find_antinodes_harmonics(map, ant_coords, verbose=False):
    antinodes = list() 
    
    for ant in ant_coords:
        coords = ant_coords[ant]
        if len(coords) <= 1: continue
        
        for ant1, ant2 in combinations(ant_coords[ant], 2):    
            antinodes.append( (ant, ant1, ant1, ant2) )
            antinodes.append( (ant, ant2, ant1, ant2) )
            
            ant1_x, ant1_y = ant1 
            ant2_x, ant2_y = ant2
            ant_x_diff = ant1_x - ant2_x
            ant_y_diff = ant1_y - ant2_y 
            ant_slope = ant_x_diff / ant_y_diff
            
            for i in range(len(map)):
                ant1_node_1 = (ant1_x + ant_x_diff*i, ant1_y + ant_y_diff*i )
                ant1_node_2 = (ant1_x - ant_x_diff*i, ant1_y - ant_y_diff*i )
                ant2_node_1 = (ant2_x + ant_x_diff*i, ant2_y + ant_y_diff*i)
                ant2_node_2 = (ant2_x - ant_x_diff*i, ant2_y - ant_y_diff*i)
                
                if ant1_node_1 != ant2 and check_within_bound(ant1_node_1[0], ant1_node_1[1], map): antinodes.append( (ant, ant1_node_1, ant1, ant2) )
                if ant1_node_2 != ant2 and check_within_bound(ant1_node_2[0], ant1_node_2[1], map): antinodes.append( (ant, ant1_node_2, ant1, ant2) )
                if ant2_node_1 != ant1 and check_within_bound(ant2_node_1[0], ant2_node_1[1], map): antinodes.append( (ant, ant2_node_1, ant1, ant2) )
                if ant2_node_2 != ant1 and check_within_bound(ant2_node_2[0], ant2_node_2[1], map): antinodes.append( (ant, ant2_node_2, ant1, ant2) )
            
            if verbose: print(ant, ant1, ant2, ant_x_diff, ant_y_diff, ant_slope, '||', ant1_node_1, ant1_node_2, check_within_bound(ant1_node_1[0], ant1_node_1[1], map)) 
            if verbose: print('\t||', ant1_node_1, ant1_node_2, ant2_node_1, ant2_node_2,)
    
    return antinodes
        