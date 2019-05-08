import random

class Cluster:

	def init(self):
		self.x_points = []
		self.y_points = []
	def set_centroid(self,x, y):
		self.centroid = []
		self.centroid.append(x)
		self.centroid.append(y)
	def get_centroid_x(self):
		return self.centroid[0]
	def get_centroid_y(self):
		return self.centroid[1]
	def add_point(self, x,y):
		self.x_points.append(x)
		self.y_points.append(y)

	def get_distance(self,x, y):
		x_dist = x - self.centroid[0]
		y_dist = y - self.centroid[1]
		distance = abs(x_dist + y_dist)
		return distance

	def get_avg_x(self):
		x_sum = sum(self.x_points)
		x_avg = float(x_sum) / len(self.x_points) 
		return x_avg

	def get_avg_y(self):
		y_sum = sum(self.y_points)
		y_avg = float(y_sum) / len(self.y_points)
		return y_avg

	def update_centroid(self,x,y):
		self.centroid[0] = x
		self.centroid[1] = y



def use_default():
	global points, x_points, y_points
	points = 8
	print(points)
	x_points = [2,2,8,5,7,6,1,4]
	y_points = [10,5,4,8,5,4,2,9]
	num_clusters(3)


# get dataset
def enter_dataset():
	global points,x_points,y_points
	x_points = []
	y_points = []
	points = int(input('please enter number of points of dataset: '))
	for point in range(points): 
		x_points.append(int(input('please enter x of point %d : ' %(point+1))))
		y_points.append(int(input('please enter y of point %d : ' %(point+1))))

#create clusters 
def num_clusters(default=0):
	global cluster_list, cluster_number
	cluster_list = []
	if default==0:
		cluster_number = int(input('please enter number of clusters'))
	else:
		cluster_number = default
	for i in range(cluster_number): 
		i = Cluster()
		i.init()
		cluster_list.append(i)

def set_centroid_points(randomize=0):
	global cluster_list, points, x_points, y_points
	for cluster in range(len(cluster_list)):
		if randomize == 1:
			centroid_x = int(input('please enter x of centroid of cluster %d : ' %(cluster +1)))
			centroid_y = int(input('please enter y of centroid of cluster %d : ' %(cluster +1)))
			cluster_list[cluster].set_centroid(centroid_x, centroid_y)
		else:
			randi = random.randint(0, (points-1)) # same index in parallel arrays to get points
			centroid_x = x_points[randi]
			centroid_y = y_points[randi]
			cluster_list[cluster].set_centroid(centroid_x, centroid_y)
def display(cluster_list, iterations):
	i = 1
	print('cluster centroids = '),
	for cluster in cluster_list:
		print('cluster %d x=%f y=%f' %(i, cluster.get_centroid_x(), cluster.get_centroid_y()))
		i += 1
	print('\n iterations = %d' %iterations)

def calculate():
	global cluster_list, points, x_points, y_points
	iterations = 1
	flag = False
	while(not flag):
		
		print('point',end='')
		for i in range(len(cluster_list)): #header
			print('-----M%d distance ------' %(i+1), end=''),
		print('Cluster', end='')
		
		for i in range(points):
			print('\n')
			print('(%d,%d) '%(x_points[i], y_points[i]), end='')
			min = 999
			for cluster in cluster_list:
				distance = cluster.get_distance(x_points[i], y_points[i])
				print('\t %d \t\t' %distance, end='')
				if distance < min:
					min = distance
					nearest = cluster
			print('cluster %d' %(cluster_list.index(nearest) +1))
			nearest.add_point(x_points[i], y_points[i])
		print('\n\n\n-----------------iteration %d----------------' %iterations)
		iterations += 1

		for i in range(len(cluster_list)): #header
			print('-----cluster %d ------' %(i+1), end=''),
			print('\n')
			print('point----x----y----\n', end=''),
			clusterr = cluster_list[i]
			for j in range(len(clusterr.x_points)):
				x = clusterr.x_points[j]
				y = clusterr.y_points[j]
				print('(%d,%d)----%d------%d' %(x, y ,x, y))
			if(clusterr.x_points):	
				x = clusterr.get_avg_x()
				y = clusterr.get_avg_y()
				if(x == clusterr.get_centroid_x() and y == clusterr.get_centroid_y()):
					flag = True
				else:
					flag = False
				clusterr.set_centroid(x,y)
				clusterr.init() # remove all points from clusters
				print('avg-----%.2f-------%.2f'%(x, y))
				print('new M%d--%.2f------%.2f'%(i+1, x, y))
				

			print('\n\n\n')

	display(cluster_list, iterations)
			
		




while(True):
	print("-------------------------------------")
	print("1) use default dataset and clusters")
	print("2) enter dataset")
	print("3) enter number of clusters ")
	print("4) use random centroid points")
	print("5) set centroid points ")
	print("6) calculate")
	print("-------------------------------------")
	choice = int(input('select: '))
	if choice == 1:
		use_default()
	if choice == 2:
		enter_dataset()
	if choice == 3:
		num_clusters()
	if choice == 4:
		set_centroid_points()
	if choice == 5:
		set_centroid_points(1)
	if choice == 6:
		calculate()
