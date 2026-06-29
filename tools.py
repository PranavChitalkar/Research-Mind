
from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
#from rich import print
from rich import print
load_dotenv()

## first tool by tavily;

tavily=TavilyClient(api_key=os.getenv("TVLY_API_KEY"))
 
@tool
def web_search(query:str)->str:
    """ Search the web for the given query and return the top result.(titles,urls,snippets) """
    results=tavily.search(query=query,max_results=5)
    out=[]
    for r in results['results']:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\r"
        )
         
    return "\n----\n".join(out)

#print(web_search.invoke("what are latest news about wars"))

## tool 2 web scapper;

@tool
def scapper_url(url:str)->str:
    """Scrape and return the text content from the given URL for deeper reading."""
    try:
        resp=requests.get(url,timeout=8,headers={"User-Agent":"Mozilla/5.0"})
        soup=BeautifulSoup(resp.text,"html.parser")
        for tag in soup(["script","style","nav","footer"]):
            tag.decompose()
        return soup.get_text(separator=" ",strip=True)[:3000]
    
    except Exception as e:
        return f"Could not scraper URL :{str(e)}"


#print(web_scapper.invoke(" https://www.cbsnews.com/us-iran-tensions"))