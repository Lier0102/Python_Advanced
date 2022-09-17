class Calculator:
    def __init__(self): # 생성자
        self.value = 0

    def add(self, val): # 덧셈 함수
        self.value += val # 현재 value에 val만큼 더함

class UpgradeCalculator(Calculator): # 추가적인 기능을 더한 계산기
    def minus(self, val): # 상속을 받으며, minus 함수까지 추가.
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

# DISCORD : Abypass#1663
# I'm upgrading