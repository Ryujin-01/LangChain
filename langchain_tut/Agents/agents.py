from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain_classic.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent
import requests, os

load_dotenv()

# Creating a search tool
search_tool = DuckDuckGoSearchRun()


# Creating a weather tool
Weather_API = os.getenv("OPEN_WEATHER_MAP_API_KEY")


@tool
def get_weather_data(city: str) -> str:
    """Get the current weather data for a city"""

    # You can get the url endponints from the official documentation for Open Weather Map

    # Step 1: First convert city to lat and lon as our weather api requires that
    # geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={Weather_API}"

    # A better way to write the above url is:
    # Trimming the url
    geo_url = "http://api.openweathermap.org/geo/1.0/direct"

    # Putting the parameters part into a dictionary. It is cleaner and more readable.
    geo_params = {
        "q": city,  # The actual variable we are passing to this function
        "limit": 1,  # Number of the locations in the API response (up to 5 results can be returned in the API response)
        "appid": Weather_API,
    }

    try:
        geo_response = requests.get(
            url=geo_url,  # Our trimmed url
            params=geo_params,  # The parameters of the url
            timeout=10,  # This means to wait at most 10 seconds for the HTTP request before giving up. Otherwise it could take forever.
        )

        # ".raise_for_status()" is a method from the requests library that checks whether your HTTP request was successful.
        # If .raise_for_status() encounters an unsuccessful HTTP status code, it raises an exception and stops executing the remaining lines inside the try block.
        geo_response.raise_for_status()

        location = geo_response.json()

        # If the city name is invalid
        if not location:
            raise ValueError("Could not find city :(")

        # Check the response structure from the Open Weather Map documentation. You can also print it in the terminal to check.
        lat = location[0]["lat"]
        lon = location[0]["lon"]

        # Step 2: Finally get the weather data for the required city.
        weather_url = f"https://api.openweathermap.org/data/2.5/weather"
        weather_params = {
            "lat": lat,
            "lon": lon,
            "appid": Weather_API,
            "units": "metric",  # Gives response in metric system
        }

        weather_response = requests.get(
            url=weather_url,
            params=weather_params,
            timeout=10,
        )

        weather_response.raise_for_status()

        return weather_response.json()

    # If a RequestException occurs inside the try block, this catches that error and stores the error object in a variable called e.
    # requests.RequestException. This is a base exception class provided by the requests library.
    # It covers errors related to making HTTP requests, such as: Connection error, Timeout, Invalid URL, HTTP-related request errors
    except requests.RequestException as e:
        raise RuntimeError(
            f"Couldn't get API response :(\n {e}",
        )


# Creating an LLM
llm_model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

# Creating a prompt for the agent
prompt = """
You are a helpful assistant.

You have access to two tools:

1. A web search tool for finding current or external information.
2. A weather tool for getting current weather for a city.

Use the weather tool whenever the user asks about current weather.
Use the web search tool when you need current information that
cannot be obtained from the weather tool.

Answer clearly and concisely.
"""

# Standard way to create an agent
agent = create_agent(
    model=llm_model,
    tools=[search_tool, get_weather_data],
    system_prompt=prompt,
    debug=True,  # Shows detailed agent execution/debug information
)

# e.g. What is the weather at capital of Spain ?
query = input("Ask: ")

# Standard way to pass the user query to the agent
result = agent.invoke({"messages": [{"role": "user", "content": query}]})

# If you want the whole agent state
print(result)

# If you just want the final output
print(result["messages"][-1].content)
