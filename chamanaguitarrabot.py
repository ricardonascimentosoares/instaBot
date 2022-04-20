from instapy import InstaPy
from getpass import getpass
import random


# users_followed = ["studiodjango"]
words_dont_like = ["naked", "nsfw"]


def read_hashtag_files():
    with open('hashtags.txt') as file:
        lines = [line.rstrip() for line in file]
        print(lines)
        return lines


if __name__ == '__main__':
    bot_username = input('Usuário:')
    bot_password = getpass('Senha:')

    session = InstaPy(username=bot_username, password=bot_password, want_check_browser=True, headless_browser=False)
    session.login()

    hashtags = read_hashtag_files()

    session.set_quota_supervisor(enabled=True, peak_likes_hourly=21, peak_comments_daily=240)
    session.set_relationship_bounds(enabled=True, max_followers=15000)
    session.set_user_interact(amount=random.randint(5, 10), randomize=True, percentage=50)
    session.set_dont_like(words_dont_like)
    session.set_do_like(True, percentage=50)
    session.set_do_follow(True, percentage=50)
    # session.set_do_comment(True, percentage=50)
    # session.set_comments(comments)

    session.like_by_tags(hashtags,
                         amount=random.randint(5, 10),
                         use_random_tags=True,
                         randomize=True,
                         interact=True,
                         media='Video')
    # session.follow_by_tags(hashtags.txt,
    #                        amount=random.randint(5, 10),
    #                        randomize=True,
    #                        skip_top_posts=True,
    #                        interact=True,
    #                        media='Video')
    # session.like_by_users(users_followed, amount=5, randomize=True)

    session.end()
