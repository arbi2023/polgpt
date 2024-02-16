# POLGpt

Fine tuned conversation with the man behind https://comemesuunaslavina.retrocog.org
The openai pip package and a subscription are required for model generation and usage.

## Scraper

`scraper.py` is hardcoded to work on comemesuunaslavina, it may be used to update the training and validation datasets

## Existing datasets

The Word as of Feb 2024

## Model generation

`openai api fine_tunes.create -t .datasets/training_dataset.jsonl -v ./datasets/validation_dataset.jsonl --model gpt-3.5-turbo --n_epochs 4`, provided you have set env variable `OPENAI_API_KEY` to a valid openai API key, creates a decent first iteration

## Model usage

` openai api completions.create -m your_model_id --prompt "your_prompt_text"`
