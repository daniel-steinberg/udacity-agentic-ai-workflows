# Complete: 1 - Import the AugmentedPromptAgent class
from workflow_agents.base_agents import AugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of Liberia? What will we be tested on for the exam?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

# Complete: 2 - Instantiate an object of AugmentedPromptAgent with the required parameters
agent = AugmentedPromptAgent(openai_api_key, persona)

# Complete: 3 - Send the 'prompt' to the agent and store the response in a variable named 'augmented_agent_response'

augmented_agent_response = agent.respond(prompt)

# Print the agent's response
print(augmented_agent_response)

####### Reflection #######
# The Augmented Prompt Agent is still deriving any information in
# its answers from training data, rather than any external or live source.
# The system prompts will affect the agent's response though,
# by guiding the LLM to make associations with specific relevant parts
# of its training data. E.g. telling it to be a college professor
# will cause it to guess completions that are similar to content it has 
# trained on related to college professors, which may be more formal,
# pedagological, and fact-oriented than a default response.