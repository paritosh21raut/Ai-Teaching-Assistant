import requests
import os

HEADERS = {
    "User-Agent": "TeachingAssistantBot/1.0 (paritoshproject@example.com)"
}


def search_wikipedia(query):
    search_url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json"
    }

    response = requests.get(search_url, params=params, headers=HEADERS)

    if response.status_code != 200:
        return None

    data = response.json()
    search_results = data.get("query", {}).get("search", [])

    if not search_results:
        return None

    # Try to find exact or closest match
    query_lower = query.lower()

    for result in search_results:
        if query_lower in result["title"].lower():
            return result["title"]

    # fallback to first result
    return search_results[0]["title"]


def fetch_wikipedia_summary(title):
    summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"

    response = requests.get(summary_url, headers=HEADERS)

    if response.status_code != 200:
        print("Summary API failed:", response.status_code)
        return None, None, None

    data = response.json()

    title = data.get("title", "No Title Found")
    summary = data.get("extract", "No Summary Found")

    image_url = None
    if "thumbnail" in data:
        image_url = data["thumbnail"].get("source")

    return title, summary, image_url


def retrieve_wikipedia_data(query):
    best_title = search_wikipedia(query)

    if not best_title:
        return None, None, None

    title, summary, image_url = fetch_wikipedia_summary(best_title)

    image_path = None
    if image_url:
        image_path = download_image(image_url)

    return title, summary, image_path

import os
import requests

def download_image(image_url, save_folder="images"):
    if not image_url:
        return None

    os.makedirs(save_folder, exist_ok=True)

    headers = {
        "User-Agent": "TeachingAssistantBot/1.0"
    }

    response = requests.get(image_url, headers=headers, stream=True)

    if response.status_code != 200:
        print("Image download failed:", response.status_code)
        return None

    image_name = image_url.split("/")[-1]
    image_path = os.path.join(save_folder, image_name)

    with open(image_path, "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)

    return os.path.abspath(image_path)
