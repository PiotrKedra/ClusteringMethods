from dbscan.dbscan import dbscan
from src.measurement import DBI
from sklearn import metrics as met

# x = k_means(15, '../resources/2d_dataset/r15.csv')
x = dbscan(1, 3, '../resources/2d_dataset/compound.csv', True)
dbi = DBI.computeDBI(x)
dbi_sklearn = met.davies_bouldin_score(x[:, :-1], x[:, -1])
print(dbi)
print(dbi_sklearn)
