from app.catalog import search_catalog
from app.gemini import ask_gemini


def get_chat_response(message: str):

    # Reject unrelated questions
    allowed_keywords = [
        "assessment",
        "test",
        "developer",
        "engineer",
        "manager",
        "analyst",
        "java",
        "python",
        "sql",
        "javascript",
        "excel",
        "cloud",
        "aws",
        "azure",
        "data",
        "software",
        "coding",
        "programming",
        "skill",
        "graduate",
        "sales",
        "finance",
        "accountant",
        "customer",
        "personality",
        "leadership"
    ]

    message_lower = message.lower()

    if not any(word in message_lower for word in allowed_keywords):
        return {
            "user_message": message,
            "reply": (
                "# SHL AI Assessment Assistant\n\n"
                "I can recommend **SHL assessments** based on job roles, skills, or technologies.\n\n"
                "### Example Queries\n"
                "- Java Developer\n"
                "- Python Developer\n"
                "- Software Engineer\n"
                "- Leadership Assessment\n"
                "- Sales Assessment\n"
                "- Personality Assessment"
            )
        }

    results = search_catalog(message)

    if results:

        catalog_text = ""

        for item in results[:5]:
            catalog_text += f"""
Assessment Name: {item.get("name")}
Description: {item.get("description")}
Duration: {item.get("duration")}
Job Levels: {", ".join(item.get("job_levels", []))}
Languages: {", ".join(item.get("languages", []))}
Remote Testing: {item.get("remote")}
Adaptive: {item.get("adaptive")}
Link: {item.get("link")}

------------------------------------
"""

        prompt = f"""
You are an SHL Assessment Expert.

The user asked:

"{message}"

Use ONLY the assessment information below.

{catalog_text}

Instructions:

1. Recommend ONLY assessments from the provided catalog.
2. Never invent assessment names.
3. Recommend a maximum of 3 assessments.
4. Keep the response under 200 words.
5. Format the response using Markdown.
6. Use bullet points.
7. Use bold titles.
8. For every assessment include:
   - **Assessment Name**
   - **Duration**
   - **Job Levels**
   - **Short Description**
   - **Reason**
   - **Link:** [View Assessment](URL)
9. Do not include any information that is not present in the catalog.
"""

    else:

        prompt = f"""
You are an SHL Assessment Expert.

The user asked:

"{message}"

No suitable assessment was found.

Reply in Markdown.

Politely explain that no matching SHL assessment exists.

Suggest the user try another related role or technology.
"""

    answer = ask_gemini(prompt)

    return {
        "user_message": message,
        "reply": answer
    }