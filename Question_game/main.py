import json

# 讀取 JSON 文件
with open("Question_game\questions.json","r") as file:
    questions = json.load(file)



def run(questions):
    score = 0
    for qs in questions:
        print(qs["prompt"])
        for option in qs["options"]:
            print(option)
        answer = input("Enter Your Answer:  ")
        if answer == qs["answer"]:
            print("Correct\n")
            score+=1
        else:
            print("Wrong, the answer is",qs["answer"])
    print(score)        


run(questions)