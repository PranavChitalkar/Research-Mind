// This is the Multi-Agent System for the Research  
 
 >> There is the two tools
    1. Web Search : tool which talk to tavily
         api and fetch search results
    2. scrape_url : which take URL visit that page and extract
         clean readable text from it using BeautifullSoup


 >> There is agensts (we build the 4 agents in this)
    1. Search Agent using create_react_agent + AgentExecutor (use web search tools)
    2. Reader Agent using with same pattern but use scaper_url tool
    3. Write chain using the modern LCEL pipe syntax -prompt | llm | StrOutputParser()
        which take all research and  writes full report 
    4. Critic Chain again using LCEL pipe  which reads the report and give a score and feedback.
