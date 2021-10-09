from google_play_scraper import Sort, review
import os

result = review(
            'com.gamma.scan',
            sleep_milliseconds=0,  # defaults to 0
            lang='en',  # defaults to 'en'
            country='pk',  # defaults to 'us'
            sort=Sort.RATING,  # defaults to Sort.MOST_RELEVANT
            filter_score_with=4,  # defaults to None(means all score)
            count = 10
        )

count = 0
for info in result:
    count += 1
    print(info)
print(count)               
