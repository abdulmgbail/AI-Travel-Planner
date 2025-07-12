from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent.agentic_workflow import GraphBuilder
from fastapi.responses import JSONResponse
from utils.save_to_document import save_document
from starlette.responses import JSONResponse
from langchain_core.messages import HumanMessage
import os 
import datetime
from dotenv import load_dotenv
from typing import Optional

load_dotenv()


app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

class QueryRequest(BaseModel):
    question: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    budget_range: Optional[str] = None
    trip_duration: Optional[int] = None
    tavel_style: Optional[str] = None

@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    """
        Endpoint to handle queries to the travel agent.
    """
    try:
        print(query)
        graph = GraphBuilder(model_provider="groq")
        react_app = graph()
    
        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as f:
            f.write(png_graph)

        print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")

        query_dict = query.model_dump(exclude_none=True)
        
        # Assuming request is a pydantic object like: {"question": "your text"}
        messages = {"messages": [query_dict]}

        prompt = (
            f"{query.question}\n"
            f"Start Date: {query.start_date or 'Not specified'}\n"
            f"End Date: {query.end_date or 'Not specified'}\n"
            f"Budget: {query.budget_range or 'Not specified'}\n"
            f"Trip Duration: {query.trip_duration or 'Not specified'} days\n"
            f"Travel Style: {query.tavel_style or 'Not specified'}"
        )

        # Send properly formatted message
        messages = [{"role": "user", "content": prompt}]
        output = react_app.invoke({"messages": messages})

       # output  = react_app.invoke(messages)

         # If result is dict with messages:
        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content  # Last AI response
        else:
            final_output = str(output)

        
        # ✅ Save the final output to a Markdown file
        saved_filename = save_document(final_output)
        
        return {"answer": final_output,"saved_file": saved_filename}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})