from crewai import Agent
from dotenv import load_dotenv
load_dotenv()
from tools import tools
from langchain_google_genai import ChatGoogleGenerativeAI
import os


##call gemeni 
llm=ChatGoogleGenerativeAI(model="gemini-flash-latest" ,verbose=True,temprature=0.5,google_api_key=os.getenv("GOOGLE_API_KEY"))
#creating the agent

news_researcher=Agent(
    role="Senior Researcher",
    goal="Uncover the breaking technology in{topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity,yo're at the forefront of"
        "inovation ,eger to explore and share knowledge that could change th world"
    ),
    tools=[tools],
    llm=llm,
    allow_delegation=True


)
news_writer=Agent(
    role="Senior writer",
    goal="Narrate the breaking technology in{topic}",
    verbose=True,
    memory=True,
    backstory=(
        "with a fair and engaging writing style,you're dedicated to crafting compelling narratives that captivate readers and shed light on the latest technological breakthroughs"
    ),
    tools=[tools],
    llm=llm,
    allow_delegation=True


)