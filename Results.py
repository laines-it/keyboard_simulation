import pygame
import time, sys

class Results():
    def __init__(self):
        self.time_start = 0 # фиксация времени начала
        self.total_time = 0 # всё время
        self.accuracy = '0%' # процент грамотности
        self.results = 'Time:0 Accuracy:0 % Wpm:0 ' # результаты
        self.wpm = 0 # слов в минуту
        self.all_words = '' # все слова в строку
        self.word_count = 0 # кол-во слов
        self.awl = 0.0 # средняя длина слова

    def show_results(self, screen): # демонстрация результатов
        if(not self.end): 
            #Время
            self.total_time = time.time() - self.time_start # время написания = всё время - время начала
               
            #Аккуратность
            count = 0 # счётчик правильных слов
            for i,c in enumerate(self.word): # перебор всех символов в предложении
                try:
                    if self.input_text[i] == c: # если соответствует тому же символу из исходного текста
                        count += 1 # прибавить единицу к счётчику
                except:
                    pass
            self.accuracy = count/len(self.word)*100

            #Средняя длина слова
            self.awl = len(self.all_words)/self.word_count

            #Кол-во слов в минуту
            self.wpm = len(self.input_text)*60/(5*self.total_time)
            self.end = True  # завершить проход цикла if
            print(self.total_time) # написать всё время
                
            self.results = 'Time:'+str(round(self.total_time)) +' secs\nAccuracy:'+ str(round(self.accuracy)) + '%\nWpm: ' + str(round(self.wpm)) + '\nAwl: ' + str(round(self.awl))
            print(self.results)
             # отформатировать и написать результаты

            self.screen_results = pygame.display.set_mode((300, 300))
            self.screen_results.fill()
            pygame.font.init()
            f1 = pygame.font.Font(None, 36)
            text1 = f1.render(self.results, True, (180, 0, 0))
 
            self.screen_results.blit(text1, (10, 50))
            pygame.display.update()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

# внутри цикла
pygame.time.Clock()
self.time_start = time.time() # запустить отсчёт времени

# при выведении нового слова
self.all_words += '' # добавить слово в строку
self.word_count += 1 # добавить один к счётчику слов

# при нажатии кнопки (её следовало бы добавить)
self.show_results(self.screen) # вычислить результаты
