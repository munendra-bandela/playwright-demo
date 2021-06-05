#!/usr/bin/env python
import sys
import os

# To solve import issues with Robot, add root directory to SYS PATH

current_dir = os.path.dirname(__file__)
print('Current DIR:', current_dir)
sys.path.append(os.path.join(current_dir))
