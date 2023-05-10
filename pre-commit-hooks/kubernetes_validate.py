#!/usr/bin/env python3

import re
import yaml

def validate_labels(file):
  try:
    f = open(file)
    yamls = yaml.load_all(f, yaml.FullLoader)
    for y in yamls:
      for k,v in y['metadata']['labels'].items():
        regex = r"(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])?"
        label_regex = re.compile(regex)
        assert re.fullmatch(label_regex, v), ('%s contains invalid label value in %s: %s validation regex is %s' % (file, k, v, regex))

  except (KeyError, TypeError):
   pass
