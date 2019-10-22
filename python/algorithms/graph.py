import queue
class Graph():
	def __init__(self, n, edges):
		self.n = n
		self.edges = edges
		self.mat = [[0 for i in range(self.n)] for j in range(self.n)]
		for x in self.edges:
			self.mat[x[0]-1][x[1]-1] = 1
			#self.mat[x[1]-1][x[0]-1] = 1
	
	def adjacancy_matrix(self):
		return self.mat

	def out_degree(self):
		d = dict()
		for r in range(self.n):
			d[r+1]  = sum(self.mat[r])
		return d

	def in_degree(self):
		d = dict()
		for c in range(self.n):
			summ = 0
			for r in range(self.n):
				summ += self.mat[r][c]
			d[c+1]  = summ
		return d

	def bfs(self, start_node):
		q = queue.Queue(100)
		q.put(start_node)
		l = []
		m = self.mat
		visited = [False for i in range(self.n)]
		visited[start_node-1] = True
		while(not q.empty()):
			x = q.get()
			l.append(x)
			for i in range(self.n):
				if m[x-1][i] == 1 and not visited[i]:
					q.put(i+1)
					visited[i] = True
		return l

	def dfs(self, start_node):
		def travel_depth(v, visited, l):
			visited[v-1] = True
			l.append(v)
			for i in range(self.n):
				if self.mat[v-1][i] == 1 and not visited[i]:
					travel_depth(i+1, visited, l)
			return l

		visited = [False for i in range(self.n)]
		l = []
		l = travel_depth(start_node, visited, l)
		return l

g = Graph(6, [(1, 2), (1, 3), (2, 4), (2, 5), (3, 5), (4, 5), (4, 6), (5, 6)])
for x in g.adjacancy_matrix():
	for y in x:
		print(y, end="  ")
	print()

g2 = Graph(4, [(1, 2), (1, 3), (2, 3), (3, 1), (3, 4), (4, 4)])
print(g2.dfs(3))

# n = int(input("No.of nodes: "))
# edges = [[0 for i in range(n)] for i in range(n)]
# n_edges = int(input("No.of edges: "))
# edges = []
# for i in range(n_edges):
# 	u, v = map(int,input().split())
# 	edges.append((u, v))

# g = Graph(n, edges)
# matrix = g.adjacancy_matrix()

# for z in matrix:
# 	print(z)

# indeg = g.in_degree()
# outdeg = g.out_degree()

# print("Out degree: ", outdeg)
# print("In degree: ", indeg)