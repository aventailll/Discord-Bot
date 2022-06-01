from riotwatcher import LolWatcher, ApiError
from soupsieve import match

api_key = 'RGAPI-68af1e4a-fce4-4bb5-85aa-5fdfa3321893'
watcher = LolWatcher(api_key)
region = 'na1'
username = input('What is your username? ')

user_data = watcher.summoner.by_name(region, username)

ranked_stats = watcher.league.by_summoner(region, user_data['id'])

for i in range(len(ranked_stats)):
    gamemode = ranked_stats[i]['queueType']
    if gamemode == 'RANKED_SOLO_5x5':
        print('Queue Type: Ranked Solo Duo')
    elif gamemode == 'RANKED_FLEX_SR':
        print('Queue Type: Ranked Flex')
    tier = ranked_stats[i]['tier']
    rank = ranked_stats[i]['rank']
    print('Rank: ' + tier + ' ' + rank)

puuid = user_data.get('puuid')
my_matches = watcher.match.matchlist_by_puuid(region, puuid)
matches = []
for i in range(10):
    last_match = my_matches[i]
    matches.append(watcher.match.by_id(region, last_match))


print('Recent 10 Games:')
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
print(''.join(win_lost))