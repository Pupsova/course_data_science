"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    smallest_num = 1
    largest_num = 101
    
    while True:
        count += 1
        predict_number = (smallest_num + largest_num) // 2  # предполагаемое число
        
        if number == predict_number:
            break  # выход из цикла если угадали
        
        if number > predict_number:
            smallest_num = predict_number
        
        else:
            largest_num = predict_number
            
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток максимально за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: максимальное количество попыток
    """
    
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(max(count_ls))
    print(f"Ваш алгоритм угадывает число максимум за {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)