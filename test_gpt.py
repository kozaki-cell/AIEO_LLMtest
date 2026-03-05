import os
from datetime import datetime
from openai import OpenAI

# OpenAI クライアント初期化
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# テスト質問
questions = [
    "AIEOに対する対策は何ですか？",
    "生成AIコンテンツの特徴は？",
    "複数LLMの回答をどう評価しますか？"
]

# 結果を保存するディレクトリを作成
os.makedirs("results", exist_ok=True)

# 結果をテキストファイルに保存
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
results_file = f"results/gpt_results_{datetime.now().strftime('%Y%m%d')}.txt"

with open(results_file, "w", encoding="utf-8") as f:
    f.write(f"GPT API Test Results\n")
    f.write(f"Generated: {timestamp}\n")
    f.write("=" * 50 + "\n\n")
    
    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question}")
        f.write(f"【Question {i}】\n")
        f.write(f"{question}\n\n")
        
        # GPT APIを呼び出し
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        answer = response.choices[0].message.content
        print(f"Answer: {answer[:100]}...\n")
        
        f.write(f"【Answer】\n")
        f.write(f"{answer}\n")
        f.write("-" * 50 + "\n\n")

print(f"Results saved to {results_file}")
