import random
import winsound  # Windowsで音を鳴らすための道具

# 1. ファイルから単語を読み込む
words = {}
with open("wordlist.txt", "r", encoding="utf-8") as f:
    for line in f:
        english, japanese = line.strip().split(",")
        words[english] = japanese
def load_data():
    words = {}
    try:
        with open("wordlist.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if "," in line: # カンマがある行だけ処理する
                    parts = line.split(",")
                    if len(parts) == 2:
                        english, japanese = parts
                        words[english.strip()] = japanese.strip()
    except Exception as e:
        st.error(f"データの読み込みでエラーが発生しました: {e}")
    return words
for english, japanese in word_list:
    # --- 3択の選択肢を作る ---
    # 他の単語の意味をランダムに2つ選んで、正解と混ぜる
    other_meanings = [v for k, v in words.items() if v != japanese]
    choices = random.sample(other_meanings, 2) + [japanese]
    random.shuffle(choices) # 選択肢の順番をバラバラにする

    print(f"\n問題: {english}")
    for i, choice in enumerate(choices):
        print(f"  {i+1}: {choice}")

    # ユーザーの入力を受け取る
    try:
        user_choice = int(input("番号を選んでください (1-3): "))
        selected_meaning = choices[user_choice - 1]
    except:
        print("数字を入力してください。")
        continue

   # --- 判定と派手な音（ファイル再生バージョン） ---
    if selected_meaning == japanese:
        print("正解！ ✨")
        # SND_FILENAME は「ファイル名で再生する」という意味
        # SND_ASYNC は「音を鳴らしながら次の処理（文字表示など）を進める」という意味
        winsound.PlaySound("seikai.wav", winsound.SND_FILENAME | winsound.SND_ASYNC) 
        score += 1
    else:
        print(f"残念... 正解は【 {japanese} 】でした。")
        winsound.PlaySound("huseikai.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        review_list.append(f"{english},{japanese}")

print(f"\n終了！結果: {len(word_list)}問中 {score}問正解")