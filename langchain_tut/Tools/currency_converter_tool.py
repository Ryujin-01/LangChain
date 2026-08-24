from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
import requests, os

load_dotenv()

# Loading up the API
API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")


# Creating the tool to hit the API and fetch the conversion rate
@tool
def get_conversion_rate(BaseCurrency: str, RequiredCurrency: str) -> float:
    """Converts base currency to required currency"""

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{BaseCurrency}/{RequiredCurrency}"

    try:  # Runs this code, but if a particular error occurs, don't immediately crash. Instead, go to the corresponding except block.

        # This sends an HTTP GET request to the URL stored in url.
        response = requests.get(url=url)

        # This checks whether the HTTP request was successful. e.g. 200	Successful, 400	Bad request etc.
        response.raise_for_status()

        # The API doesn't normally send Python dictionaries directly. It sends JSON.
        # response.json() converts that JSON into a Python object, normally a dictionary:
        data = response.json()

        # This extracts the value associated with the "conversion_rate" key.
        return data["conversion_rate"]

    # If a "requests.RequestException" occurs anywhere inside the try block, execute this code.
    # RequestException is a base exception type provided by the requests library.
    # "as e" stores the actual exception object in the variable:
    except requests.RequestException as e:

        # You're essentially saying: "The API request failed, so tell the rest of my program that something went wrong."
        # Why use raise and not print ?
        # print() merely displays a message. raise actually tells Python: "An error occurred. Stop normal execution here."
        raise RuntimeError(f"Couldn't get the API response: {e}")


# print(get_conversion_rate.invoke({"BaseCurrency": "USD", "RequiredCurrency": "INR"}))


# Creating the tool to actually convert the currency. It is just a simple multiply tool
@tool
def convert(BaseCurrency: float, ConversionRate: float) -> float:
    """Converts the Base Currency to the Required Currency by multiplying it to the Conversion Rate"""

    return BaseCurrency * ConversionRate


baseCurr = input("Base Currency: ")  # e.g. USD
reqCurr = input("Required Currency: ")  # e.g. INR
amount = input("Amount: ")  # e.g. 100

query = f"Give me the conversion rate of {baseCurr} to {reqCurr}. Also convert {amount} {baseCurr} to {reqCurr}"
history = [HumanMessage(query)]

# Setting up and binding the LLM
llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
llm_with_tools = llm.bind_tools([get_conversion_rate, convert])

# Calling our tools
llm_response = llm_with_tools.invoke(query)
history.append(llm_response)
tools = llm_response.tool_calls
# NOTE: There will be only one tool because we haven't got the second parameter of the tool "convert" that is the "ConversionRate"
# print(tools)

# Executing our tool
conversion_rate_response = get_conversion_rate.invoke(tools[0])
history.append(conversion_rate_response)
# print(conversion_rate_response)

# Calling our "convert" tool cause now we've got the conversion rate.
convert_tool = llm_with_tools.invoke(history)
history.append(convert_tool)

# Executing our convert tool
convert_tool_response = convert.invoke(convert_tool.tool_calls[0])
history.append(convert_tool_response)
# print(convert_tool_response)

# print(history)

# Final result
parser = StrOutputParser()
chain = llm_with_tools | parser
final_result = chain.invoke(history)
print(final_result)
