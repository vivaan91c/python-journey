# Filter the list of student scores to keep only the passing scores (>= 50). 
# Store in "passing" and print.

scores = [88, 45, 92, 33, 67, 55, 28, 71]
passing = list(filter(lambda s: s >= 50, scores))
print(passing) 