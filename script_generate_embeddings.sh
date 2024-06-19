#!/bin/bash
if [ ! -f ".env" ]; then
  echo "[ERROR] .env file not found!"
  exit 1
fi
source venv/bin/activate
time bash -c "$(grep -v '^#' .env | xargs) python3 build_faq_embeddings.py"
