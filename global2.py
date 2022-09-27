names = ["Ben","Omer","Karen"]
revenues = [2400,60,12000]

names_array = np.array([names])

data = np.concatenate((names_array,revenues),axis = 0)
print(data)