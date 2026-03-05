name: GPT API Test

on:
  schedule:
    - cron: '0 9 * * 1'
  workflow_dispatch:

jobs:
  test-gpt:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3    ← この行を追加
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install OpenAI library
        run: pip install openai
      
      - name: Run GPT test
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: python test_gpt.py
