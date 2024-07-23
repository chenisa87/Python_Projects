import random

words = [
    {"English": "the", "Chinese": "這"},
    {"English": "be", "Chinese": "是"},
    {"English": "to", "Chinese": "到"},
    {"English": "of", "Chinese": "的"},
    {"English": "and", "Chinese": "和"},
    {"English": "a", "Chinese": "一個"},
    {"English": "in", "Chinese": "在"},
    {"English": "that", "Chinese": "那"},
    {"English": "have", "Chinese": "有"},
    {"English": "I", "Chinese": "我"},
    {"English": "it", "Chinese": "它"},
    {"English": "for", "Chinese": "為了"},
    {"English": "not", "Chinese": "不"},
    {"English": "on", "Chinese": "在...上"},
    {"English": "with", "Chinese": "與"},
    {"English": "he", "Chinese": "他"},
    {"English": "as", "Chinese": "如同"},
    {"English": "you", "Chinese": "你"},
    {"English": "do", "Chinese": "做"},
    {"English": "at", "Chinese": "在"},
    {"English": "this", "Chinese": "這個"},
    {"English": "but", "Chinese": "但是"},
    {"English": "his", "Chinese": "他的"},
    {"English": "by", "Chinese": "通過"},
    {"English": "from", "Chinese": "從"},
    {"English": "they", "Chinese": "他們"},
    {"English": "we", "Chinese": "我們"},
    {"English": "say", "Chinese": "說"},
    {"English": "her", "Chinese": "她的"},
    {"English": "she", "Chinese": "她"},
    {"English": "or", "Chinese": "或者"},
    {"English": "an", "Chinese": "一個"},
    {"English": "will", "Chinese": "將"},
    {"English": "my", "Chinese": "我的"},
    {"English": "one", "Chinese": "一"},
    {"English": "all", "Chinese": "全部"},
    {"English": "would", "Chinese": "會"},
    {"English": "there", "Chinese": "那裡"},
    {"English": "their", "Chinese": "他們的"},
    {"English": "what", "Chinese": "什麼"},
    {"English": "so", "Chinese": "所以"},
    {"English": "up", "Chinese": "向上"},
    {"English": "out", "Chinese": "出"},
    {"English": "if", "Chinese": "如果"},
    {"English": "about", "Chinese": "關於"},
    {"English": "who", "Chinese": "誰"},
    {"English": "get", "Chinese": "得到"},
    {"English": "which", "Chinese": "哪個"},
    {"English": "go", "Chinese": "去"},
    {"English": "me", "Chinese": "我"},
    {"English": "when", "Chinese": "何時"},
    {"English": "make", "Chinese": "製造"},
    {"English": "can", "Chinese": "能"},
    {"English": "like", "Chinese": "喜歡"},
    {"English": "time", "Chinese": "時間"},
    {"English": "no", "Chinese": "不"},
    {"English": "just", "Chinese": "剛剛"},
    {"English": "him", "Chinese": "他"},
    {"English": "know", "Chinese": "知道"},
    {"English": "take", "Chinese": "拿"},
    {"English": "people", "Chinese": "人"},
    {"English": "into", "Chinese": "進入"},
    {"English": "year", "Chinese": "年"},
]

def quiz_user(words):
    # 隨機排列
    random.shuffle(words)
    score = 0


    for word in words:
        print(f"What is the Chinese translation of '{word['English']}'?")
        user_answer = input("Your answer: ").strip()
        correct_answer = word['Chinese']

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['Chinese']}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")

def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
    main()