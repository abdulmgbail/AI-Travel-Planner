from utils.model_loaders import ModelLoader

from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition
from tools.place_search_tool import PlaceSearchTool
from tools.currency_conversion_tool import CurrencyConverterTool
from tools.expense_calculator_tool import CalculatorTool
from tools.weather_info_tool import WeatherInfoTool
from prompt_library.prompt import create_system_prompt
from typing import Optional


class GraphBuilder():
    def __init__(self,model_provider:str = "groq"):
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm = self.model_loader.load_llm()
        self.tools = []

        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        budget_type: Optional[str] = "medium",
        currency: Optional[str] = "USD",
        travel_style: Optional[str] = "mixed"
        question: str = ""

        # self.weather_tool = WeatherInfoTool()
        self.currency_tool = CurrencyConverterTool()
        self.expense_tool = CalculatorTool()
        self.place_search_tool = PlaceSearchTool()

        # Store trip parameters
        self.start_date = start_date
        self.end_date = end_date
        self.budget_type = budget_type
        self.currency = currency
        self.travel_style = travel_style
        self.question = question

        self.system_prompt = create_system_prompt(
            user_input=self.question,
            start_date=self.start_date,
            end_date=self.end_date,
            budget_type=self.budget_type,
            currency=self.currency,
            travel_style=self.travel_style
        )

        self.tools.extend([
            #* self.weather_tool.weather_tool_list
            * self.currency_tool.currency_converter_tool_list,
            * self.expense_tool.calculator_tool_list,
            * self.place_search_tool.place_search_tool_list
        ])

        self.llm_with_tools = self.llm.bind_tools(tools=self.tools)

       # self.system_prompt = SYSTEM_PROMPT

        self.graph = None

    def agent_function(self, state: MessagesState):
        """ Main Agent Function """
        user_question  = state["messages"]
        user_input = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(user_input)
        return {"messages":[response]}


    def build_graph(self):
        graph_builder = StateGraph(MessagesState)
        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))
        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditional_edges("agent",tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge("agent", END)

        self.graph = graph_builder.compile()
        return self.graph

    def __call__(self):
        return self.build_graph()
    