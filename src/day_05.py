
import networkx as nx 


def process_input(input):
    rules = list() 
    manuals = list() 

    if isinstance(input, str): lines = input.split()
    else: lines = input 

    for line in lines:
        if line.find('|') >= 0: rules.append(line.strip())
        elif line.find(',') >= 0: manuals.append(line.strip())

    return rules, manuals


def is_valid_manual(rules, manual):
    for m1, m2 in zip(manual[:-1], manual[1:]):
        if f'{m1}|{m2}' not in rules: return False

    return True


def find_valid_manuals(rules, manuals, verbose = False):
    manual_valid = list() 

    for m in manuals:
        m_list = m.split(',')

        if is_valid_manual(rules, m_list):
            if verbose: print('VALID', m_list)
            manual_valid.append(m_list)
        else: 
            if verbose: print('INVALID', m_list)

    return manual_valid


def sum_middle_numbers(manuals):
    result = 0 

    for m in manuals:
        result = result + int( m[int(len(m)/2)] )

    return result


def find_invalid_manuals(rules, manuals, verbose = False):
    manual_invalid = list() 

    for m in manuals:
        m_list = m.split(',')

        if is_valid_manual(rules, m_list):
            if verbose: print('VALID', m_list)
        else: 
            if verbose: print('INVALID', m_list)
            manual_invalid.append(m_list)

    return manual_invalid


def build_rule_graph(rules):
    G = nx.DiGraph()

    for r in rules:
        r1, r2 = r.split('|')
        G.add_edge(r1, r2)

    return G


def fix_manual_graph(G, rules, manual):
    Gs = nx.subgraph(G, manual)
    start_nodes = [node for node in Gs.nodes() if Gs.in_degree(node)==0]
    end_nodes = [node for node in Gs.nodes() if Gs.out_degree(node)==0]

    for sn in start_nodes:
        for en in end_nodes:
            for p in nx.all_simple_paths(Gs, sn, en):
                if len(p) == len(manual) and is_valid_manual(rules, p): return p 

    return None
