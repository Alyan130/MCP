from mcp.server import FastMCP
import httpx
from bs4 import BeautifulSoup

mcp = FastMCP("scrapper")

@mcp.tool()
async def web_scrapper(url: str):
    '''Scrapes web content with url 
    
    Args:
      url : webpage url to scrape content 

    Return:
      text : text of scrapped web page
    '''
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text()
            return text
    except Exception as e:
        return "Error scraping URL!"

if __name__ == "__main__":
    mcp.run(transport="stdio")
