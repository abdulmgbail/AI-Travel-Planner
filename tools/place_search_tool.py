import os
from typing import List
from langchain.tools import tool
from utils.place_info_search import GooglePlacesSearchTool, TavilySearchTool
from dotenv import load_dotenv


class PlaceSearchTool:

    def __init__(self):
        load_dotenv()
        self.google_places_api_key=os.getenv("GOOGLE_PLACES_API_KEY")
        print(f"Google Places API Key: {self.google_places_api_key}")
        self.tavily_search = TavilySearchTool()
        self.google_search = GooglePlacesSearchTool(self.google_places_api_key)
        self.place_search_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        
        """Setup all tools for the place search tool"""

        @tool
        def search_attractions(place: str) -> str:
            """Search for attractions in a given place"""
            try:
                attraction_result = self.google_search.google_search_attractions(place)
                if attraction_result:
                    return f"Following are the attractions of {place} as suggested by google:{ attraction_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_attractions(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the attractions of {place}: {tavily_result}"  ## Fallback search using tavily in case google places fail
    
        @tool
        def search_resturants(place: str) -> str:
            """Search for restaurants in a given place"""
            try:
                resturant_result = self.google_search.google_search_restaurants(place)
                if resturant_result:
                    return f"Following are the restaurants of {place} as suggested by google: {resturant_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_restaurants(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the restaurants of {place}: {tavily_result}"  ## Fallback search using tavily in case google places fail

        @tool
        def search_activities(place: str) -> str:
            """Search for activities in a given place"""
            try:
                activity_result = self.google_search.google_search_activities(place)
                if activity_result:
                    return f"Following are the activities of {place} as suggested by google: {activity_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_activities(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the activities of {place}: {tavily_result}"  ## Fallback search using tavily in case google places fail

        @tool
        def search_transportation(place: str) -> str:
            """Search for transportation options in a given place"""
            try:
                transport_result = self.google_search.google_search_transportation(place)
                if transport_result:
                    return f"Following are the transportation options of {place} as suggested by google: {transport_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the transportation options of {place}: {tavily_result}"

        return [search_attractions, search_resturants, search_activities,search_transportation]
