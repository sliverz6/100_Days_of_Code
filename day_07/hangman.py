# hangman.py

import random
from hangman_art import logo, stages
from hangman_words import word_list

# 목숨
lives = 6

# 단어를 뽑는다.
chosen_word = random.choice(word_list)

# 빈칸을 만든다.
word_length = len(chosen_word)
display = []
for _ in range(word_length):
    display.append("_")

# 로고를 출력한다.
print(logo)

# 반복
game_is_running = True
while game_is_running:
    # 글자를 물어본다.
    guess = input("\n알파벳을 맞추세요: ").lower()

    # 이미 예측한 알파벳을 입력하면 알려준다.
    if guess in display:
        print(f"\n{guess} 은/는 이미 예측한 알파벳입니다. 다른 알파벳을 입력해보세요.")

    # 단어에 예측한 알파벳이 있다면 빈칸을 채운다.
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # 빈칸이 모두 채워졌다면 게임을 종료한다.
    if "_" not in display:
        game_is_running = False
        print(f"\n단어를 맞췄습니다! 정답은 {chosen_word} 입니다.")

    # 단어에 예측한 알파벳이 없다면 목숨을 1 줄인다.
    if guess not in chosen_word:
        print(f"\n{guess} 은/는 단어에 없습니다. 목숨을 잃었습니다.")
        lives -= 1

    # 목숨을 모두 잃으면 게임을 종료한다.
    if lives == 0:
        game_is_running = False
        print(f"\n당신은 졌습니다. 정답은 {chosen_word} 입니다.")

    # 빈칸을 출력한다.
    print(" ".join(display))

    # 교수대 그림을 출력한다.
    print(stages[lives])
