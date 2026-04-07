import os
import time
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from tools import search_flights, search_hotels, calculate_budget
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# 1. Đọc System Prompt
try:
    with open("system_prompt.txt", "r", encoding="utf-8") as f:
        SYSTEM_PROMPT = f.read()
except FileNotFoundError:
    SYSTEM_PROMPT = "Bạn là trợ lý du lịch của TravelBuddy. Hãy trả lời bằng tiếng Việt."

# 2. Khai báo State
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

# 3. Khởi tạo LLM (OpenRouter) và Tools
tools_list = [search_flights, search_hotels, calculate_budget]

# Chú ý: Sử dụng base_url của OpenRouter và model qwen3.6-plus:free
llm = ChatOpenAI(
    model="qwen/qwen3.6-plus:free",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "https://localhost:3000", # Tùy chọn cho OpenRouter
        "X-Title": "TravelBuddy Agent",           # Tùy chọn cho OpenRouter
    }
)

llm_with_tools = llm.bind_tools(tools_list)

# 4. Agent Node
def agent_node(state: AgentState):
    messages = state["messages"]
    
    # Đảm bảo có System Message ở đầu nếu chưa có
    if not any(isinstance(m, SystemMessage) for m in messages):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages
    
    response = llm_with_tools.invoke(messages)
 
    # === LOGGING ===
    if response.tool_calls:
        for tc in response.tool_calls:
            print(f"-> Gọi tool: {tc['name']}({tc['args']})")
    else:
        # print(f"-> Trả lời trực tiếp")
        pass
        
    return {"messages": [response]}

# 5. Xây dựng Graph
builder = StateGraph(AgentState)

# Thêm các Node
builder.add_node("agent", agent_node)
tool_node = ToolNode(tools_list)
builder.add_node("tools", tool_node)

# Thêm các Edge
builder.add_edge(START, "agent")
builder.add_conditional_edges(
    "agent",
    tools_condition,
)
builder.add_edge("tools", "agent")

# Compile Graph với Checkpointer
checkpointer = MemorySaver()
graph = builder.compile(checkpointer=checkpointer)

# 6. Chat loop
if __name__ == "__main__":
    print("=" * 60)
    print("TravelBuddy — Trợ lý Du lịch Thông minh (Powered by Qwen 3.6 Plus)")
    print(" Gõ 'quit' để thoát")
    print("=" * 60)

    while True:
        user_input = input("\nBạn: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            print("Tạm biệt! Chúc bạn có những chuyến đi tuyệt vời.")
            break

        # Cơ chế thử lại (Retry Mechanism)
        max_retries = 1
        attempt = 0
        success = False
        
        while attempt <= max_retries and not success:
            try:
                print("\nTravelBuddy đang suy nghĩ...")
                # Sử dụng invoke với thread_id để duy trì bộ nhớ
                config = {"configurable": {"thread_id": "user_123"}}
                result = graph.invoke(
                    {"messages": [HumanMessage(content=user_input)]},
                    config=config
                )
                
                # Lấy message cuối cùng làm câu trả lời
                final_response = result["messages"][-1]
                print(f"\nTravelBuddy: {final_response.content}")
                success = True
            except Exception as e:
                attempt += 1
                if attempt <= max_retries:
                    print(f"\n[Thông báo]: Đang gặp sự cố (có thể là Rate Limit). Sẽ thử lại sau 15 giây... (Lần thử {attempt}/{max_retries})")
                    time.sleep(15)
                else:
                    print(f"\n[Lỗi nghiêm trọng]: Không thể kết nối sau {max_retries + 1} lần thử. Chi tiết: {str(e)}")
