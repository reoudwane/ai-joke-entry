JOKE = "I asked my AI coding agent to fix one bug. It fixed it, introduced 47 more, and charged me in tokens to apologise for each one."

import os
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
