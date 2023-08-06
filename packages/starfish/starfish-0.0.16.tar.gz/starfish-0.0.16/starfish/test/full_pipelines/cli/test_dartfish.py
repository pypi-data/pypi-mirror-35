# STEPS
#
# starfish filter ScaleByPercentile
# starfish filter ZeroByChannelMagnitude
# starfish detect_spots PixelSpotDetector

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from typing import Sequence

import jsonpath_rw
import numpy as np
import pandas as pd

from starfish.intensity_table import IntensityTable
from starfish.types import Features
from starfish.util import clock


# class TestWithIssData(unittest.TestCase):
#     STAGES = (
#         []# starfish filter ScaleByPercentile,
#         []# starfish filter ZeroByChannelMagnitude,
#         []# starfish detect_spots PixelSpotDetector)