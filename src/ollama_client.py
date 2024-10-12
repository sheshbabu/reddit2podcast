import requests


def send_single_message(model, messages):
    url = "http://localhost:11434/api/chat"

    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "options": {"num_ctx": 8192},
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()

        data = response.json()
        if "message" in data and "content" in data["message"]:
            return data["message"]["content"]
        else:
            raise ValueError("Unexpected response format from Ollama API")

    except requests.RequestException as e:
        raise requests.RequestException(
            f"Error communicating with Ollama API: {str(e)}"
        )
