from bs4 import BeautifulSoup
import requests

def val_stats(username):
    user = username[:username.rfind("#")]
    tag = username[username.rfind("#"):][1:]
    url = 'https://tracker.gg/valorant/profile/riot/' + user + '%23' + tag + '/overview'
    
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    current_rank = soup.find_all('div', {'class': 'stat'})
    for stat in current_rank:
        stat_type = stat.find('span', {'class': 'stat__label'})
        if stat_type.text == 'Rating':
            rank = stat.find('span', {'class': 'stat__value'})
            break
    rank_output = '**Rank:** ' + rank.text
    
    def stats(type_of_stat):
        all_stats = soup.find_all('div', {'class': 'numbers'})
        for statter in all_stats:
            stat_type = statter.find('span', {'class': 'name'})
            if stat_type.text == type_of_stat:
                stat_val = statter.find('span', {'class': 'value'})
                break
        stat_val_output = '**' + type_of_stat + ':** ' + stat_val.text
        return stat_val_output

    kd = stats('K/D Ratio')

    hs = stats('Headshot%')
    
    wr = stats('Win %')
    output = [username, rank_output, kd, hs, wr]
    output = ' '.join(output)
    return output 
