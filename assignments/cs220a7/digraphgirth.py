import sys

def find_girth(graph, order):
    min_cycle = float('inf') #pos infiity to say nothings been found yet
    
    # bfs
    for start in range(order):
        distances = {start: 0}
        
        queue = [start]
        queue_index = 0
        
        #loop til pointer at end of list
        while queue_index < len(queue):
            current = queue[queue_index]#manual queue here
            queue_index += 1 
            
            for neighbor in graph.get(current, []):
                if neighbor == start: #found a cycle back to start
                    min_cycle = min(min_cycle, distances[current] + 1)
                #bfs next step to visit other nodes
                elif neighbor not in distances:
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)
                    
    return min_cycle if min_cycle != float('inf') else 0

def main():
    lines = sys.stdin.read().splitlines()

    current_node = 0
    graph = {}
    order = None

    for line in lines:
        line_str = line.strip()
        
        #setup order for the graph if not set
        if order is None:
            if line_str == "0":
                break
            if line_str == "":
                continue
            order = int(line_str)
            current_node = 0
            graph = {}
            continue
        
        #make sure nothing is empty and that we place the neighbors in the graph
        if line_str == "":
            out_neighbors = []
        else:
            out_neighbors = [int(x) for x in line_str.split() if x.isdigit()]

        graph[current_node] = out_neighbors
        current_node += 1

        #end of order print girth of digraph;
        if current_node == order:
            print(find_girth(graph, order))
            order = None
        

if __name__ == "__main__":
    main()
