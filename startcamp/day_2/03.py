movie = { # movie dictionary
    'movieInfo': { # movie 의 키는 movieInfo 1개
        'movieNm': '광해, 왕이 된 남자',  # movieInfo의 value 는 Dictionary
        'movieNmEn': 'Masquerade',
        'showTm': '131',
        'prdtYear': '2012',
        'openDt': '20120913',
        'typeNm': '장편',
        'nations': [
            {
            'nationNm': '한국' # value가 List
            }
        ],
        'genres': [
            {
            'genreNm': '사극'
            },
            {
            'genreNm': '드라마'
            }
        ],
        'directors': [ # directors 에는 길이가 1인 Dictionary가 들어있는데, 그 Dictionary 안에는 길이 2짜리가 들어있다
            {
            'peopleNm': '추창민',
            'peopleNmEn': 'CHOO Chang-min'
            }
        ],
        'actors': [ # actors 키에 value가 길이가 3인 list
            {
            'peopleNm': '이병헌',
            'peopleNmEn': 'LEE Byung-hun',
            'cast': '광해/하선'
            },
            {
            'peopleNm': '류승룡',
            'peopleNmEn': 'RYU Seung-ryong',
            'cast': '허균'
            },
            {
            'peopleNm': '한효주',
            'peopleNmEn': 'HAN Hyo-joo',
            'cast': '중전'
            }
        ]
    }
}

# 1. 영화의 제목을 출력하시오.
print(movie['movieInfo']['movieNm'])

# 2. 다음 movie의 감독의 영어 이름을 출력하시오. <-중요!
print(movie['movieInfo']['directors']) # 출력하면 값이 1개인 list가 나온다
print(movie['movieInfo']['directors'][0]['peopleNmEn']) # 윗줄에서 나온 list의 0번 인덱스를 불러와서 'peopleNmEn' 가져옴 
print(len(movie['movieInfo']['directors']))
# 3. 다음 movie의 배우의 인원을 출력하시오.
print(len(movie['movieInfo']['actors']))