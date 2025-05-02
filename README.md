LangChain Groq Demo 🚀
Welcome to the LangChain Groq Demo project! This showcase highlights the integration of the powerful ChatGroq model within the LangChain framework, illustrating a wide range of use cases. From generating simple responses to creating role-based personalities, this demo covers the exciting potential of AI interactions.

Key Features ✨
🔮 Simple Predictions:

Description: Generate quick, accurate responses to queries like "What are the 7 wonders of the world?"

Example: "What are the 7 wonders of the world?" → [Response from ChatGroq]

🏴‍☠️ Role-based Personality Responses:

Description: Transform ChatGroq into a fun, engaging persona! For instance, use a pirate persona to respond to inquiries.

Example: "Tell me a joke!" → *Pirate Persona*: "Why did the pirate go to school? To improve his arrrrrrrticulation!"

🍽️ Meal Title Generator:

Description: Leverage prompt templates and LLM chains to generate creative meal names for your next culinary adventure.

Example: "Suggest a meal title!" → *Generated Title*: "Fiery Dragon's Delight"

📊 Structured Output with Pydantic:

Description: Parse AI responses into structured, easily readable formats like movie recommendations, travel tips, and more.

Example: "Suggest a good movie!" → [Structured Response: { 'title': 'Inception', 'genre': 'Sci-Fi', 'rating': 8.8 }]

🛠️ AI Agent with Tools:

Description: Combine various tools (math calculator, web search) to create a powerful, multi-functional agent capable of handling complex tasks.

Example: "How far is Paris from New York?" → [Agent Response with Web Search Tool]

📚 RAG and Memory (Conceptual):

Description: Explore the potential of memory and document retrieval in AI agents for more personalized, context-aware interactions.

Concept: This section explores how memory functions and how document retrieval could enhance the AI’s ability to answer questions based on prior conversations or external knowledge sources.

## Requirements

Before running the script, make sure to install the necessary dependencies:

```bash
pip install langchain langchain_groq pydantic duckduckgo-search
