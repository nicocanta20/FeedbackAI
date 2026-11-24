# FeedbackAI

Get feedback on a startup idea, a critical analysis of it, or a new idea if you
don't have one yet. A small Streamlit app on top of OpenAI's chat models.

## Features
- **Get Feedback**: constructive feedback on your idea
- **Get Critique**: critical analysis focused on market viability, innovation,
  and potential challenges
- **Don't have an idea?**: generates a startup idea based on current trends

You use your own OpenAI API key, entered in the sidebar. It is not stored.

## Run locally
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Stack
Python · Streamlit · OpenAI Python SDK · `gpt-3.5-turbo`

Started in November 2022; rewritten in January 2024.

## Status
No longer runs: OpenAI retired `gpt-3.5-turbo` on October 23, 2026.
