# 让用户注册
import time
import random

name = input('请填写用户名：')
age = input("{}您好，请输入您的年龄 : ".format(name))
user_info = {'name': name, 'age': int(age)}  # 用户信息
user_properties = ['X 1-5']  # 用于存放用户道具 默认道具
properties = ['X3 (250G)', 'X1-5 (300G)']
# 根据用户年龄 给与不同的初始金币
if 10 < user_info['age'] < 18:
    glod = 1000
elif 18 <= user_info['age'] <= 30:
    glod = 1500
else:
    glod = 500
user_info['glod'] = glod

# 输出相关提示信息
print("{}您好，欢迎游玩本游戏，您的初始金币为：{}".format(user_info['name'], user_info['glod']))
print("\n")
time.sleep(1)
print('游戏说明'.center(50, '*'))
print('*'.ljust(53), '*')
print('*', end='')
print("电脑每次投掷三枚骰子，总点数>=10为大，否则为小".center(32), end='')
print('*')
print('*'.ljust(53), '*')
print('*' * 54)
print("\n")

#             开始游戏
result = input('是否开始游戏 yes or no :  ')
go = True
if (result.lower() == 'yes'):
    pass
    while go:
        dices = []
        # 开始投掷
        for i in range(0, 3):
            dices.append(random.randint(1, 6))
        total = sum(dices)  # 计算总和
        user_input = input('请输入big OR small : ')  # 等待用户输入
        u_input = user_input.strip().lower()
        time.sleep(1)
        # 判断用户输入
        print('骰子点数为：{}'.format(dices),end=' ')
        if (total >= 10 and u_input == 'big') or (total < 10 and u_input == 'small'):
            print('您赢了!!!')
            if len(user_properties) > 0:  # 如果用户有道具 选择是否使用道具
                use_pro = input('是否使用道具： ')
                if use_pro.lower() == 'yes':
                    use_pro = int(input('请选择使用第几个道具{} ：'.format(user_properties)))
                    use_pro -= 1
                    # 判断道具类型
                    if user_properties[use_pro] == 'X 3':
                        user_info['glod'] += 100 * 3;
                        print('奖金翻3倍')
                    elif user_properties[use_pro] == 'X 1-5':
                        suiji = random.randint(1, 5)
                        print('奖金翻{}倍'.format(suiji))
                        user_info['glod'] += 100 * 5;

                    user_properties.remove(user_properties[use_pro])  # 删除道具
                else:
                    user_info['glod'] += 100;  # 不使用道具 用户金币加 100
            else:
                user_info['glod'] += 100;  # 正确 用户金币加 100
        else:
            print('您输了!')
            user_info['glod'] -= 100;  # 错误 用户金币减 100

        # 判断用户金币 是否够下次玩 不够则退出程序
        if (user_info['glod'] <= 0):
            print('您的金币已经用完，感谢您的游玩')
            break

        if user_info['glod'] % 1000 == 0:  # 用户金币 是1000的倍数是 可购买道具
            shop = input('您现在有金币:{}，是否购买道具 yes or no: '.format(user_info['glod']))
            if shop.lower() == 'yes':
                good_num = int(input('请选择要购买第几个道具 {}'.format(properties)))
                if good_num == 1:
                    user_properties.append('X 3')  # 给用户添加道具
                    user_info['glod'] -= 250
                    print('购买成功！消耗金币250')
                elif good_num == 2:
                    user_properties.append('X 1-5')  # 给用户添加道具
                    user_info['glod'] -= 300  # 用户金币减 300
                    print('购买成功！消耗金币300')
                else:
                    print('没有该道具，您失去了这次机会')
        else:
            #  一直提示 太烦
            # conti = input('您现在有金币:{}，是否继续游玩,yes or no: '.format(user_info['glod']))
            # if conti.lower() == 'no':
            #     print('您的金币已经用完，感谢您的游玩')
            #     break
            print('您现在有金币:{} '.format(user_info['glod']))

else:
    print('欢迎下次游玩，再见！')
