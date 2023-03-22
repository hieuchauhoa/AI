# Input graph:
graph = {
    '1': ['2', '4','12'],
    '2': ['1', '4'],
    '3': ['7'],
    '4': ['1','2','6','7'],
    '5': ['6','8','9'],
    '6': ['4','5','7','13'],
    '7': ['3','4','6'],
    '8': ['5','9'],
    '9': ['5','8'],
    '10': ['11','12'],
    '11': ['10','12'],
    '12': ['1','10','11'],
    '13': ['6']
}
Close = []  # List for visited nodes.
Open = []  # Initialize a queue
def bfs(Close, graph, s,g):  # function for BFS
    Open.append(s)
    while Open:          # Creating loop to visit each node
        n = Open.pop(0)
        if n==g:
            break
        for neighbour in graph[n]:
            if neighbour not in Close and neighbour not in Open:
                Open.append(neighbour)
        Close.append(n)
# Driver Code
print("Following is the Breadth-First Search")
# Input bfs(close, đồ thị, điểm đầu, điểm cuối):
bfs(Close, graph, '1','9')# function calling
print(Open)
print(Close)
