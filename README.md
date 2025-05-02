# LangChain Groq Demo

This project demonstrates various features of the LangChain framework, with a focus on integrating the `ChatGroq` model. It showcases different use cases such as generating simple responses, creating role-based personalities, generating structured outputs, building agents, and more.

## Features

1. **Simple Predictions:**
   - Uses `ChatGroq` to generate a simple response to a query like "What are the 7 wonders of the world?"
  
2. **Role-based Personality Responses:**
   - Uses a pirate persona to generate responses, applying role-based messages.

3. **Meal Title Generator:**
   - Generates meal names using a prompt template and an LLM chain.

4. **Structured Output with Pydantic:**
   - Parses the output into structured formats, such as movie recommendations based on a prompt.

5. **AI Agent with Tools:**
   - Integrates multiple tools, including a math calculator and a web search tool, to answer complex queries.

6. **RAG and Memory (Conceptual):**
   - Discusses how to extend the agent with document retrieval and memory features.

## Requirements

Before running the script, make sure to install the necessary dependencies:

```bash
pip install langchain langchain_groq pydantic duckduckgo-search
