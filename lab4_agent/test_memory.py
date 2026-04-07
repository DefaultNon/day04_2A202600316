import time
from agent import graph
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

def invoke_with_retry(input_messages, config):
    max_retries = 2
    for i in range(max_retries + 1):
        try:
            return graph.invoke({"messages": input_messages}, config=config)
        except Exception as e:
            if i < max_retries:
                print(f"Lỗi: {e}. Thử lại sau 20s...")
                time.sleep(20)
            else:
                raise e

def test_memory():
    print("--- TESTING PERSISTENT MEMORY ---")
    config = {"configurable": {"thread_id": "test_user_001"}}
    
    # Lần 1: Giới thiệu bản thân
    print("\n[Lần 1] Bạn: Chào nhé, mình tên là Giang. Mình rất thích leo núi.")
    result1 = invoke_with_retry([HumanMessage(content="Chào nhé, mình tên là Giang. Mình rất thích leo núi.")], config=config)
    print(f"TravelBuddy: {result1['messages'][-1].content}")
    
    # Chờ 30s giữa các lần test
    print("\n(Đang chờ 30 giây để gọi lượt tiếp theo...)")
    time.sleep(30)
    
    # Lần 2: Hỏi lại xem Agent có nhớ không
    print("\n[Lần 2] Bạn: Bạn nhớ tên mình không? Và mình thích làm gì nhất nhỉ?")
    result2 = invoke_with_retry([HumanMessage(content="Bạn nhớ tên mình không? Và mình thích làm gì nhất nhỉ?")], config=config)
    print(f"\nTravelBuddy: {result2['messages'][-1].content}")

if __name__ == "__main__":
    test_memory()
