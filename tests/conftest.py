testing_urls = [
    ('http://example.ru',
     'http://example.ru/'),
    ('https://привет.рф',
     'https://xn--b1agh1afp.xn--p1ai/'),
    ('https://ya.ru/привет',
     'https://ya.ru/%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82'),
    ('https://aa.tu/a?так&то=вот#а',
     'https://aa.tu/a?%D1%82%D0%B0%D0%BA&%D1%82%D0%BE'
     '=%D0%B2%D0%BE%D1%82#%D0%B0'),
    ('https://a:b@aa.tu:80/a?так&то=вот#а',
     'https://a:b@aa.tu:80/a?%D1%82%D0%B0%D0%BA&%D1%82%D0%BE'
     '=%D0%B2%D0%BE%D1%82#%D0%B0')
]

urls_with_error = [
    '*https://aa.bb/rrr?rr=ss#ww',
    'https://////aa.bb/rrr?rr=ss#ww'
]
