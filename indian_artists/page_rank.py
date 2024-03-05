import csv
import json

epsilon = 0.01
d = 0.85

edges = {}
inside_category = {}

with open('graph.csv', newline='') as graph_csv_file:
    reader = csv.DictReader(graph_csv_file)
    for row in reader:
        # if row['hop_from_category'] == '0':
        edges[row['node']] = json.loads(row['edges_within_category'])['key']
        edges[row['node']].extend(json.loads(row['edges_outside_category'])['key'])
        inside_category[row['node']] = row['hop_from_category'] == "0"

n = len(edges)

page_ranks = {node: 1/n for node in edges}

i = 0

while True:
    new_page_ranks = {node: 0 for node in edges}
    for node in edges:
        for out_node in edges[node]:
            new_page_ranks[out_node] += page_ranks[node] / len(edges[node])
    
    delta = 0
    for node in edges:
        new_page_ranks[node] = d * new_page_ranks[node] + (1-d) / n
        delta += abs(page_ranks[node] - new_page_ranks[node])
    
    page_ranks = new_page_ranks
    i += 1
    print(i, end=",")

    if delta < epsilon:
        break
output = {}
for page in page_ranks:
    output[page] = {"rank": page_ranks[page], "inside_category": inside_category[page]}
# with open('page_ranks_inside_only.json', 'w') as fp:
with open('page_ranks.json', 'w') as fp:
    json.dump(output, fp)
    
