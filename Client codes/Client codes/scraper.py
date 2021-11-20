import asyncio
import discord
from discord import GuildSubscriptionOptions
import requests as req


def has_common(a, b):
    set_a = set(a)
    set_b = set(b)

    if set_a & set_b:
        return True
    else:
        return False

rf_token = "XtOP5FZKRV5XuzTnzJijUi_dARJDAWfr" 
url = "http://143.198.141.232/api/"

servers = [
	"896093228154093638:896093228154093641",
	"887284123239055370:887313755124400158",
	"895758048965058570:895758052110762031",
	"872178033547689984:872178033547689991",
	"895176440130174986:895176441132617753",
	"841359732786331658:841709532102000640",
	"900641060873728010:900641060873728013",
	"873976168867569684:882562416129486848",
	"883622714814906369:883624993135681537",
	"870127360127696896:899138575499665440",
	"860588760550604811:860588761250791442",
	"876214810612731945:906306775689596958",
	"860236841205628928:860236841205628931",
	"889612451287552021:904834031693221929",
	"885079268374245376:888477650606227467",
	"892133539758366721:892457043292745758",
	"881946094379085886:882996529089097789",
	"876667418733334548:876673844566429726",
	"889146830800167003:889149371684356096",
	"886355434003374090:886652097800581131",
	"894337851762802718:894337851922198570",
	"888931485799817226:888931485799817229",
	"875444302904426536:877278029741694976",
	"863865570666348564:865016140953419788",
	"636847870556897280:637139196699475979",
	"876452951282044938:876453497275564044",
	"879801000691662908:897709956399267911",
	"860236841205628928:860236841205628931",
	"831287358355275877:831287365988384881",
	"817354956184354846:817354956184354849",
	"785124017430331395:785124017430331395",
	"868156749184651276:886667609003675728",
	"870224516515762207:870224517325275156",
	"885055614479392848:885055614479392851",
	"497312527093334036:497312527550775297",
	"901208384890601502:901208384890601506",
	"883819673332875314:883825516283592716",
	"861762240663388210:861770354699141120",
	"885567600447332385:885567601491705900",
	"870664124932161657:870664126714769412",
	"899934798477406218:899934798938771465",
	"887056538911506462:887056539247071290",
	"669653521007902751:909889033142947860",
	"875518063552921690:875541860871970836",
	"821417965374668810:906888746148978709",
	"873637563401904148:880962819460333568",
	"884780343796850728:884780343796850731",
	"891991497833078785:891991498994909185",
	"888661771878031360:888661771878031363",
	"887639153863426070:887639154417106987",
	"746030009143263354:879584682684055592",
	"901088850191994950:901088853216071746",
	"897681978734821377:897681978734821379",
	"894479658647687238:894479659490766902",
	"902828426501689384:902838244641767465",
	"877513061521584169:900830519439274096",
	"883829465732489246:883829465732489248",
	"892250541466460160:893923958599061575",
	"901146935900127232:901146936453779503",
	"881141613613682749:881173300422770748",
	"884865574272892968:884877354655182848",
	"883481593052803113:890321313946820689",
	"899637628691963904:899680416611565608",
	"889618101048573973:892418049527918603",
	"836726335330058291:836726335832588380",
	"834552122766262272:834552124418424860",
	"881232726362062928:881605574289145937",
	"722374645528920105:722374648863522919",
	"397566282729390110:722374645528920105",
	"883039347371302922:883811083905814528"
] # You can add multiple targets if you want. But make sure that your bot is inside those servers
# The problem with multiple server scraping is that you have to make sure that all DM tokens are also
# inside those servers. Unfortunately trying to autojoin a lot of servers make discord ban IPs (worse than banning tokens)

def get_from_api(api, token):
    return req.post(
        f"{url}{api}",
        json = {
            'token': token
        }
    ).json()

def log_result(success, token, target):
    return req.post(
        f"{url}log-result",
        json = {
            'token': token,
            'target': target,
            'success': success
        }
    )

init_data = get_from_api('get-init-data', rf_token)
tokens = get_from_api('get-tokens', rf_token).get('tokens')

# client to scrap data
class RootClient(discord.Client):
    async def on_ready(self):
        print("Logged in as", self.user)
        while True:
            for server in servers:
                guild = self.get_guild(int(server.split(':')[0]))
                clients = []
                print(f"Scraping guild {guild}. This might take some time")
                try:
                    await guild.subscribe(channel_id = int(server.split(':')[1]))
                except:
                    print("Error with server", server.split(':')[0])
                    continue
                for member in guild.members:
                    if not (
                        member.bot
                        or member.guild_permissions.administrator
                        or has_common(
                            init_data.get("restricted_roles"),
                            [i.name for i in member.roles]
                        )
                    ):
                        clients.append({
                            "id": member.id,
                            "username": f"{member.name}#{member.discriminator}",
                        })
                print("Completed scraping")
                print(len(clients), "from", guild)
                req.post(
                    f"{url}add-scraped",
                    json = {
                        'token': rf_token,
                        'users': clients
                    }
                )
            await asyncio.sleep(300)

should_scrape = True
print(should_scrape)
if should_scrape:
    client = RootClient(guild_subscription_options=GuildSubscriptionOptions.off())
    client.run("OTA3ODQ4MDA1NDU2MTAxNDA2.YYv_MA.9-5UQJv81TgA8JlHHgbWMcBPL5o")
