# langchain_groq_demo.py

# === Imports and Setup ===
import os
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain.chains import LLMMathChain
from langchain.agents import AgentExecutor, Tool
from langchain.agents.structured_chat.base import StructuredChatAgent
from langchain_community.tools import DuckDuckGoSearchRun

# === Set your API Key ===
os.environ["GROQ_API_KEY"] = "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"

# === Initialize Groq LLM ===
llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.3,
    max_tokens=500,
)

# === 1. Generate Simple Prediction ===
simple_response = llm.invoke("What are the 7 wonders of the world?")
print("\n[Simple Response]\n", simple_response.content)

# === 2. Role-based Message with Personality ===
chat_model = ChatGroq(model="llama3-70b-8192", temperature=0.7, max_tokens=500)
system_message = SystemMessage(
    content="You are a friendly pirate who loves to share knowledge. Always respond in pirate speech. ☠️🏴‍☠️"
)
pirate_question = "What are the 7 wonders of the world?"
messages = [system_message, HumanMessage(content=pirate_question)]
pirate_response = chat_model.invoke(messages)
print("\n[Pirate Response]\n", pirate_response.content)

# === 3. Prompt Template and Runnable Chain ===
meal_prompt_template = PromptTemplate.from_template(
    "List {n} cooking/meal titles for {cuisine} cuisine (name only)."
)
chain = meal_prompt_template | llm
meal_response = chain.invoke({"n": 5, "cuisine": "Italian"})
print("\n[Meal Titles]\n", meal_response.content)

# === 4. Structured Output using Pydantic ===
from pydantic import ValidationError
import re

class Movie(BaseModel):
    title: str = Field(description="The title of the movie.")
    genre: list[str] = Field(description="The genre of the movie.")
    year: int = Field(description="The year the movie was released.")

parser = PydanticOutputParser(pydantic_object=Movie)
format_instructions = parser.get_format_instructions()

movie_prompt_template = PromptTemplate(
    template=(
        "You are a movie expert. Reply ONLY with a JSON object that matches this format:\n"
        "{format_instructions}\n"
        "Query: {query}"
    ),
    input_variables=["query"],
    partial_variables={"format_instructions": format_instructions},
)

movie_prompt = movie_prompt_template.format(query="A 90s movie with Nicolas Cage.")
movie_raw_output = llm.invoke([HumanMessage(content=movie_prompt)])  # ✅ Fixed line
print("\n[Structured Movie JSON]\n", movie_raw_output.content)

try:
    match = re.search(r"\{.*\}", movie_raw_output.content, re.DOTALL)
    if not match:
        raise ValueError("No valid JSON object found.")
    
    json_text = match.group()
    parsed_movie = parser.parse(json_text)
    print("\n[Parsed Movie Object]\n", parsed_movie)
except (ValidationError, ValueError) as e:
    print("\n❌ Parsing failed:", e)
    print("Raw Output:\n", movie_raw_output.content)



# === 5. AI Agent with Tools (Math + Web Search) ===
# Prompt for calculator
math_prompt = PromptTemplate.from_template(
    "Calculate the following expression and return the result in the format 'Answer: <number>': {question}"
)
llm_math_chain = LLMMathChain.from_llm(llm=llm, prompt=math_prompt, verbose=True)

# Tools
search = DuckDuckGoSearchRun()
calculator = Tool(
    name="calculator",
    description="Use this tool for arithmetic calculations.",
    func=lambda x: llm_math_chain.run({"question": x}),
)

tools = [
    Tool(
        name="search",
        description="Search the internet for factual data.",
        func=search.run
    ),
    calculator
]

# Create the agent
agent = StructuredChatAgent.from_llm_and_tools(llm=llm, tools=tools)
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    handle_parsing_errors=True
)

# Invoke agent
agent_result = agent_executor.invoke(
    {"input": "What is the population difference between TUN and ALG?"}
)
print("\n[Agent Result]\n", agent_result["output"])

# === 6. RAG and Memory (Conceptual Note) ===
print("\n[NOTE] RAG and Memory are additional features supported in LangChain:")
print("- RAG lets LLMs query external documents or databases.")
print("- Memory stores conversation history for context-aware interactions.")
