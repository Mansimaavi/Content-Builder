import os
from openai import OpenAI
from dotenv import load_dotenv
from guardrail import check_guardrail
from tools import search_wikipedia

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_content(query: str):

    if not check_guardrail(query):
        return "This agent cannot provide information related to agriculture topics."

    context = search_wikipedia(query)

    prompt = f"""
Use the context below to generate structured content.

Context:
{context}

Topic:
{query}

Format:
Title
Introduction
Key Points
Conclusion
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":
    query = input("Enter topic: ")
    result = generate_content(query)
    print("\nGenerated Content:\n")
    print(result)
