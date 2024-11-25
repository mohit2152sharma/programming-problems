#!/bin/bash

ns=(1 10 100 1000 10000 100000 1000000 10000000 100000000 1000000000 10000000000)
versions=(3.9 3.10 3.11 3.12)

for python_version in "${versions[@]}"; do
  uv venv --python "$python_version" &>/dev/null
  source .venv/bin/activate
  python --version

  for i in "${ns[@]}"; do
    # setup python
    python test_for.py "$i"
  done
done
