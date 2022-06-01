from riotwatcher import LolWatcher, ApiError
from soupsieve import match

def get_rank(username):
    api_key = 'RGAPI-1e891e9b-310f-4c7a-a3b8-7386a0c39847'
    watcher = LolWatcher(api_key)
    region = 'na1'

    user_data = watcher.summoner.by_name(region, username)

    ranked_stats = watcher.league.by_summoner(region, user_data['id'])

    for i in range(len(ranked_stats)):
        gamemode = ranked_stats[i]['queueType']
        if gamemode == 'RANKED_SOLO_5x5':
            queue = 'Queue Type: Ranked Solo/Duo'
        elif gamemode == 'RANKED_FLEX_SR':
            queue = 'Queue Type: Ranked Flex'
        tier = ranked_stats[i]['tier']
        rank = ranked_stats[i]['rank']
        tier_rank = 'Rank: ' + tier + ' ' + rank

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
            if key['summonerName'] == username:
                target = key
                if key['win'] == False:
                    win_lost.append('🟥')
                else:
                    win_lost.append('🟩')
                break
    win_streak = ''.join(win_lost)
    return username, queue, tier_rank, 'Recent 10 Games:', win_streak