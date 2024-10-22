import numpy as np

def caculate(matr_list):
  if len(matr_list) < 9:
			raise ValueError("List must contain nine numbers.")

	#转化
	matr = np.array(matr_list).reshape(3,3)

	#计算统计量
	mean_axis1 = np.mean(matr,axis=1)
	mean_axis2 = np.mean(matrix,axis=0)
	mean_flattened = np.mean(matr)

  variance_axis1 = np.var(matrix, axis=1)
  variance_axis2 = np.var(matrix, axis=0)
  variance_flattened = np.var(matrix)
 	std_axis1 = np.std(matrix, axis=1)
  std_axis2 = np.std(matrix, axis=0)
  std_flattened = np.std(matrix)
    
  max_axis1 = np.max(matrix, axis=1)
  max_axis2 = np.max(matrix, axis=0)
  max_flattened = np.max(matrix)
    
  min_axis1 = np.min(matrix, axis=1)
  min_axis2 = np.min(matrix, axis=0)
  min_flattened = np.min(matrix)
    
  sum_axis1 = np.sum(matrix, axis=1)
  sum_axis2 = np.sum(matrix, axis=0)
  sum_flattened = np.sum(matrix)

	result = {
        'mean': [mean_axis1.tolist(), mean_axis2.tolist(), mean_flattened],
        'variance': [variance_axis1.tolist(), variance_axis2.tolist(), variance_flattened],
        'standard deviation': [std_axis1.tolist(), std_axis2.tolist(), std_flattened],
        'max': [max_axis1.tolist(), max_axis2.tolist(), max_flattened],
        'min': [min_axis1.tolist(), min_axis2.tolist(), min_flattened],
        'sum': [sum_axis1.tolist(), sum_axis2.tolist(), sum_flattened]
    }

	return result

print(calculate([0,1,2,3,4,5,6,7,8]))
