import os
import time
from agent import graph
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

test_cases = {
    4: "Tôi muốn đặt khách sạn",
    5: "Giải giúp tôi bài tập lập trình Python về linked list"
}

def retry_tests():
    results = {}
    for i in [4, 5]:
        text = test_cases[i]
        print(f"Retrying Test {i}: {text}...")
        
        # Wait to avoid rate limit
        if i == 5:
            print("Waiting 65 seconds before Test 5...")
            time.sleep(65)
            
        try:
            config = {"configurable": {"thread_id": "retry_test"}}
            result = graph.invoke({"messages": [HumanMessage(content=text)]}, config=config)
            final_response = result["messages"][-1].content
            results[i] = final_response
            print(f"Test {i} Success!")
        except Exception as e:
            results[i] = f"Error: {str(e)}"
            print(f"Test {i} Failed: {e}")
            
    return results

if __name__ == "__main__":
    results = retry_tests()
    
    # Simple output to a temp file so Antigravity can read it
    with open("retry_temp.txt", "w", encoding="utf-8") as f:
        for i, res in results.items():
            f.write(f"--- TEST {i} ---\n{res}\n")
