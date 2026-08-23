from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

text = """
Football is played between two teams, with the objective of scoring more goals than the opponent. 
Players use their feet to control and pass the ball, although goalkeepers are allowed to use their hands 
inside their penalty area. A standard professional match consists of two 45-minute halves.

The modern game has produced many legendary players. Lionel Messi is widely recognized for his dribbling, 
close control, passing ability, and creativity. Cristiano Ronaldo is known for his athleticism, finishing, 
heading ability, and goal-scoring record. Both players have won numerous individual and team awards.

The Earth's climate has changed throughout its history, but human activities have significantly increased 
the concentration of greenhouse gases in the atmosphere. Burning fossil fuels releases carbon dioxide, 
while deforestation reduces the planet's ability to absorb it. Rising global temperatures can contribute 
to melting ice sheets, rising sea levels, and changes in weather patterns.

Renewable energy sources provide alternatives to fossil fuels. Solar panels convert sunlight into electricity, 
while wind turbines use moving air to generate power. Hydroelectric plants generate electricity by using 
flowing water. These technologies can reduce greenhouse gas emissions when replacing fossil-fuel-based 
electricity generation.

Python is a high-level programming language known for its relatively simple syntax. It is widely used in 
web development, data analysis, automation, scientific computing, and artificial intelligence. Python's 
large ecosystem of libraries makes it particularly useful for rapidly developing applications.

Machine learning is a branch of artificial intelligence in which computer systems learn patterns from data. 
Supervised learning uses labeled examples, while unsupervised learning attempts to discover patterns without 
explicit labels. Neural networks are a family of machine-learning models that have become particularly 
successful in areas such as image recognition and natural-language processing.

The human heart is a muscular organ that circulates blood throughout the body. It contains four chambers 
and contracts rhythmically to pump blood through the circulatory system. The right side generally sends 
blood toward the lungs, while the left side pumps oxygen-rich blood to the rest of the body.

Regular physical activity can improve cardiovascular fitness and strengthen muscles. Exercise can also help 
maintain healthy body weight and improve overall physical well-being. Activities such as walking, swimming, 
cycling, and running can all contribute to an active lifestyle.
"""

# We use semantic chunker to split the text based on their meaning.
# It generates vector embedding of every chunk and then compares their meaning, if two chunks differ by a good margin, then it will split them.
# However it is not very accurate :(

# The "breakpoint_threshold_type" is used to specify the function by which the splitter should split the text.
# These are the major types: percentile, standard_deviation, interquartile, gradient
# Study about them for more information.

splitter = SemanticChunker(
    model, breakpoint_threshold_type="standard_deviation", breakpoint_threshold_amount=1
)

result = splitter.split_text(text)

print(len(result))

print(result[0])
