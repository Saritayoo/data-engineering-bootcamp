import os

import google.genai as genai


# GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"


def get_embedding(client, model: str = "gemini-embedding-exp-03-07", text: str = ""):
    result = client.models.embed_content(
        model=model,
        contents=text,
    )
    return result.embeddings[0]


# Set up a Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# Get embeddings
vec_q = get_embedding(client, text="Remote work allows employees to be more flexible and productive.").values
vec_c = get_embedding(client, text="Work from home is very productive for me").values
print(vec_q, vec_c)

vec_q = get_embedding(client, text="Hello").values
vec_c = get_embedding(client, text="Hey").values
print(vec_q, vec_c)
