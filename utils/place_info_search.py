import os
import json
from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper

class GooglePlacesSearchTool:

    def __init__(self, api_key: str):
        self.places_wrapper = GooglePlacesAPIWrapper(api_key=api_key)
        self.places_tool = GooglePlacesTool(api_wrapper=self.places_wrapper)
    

    def google_search_attractions(self, place: str) -> dict:
        """
        Searches for attractions in a given place using Google Places API.

        Args:
            place (str): The name of the place to search for attractions.

        Returns:
            dict: A dictionary containing the search results.
        """
        return self.places_tool.run(f"top attractive places in and around {place}")
    
    def google_search_restaurants(self, place: str) -> dict:
        """
        Searches for restaurants in a given place using Google Places API.

        Args:
            place (str): The name of the place to search for restaurants.

        Returns:
            dict: A dictionary containing the search results.
        """
        return self.places_tool.run(f"what are the top 10 restaurants and eateries in and around {place}")


    def google_search_activity(self, place: str) -> dict:
        """
        Searches for popular activities in the specified place using GooglePlaces API.
        """
        return self.places_tool.run(f"Activities in and around {place}")
    

    def google_Search_transportation(self, place: str) -> dict:
        """
        Searches for transportation options in the specified place using GooglePlaces API.
        """
        return self.places_tool.run(f"What are the different modes of transportations available in {place}")
    
class TavilySearchTool:

    def __init__(self):
        pass

    def tavily_search_attractions(self, place: str) -> dict:
        """
        Searches for attractions in a given place using Tavily Search API.

        Args:
            place (str): The name of the place to search for attractions.

        Returns:
            dict: A dictionary containing the search results.
        """
        tavily_tool = TavilySearch(topic="general",include_answer="advanced")
        result = tavily_tool.invoke({"query":f"top attractive places in and around {place}"})
        if isinstance(result,dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_restaurants(self, place: str) -> dict:
        """
        Searches for restaurants in a given place using Tavily Search API.

        Args:
            place (str): The name of the place to search for restaurants.

        Returns:
            dict: A dictionary containing the search results.
        """
        tavily_tool = TavilySearch(topic="general",include_answer="advanced")
        result = tavily_tool.invoke({"query":f"what are the top 10 restaurants and eateries in and around {place}"})
        if isinstance(result,dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_activity(self, place: str) -> dict:
        """
        Searches for popular activities in the specified place using Tavily Search API.
        """
        tavily_tool = TavilySearch(topic="general",include_answer="advanced")
        result = tavily_tool.invoke({"query":f"Activities in and around {place}"})
        if isinstance(result,dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_transportation(self, place: str) -> dict:
        """
        Searches for transportation options in the specified place using Tavily Search API.
        """
        tavily_tool = TavilySearch(topic="general",include_answer="advanced")
        result = tavily_tool.invoke({"query":f"What are the different modes of transportations available in {place}"})
        if isinstance(result,dict) and result.get("answer"):
            return result["answer"]
        return result
    