# Проект Андан

Всем привет! Добро пожаловать в наш проект по анализу данных. 

Мы долго думали, какую тему выбрать, и сошлись на анализе рынка автомобилей. В рамках проекта мы выясним, как различные показатели влияют на цену автомобиля. Кроме того, мы постараемся проверить несколько любопытных гипотез. Надеемся, что в проекте нам удастся построить достаточно хорошую модель, а вы сможете найти интересные наблюдения и качественный анализ.

Приятного просмотра,
команда 'Закусь'


А теперь поговорим немного о модели и предварительных гипотезах: 

Модель машинного обучения - регрессия. Мы выбрали именно ее, так как собираемся предсказывать цену автомобиля по различным ее признакам. Эту модель можно улучшать разными способами: при помощи подбора гиперпараметров, использования регуляризации и применения множества дополнительных инструментов. 

Задачи по машинному обучению:

1) Обработка выбросов
2) Нормализация количественнх признаков
3) Энкодинг категориальных переменных 
4) Выбор и оптимизация модели 
5) Оценка модели и интерпретация результатов


Также по дороге мы собираемся проверить некоторые любопытные гипотезы. Вот их предварительный список. 

Гипотезы: 

1) Средняя мощность автомобилей, выпущенных в теченение последних 5 лет выше, чем средняя мощность более старых автомобилей (гипотеза о равенстве мат. ожиданий)
Можно проверить с помощью z-статистики, поскольку наблюдений достаточно много и среднее асим. нормально. 

2) Доля машин, оборудованной МКПП, ниже среди машин, выпущенных в течение последних 5 лет, чем среди более старых. (гипотеза о равенстве мат. ожидания)
Можно проверить с помощью z-статистики, поскольку наблюдений достаточно много и доля асим. нормально. 

А вот и долгожданное продолжение!

В первую очередь хотелось бы отметить, что мы проделали невероятно интересную и прикладную работу, которая показала, насколько работа с данными может быть полезной в реальной жизни. К тому же, у нас получились очень качественные результаты, с которыми можно делать более сложные вещи и развивать данную тему в будущем. Но сейчас хотелось бы поговорить о проделанной работе! 

После обработки и анализа данных, добавления новых признаков и удаления выбросов мы обучили несколько [моделей](model/ML.ipynb) для предсказания цены автомобиля. Мы добились высокого качества на тестовой выборке при помощи линейной регрессии с регуляризацией после подбора оптимальных параметров и градиентного бустинга. Обе модели показали себя очень хорошо и выдали высокое качество.
 
