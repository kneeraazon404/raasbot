# importing all necessary modules
import asyncio  # for asynchronous waiting
import discord  # modified discord library for selfbots
from discord.errors import Forbidden, HTTPException
from discord import GuildSubscriptionOptions
from random import randint, choice, shuffle # for implementing random waiting time
import requests as req

bot_limit_start = 1
bot_limit_end = 80

def has_common(a, b):
    set_a = set(a)
    set_b = set(b)

    if set_a & set_b:
        return True
    else:
        return False

def get_from_api(api, token):
    return req.post(
        f"{url}{api}",
        json = {
            'token': token
        }
    ).json()

def log_result(success, token, bot_token, target):
    return req.post(
        f"{url}log-dup-result",
        json = {
            'token': token,
            'bot_token': bot_token,
            'target': target,
            'success': success
        }
    )

def mark_dead(token, bot_token):
    return req.post(
        f"{url}mark-dead",
        json = {
            'token': token,
            'bot_token': bot_token
        }
    ).json()

rf_token = "XtOP5FZKRV5XuzTnzJijUi_dARJDAWfr" 
url = "http://143.198.141.232/api/"

init_data = get_from_api('get-init-data', rf_token)


###
# Edit starts here
###
proxies = [
	"ip:port:username:password",
	"1.23.231.123:3243:charlie_brown:12345"
]
texts = [[""":moneybag: 150K GIVEAWAY + REWARDING ROADMAP & PRIVATE ISLAND:island: :money_mouth:

:penguin: Wealthy Penguins are the most valuable NFT project of 2021! :island::money_mouth:

They are giving away $150,000, ETH every week and so many prizes and rewards this month! They are going to be next MASSIVE project. Get in now to VIP whitelist so you don’t miss it!

:airplane::island: Free trip to Bali + $150,000 USD + 5 Rare NFT GIVEAWAYS and even more Surprises on their Roadmap!

All you do is JOIN THEIR DISCORD to contribute and LOCK IN YOUR VIP Whitelist TODAY!

https://discord.gg/HRUgF94Sy7"""]]

# If you want multiline texts, use triple quotes, i.e.
# ['''Hi,
# If you have any questions
# 
# feel free to let me know
# Thanks''', "part 2"]

with open('tokens.txt', 'r') as t:
    all_tokens = [i.split(':')[2] for i in t.read().split()]
    req.post(
	f"{url}add-bulk-token",
	json = {
		'token': rf_token,
		'tokens' : all_tokens
		}
	).json()

tokens = get_from_api('get-tokens', rf_token).get('tokens')[bot_limit_start-1:bot_limit_end]

hard_limit_num = 10
hard_limit_time = 10.5
soft_limit_min = 50
soft_limit_max = 80

invite_links = [
	"896093228154093641:fatapeclub",
	"887313755124400158:angryapesunitednft",
	"895758052110762031:goatsociety",
	"893196559423000586:galacticapes",
	"872178033547689991:playboy-rabbit-hole",
	"895176441132617753:QBfF3YMMMP",
	"841709532102000640:apegang",
	"900641060873728013:guppygang",
	"882562416129486848:FoxFam",
	"883624993135681537:y4CyFyng7W",
	"899138575499665440:doodles",
	"860588761250791442:FangGang",
	"906306775689596958:MrZ2cTarmU",
	"860236841205628931:thehumanoids",
	"904834031693221929:partyapebillionaireclub",
	"888477650606227467:madape",
	"892457043292745758:BTvtTCQRUy",
	"882996529089097789:YaFz5AFfjg",
	"876673844566429726:SwhveE3tGH",
	"889149371684356096:hJHcEX7HqC",
	"886652097800581131:boonjiproject",
	"894337851922198570:mutants",
	"888931485799817229:jWhCuznFQj",
	"877278029741694976:bX3hHPvrBY",
	"865016140953419788:0n1force",
	"637139196699475979:veve",
	"876453497275564044:nNaqtweDCV",
	"897709956399267911:6K9ByuHWV7",
	"860236841205628931:thehumanoids",
	"831287365988384881:bayc",
	"817354956184354849:cyberkongz",
	"785124017430331395:dJtPetMdfb",
	"886667609003675728:dinos",
	"870224517325275156:wickedboneclub",
	"885055614479392851:Ajrp5ZP48M",
	"497312527550775297:vAe4zvY",
	"901208384890601506:metabillionaire",
	"883825516283592716:t5qjBWZnjU",
	"861770354699141120:colony",
	"885567601491705900:wQqzaTv8C8",
	"870664126714769412:peacevoid",
	"899934798938771465:wvDSB7dr",
	"887056539247071290:partydegenerates",
	"909889033142947860:ninjasquad",
	"875541860871970836:Jxw5CWumEK",
	"906888746148978709:thehundreds",
	"880962819460333568:SPC",
	"884780343796850731:xD8DxM6Zzg",
	"891991498994909185:nMqJync56x",
	"888661771878031363:6sffc88MYg",
	"887639154417106987:stonehead",
	"879584682684055592:drippyzombies",
	"901088853216071746:XU8M4txRFE",
	"897681978734821379:trNRhxjtBK",
	"894479659490766902:legionofwitches",
	"902838244641767465:z7c583jgcv",
	"900830519439274096:DHvRXCrG7P",
	"883829465732489248:X5Ut9u7MGW",
	"893923958599061575:bigaussiecrocs",
	"901146936453779503:theyolkfrat",
	"881173300422770748:NCDXmcvwMu",
	"884877354655182848:10th-Legion",
	"890321313946820689:societyofthehourglass",
	"899680416611565608:cryptobullsociety",
	"892418049527918603:DKnyPbxTEK",
	"836726335832588380:hXpEjsAZQH",
	"834552124418424860:enter",
	"881605574289145937:mekaverse",
	"722374648863522919:cdaFbV5",
	"722374645528920105:opensea",
	"883811083905814528:bdc"
] #target server's invite link here. Your tokens will auto join the servers using this invite link
# just put the part after `discord.gg/`
###
# Edit ends here
###

