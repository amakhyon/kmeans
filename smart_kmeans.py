import random
import math
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

	def get_distance(self,x, y,eqn): #eqn.. 1 for Manhattan, 2 for Euclidian
		if(eqn == 1):
			x_dist = abs(x - self.centroid[0])
			y_dist = abs(y - self.centroid[1])
			distance = x_dist + y_dist
		else:
			distance = math.sqrt( (x - self.centroid[0])**2 + (y - self.centroid[1])**2 )
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
	global points, x_points, y_points,cluster_list
	points = 8
	print(points)
	x_points = [2,2,8,5,7,6,1,4]
	y_points = [10,5,4,8,5,4,2,9]
	num_clusters(3)
	cluster_list[0].set_centroid(2,10)	
	cluster_list[1].set_centroid(5,8)	
	cluster_list[2].set_centroid(1,2)	


# get dataset
def enter_dataset():
	global points,x_points,y_points
	x_points = []
	y_points = []
	points = int(input('please enter number of points of dataset: '))
	for point in range(points): 
		x_points.append(float(input('please enter x of point %d : ' %(point+1))))
		y_points.append(float(input('please enter y of point %d : ' %(point+1))))

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
	global cluster_list, points, x_points, y_points, cluster_number
	for cluster in range(cluster_number):
		if randomize == 1:
			centroid_x = float(input('please enter x of centroid of cluster %d : ' %(cluster +1)))
			centroid_y = float(input('please enter y of centroid of cluster %d : ' %(cluster +1)))
			cluster_list[cluster].set_centroid(centroid_x, centroid_y)
		else:
			randi = random.randint(0, (points-1)) # same index in parallel arrays to get points
			centroid_x = x_points[randi]
			centroid_y = y_points[randi]
			cluster_list[cluster].set_centroid(centroid_x, centroid_y)
def display(cluster_list, iterations):
	i = 1
	print('\n\n\n\n')
	print('===========================================')
	print('cluster centroids = '),
	for cluster in cluster_list:
		print('cluster %d x=%.2f y=%.2f' %(i, cluster.get_centroid_x(), cluster.get_centroid_y()))
		i += 1
	print('\n iterations = %d' %(iterations-1))
	print('===========================================')
	print('\n\n\n\n')

def calculate(eqn):
	global cluster_list, points, x_points, y_points
	iterations = 1
	flag = False
	while(flag < len(cluster_list)):
		flag=0
		print('point',end='')
		for i in range(len(cluster_list)): #header
			print('-----M%d distance ------' %(i+1), end=''),
		print('Cluster', end='')
		
		for i in range(points):
			print('\n')
			print('(%d,%d) '%(x_points[i], y_points[i]), end='')
			min = 999
			for cluster in cluster_list:
				if eqn == 1:
					distance = cluster.get_distance(x_points[i], y_points[i],1)
				else:
					distance = cluster.get_distance(x_points[i], y_points[i],2)
				print('\t %.2f \t\t' %distance, end='')
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
					flag += 1
				else:
					flag -= 1
				clusterr.set_centroid(x,y)
				clusterr.init() # remove all points from clusters
				print('avg-----%.2f-------%.2f'%(x, y))
				print('new M%d--%.2f------%.2f'%(i+1, x, y))
				

			print('\n\n\n')

	display(cluster_list, iterations)
print('\n\t\t\tAssem Makhyon')			
print('\n\n\n\n***************************************************************')
print('*[[please follow this sequence]]                             		 ')
print('*a)enter dataset[2]  b)enter number of clusters[3] c)set centroid points[5]    ')
print('OR to use default settings: a)use default dataset and clusters[1] b)calculate[6]')
print('***************************************************************\n\n\n\n')



while(True):
	print("-------------------------------------")
	print("1) use default dataset and clusters")
	print("2) enter dataset")
	print("3) enter number of clusters ")
	print("4) use random centroid points")
	print("5) set centroid points ")
	print("6) calculate Manhattan")
	print("7) calculate Euclidian")
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
		calculate(1)
	if choice == 7:
		calculate(2)
