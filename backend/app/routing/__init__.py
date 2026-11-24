"""Accessible routing: pure Python, no web framework and no database.

Stage 1 builds this package. Planned modules:

- geo.py        LatLon (a validated coordinate) and haversine distance in meters
- graph.py      Node, Edge, and Graph (adjacency lists; each edge usable both ways)
- edge_cost.py  The accessibility rules: an edge's cost for a profile, or "blocked"
- astar.py      A* search over the graph using edge_cost

Keeping this free of FastAPI and the database means it can be tested on a
small hand-drawn network in milliseconds.
"""