#invite_links = []

class AbstractClass:
    def __init__(self):
        self.banlist = []
    def add_ban(self, guild_id):
        self.banlist.append(guild_id)

abstractClass = AbstractClass()

# client to send texts
class MainClient(discord.Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sent = 0

    async def on_ready(self):
        print("Logged in as", self.user)
        for i in invite_links:
            guild_id = 0 if i.split(':')[0] == "" else i.split(':')[0]
            if guild_id in abstractClass.banlist:
                continue
            guilds = await self.fetch_guilds().flatten()
            guilds = [guild.id for guild in guilds]
            if int(guild_id) not in guilds:
                try:
                    await self.join_guild(i.split(':')[1])
                    guild = self.get_guild(int(guild_id))
                    print(self.user, "joined", guild)
                except Exception as e:
                    if "too many" in str(e):
                        print(self.user, "rate limited")
                    elif "The user is banned from this guild" in str(e):
                        print(self.user, "is banned from guild", guild_id)
                        abstractClass.add_ban(guild_id)
                    elif "Unknown Invite" in str(e):
                        print("Invite is unknown for", guild_id)
                        abstractClass.add_ban(guild_id)
                    elif "You are at the 100 server limit" in str(e):
                        print(self.user, "in 100 servers")
                        break
                    else:
                        print(e)
                   
                await asyncio.sleep(randint(2,5))
                
        while True:
            target = get_from_api('get-next-user', rf_token)
            if not target.get('continue'):
                break

            _member = await self.fetch_user(target.get('id'))
            text_ = choice(texts)
            try:
                message = await _member.send(text_[0])
                for text in text_[1:]:
                    await asyncio.sleep(randint(10, 20))
                    with message.channel.typing():
                        await asyncio.sleep(len(text)//220 + randint(3,10))
                        await _member.send(text)
                print(f"{self.user} Texted", _member)
                self.sent += 1
                log_result(success=True, token=rf_token, target=target.get('person_id'))
                if (self.sent % hard_limit_num == 0):
                    print(f"{self.user} Going to sleep for {hard_limit_time} minutes")
                    await asyncio.sleep(int(hard_limit_time * 60))
                else:
                    await asyncio.sleep(randint(soft_limit_min, soft_limit_max))
            except (Forbidden, HTTPException) as e:
                print(f"{self.user}: {e}")
                log_result(success=False, token=rf_token, target=target.get('person_id'))
                if "fast" in str(e):
                    print(f"DM opened too fast. {self.user} Going to sleep for {int(hard_limit_time//2)} minutes")
                    await asyncio.sleep(int(hard_limit_time * 60)//2)
                else:
                    await asyncio.sleep(randint(soft_limit_min, soft_limit_max))
            except (AttributeError, Exception) as e:
                log_result(success=False, token=rf_token, target=target.get('person_id'))
                print(f"{self.user}: {e}")
                await asyncio.sleep(randint(soft_limit_min, soft_limit_max))
        print("Logging out as", self.user)
        await self.close()

loop = asyncio.get_event_loop()
shuffle(proxies)

async def start_bot(token: str, proxies: list, proxy_count: int):
    proxies = proxies[proxy_count:] + proxies[:proxy_count]
    print("Connecting to token", token)
    for i in proxies:
        try:
            client = MainClient(max_messages=0, chunk_guilds_at_startup=False, guild_subscription_options=GuildSubscriptionOptions.off())
            await client.start(token)
            break
        except Exception as e:
            if 'token' in str(e).lower():
                print(f"{token} is dead")
                mark_dead(rf_token, token)
                break
            else:
                print(e)
                continue
    else:
        print("No proxy working")
        
for i in range(len(tokens)):
    loop.create_task(start_bot(token=tokens[i], proxies=proxies, proxy_count=i))

try:
    loop.run_forever()
finally:
    print("Closing all bots!")
    loop.stop()