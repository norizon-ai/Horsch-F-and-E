import urllib.request
import urllib.error
import json
import base64

url = "https://norizon.atlassian.net/wiki/rest/api/space"
username = "omar.lotfy@norizon.de"
token = "ATATT3xFfGF0KGsnOZ-ghY-b-GujVOVtB4Hv5-QV3I_rJqTJ6BOBzMeDL0WXTuXP65oNL9n13U1DBtCkhU4X2dlpLYbFd767wHSB_9_WlXsvpUnTrcGKoww1wFu06d5b1n-sdvaxohUlSKkrURFpkneLAJo1TxyQuPc7xqbf7UQjH3hQltwtc2M=0EE5EFF8"

auth_string = f"{username}:{token}"
encoded_auth = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")

req = urllib.request.Request(url)
req.add_header("Authorization", f"Basic {encoded_auth}")
req.add_header("Accept", "application/json")

try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        results = data.get("results", [])
        print(f"Found {len(results)} spaces.")
        for space in results:
            key = space.get("key")
            name = space.get("name")
            print(f"- {key}: {name}")
except urllib.error.URLError as e:
    if hasattr(e, "code"):
        print(f"HTTP Error: {e.code} - {e.reason}")
        print(e.read().decode())
    else:
        print(f"URL Error: {e.reason}")
except Exception as e:
    print(e)
