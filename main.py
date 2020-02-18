import numpy as np
count = 0                          
number = np.random.randint(1,100)   
def score_game(game):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 100, size=(1000))
    for number in random_array:
        count_ls.append(game(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
    def game333(number):
        count = 0
        predict = np.random.randint(1,100)
        max_value = 100
        min_value = 1
        while number != predict:
            count+=1
            if predict > number: 
                max_value = predict
            else: 
                min_value = predict
            predict = min_value + int((max_value - min_value)/2)
            print(count, predict)
    return(count) 
score_game(game333)
