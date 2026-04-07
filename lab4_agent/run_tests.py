import os
import time
from agent import graph
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

test_cases = [
    "Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.",
    "Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng",
    "Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!",
    "Tôi muốn đặt khách sạn",
    "Giải giúp tôi bài tập lập trình Python về linked list"
]

def run_tests():
    with open("test_results.md", "w", encoding="utf-8") as f:
        f.write("# BÁO CÁO KẾT QUẢ TEST - LAB 4\n\n")
        
        for i, text in enumerate(test_cases, 1):
            print(f"Running Test {i} ({text})...")
            if i > 1:
                print("Waiting 60 seconds to avoid rate limiting...")
                time.sleep(60)
            
            f.write(f"## Test {i}: {text}\n")
            f.write("### Diễn giải:\n")
            
            # Reset state for each test if needed, but here we just send a single message per test 
            # as per the lab requirements for individual test scenarios.
            try:
                config = {"configurable": {"thread_id": f"test_{i}"}}
                result = graph.invoke({"messages": [HumanMessage(content=text)]}, config=config)
                
                # Capture tool calls from the state
                messages = result["messages"]
                
                f.write("#### Các bước xử lý:\n")
                for msg in messages:
                    if hasattr(msg, 'tool_calls') and msg.tool_calls:
                        for tc in msg.tool_calls:
                            f.write(f"- Gọi tool: `{tc['name']}({tc['args']})`\n")
                    if msg.type == "tool":
                        f.write(f"- Kết quả tool `{msg.name}`: {msg.content[:200]}...\n")
                
                final_response = messages[-1].content
                f.write(f"#### Phản hồi cuối cùng:\n")
                f.write(f"> {final_response}\n\n")
                f.write("---\n\n")
                
            except Exception as e:
                f.write(f"#### Lỗi:\n")
                f.write(f"> {str(e)}\n\n")
                f.write("---\n\n")

if __name__ == "__main__":
    run_tests()
    print("Tests completed. Results saved to test_results.md")
