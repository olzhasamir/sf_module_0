{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "count = 0                            # счетчик попыток\n",
    "number = np.random.randint(1,100)   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [],
   "source": [
    "def score_game(game):\n",
    "    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''\n",
    "    count_ls = []\n",
    "    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!\n",
    "    random_array = np.random.randint(1, 100, size=(1000))\n",
    "    for number in random_array:\n",
    "        count_ls.append(game(number))\n",
    "    score = int(np.mean(count_ls))\n",
    "    print(f\"Ваш алгоритм угадывает число в среднем за {score} попыток\")\n",
    "    return(score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [],
   "source": [
    "def game333(number):\n",
    "    count = 0\n",
    "    predict = np.random.randint(1,100)\n",
    "    max_value = 100\n",
    "    min_value = 1\n",
    "    while number != predict:\n",
    "        count+=1\n",
    "        if predict > number: \n",
    "            max_value = predict\n",
    "        else: \n",
    "            min_value = predict\n",
    "        predict = min_value + int((max_value - min_value)/2)\n",
    "    return(count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ваш алгоритм угадывает число в среднем за 5 попыток\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "score_game(game333)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
