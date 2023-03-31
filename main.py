import json
import tkinter as tk

def search_question():
    keyword = keyword_entry.get()
    result_text.delete("1.0", "end")
    with open("questions.json", "r", encoding="utf-8-sig") as f:
        for line in f:
            data = json.loads(line)
            if keyword in data["keywords"]:
                result_text.insert("end", f"题目: {data['question']}\n")
                result_text.insert("end", f"答案: {data['answer']}\n")
#                result_text.insert("end", f"关键字: {' '.join(data['keywords'])}\n\n")

# 创建窗口
window = tk.Tk()
window.title("不务正业系列-阿里云题库程序")

# 创建查询控件
keyword_label = tk.Label(window, text="请输入关键字：")
keyword_label.pack()
keyword_entry = tk.Entry(window)
keyword_entry.pack()

search_button = tk.Button(window, text="查询", command=search_question)
search_button.pack()

# 创建结果显示控件
result_label = tk.Label(window, text="查询结果：")
result_label.pack()
result_text = tk.Text(window)
result_text.pack()

window.mainloop()
