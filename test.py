from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool
from langchain_aws import ChatBedrock
import logging
import os

os.environ["AWS_REGION_NAME"] = "us-east-1"

# CrewAI LLM config uses LiteLLM
llm = LLM(model="bedrock/anthropic.claude-3-haiku-20240307-v1:0")
researcher = Agent(
 role='Senior Research Analyst',
 goal='Uncover cutting-edge developments in AI and data science',
 backstory="You work at a leading tech think tank…",
 verbose=True,
 allow_delegation=False,
 llm=llm,
 tool=[SerperDevTool()] # Tool for online searching
)
# Define the Task
task1 = Task(
 description="Conduct a comprehensive analysis of the following topic: {topic}",
 expected_output="Full analysis report in bullet points",
 agent=researcher
)
crew = Crew(
 agents=[researcher],
 tasks=[task1],
 verbose=True,
)

logging.basicConfig(level=logging.DEBUG)

result = crew.kickoff(inputs={"topic":"Amazon Bedrock Foundation Models"})