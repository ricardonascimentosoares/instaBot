from instapy import InstaPy
import random

bot_username = "chamanaguitarra"
bot_password = "overdrive"

hashtags = ['ozzyosbournecover', 'eletricguitar', 'rockmusic', 'metal', 'heavymetal', 'guitarcover', 'instamusic',
            'rocknroll', 'thrashmetal', 'heavymetal', 'guitarra', '80s', 'hardrock', 'glammetal', '70s',
            'audioslavecover', 'angracover', 'bonjovi', 'nirvanacover', 'aliceinchainscover', 'music', 'metallica',
            'blacksabbath', 'ironmaiden',
            'cortguitar', 'jacksonguitar', 'acdc', 'ibanezguitar', 'acdccover', 'whitesnakescover', 'europecover']
# users_followed = ["studiodjango"]
words_dont_like = ["naked", "nsfw"]
comments = ["Curti!", "Top!!", "Muito bom!!", "Show de bola hein!", "Show!"
                                                                    "Massa demais! Depois dá uma olhada no @chamanaguitarra! Valeu! #tmj"]

if __name__ == '__main__':
    session = InstaPy(username=bot_username, password=bot_password, want_check_browser=True)
    session.login()

    session.set_relationship_bounds(enabled=True, max_followers=15000)
    session.set_user_interact(amount=random.randint(5, 10), randomize=True, percentage=50)
    session.set_dont_like(words_dont_like)
    session.set_do_like(True, percentage=50)
    session.set_do_follow(True, percentage=50)
    session.set_do_comment(True, percentage=50)
    session.set_comments(comments)
    session.set_quota_supervisor(enabled=True, peak_likes_hourly=21, peak_comments_daily=240, peak_comments_hourly=21)

    # session.like_by_tags(hashtags,
    #                      amount=random.randint(5, 10),
    #                      use_random_tags=True,
    #                      randomize=True,
    #                      interact=True,
    #                      use_smart_location_hashtags=True,
    #                      media='Video')
    session.follow_by_tags(hashtags,
                           amount=random.randint(5, 10),
                           randomize=True,
                           interact=True,
                           media='Video')
    # session.like_by_users(users_followed, amount=5, randomize=True)

    session.end()
