# Находим в реестре Corus ссылку на Lenta.ru, загружаем:
# wget https://github.com/yutkin/Lenta.Ru-News-Dataset/...

from corus import load_lenta

path = 'lenta-ru-news.csv.gz'
records = load_lenta(path)  # 2ГБ, 750 000 статей
next(records)

LentaRecord(
    url='https://lenta.ru/news/2018/12/14/cancer/',
    title='Названы регионы России с\xa0самой высокой ...',
    text='Вице-премьер по социальным вопросам Татьяна ...',
    topic='Россия',
    tags='Общество'
)