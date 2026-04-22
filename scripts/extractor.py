
import json, os, sys

def run():
    manifest_path = sys.argv[1]
    if not os.path.exists(manifest_path):
        return

    with open(manifest_path, 'r') as f:
        data = json.load(f)
    
    # Advanced Mapping for KiCad-style Manifests
    package = {
        "name": data.get("name"),
        "desc": data.get("description"),
        "tags": data.get("keywords", "").split(" ") if isinstance(data.get("keywords"), str) else data.get("keywords", []),
        "footprint": data.get("footprint"),
        "datasheet": data.get("datasheet"),
        "schema_version": data.get("version", "1.1"), # Incremented version
        "base_url": f"https://cdn.jsdelivr.net/gh/{os.environ['GITHUB_REPOSITORY']}@main/{os.path.dirname(manifest_path)}/"
    }
    print(json.dumps(package))

if __name__ == "__main__":
    run()
