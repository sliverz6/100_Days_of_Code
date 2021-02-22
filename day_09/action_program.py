# action_program.py

from art import logo

# 로고 출력
print(logo)

# 인사말 출력
print("암묵적 경매 프로그램에 오신 것을 환영합니다!")

# 입찰자 딕셔너리
bidders = {}

# 반복해서 입력 받기
running = True
while running:
    # 사용자 입력
    name = input("이름이 뭔가요?: ").lower()
    bid = int(input("입찰 금액을 입력하세요: $"))

    # 딕셔너리에 저장
    bidders[name] = bid

    # 종료 여부 묻기
    choice = input("다른 입찰자가 있나요? 있으면 'yes', 없으면 'no'를 입력하세요. ")
    if choice == "no":
        running = False

# 낙찰자 판단
winner = ""
winners_bid = 0
for bidder in bidders:
    if bidders[bidder] > winners_bid:
        winner = bidder
        winners_bid = bidders[bidder]

print(f"낙찰자는 ${winners_bid}에 입찰한 {winner.title()}입니다.")
