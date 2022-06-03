# Discord-Bot

> This Discord bot allows for users to type in discord chat to see their League of Legends or their Valorant stats. 

The League of Legends data is supported by the Riot API, using their updated datasets to display the stats the bot outputs. This is seen in the ranked_finder.py file.

The Valorant data is obtained through webscrapping, using the BeautifulSoup library. The website the data was scrapped from is Valorant Tracker. This is seen in the valorant_stats.py file.

- `$league <username>` : outputs the users solo/duo rank, ranked flex rank, and wins/losts of their lasst 10 games
![image](https://user-images.githubusercontent.com/105384095/171774370-e6c67c75-121a-417b-918e-66b927f87c18.png)
- `$val <username#tag>` : outputs the users rank, K/D ratio, headshot percentage, and winrate
![image](https://user-images.githubusercontent.com/105384095/171774346-037a203b-801d-4c0c-bac9-047332118a7f.png)
