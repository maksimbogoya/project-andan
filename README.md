# Проект по андану, команда "Закусь"
### Выполнили: Богоявленский Максим, Микаелян Арман, Пахомов Иван

Добро пожаловать в наш проект по анализу данных. 

Мы долго думали, какую тему выбрать, и сошлись на анализе рынка автомобилей. В рамках проекта мы выясним, как различные показатели влияют на цену автомобиля. Кроме того, мы постараемся проверить несколько интересных гипотез. Надеемся, что в проекте нам удастся построить достаточно хорошую модель, а вы сможете найти интересные наблюдения и качественный анализ.

Приятного прочтения,
команда 'Закусь'


А теперь о сделанном (более подробное описание есть непосредственно в файлах): 

Был проведён [парсинг](parsing/parser.ipynb) объявлений с сайта авто.ру, откуда было получено 3701 наблюдений с 12 переменными (в ходе EDA и обработки выбросов осталось 2368, а переменных стало 14).

Перед обучением модели был проведён разведочный анализ данных ([EDA](EDA/EDA.ipynb)), включивший в себя следующие задачи:

1) Подготовка данных (удаление дубликатов, заполнение NA)
2) Визуализация распределений переменных, связей между ними
3) Создание новых, релевантных для задач машинного обучения, [переменных](modules/new_attributes.py)
4) Формулировка выводов о данных

Далее, непосредственно [ML](model/ML.ipynb).

Модель машинного обучения - регрессия. Мы выбрали именно её, так как предсказываем цену автомобиля по различным его признакам. Эту модель можно улучшать разными способами: при помощи подбора гиперпараметров, использования регуляризации и применения множества дополнительных инструментов и типов регрессий. 

Задачи по машинному обучению:

1) Обработка выбросов
2) Нормализация количественнх признаков
3) Энкодинг категориальных переменных 
4) Выбор и оптимизация моделей
5) Оценка моделей и интерпретация результатов

Также было проверено несколько любопытных гипотез:

1) Стоимость белых & черных машин выше, чем машин других цветов. $H_0 : \mu_{bnw} = \mu_{oth}\quad H_1 : \mu_{bnw} > \mu_{oth}$

2) Доля машин с МКПП ниже среди машин, выпущенных в последние 5 лет, чем среди более ранних. $H_0 : p_{new} = p_{old} \quad H_1 : \p_{new} < \p_{old}$

Проверив эти гипотезы с помощью разных тестов, мы пришли к выводу, что альтернативные гипотезы не отвергаются на любом разумном уровне значимости.

После обработки и анализа данных, добавления новых признаков и удаления выбросов мы обучили несколько моделей для предсказания цены автомобиля. Мы добились высокого качества на тестовой выборке при помощи линейной регрессии - с регуляризацией после подбора оптимальных параметров - и градиентного бустинга. 

Обе модели оказались эффективными и показали высокие значения необходимых метрик.

Также были сделаны выводы о направленности и размерах влияния отдельных перменных на стоимость автомобиля, даны логические и экономические объяснения.
 
Хотелось бы отметить, что мы проделали интересную и прикладную работу, которая показала, насколько анализ данных может быть полезен в жизни. 
К тому же, у нас получились достаточно качественные и релевантные результаты, с которыми в дальнейшем можно решать дополнительные аналитические задачи, развивая данный проект. 
