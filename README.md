# Implementation of clustering ML methods

Here you can find our implementations of several clustering methods. We made them for university project.

Implemented methods:
- dbscan
- k-means
- mean-shift
- ward
- hierarchical (single linkage)
- hierarchical (complete linkage)

For testing we used few indexes, 3 of them also were implemented:
- DBI
- jaccard index
- silhouette index

## Report 

Report sumarizing our form can be found in the main folder as a file research-report.pdf


## How to run (windows)

first install required packages

    pip install -r requirements.txt
    
Each method is in separate folder (our implementation and sklearn usage).
Single and hierarchical methods have same base codes since they are very similar.

run by command

    python main.py
