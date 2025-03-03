# Problem: A - Language Identifier - https://codeforces.com/gym/591928/problem/A

t= int(input())

for _ in range(t):
    lang = input()
    
    if "po" == lang[-2:]:
        print("FILIPINO")
    elif "desu" == lang[-4:] or "masu" == lang[-4:]:
        print("JAPANESE")
    elif "mnida" == lang[-5:]:
        print("KOREAN")