def sendMastodon(photo, message, config):
    from mastodon import Mastodon
    mastodon = Mastodon(
        access_token=config.get('MASTODON', 'ACCESS_TOKEN'),
    )

    mastodon.media_post(photo, description=message, message=message)


# >>> mastodon = Mastodon(access_token = 'elonjet_usercred.secret')
# >>> mastodon.toot("First post test of app")