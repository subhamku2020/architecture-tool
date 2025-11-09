def create_diagram_json(architecture):
    root = [{"id": "0"}, {"id": "1", "parent": "0"}]
    i = 2
    for group, services in architecture.items():
        for s in services:
            root.append({
                "id": str(i),
                "value": s,
                "parent": "1",
                "style": "shape=rectangle"
            })
            i += 1
    return {"mxGraphModel": {"root": root}}
