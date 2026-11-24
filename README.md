# Accessible Sidewalk Map

Most cities don't have complete data on sidewalks, crosswalks, and curb ramps,
so wheelchair and stroller routing is unreliable. This project builds an
accessible pedestrian map of the UW–Madison campus and downtown Madison, with
routing that avoids stairs, raised curbs, and steep grades. Later phases use
aerial and street-level imagery to fill in what OpenStreetMap is missing.

| Phase | What it does | Status |
|---|---|---|
| **1. Platform** | OpenStreetMap sidewalk data in PostGIS, accessible A* routing behind a FastAPI service, a React map, an LLM "Ask" box, deployed on AWS | in progress |
| **2. Overhead imagery** | Detect sidewalks and crosswalks in NAIP aerial imagery; find what OSM is missing | planned |
| **3. Street imagery** | Detect curb ramps in Mapillary photos; feed per-crossing curb status into routing | planned |

## Stack

| Layer | Choice |
|---|---|
| Backend | Python 3.12, FastAPI, pytest |
| Database | PostgreSQL + PostGIS (Docker) |
| Frontend | React + TypeScript (Vite), ArcGIS Maps SDK for JavaScript |
| CI/CD | GitHub Actions |
| Hosting | AWS |

## Phase 1 roadmap

- [ ] **Stage 1: Routing core.** Haversine, graph, edge costs, A* in plain Python, tested on a hand-drawn network
- [ ] **Stage 2: Database.** PostGIS in Docker, schema, spatial queries
- [ ] **Stage 3: Data import.** Download OSM sidewalks, split into a graph, load into PostGIS
- [ ] **Stage 4: API.** FastAPI endpoints for routes, places, and the network layer
- [ ] **Stage 5: Map.** React + TypeScript front end
- [ ] **Stage 6: Deploy.** Docker image, AWS, CI deploys on merge
- [ ] **Stage 7: AI layer.** Natural-language route requests with LLM tool calling, plus an eval

## Run locally

```bash
cd backend
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
uvicorn app.main:app --reload      # http://localhost:8000/health
                                   # interactive API docs: http://localhost:8000/docs
pytest
```

## Data and licenses

Map data © [OpenStreetMap contributors](https://www.openstreetmap.org/copyright), ODbL.
