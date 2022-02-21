import requests
import datetime as dt

TOKEN = "J0n4th4n"
USERNAME = "jonathangarvin"
GRAPH_ID = "boozefree"

# curl -X POST https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret'
#     -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu"}'

pixela_graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

graph_cfg = {
    "id": GRAPH_ID,
    "name": GRAPH_ID,
    "unit": "commit",
    "type": "int",
    "color": "shibafu"
}

pixela_header = {
    "X-USER-TOKEN": TOKEN
}
# Create the graph
response = requests.post(url=pixela_graph_endpoint, json=graph_cfg, headers=pixela_header)

graph_endpoint = f"{pixela_graph_endpoint}/{GRAPH_ID}"
# Plot a point on the graph

# day = (dt.datetime.now() - dt.timedelta(days=1)).strftime("%Y%m%d")
Today = dt.datetime.now().strftime("%Y%m%d")
graph_plot = {
    "date": Today,
    "quantity": "1"
    }
update_graph = requests.post(url=graph_endpoint, json=graph_plot, headers=pixela_header)

print(f"Access graph at {pixela_graph_endpoint}/{GRAPH_ID}.html")

# Update a pixel

date = (dt.datetime.now() - dt.timedelta(days=3)).strftime("%Y%m%d")
update_endpoint = f"{graph_endpoint}/{date}"
update_cfg = {
    "quantity": "1"
}
modify = requests.put(url=update_endpoint, headers=pixela_header, json=update_cfg)

#Delete graph
del_endpoint = "https://pixe.la/v1/users/jonathangarvin/graphs/graph1"
delete = requests.delete(url=del_endpoint, headers=pixela_header)
