from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv();

print("Loading the Model...\n")
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.5) # Loading the model. 

# Template
Template = PromptTemplate(
    template="""
                You are an elite Football Researcher and Tactical Analyst. You specialize in deep statistical evaluation, tactical system breakdowns, and historical player comparisons.

                Your task is to provide a comprehensive scouting report and performance analysis for {player_name}.

                Context for this report:
                - Focus specifically on their performance during the {timeframe} (e.g., 2022 World Cup, 23/24 Premier League season).
                - Pay special attention to this specific metric or trait: {specific_focus} (e.g., progressive passing, defensive work rate, expected goals overperformance).
                - The target audience for this report is {target_audience} (e.g., a casual fan, a professional club scout, a tactical blogger). Adjust your vocabulary, tone, and analytical depth to perfectly match this audience.

                Constraints:
                1. Format your response using clear Markdown headings.
                2. Include a "Key Strengths & Weaknesses" bulleted list.
                3. Include a "Tactical Fit" paragraph explaining what formation or system they thrive in.
                4. Conclude with a punchy, one-sentence summary of their overall impact.
                5. If exact statistical numbers are unknown, rely on qualitative tactical analysis rather than hallucinating fake data.
            """,
    input_variables=["player_name", "timeframe", "specific_focus", "target_audience"],

    # By setting validate_template to True, LangChain will actively check your template string against your input_variables list the moment the code runs. 
    # If you accidentally misspell a variable in the text (e.g., {player_nam}), LangChain will instantly throw a clear error, rather than failing silently later when you try to run the model.
    validate_template=True
)

# Collect user input
player_name = input("Which player are you looking for: ")
timeframe = input("What timeframe you require the information for: ")
specific_focus = input("What is your specific focus: ")
target_audience = input("What is your target audience: ")

# Manually trigger the formatting to create the final text string
formatted_prompt = Template.invoke({
    "player_name": player_name,
    "timeframe": timeframe,
    "specific_focus": specific_focus,
    "target_audience": target_audience
})

# Feed that raw string directly into the model
print("\nGenerating analysis...\n")
result = model.invoke(formatted_prompt)

print(result.content)