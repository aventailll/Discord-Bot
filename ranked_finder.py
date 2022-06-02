from riotwatcher import LolWatcher, ApiError
from soupsieve import match

def get_rank(username):
    api_key = 'RGAPI-1e891e9b-310f-4c7a-a3b8-7386a0c39847'
    watcher = LolWatcher(api_key)
    region = 'na1'

    user_lower = username.lower()
    user_data = watcher.summoner.by_name(region, user_lower)

    ranked_stats = watcher.league.by_summoner(region, user_data['id'])

    for i in range(len(ranked_stats)):
        gamemode = ranked_stats[i]['queueType']
        if gamemode != 'RANKED_TFT_PAIRS':
            if gamemode == 'RANKED_SOLO_5x5':
                queue = 'Ranked Solo/Duo: '
            else:
                break
            tier = ranked_stats[i]['tier']
            rank = ranked_stats[i]['rank']
            tier_rank = queue + tier + ' ' + rank

    puuid = user_data.get('puuid')
    my_matches = watcher.match.matchlist_by_puuid(region, puuid)
    matches = []
    for i in range(10):
        last_match = my_matches[i]
        matches.append(watcher.match.by_id(region, last_match))

    win_lost = []
    for i in range(10):
        match_detail = matches[i]
        target = ''
        for key in match_detail['info']['participants']:
            key_lower = key['summonerName'].lower()
            if key_lower == user_lower:
                target = key
                if key['win'] == False:
                    win_lost.append('🟥')
                else:
                    win_lost.append('🟩')
                break
    win_streak = ''.join(win_lost)
    return username, tier_rank, 'Recent 10 Games:', win_streak

print(get_rank('halal meat'))