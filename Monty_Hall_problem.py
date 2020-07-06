import random
import matplotlib.pyplot as plt
from celluloid import Camera

BIG_NUM = 1000000

def init_behind_of_door():
    # 0은 염소 1은 자동차
    # behind_of_door은 [0, 1, 0]과 같은 형식으로 될 것임
    behind_of_door = [0, 0, 0]
    car = random.randrange(3)
    behind_of_door[car] = 1
    return behind_of_door

def except_one_of_goat(behind_of_door, choice_of_participant):
    # 선택된 곳과 염소인 곳 표시
    # behind_of_door은 ['choice', 'goat', 1]과 같은 형식으로 될 것임
    for i in range(3):
        if choice_of_participant == i:
            behind_of_door[i] = 'choice'
        elif behind_of_door[i] == 0:
            behind_of_door[i] = 'goat'
            break

def change_selection(behind_of_door):
    # behind_of_door[i]가 정수형인 경우 반환
    for i in range(3):
        if type(behind_of_door[i]) == int:
            return behind_of_door[i]

def makeAnimation(total_car, i, fig, camera):
    y = [total_car / (i + 1), 1 - (total_car / (i + 1))]
    x = [0, 1]
    percen = total_car / (i + 1)
    bar = plt.bar(x, y, color='b')
    plt.xticks(x, ['car', 'goat'])
    plt.legend(bar, [f'step : {i+1}\ncar percentage {percen:.2f}'])
    
    camera.snap()

if __name__ == '__main__':
    fig = plt.figure()
    camera = Camera(fig)

    total_car = 0

    for i in range(BIG_NUM):
        behind_of_door = init_behind_of_door()
        choice_of_participant = random.randrange(3)
        except_one_of_goat(behind_of_door, choice_of_participant)
        final_choice = change_selection(behind_of_door)
        
        total_car += final_choice

        #makeAnimation(total_car, i, fig, camera)

    #animation = camera.animate(interval=5)

    #plt.show()

    print(total_car / BIG_NUM)
