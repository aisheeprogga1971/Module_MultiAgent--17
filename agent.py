from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent

# Connect to your SQLite database
db = SQLDatabase.from_uri("sqlite:///data/my_database.db")


# Create LLM
llm = ChatOpenAI(
    temperature=0,
    model="gpt-4"  
)

# Create SQL Agent
agent = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True
)