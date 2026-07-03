import json


def load_catalog():
    with open("data/shl_catalog.json", "r", encoding="utf-8") as file:
        return json.load(file)


catalog = load_catalog()


def search_catalog(query):
    query = query.lower()

    results = []

    for item in catalog:

        searchable_text = (
            item.get("name", "") + " " +
            item.get("description", "") + " " +
            " ".join(item.get("keys", []))
        ).lower()

        score = 0

        # Match every word
        for word in query.split():
            if len(word) > 2 and word in searchable_text:
                score += 2

        # Extra weight if role/technology appears in assessment name
        if "python" in query and "python" in item.get("name", "").lower():
            score += 10

        if "java" in query and "java" in item.get("name", "").lower():
            score += 10

        if "sql" in query and "sql" in item.get("name", "").lower():
            score += 10

        if "javascript" in query and "javascript" in item.get("name", "").lower():
            score += 10

        if "developer" in query:
            if "developer" in searchable_text:
                score += 5

        if "engineer" in query:
            if "engineer" in searchable_text:
                score += 5

        if "software" in query:
            if "software" in searchable_text:
                score += 5

        if score > 0:
            new_item = item.copy()
            new_item["score"] = score
            results.append(new_item)

    results.sort(key=lambda x: x["score"], reverse=True)

    return results