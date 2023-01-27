#!/usr/bin/env python3

import os
import json

print("Content Type: aplication/json")
print()
print(json.dumps(dict(os.environ), indent=2))

#Q:3 http_user_agent