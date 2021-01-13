"""
Update the default browsers.json file in order to only download the Chromium binary
"""

import inspect
import json
from pathlib import Path

import playwright


if __name__ == "__main__":
    browsers_path = Path(inspect.getfile(playwright)).parent / "driver/browsers.json"
    browsers = json.loads(browsers_path.read_text())
    browsers["browsers"] = [b for b in browsers["browsers"] if b["name"] == "chromium"]
    browsers_path.write_text(json.dumps(browsers, indent=4))
