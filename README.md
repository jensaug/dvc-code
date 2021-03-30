# dvc-code

## Init
poetry shell
poetry install

## Ingest
python src/ingest.py

## Run pipeline
dvc repro

## Store DVC data in tmp remote
dvc push


