from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import load_prompt
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv();

print("\nLoading the Model...\n")
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.5) # Loading the model. 
 
# Importing the template. It automatically turns the json into PromptTemplate
Template = load_prompt('template.json')

# Create the parser. This parses the text automatically.
parser = StrOutputParser()

# CHAIN THEM TOGETHER
# This creates a single pipeline: Data goes into the Template -> gets formatted -> goes into the Model -> gets parsed
chain = Template | model | parser

# Collect user input
player_name = input("Which player are you looking for: ")
timeframe = input("What timeframe you require the information for: ")
specific_focus = input("What is your specific focus: ")
target_audience = input("What is your target audience: ")

request = {
    "player_name": player_name,
    "timeframe": timeframe,
    "specific_focus": specific_focus,
    "target_audience": target_audience
}

print("\nGenerating analysis...\n")
result = chain.invoke(request)

print(result)