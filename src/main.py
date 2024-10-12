import sys
from src import reddit_client, ollama_client


# =================
# Get the comments
# =================

if len(sys.argv) != 2:
    print("Usage: make run url=<reddit_url>")
    sys.exit(1)
url = sys.argv[1]

comments = reddit_client.get_json(url)
comments = reddit_client.extract_comments(comments)

print(comments)

# ======================
# Summarize the comments
# ======================

prompt = f"""
Summarize the following discussion delimited with triple backticks in a narrative format.

Please summarize the provided text with the following criteria:
1. Provide a detailed, thorough, and concise summary.
2. Focus on capturing the main ideas and essential information, especially key insights.
3. Eliminate unnecessary details and emphasize critical points.
4. Strictly use the provided text without incorporating any external information.

```
{comments}
```
"""

messages = [{"role": "user", "content": prompt}]
summary = ollama_client.send_single_message("llama3.1", messages)

print(summary)

# ===============================
# Generate the podcast transcript
# ===============================

prompt = f"""
Use the following article delimited by triple backticks and write an engaging and interesting script for a 5 min podcast between Anna and Elsa.

Follow these rules:
* Don't use punctuations
* Spell out the numbers
* Add a space between acronyms
* Use [laugh] for laughing and [uv_break] for pause where necessary
* Strictly use the provided text without incorporating any external information
* Output without any accompanying text or explanation

Strictly output in JSON as per example:
[{{ "speaker": "Anna", "dialogue": "Hey Elsa, [laugh] how are you?" }},{{ "speaker": "Elsa", "dialogue": "I'm good, Anna. [uv_break] How are you?" }}]

```
{summary}
```
"""

messages = [{"role": "user", "content": prompt}]
transcript = ollama_client.send_single_message("llama3.1", messages)

print(transcript)
