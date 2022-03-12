from instapy import InstaPy
import random

bot_username = "consultoriows"
bot_password = "protese87"

hashtags = ["maquiagem", "makeup", "blogueira", "smile", "alegria", "bomdia", "boasemana", "beleza", "estetica",
            "felicidade", "happy", "campograndems", "wedding", "noiva", "casamento", "hair", "aesthetics", "dedication",
            "closeup", "lovely"]
# users_followed = ["studiodjango"]
words_dont_like = ["naked", "nsfw", "dentista"]
comments = []
locations = ['213513773/move-club',
             '14442985/la-riviera-buffet',
             '104583669592181/estudio-make',
             '750043467/ymakay',
             '774602512896962/moda-lab',
             '1588477711382778/unhas-belas-cg',
             '937511456351214/dra-karina-souza',
             '1041364909312204/mk-pilates-nosso-cantinho',
             '632030520647335/studio-bia-e-elza-machado',
             '342622589139604/nutricionista-jessica-alves-ferreira',
             '1024334354/dr-marcio-belini',
             '1021497155/princess-hair',
             '94988772/atelie-marcio-rocha',
             '2015475105449021/yara-modas-feminina-av-mato-grosso-1110',
             '108176184247151/malibu-cg',
             '4412993/positivamente-academia']

follow_users_from = ['drgustavomarques', 'dr.felipebrito']

if __name__ == '__main__':
    session = InstaPy(username=bot_username, password=bot_password, want_check_browser=True, headless_browser=False)
    session.login()
    session.set_quota_supervisor(enabled=True, peak_likes_hourly=21, peak_comments_daily=240, peak_comments_hourly=21)
    session.set_relationship_bounds(enabled=True, max_followers=15000)
    session.set_user_interact(amount=random.randint(5, 10), randomize=True, percentage=50)
    # session.set_smart_location_hashtags(locations)
    session.set_dont_like(words_dont_like)
    session.set_do_like(True, percentage=50)
    session.set_do_follow(True, percentage=50)
    # session.set_do_comment(True, percentage=50)
    # session.set_comments(comments)

    # session.set_smart_location_hashtags(['110879272274192/campo-grande-brazil'], radius=100, limit=10)

    # session.like_by_locations(locations, randomize=True)
    # session.like_by_users(users_followed, amount=5, randomize=True)
    session.like_by_tags(hashtags,
                         amount=random.randint(5, 10),
                         use_random_tags=True,
                         randomize=True,
                         interact=True)


    # session.follow_by_tags(hashtags,
    #                        amount=random.randint(5, 10),
    #                        randomize=True,
    #                        interact=True)

    # session.follow_by_locations(locations, amount=random.randint(5, 10))

    # session.follow_user_followers(follow_users_from)

    session.end()
