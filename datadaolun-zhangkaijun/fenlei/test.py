testdata = ['overcast', 'hot', 'high', 'FALSE']
labels = ['outlook', 'temperature','humidity','windy']



a = {'outlook': {'sunny': {'humidity': {'high': 'no', 'normal': 'yes'}}, 'rainy': {'windy': {'FALSE': 'yes', 'TRUE': 'no'}}, 'overcast': 'yes'}}
print(a['outlook']['sunny'])