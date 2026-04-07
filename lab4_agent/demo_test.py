import os
import time
from agent import graph
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

def demo():
    print("--- BẮT ĐẦU TEST TRAVELBUDDY AGENT ---")
    
    steps = [
        "Chào bạn, mình đang ở Hà Nội và muốn đi du lịch Đà Nẵng.",
        "Mình đi 2 đêm, tổng ngân sách cho cả vé máy bay và khách sạn là 4 triệu. Hãy tìm giúp mình phương án rẻ nhất.",
        "Cảm ơn bạn. À, tiện thể giải giúp mình bài tập hóa học lớp 12 này với."
    ]
    
    thread_id = "demo_thread_1" # In a real app we'd use a session/thread ID
    # Note: LangGraph StateGraph handles history if we pass it back. 
    # For this simple demo, we'll keep track of the messages list.
    
    messages = []
    
    for i, user_input in enumerate(steps, 1):
        print(f"\n[Bước {i}] Bạn: {user_input}")
        
        # Add delay between steps to avoid rate limit
        if i > 1:
            print("(Đang chờ 60 giây để tránh rate limit của OpenRouter...)")
            time.sleep(60)
            
        try:
            messages.append(HumanMessage(content=user_input))
            result = graph.invoke({"messages": messages})
            
            # The result contains the whole message history
            final_response = result["messages"][-1]
            messages = result["messages"] # Update message history for next turn
            
            print(f"\nTravelBuddy: {final_response.content}")
            
        except Exception as e:
            print(f"\n[Lỗi]: {str(e)}")

if __name__ == "__main__":
    demo()
