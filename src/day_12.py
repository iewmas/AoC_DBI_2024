
import networkx as nx 


def get_fence_cost(regions):
    cost = 0
    
    for region in nx.connected_components(regions):
        #print(type(region), len(region))
        
        if len(region) == 1:
            cost = cost + (1 * 4)
        else: 
            perimeters = sum( [4 - nx.degree(regions, n) for n in region] )
            
            cost = cost + ( len(region) * perimeters )
            #print( [nx.degree(regions, n) for n in region], perimeters, ( len(region) * perimeters ), ' || ', cost )
         
    
    return cost

