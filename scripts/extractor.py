
import json, os, sys
def run():
    # Find the changed manifest
    manifest_path = sys.argv[1]
    with open(manifest_path, 'r') as f:
        data = json.load(f)
    
    # Generate the rich metadata package
    package = {
        "name": data.get("name"),
        "desc": data.get("description"),
        "tags": data.get("tags", []),
        "schema_version": data.get("version", "1.0"),
        "base_url": f"https://cdn.jsdelivr.net/gh/{os.environ['GITHUB_REPOSITORY']}@main/{os.path.dirname(manifest_path)}/"
    }
    print(json.dumps(package))
if __name__ == "__main__": run()
