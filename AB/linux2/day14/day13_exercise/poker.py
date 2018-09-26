# 2. 模拟斗地主发牌，扑克牌共54张:
#   花色:
#     黑桃('\u2660'), 梅花('\u2663'), 方块('\u2665'), 红桃('\u2666')
#   数值:
#     A2-10JQK
#   大小王
#   三个人，每人发17张牌，底牌留三张:
#     输入回车,打印第1个人的17张牌
#     输入回车,打印第2个人的17张牌
#     输入回车,打印第3个人的17张牌
#     再输入回车，打印出三张底牌

import random

def get_new_poker():
    kinds = ['\u2660', '\u2663', '\u2665', '\u2666']

    numbers = ['A']
    numbers += [str(x) for x in range(2, 11)]
    numbers += ['J', 'Q', 'K']
    # 以下生成52张牌
    L = [k + n for k in kinds for n in numbers]
    L += ['大王', '小王']
    return L


def play():
    poker = get_new_poker()
    random.shuffle(poker)
    input("按任意键发第一个人的牌：")
    print("第一个人的牌是:", poker[:17])
    input("按任意键发第二个人的牌：")
    print("第二个人的牌是:", poker[17:34])
    input("按任意键发第三个人的牌：")
    print("第三个人的牌是:", poker[34:51])
    input("按任意键看底牌：")
    print("底牌是:", poker[51:])
    

play()


