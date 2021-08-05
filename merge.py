#!/usr/bin/env python3

# Copyright Brian Warner
# SPDX-License-Identifier: MIT
#
# Usage: merge.py template_file data_file output_file
#

import sys
import os
from pprint import pprint
from string import Template
import csv

if len(sys.argv) != 4:
  print('\nUsage: merge.py template_file data_file output_file\n')
  sys.exit(1)

template_filename = sys.argv[1]
data_filename = sys.argv[2]
output_filename = sys.argv[3]

if not os.path.isfile(template_filename):
  print('\nError: Template file does not exist\n')
  sys.exit(1)

if not os.path.isfile(data_filename):
  print('\nError: Data file does not exist\n')
  sys.exit(1)

if os.path.isfile(output_filename):
  print('\nError: Output file already exists, delete it or choose another name\n')
  sys.exit(1)

with open(template_filename) as template_file:
  template = Template(template_file.read())

with open(data_filename) as data_file:
  datareader = csv.DictReader(data_file)
  for row in datareader:

    with open(output_filename, 'a') as output_file:
      output_file.write(template.substitute(row))


