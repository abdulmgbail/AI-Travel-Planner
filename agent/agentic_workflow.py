from utils.model_loaders import ModelLoader
from prompt_library.prompt import SystetmPrompt
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition


class GraphBuilder():
    def __init__(self,model_provider:str = "groq"):
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm = self.model_loader.load_llm()
        self.tools = []

        self.system_prompt = SYSTEM_PROMPT

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
        graph_builder.add_conditional_edge("agent",tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge("agent", END)

        self.graph = graph_builder.compile()
        return self.graph

    def __call__(self):
        return self.build_graph()
    