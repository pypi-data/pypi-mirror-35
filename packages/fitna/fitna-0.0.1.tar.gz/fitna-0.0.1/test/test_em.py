import fitna
import numpy as np


normal_params = [
    fitna.data.NormalDist(norm=1, mean=np.array([4.5, 4.5]), cov=np.array([[1, -0.5], [-0.5, 1]]), size=20),
    fitna.data.NormalDist(norm=1, mean=np.array([6.0, 7.0]), cov=np.array([[1,  0.5], [ 0.5, 1]]), size=20)
]

normal_mixture = fitna.data.NormalMixture(normal_params)
data_points = normal_mixture.rvs()

print('*** NormalMixture ***')

data_points = np.concatenate(data_points, 1).T
#print(data_points)
print('concatenated data shape:', data_points.shape)


initial_estimates = [
    fitna.data.NormalDist(norm=0.5, mean=np.array([3.0, 5.0]), cov=np.array([[1, 0.0], [0.0, 1]]) ),
    fitna.data.NormalDist(norm=0.5, mean=np.array([8.0, 8.0]), cov=np.array([[1, 0.5], [0.5, 1]]) )
]


ll_new, all_estimates = fitna.em.do_em(data_points, initial_estimates)

print('*** Original params ***')
print(normal_params)

print('*** Initial estimates ***')
print(initial_estimates)

print('*** All estimates ***')
print(all_estimates)
