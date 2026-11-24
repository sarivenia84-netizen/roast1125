#!/usr/bin/env python3
import os, sys
out_dir=os.getenv("MAKEFUN_OUTPUT_DIR")
if not out_dir: sys.exit("MAKEFUN_OUTPUT_DIR not set")
roast="My agent loops read_file on a path it invented, apologizes, loops again—same path."
with open(os.path.join(out_dir,"entry.txt"),"w",encoding="utf-8") as f: f.write(roast)