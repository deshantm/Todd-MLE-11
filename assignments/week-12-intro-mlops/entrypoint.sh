#!/bin/bash

. /opt/conda/etc/profile.d/conda.sh
conda activate stock-predictor
uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8000
