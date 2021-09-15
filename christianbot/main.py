import discord
import os
import random
import asyncio
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix=')')
client.remove_command("help")



#Status
@client.event
async def ch_pr():
    await client.wait_until_ready()

    statuses = [
        "Discipleship | )help",
        f" in {len(client.guilds)} servers",
        "Version 1.2.0 BETA",
        "Check my bio",
    ]

    while not client.is_closed():

        status = random.choice(statuses)

        await client.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(3)


client.loop.create_task(ch_pr())


#moderation cmds


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
    await user.ban(reason=reason)
    await ctx.send(f"{user} has been bannned successfully")


#cmds and hlp menus

@client.command()
async def help(ctx):
    embed1 = discord.Embed(title="Main Menu",
                           description="    ",
                           color=discord.Color.random())
    embed1.add_field(name="`)help`",
                     value="Gets you this message.",
                     inline=False)
    embed1.add_field(name="`)ban`",
                    value="Do `)ban @user` for this to work",
                    inline=False)
    embed1.add_field(name="`)motivation`",
                    value="gives you a motivational quote",
                    inline=False)
    embed1.add_field(name="`)ping`",
                    value="shows the bot's latency",
                    inline=False)
    embed1.add_field(name="`)about`",
                    value="gives you a bit of info about the bot",
                    inline=False)
    embed1.add_field(name="`)invite`",value="Gives you the invite link for the bot")
    embed1.add_field(
        name="`)library`",
        value=
        "Gives you the bot's library and resource command list. This library is being updated as frequently as possible, so be sure to use it!",
        inline=False)
    embed1.set_thumbnail(url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
    embed1.set_footer(text="Help Menu", icon_url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
    await ctx.send(embed=embed1)

#library

@client.command()
async def library(ctx):
    embed12 = discord.Embed(title="Library", color=0xcdaa7d)
    embed12.add_field(name="`)creeds`",
                      value="gives you the list of available creeds",
                      inline=False)
    embed12.add_field(name="`)yeshua`",
                      value="gives you information about our Messiah",
                      inline=False)
    embed12.add_field(name="`)salvation`",
                      value="gives you information about salvation")
    embed12.add_field(name="`)nft`", value="The __N__inety-__F__ive __T__heses of Martin Luther", inline=False)
    embed12.add_field(name="`)churchfathers`", value="[Coming Soon]", inline=False)
    embed12.add_field(name="`)doctrines`", value="Coming soon", inline=False)
    embed12.add_field(name="`)OR`", value="__O__nline __R__esources [Currently adding more sites]", inline=False)
    embed12.add_field(name="`)fallacies`", value="Gives you the ten commandments of logic in an image", inline=False)
    embed12.add_field(name="`)philosophy`", value="Coming Soon", inline=False)
    embed12.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.britanniapine.co.uk%2Fcontent%2Fimages%2Fproducts%2F312%2Fmain%2F..OpusSBC_SmallBookcase_Living.jpg&f=1&nofb=1")
    embed12.set_footer(text="Library", icon_url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
    await ctx.send(embed=embed12)

@client.command()
async def fallacies(ctx):
  embed17 = discord.Embed(Title="The Ten Fallacies", Description="The Ten Fallacies You should never use", color=discord.Color.random())
  embed17.set_image(url="https://media.discordapp.net/attachments/880178538035159050/880639730612568084/FB_IMG_1630031249162.jpg?width=514&height=514")
  embed17.set_footer(text="Library | Fallacies", icon_url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
  await ctx.send(embed=embed17)

@client.command()
async def salvation(ctx):
    embed = discord.Embed(
        title="What Must I Do To Be Saved?",
        description=
        "This question was asked to one of the followers of Jesus Christ nearly 2000 years ago and is still just as important and relevant of a question for you today. Have you ever thought about this question? Do you know the answer to the question? I would like you to seriously consider this question today because your response will determine how you will live your life and where you will spend eternity after you die.  So please, read this page carefully in its entirety. **Here is how the follower of Jesus answered the question: “Believe in the Lord Jesus Christ, and you will be saved” (Acts 16:31).** It is a simple response, but what exactly does it mean to “believe in the Lord Jesus Christ”?  And from what do you need to be “saved”?", url="https://www.thechristianworldview.org/about-us-2/what-must-do-to-be-saved/",
        color=0xff4040)
    embed.add_field(name="-- What Does It Mean to be Saved?", 
    value="The Bible, which claims to be the inspired word of God (2 Timothy 3:16) and entirely truthful (John 17:17; Psalm 119:160), gives a straightforward answer to what you need to be saved from: you need to saved from God Himself. The Bible says that God created and sustains everything in the universe (Genesis 1:1; Job 38:1-41) … including you (Psalm 139:13-16). It is He who established the unchanging laws of nature and morality. It is He who has ultimate authority over His creation. It is He who desires for you to be in a right relationship with Him (1 Timothy 2:3-4). In addition to being the Creator, God has another title — Judge. He has established good and righteous laws for our benefit, but sadly you (and I and everyone else) have disobeyed His laws in one way or another: by lying, lusting, gossiping, slandering, envying, coveting, stealing, cheating, using God’s or Jesus’ name as a curse word, or loving someone or something more than God.", inline=False)
    embed.add_field(name="To Learn More, Click This Link:", value="[Here](https://www.thechristianworldview.org/about-us-2/what-must-do-to-be-saved/)", inline=False)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.istockphoto.com%2Fphotos%2Fman-praying-picture-id498338635%3Fk%3D6%26m%3D498338635%26s%3D170667a%26w%3D0%26h%3Djl6oJ5-f6MIR8e9odwIg_mAFt2udf8Ptv1Dyn9r4iYk%3D&f=1&nofb=1")
    embed.set_footer(text="Library | Salvation", icon_url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
    await ctx.send(embed=embed)


@client.command()
async def OR(ctx):
  embed16 = discord.Embed(title="Online Resources", color=0xffffff)
  embed16.add_field(name="`)ORyt`", value="Gives you the YouTube Resources", inline=False)
  embed16.add_field(name="`)ORws`", value="Gives you website resources", inline=False)
  embed16.set_thumbnail(url="https://media.istockphoto.com/photos/laptop-computer-with-empty-white-screen-on-the-table-picture-id1056971744?k=6&m=1056971744&s=170667a&w=0&h=Abwa8pKg4vlLUMYXAYyGQYInTq9HnwIgMrQVRqszRi4=")
  embed16.set_footer(text="Library | Online Resources", icon_url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
  await ctx.send(embed=embed16)

@client.command()
async def ORws(ctx):
  embed20 = discord.Embed(title="Online Resources", color=0xffffff)
  embed20.add_field(name="The Christian Worldview - Website", value="[The Christian Worldview](https://www.thechristianworldview.org/)", inline=False)
  embed20.add_field(name="The Bibilically Correct Podcast - Official Website", value="[BCP](https://www.biblicallycorrectpodcast.org/)", inline=False)
  embed20.add_field(name="To Be Continued", value="To talk more with fellow members, and access the Bot Developer's blog, click [here.](https://sjcoden.wordpress.com/)", inline=False)
  embed20.set_footer(text="Library | Online Resources | Websites", icon_url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
  await ctx.send(embed=embed20)

@client.command()
async def ORyt(ctx):
  embed18 = discord.Embed(title="Online Resources - YouTube", color=0xffffff)
  embed18.add_field(name="Exploring Reality with Than Christopolous", value="[Exploring Reality](https://www.youtube.com/channel/UChhu9MXU8Or1t6I8JazgT_g)", inline=False)
  embed18.add_field(name="ASKDrBrown", value="[AskDrBrown](https://www.youtube.com/c/AskDrBrownVideos)", inline=False)
  embed18.add_field(name="C.S. Lewis Institute", value="[C.S. Lewis Institute](https://www.youtube.com/channel/UCIDg-4JbV46fXxSZV0tvllA)", inline=False)
  embed18.add_field(name="Cross Examined with Dr. Frank Turek",
  value="[Cross Examined](https://www.youtube.com/user/TurekVideo)", inline=False)
  embed18.add_field(name="Rob Christian", value="[Rob Christian - Christian Polemicist](https://www.youtube.com/channel/UCFSZf2eM0fgtcGGzIxx_LBg)", inline=False)
  embed18.set_thumbnail(url="https://icons.iconarchive.com/icons/dakirby309/simply-styled/256/YouTube-icon.png")
  embed18.set_footer(text="Library | Online Resources | YouTube", icon_url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
  await ctx.send(embed=embed18)

@client.command()
async def luther(ctx):
  await ctx.send("https://images-ext-2.discordapp.net/external/UD6d7GGuAkJdbRoEDoDSEXdFOnS4dHey2V2JX73fOUU/%3Fv%3D1/https/cdn.discordapp.com/emojis/855070947870638090.png")
#creed



@client.command()
async def creeds(ctx):
    embed4 = discord.Embed(title="Commands for Creeds",
                           color=0x000000)
    embed4.add_field(name="`)nicene1`",
                     value="The Nicene Creed of 325 AD",
                     inline=False)
    embed4.add_field(name="`)nicene2`",
                     value="The Nicene Creed of 381 AD",
                     inline=False)
    embed4.add_field(name="`)apostles`",
                     value="The Apostles' Creed",
                     inline=False)
    embed4.add_field(name="`)athanasian`",
                     value="The Athanasian Creed",
                     inline=False)
    embed4.add_field(name="`)chalcedonian`",
                     value="The Chalcedonian Definition")
    embed4.set_footer(text="Library | Creeds", icon_url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
    await ctx.send(embed=embed4)



@client.command()
async def nicene(ctx):
    embed10 = discord.Embed(Title="Nicene Creeds",
                            Description="Nicene Creeds",
                            color=discord.Color.random())
    embed10.add_field(name="Nicene Creed of 325",
                      value="In order to use this creed, type `)nicene1`.")
    embed10.add_field(name="Nicene Creed of 381",
                      value="In order to use this creed, type `)nicene2`. ")
    embed10.set_footer(text="Library | Creeds | Nicene", icon_url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
    await ctx.send(embed=embed10)

#95 theses

@client.command()
async def nft(ctx):
    embed13 = discord.Embed(Title="The 95 theses of Martin Luther",
                            color=0x548b54)
    embed13.add_field(name="The Ninety-five Theses of Martin Luther Commands", value="-----", inline=False)
    embed13.add_field(name="`)nft1`",
                      value="the 95 theses of Martin Luther, page 1", inline=False)
    embed13.add_field(name="`)nft2`",
                      value="the 95 theses of Martin Luther, page 2", inline=False)
    embed13.add_field(name="`)nft3`",
                      value="the 95 theses of Martin Luther, page 3", inline=False)
    embed13.set_thumbnail(url="https://cdn.discordapp.com/emojis/855070947870638090.png?v=1")
    embed13.set_footer(text="Library | 95 Theses of Martin Luther", icon_url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
    await ctx.send(embed=embed13)


@client.command()
async def nft1(ctx):
    embed11 = discord.Embed(Title="95 theses",
                            description="The 95 Theses of Martin Luther - Page 1",
                            color=0x548b54)
    embed11.add_field(
        name="-",
        value=
        "Out of love for the truth and the desire to bring it to light, the following propositions will be discussed at Wittenberg, under the presidency of the Reverend Father Martin Luther, Master of Arts and of Sacred Theology, and Lecturer in Ordinary on the same at that place. Wherefore he requests that those who are unable to be present and debate orally with us, may do so by letter.",
        inline=False)
    embed11.add_field(name="-",
                      value="In the Name our Lord Jesus Christ. Amen.",
                      inline=False)
    embed11.add_field(
        name="-",
        value=
        "**1.** *Our Lord and Master Jesus Christ, when He said Poenitentiam agite, willed that the whole life of believers should be repentance.* **2.** *This word cannot be understood to mean sacramental penance, i.e., confession and satisfaction, which is administered by the priests.*  **3.** *Yet it means not inward repentance only; nay, there is no inward repentance which does not outwardly work divers mortifications of the flesh.* **4.** *The penalty [of sin], therefore, continues so long as hatred of self continues; for this is the true inward repentance, and continues until our entrance into the kingdom of heaven.* **5.** *The pope does not intend to remit, and cannot remit any penalties other than those which he has imposed either by his own authority or by that of the Canons.*",
        inline=False)
    embed11.add_field(
        name="-",
        value=
        "**6.** *The pope cannot remit any guilt, except by declaring that it has been remitted by God and by assenting to God's remission; though, to be sure, he may grant remission in cases reserved to his judgment. If his right to grant remission in such cases were despised, the guilt would remain entirely unforgiven.* **7.** *God remits guilt to no one whom He does not, at the same time, humble in all things and bring into subjection to His vicar, the priest.* **8.** *The penitential canons are imposed only on the living, and, according to them, nothing should be imposed on the dying.* **9.** *Therefore the Holy Spirit in the pope is kind to us, because in his decrees he always makes exception of the article of death and of necessity.* **10.** *Ignorant and wicked are the doings of those priests who, in the case of the dying, reserve canonical penances for purgatory.*"
    )
    embed11.add_field(
        name="-",
        value=
        "**11.** *This changing of the canonical penalty to the penalty of purgatory is quite evidently one of the tares that were sown while the bishops slept.* **12.** *In former times the canonical penalties were imposed not after, but before absolution, as tests of true contrition.* **13.** *The dying are freed by death from all penalties; they are already dead to canonical rules, and have a right to be released from them.* **14.** *The imperfect health [of soul], that is to say, the imperfect love, of the dying brings with it, of necessity, great fear; and the smaller the love, the greater is the fear.* **15.** *This fear and horror is sufficient of itself alone (to say nothing of other things) to constitute the penalty of purgatory, since it is very near to the horror of despair.* **16.** *Hell, purgatory, and heaven seem to differ as do despair, almost-despair, and the assurance of safety.* **17.** *With souls in purgatory it seems necessary that horror should grow less and love increase.*",
        inline=False)
    embed11.add_field(
        name="-",
        value=
        "**18.** *It seems unproved, either by reason or Scripture, that they are outside the state of merit, that is to say, of increasing love.* **19.** *Again, it seems unproved that they, or at least that all of them, are certain or assured of their own blessedness, though we may be quite certain of it.* **20.** *Therefore by `full remission of all penalties` the pope means not actually `of all,` but only of those imposed by himself.* **21.** *Therefore those preachers of indulgences are in error, who say that by the pope's indulgences a man is freed from every penalty, and saved;* **22.** *Whereas he remits to souls in purgatory no penalty which, according to the canons, they would have had to pay in this life.* **23.** *If it is at all possible to grant to any one the remission of all penalties whatsoever, it is certain that this remission can be granted only to the most perfect, that is, to the very fewest.*"
    )
    embed11.add_field(
        name="-",
        value=
        "**24.** *It must needs be, therefore, that the greater part of the people are deceived by that indiscriminate and highsounding promise of release from penalty.* **25.** *The power which the pope has, in a general way, over purgatory, is just like the power which any bishop or curate has, in a special way, within his own diocese or parish.* **26.** *The pope does well when he grants remission to souls [in purgatory], not by the power of the keys (which he does not possess), but by way of intercession.* **27.** *They preach man who say that so soon as the penny jingles into the money-box, the soul flies out [of purgatory].* **28.** *It is certain that when the penny jingles into the money-box, gain and avarice can be increased, but the result of the intercession of the Church is in the power of God alone.* **29.** *Who knows whether all the souls in purgatory wish to be bought out of it, as in the legend of Sts. Severinus and Paschal.*"
    )
    embed11.set_footer(text="Library | 95 Theses of Martin Luther | Page 1")
    await ctx.send(embed=embed11)

@client.command()
async def nft2(ctx):
  embed14 = discord.Embed(Title="95 Theses of Martin Luther - Page 2", color=0x548b54)
  embed14.add_field(
        name="The 95 Theses of Martin Luther - Page 2",
        value=
        "**30.** *No one is sure that his own contrition is sincere; much less that he has attained full remission.* **31.** *Rare as is the man that is truly penitent, so rare is also the man who truly buys indulgences, i.e., such men are most rare.* **32.** *They will be condemned eternally, together with their teachers, who believe themselves sure of their salvation because they have letters of pardon.* **33.** *Men must be on their guard against those who say that the pope's pardons are that inestimable gift of God by which man is reconciled to Him;* **34.** *For these `graces of pardon` concern only the penalties of sacramental satisfaction, and these are appointed by man.* **35.** *They preach no Christian doctrine who teach that contrition is not necessary in those who intend to buy souls out of purgatory or to buy confessionalia.* **36.** *Every truly repentant Christian has a right to full remission of penalty and guilt, even without letters of pardon.*", inline=False
    )
  embed14.add_field(name="-", value="**37.** *Every true Christian, whether living or dead, has part in all the blessings of Christ and the Church; and this is granted him by God, even without letters of pardon.* **38.** *Nevertheless, the remission and participation [in the blessings of the Church] which are granted by the pope are in no way to be despised, for they are, as I have said, the declaration of divine remission.* **39.** *It is most difficult, even for the very keenest theologians, at one and the same time to commend to the people the abundance of pardons and [the need of] true contrition.* **40.** *True contrition seeks and loves penalties, but liberal pardons only relax penalties and cause them to be hated, or at least, furnish an occasion [for hating them].* **41.** *Apostolic pardons are to be preached with caution, lest the people may falsely think them preferable to other good works of love.*",
        inline=False)
  embed14.add_field(name="--", value="**42.** *Christians are to be taught that the pope does not intend the buying of pardons to be compared in any way to works of mercy.* **43.** *Christians are to be taught that he who gives to the poor or lends to the needy does a better work than buying pardons;* **44.** *Because love grows by works of love, and man becomes better; but by pardons man does not grow better, only more free from penalty.* **45.** *Christians are to be taught that he who sees a man in need, and passes him by, and gives [his money] for pardons, purchases not the indulgences of the pope, but the indignation of God.* **46.** *Christians are to be taught that unless they have more than they need, they are bound to keep back what is necessary for their own families, and by no means to squander it on pardons.* **47.** *Christians are to be taught that the buying of pardons is a matter of free will, and not of commandment.*", inline=False)
  embed14.add_field(name="--", value="**48.** *Christians are to be taught that the pope, in granting pardons, needs, and therefore desires, their devout prayer for him more than the money they bring.* **49.** *Christians are to be taught that the pope's pardons are useful, if they do not put their trust in them; but altogether harmful, if through them they lose their fear of God.* **50.** *Christians are to be taught that if the pope knew the exactions of the pardon-preachers, he would rather that St. Peter's church should go to ashes, than that it should be built up with the skin, flesh and bones of his sheep.* **51.** *Christians are to be taught that it would be the pope's wish, as it is his duty, to give of his own money to very many of those from whom certain hawkers of pardons cajole money, even though the church of St. Peter might have to be sold.* **52.** *The assurance of salvation by letters of pardon is vain, even though the commissary, nay, even though the pope himself, were to stake his soul upon it.*", inline=False)
  embed14.add_field(name="--", value="**53.** *They are enemies of Christ and of the pope, who bid the Word of God be altogether silent in some Churches, in order that pardons may be preached in others.* **54.** *Injury is done the Word of God when, in the same sermon, an equal or a longer time is spent on pardons than on this Word.* **55.** *It must be the intention of the pope that if pardons, which are a very small thing, are celebrated with one bell, with single processions and ceremonies, then the Gospel, which is the very greatest thing, should be preached with a hundred bells, a hundred processions, a hundred ceremonies.* **56.** *The `treasures of the Church,` out of which the pope grants indulgences, are not sufficiently named or known among the people of Christ.* **57.** *That they are not temporal treasures is certainly evident, for many of the vendors do not pour out such treasures so easily, but only gather them.*", inline=False)
  embed14.add_field(name="--", value="**58.** *Nor are they the merits of Christ and the Saints, for even without the pope, these always work grace for the inner man, and the cross, death, and hell for the outward man.* **59.** *St. Lawrence said that the treasures of the Church were the Church's poor, but he spoke according to the usage of the word in his own time.* **60.** *Without rashness we say that the keys of the Church, given by Christ's merit, are that treasure;* **61.** *For it is clear that for the remission of penalties and of reserved cases, the power of the pope is of itself sufficient.* **62.** *The true treasure of the Church is the Most Holy Gospel of the glory and the grace of God.* **63.** *But this treasure is naturally most odious, for it makes the first to be last.* **64.** *On the other hand, the treasure of indulgences is naturally most acceptable, for it makes the last to be first.* **65.** *Therefore the treasures of the Gospel are nets with which they formerly were wont to fish for men of riches.*", inline=False)
  embed14.set_footer(text="Library | 95 Theses of Martin Luther | Page 2")
  await ctx.send(embed=embed14)

@client.command()
async def nft3(ctx):
  embed15 = discord.Embed(title="The Ninety-Five Theses of Martin Luther - Page 3", description="     ", color=0x548b54)
  embed15.add_field(name="--", value="**66.** *The treasures of the indulgences are nets with which they now fish for the riches of men.* **67.** *The indulgences which the preachers cry as the `greatest graces` are known to be truly such, in so far as they promote gain.* **68.** *Yet they are in truth the very smallest graces compared with the grace of God and the piety of the Cross.* **69.** *Bishops and curates are bound to admit the commissaries of apostolic pardons, with all reverence.* **70.** *But still more are they bound to strain all their eyes and attend with all their ears, lest these men preach their own dreams instead of the commission of the pope.* **71.** *He who speaks against the truth of apostolic pardons, let him be anathema and accursed!* **72.** *But he who guards against the lust and license of the pardon-preachers, let him be blessed!* **73.** *The pope justly thunders against those who, by any art, contrive the injury of the traffic in pardons.*", inline=False)
  embed15.add_field(name="-----", value="**74.** *But much more does he intend to thunder against those who use the pretext of pardons to contrive the injury of holy love and truth.* **75.** *To think the papal pardons so great that they could absolve a man even if he had committed an impossible sin and violated the Mother of God—this is madness.* **76.** *We say, on the contrary, that the papal pardons are not able to remove the very least of venial sins, so far as its guilt is concerned.* **77.** *It is said that even St. Peter, if he were now Pope, could not bestow greater graces; this is blasphemy against St. Peter and against the pope.* **78.** *We say, on the contrary, that even the present pope, and any pope at all, has greater graces at his disposal; to wit, the Gospel, powers, gifts of healing, etc., as it is written in I. Corinthians xii.* **79.** *To say that the cross, emblazoned with the papal arms, which is set up [by the preachers of indulgences], is of equal worth with the Cross of Christ, is blasphemy.*", inline=False)
  embed15.add_field(name="-----", value="**80.** *The bishops, curates and theologians who allow such talk to be spread among the people, will have an account to render.* **81.** *This unbridled preaching of pardons makes it no easy matter, even for learned men, to rescue the reverence due to the pope from slander, or even from the shrewd questionings of the laity.* **82.** *To wit:—`Why does not the pope empty purgatory, for the sake of holy love and of the dire need of the souls that are there, if he redeems an infinite number of souls for the sake of miserable money with which to build a Church? The former reasons would be most just; the latter is most trivial.`* **83.** *Again:—`Why are mortuary and anniversary masses for the dead continued, and why does he not return or permit the withdrawal of the endowments founded on their behalf, since it is wrong to pray for the redeemed?`*", inline=False)
  embed15.add_field(name="-----", value="**84.** *Again:—`What is this new piety of God and the pope, that for money they allow a man who is impious and their enemy to buy out of purgatory the pious soul of a friend of God, and do not rather, because of that pious and beloved soul's own need, free it for pure love's sake?`* **85.** *Again:—`Why are the penitential canons long since in actual fact and through disuse abrogated and dead, now satisfied by the granting of indulgences, as though they were still alive and in force?`* **86.** *Again:—`Why does not the pope, whose wealth is to-day greater than the riches of the richest, build just this one church of St. Peter with his own money, rather than with the money of poor believers?`* **87.** *Again:—`What is it that the pope remits, and what participation does he grant to those who, by perfect contrition, have a right to full remission and participation?`*", inline=False)
  embed15.add_field(name="-----", value="**88.** *Again:—`What greater blessing could come to the Church than if the pope were to do a hundred times a day what he now does once, and bestow on every believer these remissions and participations?`* **89.** *`Since the pope, by his pardons, seeks the salvation of souls rather than money, why does he suspend the indulgences and pardons granted heretofore, since these have equal efficacy?`* **90.** *To repress these arguments and scruples of the laity by force alone, and not to resolve them by giving reasons, is to expose the Church and the pope to the ridicule of their enemies, and to make Christians unhappy.* **91.** *If, therefore, pardons were preached according to the spirit and mind of the pope, all these doubts would be readily resolved; nay, they would not exist.* **92.** *Away, then, with all those prophets who say to the people of Christ, `Peace, peace,` and there is no peace!* **93.** *Blessed be all those prophets who say to the people of Christ, `Cross, cross,` and there is no cross!*", inline=False)
  embed15.add_field(name="-----", value="**94.** *Christians are to be exhorted that they be diligent in following Christ, their Head, through penalties, deaths, and hell;* **95.** *And thus be confident of entering into heaven rather through many tribulations, than through the assurance of peace.*", inline=False)
  embed15.set_footer(text="Library | 95 Theses of Martin Luther | Page 3")
  await ctx.send(embed=embed15)
#creed

@client.command()
async def nicene1(ctx):
    embed5 = discord.Embed(title="The Nicene Creed 325 AD",
                           description="   ",
                           color=discord.Color.random())
    embed5.add_field(
        name="-----",
        value=
        "We believe in one God, the Father Almighty, Maker of all things visible and invisible.And in one Lord Jesus Christ, the Son of God, begotten of the Father the only-begotten; that is, of the essence of the Father, God of God, Light of Light, very God of very God, begotten, not made, being of one substance with the Father; by whom all things were made both in heaven and on earth; who for us men, and for our salvation, came down and was incarnate and was made man; he suffered, and the third day he rose again, ascended into heaven; from thence he shall come to judge the quick and the dead.And in the Holy Ghost.But those who say: THERE WAS A TIME WHEN HE WAS NOT; and HE WAS NOT BEFORE HE WAS MADE and HE WAS MADE OUT OF NOTHING, or HE IS OF ANOTHER SUBSTANCE or ESSENCE, or THE SON OF GOD IS CREATED, or CHANGABLE, or ALTERABLE—they are condemned by the holy catholic and apostolic Church.",
        inline=False)
    embed5.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fzimmermanband.com%2Fwp-content%2Fuploads%2F2018%2F02%2FniceneCREED-1024x683.jpg&f=1&nofb=1")
    embed5.set_footer(text="Library | Creeds | The Nicene Creed of 325 A.D.", icon_url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
    await ctx.send(embed=embed5)


@client.command()
async def nicene2(ctx):
    embed6 = discord.Embed(title="The Nicene Creed 385 AD",
                           description="    ",
                           color=discord.Color.random())
    embed6.add_field(
        name="----",
        value=
        "We believe in one God, the Father Almighty, Maker of heaven and earth, and of all things visible and invisible. And in one Lord Jesus Christ, the only-begotten Son of God, begotten of the Father before all worlds (æons), Light of Light, very God of very God, begotten, not made, being of one substance with the Father; by whom all things were made; who for us men, and for our salvation, came down from heaven, and was incarnate by the Holy Ghost of the Virgin Mary, and was made man; he was crucified for us under Pontius Pilate, and suffered, and was buried, and the third day he rose again, according to the Scriptures, and ascended into heaven, and sitteth on the right hand of the Father; from thence he shall come again, with glory, to judge the quick and the dead; whose kingdom shall have no end.",
        inline=False)
    embed6.add_field(
        name="------",
        value=
        "And in the Holy Ghost, the Lord and Giver of life, who proceedeth from the Father and the Son, who with the Father and the Son together is worshiped and glorified, who spake by the prophets. In one holy catholic and apostolic Church; we acknowledge one baptism for the remission of sins; we look for the resurrection of the dead, and the life of the world to come. Amen."
    )
    embed6.set_thumbnail(
    url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fzimmermanband.com%2Fwp-content%2Fuploads%2F2018%2F02%2FniceneCREED-1024x683.jpg&f=1&nofb=1")
    embed6.set_footer(text="Library | Creeds | The Nicene Creed of 381 A.D.", icon_url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
    await ctx.send(embed=embed6)


@client.command()
async def athanasian(ctx):
    embed8 = discord.Embed(Title="The Athanasian Creed",
                           description="     ",
                           color=discord.Color.random())
    embed8.add_field(
        name="**The Athanasian Creed**",
        value=
        "Whosoever will be saved, before all things it is necessary that he hold the catholic faith; Which faith except every one do keep whole and undefiled, without doubt he shall perish everlastingly. And the catholic faith is this: That we worship one God in Trinity, and Trinity in Unity; Neither confounding the persons, nor dividing the substance. For there is one Person of the Father, another of the Son and another of the Holy Spirit. But the Godhead of the Father, of the Son, and of the Holy Spirit is all one, the glory equal, the majesty co-eternal. Such as the Father is, such is the Son and such is the Holy Spirit. The Father uncreated, the Son uncreated, and the Holy Spirit uncreated. The Father incomprehensible, the Son incomprehensible, and the Holy Spirit incomprehensible. The Father eternal, the Son eternal, and the Holy Spirit eternal. And yet they are not three eternals, but one eternal. As also there are not three uncreated nor three incomprehensibles, but one uncreated and one incomprehensible.",
        inline=False)
    embed8.add_field(
        name="_____",
        value=
        "So likewise the Father is almighty, the Son almighty, and the Holy Spirit almighty; And yet they are not three almighties, but one almighty. So the Father is God, the Son is God, and the Holy Spirit is God; And yet they are not three Gods, but one God. So likewise the Father is Lord, the Son Lord, and the Holy Spirit Lord; And yet they are not three Lords, but one Lord. For like as we are compelled by the Christian verity to acknowledge every person by himself to be God and Lord; so are we forbidden by the catholic religion to say: There are three Gods or three Lords. The Father is made of none, neither created nor begotten. The Son is of the Father alone; not made nor created, but begotten. The Holy Spirit is of the Father and of the Son; neither made, nor created, nor begotten, but proceeding. So there is one Father, not three Fathers; one Son, not three Sons; one Holy Spirit, not three Holy Spirits. And in this Trinity none is afore, nor after another; none is greater, or less than another.",
        inline=False)
    embed8.add_field(
        name="_____",
        value=
        "But the whole three persons are co-eternal, and co-equal. So that in all things, as aforesaid, the Unity in Trinity and the Trinity in Unity is to be worshipped. He therefore that will be saved must thus think of the Trinity. Furthermore it is necessary to everlasting salvation that he also believe rightly the incarnation of our Lord Jesus Christ. For the right faith is that we believe and confess that our Lord Jesus Christ, the Son of God, is God and man. God of the substance of the Father, begotten before the worlds; and made of the substance of His mother, born in the world. Perfect God and perfect man, of a reasonable soul and human flesh subsisting. Equal to the Father as touching His Godhead, and inferior to the Father as touching His manhood. Who, although He is God and man, yet He is not two, but one Christ. One, not by conversion of the Godhead into flesh, but by taking of the manhood into God. One altogether, not by the confusion of substance, but by unity of person.",
        inline=False)
    embed8.add_field(
        name="_____",
        value=
        "For as the reasonable soul and flesh is one man, so God and man is one Christ; Who suffered for our salvation, descended into hell, rose again the third day from the dead; He ascended into heaven, He sitteth on the right hand of the Father, God Almighty; From thence He shall come to judge the living and the dead. At whose coming all men shall rise again with their bodies; And shall give account of their own works. And they that have done good shall go into life everlasting, and they that have done evil into everlasting fire. This is the catholic faith, which except a man believe faithfully, he cannot be saved.",
        inline=False)
    embed8.set_footer(text="Library | Creeds | The Athanasian Creed", icon_url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
    await ctx.send(embed=embed8)

@client.command()
async def apostles(ctx):
    embed7 = discord.Embed(Title="The Apostle's Creed",
                           color=discord.Color.random())
    embed7.add_field(
        name="Apostles' Creed",
        value=
        "I believe in God, the Father Almighty, the Maker of heaven and earth, and in Jesus Christ, His only Son, our Lord: Who was conceived by the Holy Ghost, born of the virgin Mary, suffered under Pontius Pilate, was crucified, dead, and buried; He descended into hell. The third day He arose again from the dead; He ascended into heaven, and sitteth on the right hand of God the Father Almighty; from thence he shall come to judge the quick and the dead. I believe in the Holy Ghost; the holy catholic church; the communion of saints; the forgiveness of sins; the resurrection of the body; and the life everlasting. Amen.",
        inline=False)
    embed7.set_footer(text="Library | Creeds | Apostles' Creed", icon_url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
    await ctx.send(embed=embed7)



@client.command()
async def chalcedonian(ctx):
    embed9 = discord.Embed(Title="The Chalcedonian Definition",
                           description="**The Chalcedonian Definition**",
                           color=discord.Color.random())
    embed9.add_field(
        name="-----",
        value=
        "Therefore, following the holy fathers, we all with one accord teach men to acknowledge one and the same Son, our Lord Jesus Christ, at once complete in Godhead and complete in manhood, truly God and truly man, consisting also of a reasonable soul and body; of one substance with the Father as regards his Godhead, and at the same time of one substance with us as regards his manhood; like us in all respects, apart from sin; as regards his Godhead, begotten of the Father before the ages, but yet as regards his manhood begotten, for us men and for our salvation, of Mary the Virgin, the God-bearer; one and the same Christ, Son, Lord, Only-begotten, recognized in two natures, without confusion, without change, without division, without separation;",
        inline=False)
    embed9.add_field(
        name="_____",
        value=
        "the distinction of natures being in no way annulled by the union, but rather the characteristics of each nature being preserved and coming together to form one person and subsistence, not as parted or separated into two persons, but one and the same Son and Only-begotten God the Word, Lord Jesus Christ; even as the prophets from earliest times spoke of him, and our Lord Jesus Christ himself taught us, and the creed of the fathers has handed down to us.",
        inline=False)
    embed9.set_footer(text="Library | Creeds | The Chalcedoinian Definition", icon_url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
    await ctx.send(embed=embed9)



@client.command()
async def yeshua(ctx):
    embed = discord.Embed(
        title="יֵשׁוּעַ = Yeshua",
        description=
        "A man who came to earth and died as a man, that you might attain salvation through his blood. He was fully human, and fully God. There are many prophecies in the Hebrew Bible that foretell of this Majestic Messiah, the Suffering Servant. Many Jews today still do not believe that he was the Messiah, despite many prophecies suggesting otherwise. As Christians, we should pray for these people, who have rejected the One and Only Son (John 3:16). `For in that I speak to you Gentiles, inasmuch as I am the Apostle of the Gentiles, I magnify mine office, To try if by any means I might provoke them of my flesh to follow them, and might save some of them. For if the casting away of them be the reconciling of the world, what shall the receiving be, but life from the dead?` (Romans 11:13-15 GNV)",
        color=discord.Color.random())
    embed.set_thumbnail(url="http://www.talentshare.org/~mm9n/articles/Apostles_files/image007.jpg")
    embed.set_footer(text="Library | Yeshua", icon_url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
    await ctx.send(embed=embed)

@client.command()
async def motivation(ctx):
    responses = [
        "You can do this!", "No pain no gain. - Milk#1432, former developer of <",
        "It's win and learn; no losses.- Andy Mineo",
        "Tell me and I forget, teach me and I may remember, involve me and I learn. - Benjamin Franklin",
        "There are no uninteresting things, only uninterested people. - G.K. Chesterton",
        "The true soldier fights not because he hates what is in front of him, but because he loves what is behind him. - G.K. Chesterton",
        "Humility is not thinking less of yourself, but thinking of yourself less. - C.S. Lewis",
        "Free will, though it makes evil possible, is also the only thing that makes possible any love or goodness or joy worth having. - C.S Lewis",
        "You are the only Bible some unbelievers will ever read. - John MacArthur",
        "Is prayer your steering wheel or your spare tire? - Corrie ten Boom",
        "God doesn’t call us to be comfortable. He calls us to trust Him so completely that we are unafraid to put ourselves in situations where we will be in trouble if He doesn’t come through. - Francis Chan",
        "What you are is God’s gift to you, what you become is your gift to God. - Hans Urs von Balthasar",
        "The Christian shoemaker does his duty not by putting little crosses on the shoes, but by making good shoes, because God is interested in good craftsmanship. - Martin Luther",
        "His grace is cheapened when you think that He has only forgiven you of your sins up to the time you got saved, and after that point, you have to depend on your confession of sins to be forgiven. God’s forgiveness is not given in installments. - Joseph Prince",
        "Religion says, ‘I obey; therefore I am accepted.’ Christianity says, ‘I’m accepted, therefore I obey. -Timothy Keller",
        "Thou hast made us for thyself, O Lord, and our heart is restless until it finds its rest in thee. - St. Augustine of Hippo",
        "God loves each of us as if there were only one of us - St. Augustine",
        "The best thing about the future is that it comes only one day at a time. - Abraham Lincoln",
        "Your potential is the sum of all the possibilities God has for your life. - Charles Stanley",
        "We are all faced with a series of great opportunities brilliantly disguised as impossible situations. - Charles Swindoll",
        "Worry does not empty tomorrow of its sorrows; it empties today of its strength. - Corrie ten Boom",
        "God doesn't call us to be comfortable. He calls us to trust Him so completely that we are unafraid to put ourselves in situations where we will be in trouble if He doesn't come through. - Francis Chan",
        "Our greatest fear should not be of failure but of succeeding at things in life that don't really matter. - Francis Chan",
        "Success can come to a person who has failed, but it will never come to a person who quits - David Jeremiah"
    ]
    await ctx.send(random.choice(responses))


@client.command()
async def invite(ctx):
  embed21 = discord.Embed(title="Invite The Bot", description="[Invite Me!](https://discord.com/api/oauth2/authorize?client_id=854424955907473458&permissions=397351709763&scope=bot)", color=0x7fffd4)
  embed21.set_thumbnail(url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
  embed21.set_footer(text="Bot Invite", icon_url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
  await ctx.send(embed=embed21)


@client.command()
async def about(ctx):
    embed2 = discord.Embed(
        title="About This Bot",
        description=
        "This is a brand new bot coded by <@751556186548994149>. To learn more about this bot, dm him, and he will get to you as soon as he can! Also, we would appreciate it if you joined the support server [here.](https://discord.gg/z2RR4EvtaZ)",
        color=0x000033)
    embed2.add_field(name="Bot Version:", value="v. 1.2.0 Beta", inline=False)
    embed2.add_field(name="Date Version was Released:",
                     value="8/25/2021",
                     inline=False)
    embed2.set_footer(text="Misc Commands | About", icon_url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
    await ctx.send(embed=embed2)

#ping
@client.command()
async def ping(ctx):
    embedVar = discord.Embed(title="Pong",
                             description=":ping_pong:",
                             color=0x003366)
    embedVar.add_field(name="Latency",
                       value=str(round(client.latency * 1000)),
                       inline=False)
    embedVar.add_field(name="Support Server",
                       value="https://discord.gg/z2RR4EvtaZ",
                       inline=False)
    embedVar.add_field(name="Owners and Developers",
                       value="<@751556186548994149>",
                       inline=False)
    embedVar.add_field(name="Bot Version:", value="v.1.2.0", inline=False)
    embedVar.set_thumbnail(url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
    embedVar.set_footer(text="Misc Commands | Ping", icon_url="https://images-ext-1.discordapp.net/external/Nbi-FIZy5ReZHtLUhZvg5Ro_DHaSD4ufel2xHzmuL2Y/%3Fsize%3D256/https/cdn.discordapp.com/avatars/854424955907473458/00280a72d982788e18febb7418ec9d1f.png")
    await ctx.send(embed=embedVar)

keep_alive()
token = os.environ.get("TOKEN")
client.run(token)

token = os.environ.get("TOKEN")
client.run(token)