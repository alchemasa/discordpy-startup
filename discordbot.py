from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

pine = ['ウルフウルフ、どこ？今登った、登った！',
'ウルフいた！ウルフ後ろ！',
'いやーもぅピネって奴ふざけんなよ！',
'お前出て行けよピネって奴よ！',
'ふざけんなよ…（小声）',
'はいうけるぅーピネうけるぅーやられてんのー',
'あれ、来て？お、来たウルフ、殺すよ、まず',
'えぇ？',
'またおんなじところにいるよ今',
'場所変える？ここにしよ！',
'ウルフどこ？ウルフここ',
'来てウルフ',
'来た、じゃヘッド',
'いやーピネってやつ死ねやホント！',
'ぁいたスカイ、あぁ、ウルフいた！登るよウルフのところ',
'登るよウルフのところ',
'マジか・・・',
'あ、殺さして、あ～ウザなによこいつまたピネだ！',
'ふざっけんなこいつ・・・次見たら殺す',
'ピネって奴ホントうざったい・・・',
'ピネって奴見かけたら即効犯す',
'来たピネ発見ピネ発見',
'うわウザピネって奴ふざけんなよこいつよぉ',
'ガン待ちゴルァ！',
'ピネっていうガン待ちホントウザイこいつ',
'いー↑ピネどしたーはいピネどしたー',
'はいピネどしたー',
'ピネってやつマジヘッドやらせろやカスコラおまえ殺スゾ',
'いやピネってやつホントウザくない？',
'おいピネってやつお前ふざけんなよ',
'お前通報するからな、捕まるよ',
'はーい通報ねはいはいどうぞやってくださーい',
'いやいーいーいーいーこれはもう通報しますねー',
'（FDって）誰？だれ？',
'不☆快☆感',
'殺さして殺さして殺さして',
'ありがとぅ！',
'あれ誰だこれ？',
'またピネだオラァ！　ピネってやつおかしい！',
'めっちゃウザイ！ピネってやつ',
'坂道発進しなくていいんだよ',
'SDさん殺さしてください！　ＳＤさんヘッドお願いします！',
'SDさんヘッドお願いします、いいですか？',
'またピネだ！またピネだぁ！',
'もうあいつ死ねやぁ！',
'もうあいつめっちゃうざい！ピネって奴！',
'もうピネってやつホントうざい',
'SDさんヘッドお願いします×2',
'SDさんやー',
'なんでよ・・・',
'なんでよ・・・うざい、だって',
'もうやらせてくれないんだもんこいつSDってやつ',
'またピネだこいつうざいピネって奴ぁ',
'俺もぅもぅもぅもう荒らすわ',
'いや～俺なんで毎回・・・うざいの？',
'俺撃たないようにしてんだよ前見えてるから、毎回撃たれんだもん',
'いやピネめっちゃうぜぇこいつ',
'カスコラ',
'FDさんFDさん後ろですよ殺さしてくださいFDさん',
'ありがとぅ kousei、ヘッドでやらせて？',
'いいよ',
'kouseiヘッド',
'は？',
'おいピネェ！',
'いやキモイぞカスいくせに絶対カスいよ俺とやったら',
'ってかこいつラピッドファイアつけてるよ',
'こいつめっちゃうぜぇな',
'ｳﾝ',
'ピネ抜けろピネ抜っけろ！',
'ピネぬっけろ！',
'どうせ日本人じゃねぇんだろ・・・（小声）',
'こいつ日本人やんしかも',
'こいつしかも日本人やん！',
'なんも通じねえのかコイツ日本人なのに',
'おぉ抜けた！・・・あぁ抜けてねえし',
'なんで抜けねえのよ・・・ピネってやつ',
'ドミネ行くの？',
'うん・・・',
'優しいこの人、マジで',
'ありがとうございます！',
'よろしくお願いします メールで送ったように',
'ここ来て下さいじゃあFDさんずっと',
'僕のこと殺していいんで',
'すいません！すいません！',
'殺さないでくれ！ゴメンね？',
'え？　俺もうね・・・逃げる。脱走するもう',
'あごめん！　間違えた俺・・・',
'おーい　FDさん？',
'来て下さーい',
'あと、２回は殺さしてください　ありがとうございます',
'おーFDさんボクのこと殺してイイッスヨ',
'いいすよ殺して。　シャキッと！',
'ありがとございます',
'ねえちょっと、みんな死んだらゴメンね',
'Mステあるから',
'いやぁ良かった',
'俺チンカスに・・・俺チンカスだった・・・',
'スカイさん殺していい？',
'スカイさん殺していい・・・？',
'スカイさーん？',
'殺していい？',
'ありがとう',
'誰だよ（食い気味）',
'ハンターキラー発射！',
'待ってください！F・・・なんだっけ？',
'スカイさんゴメン',
'おい！　あmasaさんか・・・',
'じゃいまからエレベーター行きますわ',
'殺していいすか？',
'ありがとー',
'マジっすこの人マジもうヤダ最高かわいい・・・///',
'うぉビックリしたぁ',
'あいざまーす',
'かっこいい！',
'あと１キルしたら僕のこと殺していいっすよ',
'俺があと１キルしたらじゃああと殺してください',
'あいがとざーまーす',
'殺していいっすよ',
'なんで？',
'FDさん',
'いいよ殺して！',
'はいおっけおっけ',
'はいチンカス乙',
'FDさん今から行きまーす',
'おいたいたいた',
'わーぁ眩しーいいよ殺して　おっけおっけありがとございまーす',
'はい、チンカス乙',
'FDさん後ろにいます！FDさん後ろ！　FDさん',
'FDさん後ろ！',
'おっけナイスです　FDさんここいます',
'殺しますよ？　ジャンプしてください',
'っ誰？　あ、スカイさん殺すよ？',
'お゛い゛ピネ゛ェ゛ェ゛！！',
'ピネ・・・',
'アハハ☆',
'あでもFDさんはねホントに神的にイイ人だから',
'ダメだFDさんは俺の・・・仲間だ',
'F・・・',
'んあ？・・・おぅ',
'痛って！　FDさんいいっすよもぅS2って奴殺していいっすよ',
'俺は殺しちゃダメッスS・・・',
'殺ねよマジSDおい！',
'ゴリラ',
'調子乗ってんじゃねーぞお前',
'あぁごめんなさいFDさんすいません！',
'ごめんなさいFDさん',
'SDかと思いましてほんとすいません',
'FDさん　殺していいっすか？',
'殺していいっすか？',
'あいがとございまーす',
'すげえFDさんホント分かってくれてるだって！',
'俺が『殺していいですか』だって',
'えー俺が殺したい　マジでお願い',
'ありがっとん♪',
'おーまっヤバい！',
'ﾔﾒﾃ、ﾔﾒﾃﾔﾒﾃﾔﾒﾃﾔﾒﾃﾔﾒﾃ・・・',
'あごめん、間違えて何か、押しちゃった',
'あ',
'ｵﾜﾁｬﾀﾖ',
'おい！ピネぇ！',
'FDさん本当ありがとね今度こｒ・・・あ！また殺してあげるから！',
'FDさんはホント神だから',
'調子のんなって',
'みんなでブーイングする？',
'えやだやだドミネ行くのヤダこのままでいい',
'え？',
'じゃ待て。じゃあこの人F・・・さん',
'やーやーじゃここはっぱ抜けよ抜けよ！',
'いいよ、抜け早く抜けろ',
'あぁｺﾞﾒﾝｺﾞﾒﾝｺﾞﾒﾝ',
'あｺﾞﾒﾝSD',
'SD？FD?（混乱）',
'う～わっ・・・',
'FDって人と、チャット、俺やんないよ？',
'なんなん？ジミー',
'おぉー強い！',
'これ終わったらドミノ行かない？',
'SDっていう人の後ろにいるよ',
'ﾎﾗ',
'いいよ',
'あいつ荒らしですよ',
'ピネと戦ってるよ今',
'早くコイや',
'ああ・・・wolf？',
'うーわ、コイツ・・・（小声）',
'FDさんを虐めた',
'ってことでドミネ行こう',
'ドミネ行こう？・・・ドミネ行こ？',
'kouseiふざけんなマジぃ～',
'調子こいてっとKO☆RO☆SU☆ZO',
'ﾌｯ',
'じゃ殺さないからフレ消すねって言ったらどうする？',
'ﾌﾌｯ',
'え、だってさっきお前・・・ｺﾛ・・・殺されたよ？',
'いやー場所ばれてるって変えよ、もう',
'お前キメーぞピネェ？',
'キーモいわもー',
'あーもイライラする',
'つまんねえ',
'あーもテンション上っちゃう',
'テンション上っちゃう・・・↓',
'いやドミネ行く',
'ドミネ行こうよ',
'ドミネ行こう？']
dodon = ['ウルフウルフ、どこ？今登った、登った！',
'ウルフいた！ウルフ後ろ！',
'いやーもぅピネって奴ふざけんなよ！',
'お前出て行けよピネって奴よ！',
'ふざけんなよ…（小声）',
'はいうけるぅーピネうけるぅーやられてんのー',
'あれ、来て？お、来たウルフ、殺すよ、まず',
'えぇ？',
'またおんなじところにいるよ今',
'場所変える？ここにしよ！',
'ウルフどこ？ウルフここ',
'来てウルフ',
'来た、じゃヘッド',
'いやーピネってやつ死ねやホント！',
'ぁいたスカイ、あぁ、ウルフいた！登るよウルフのところ',
'登るよウルフのところ',
'マジか・・・',
'あ、殺さして、あ～ウザなによこいつまたピネだ！',
'ふざっけんなこいつ・・・次見たら殺す',
'ピネって奴ホントうざったい・・・',
'ピネって奴見かけたら即効犯す',
'来たピネ発見ピネ発見',
'うわウザピネって奴ふざけんなよこいつよぉ',
'ガン待ちゴルァ！',
'ピネっていうガン待ちホントウザイこいつ',
'いー↑ピネどしたーはいピネどしたー',
'はいピネどしたー',
'ピネってやつマジヘッドやらせろやカスコラおまえ殺スゾ',
'いやピネってやつホントウザくない？',
'おいピネってやつお前ふざけんなよ',
'お前通報するからな、捕まるよ',
'はーい通報ねはいはいどうぞやってくださーい',
'いやいーいーいーいーこれはもう通報しますねー',
'（FDって）誰？だれ？',
'不☆快☆感',
'殺さして殺さして殺さして',
'ありがとぅ！',
'あれ誰だこれ？',
'またピネだオラァ！　ピネってやつおかしい！',
'めっちゃウザイ！ピネってやつ',
'坂道発進しなくていいんだよ',
'SDさん殺さしてください！　ＳＤさんヘッドお願いします！',
'SDさんヘッドお願いします、いいですか？',
'またピネだ！またピネだぁ！',
'もうあいつ死ねやぁ！',
'もうあいつめっちゃうざい！ピネって奴！',
'もうピネってやつホントうざい',
'SDさんヘッドお願いします×2',
'SDさんやー',
'なんでよ・・・',
'なんでよ・・・うざい、だって',
'もうやらせてくれないんだもんこいつSDってやつ',
'またピネだこいつうざいピネって奴ぁ',
'俺もぅもぅもぅもう荒らすわ',
'いや～俺なんで毎回・・・うざいの？',
'俺撃たないようにしてんだよ前見えてるから、毎回撃たれんだもん',
'いやピネめっちゃうぜぇこいつ',
'カスコラ',
'FDさんFDさん後ろですよ殺さしてくださいFDさん',
'ありがとぅ kousei、ヘッドでやらせて？',
'いいよ',
'kouseiヘッド',
'は？',
'おいピネェ！',
'いやキモイぞカスいくせに絶対カスいよ俺とやったら',
'ってかこいつラピッドファイアつけてるよ',
'こいつめっちゃうぜぇな',
'ｳﾝ',
'ピネ抜けろピネ抜っけろ！',
'ピネぬっけろ！',
'どうせ日本人じゃねぇんだろ・・・（小声）',
'こいつ日本人やんしかも',
'こいつしかも日本人やん！',
'なんも通じねえのかコイツ日本人なのに',
'おぉ抜けた！・・・あぁ抜けてねえし',
'なんで抜けねえのよ・・・ピネってやつ',
'ドミネ行くの？',
'うん・・・']
kousei = [
'優しいこの人、マジで',
'ありがとうございます！',
'よろしくお願いします メールで送ったように',
'ここ来て下さいじゃあFDさんずっと',
'僕のこと殺していいんで',
'すいません！すいません！',
'殺さないでくれ！ゴメンね？',
'え？　俺もうね・・・逃げる。脱走するもう',
'あごめん！　間違えた俺・・・',
'おーい　FDさん？',
'来て下さーい',
'あと、２回は殺さしてください　ありがとうございます',
'おーFDさんボクのこと殺してイイッスヨ',
'いいすよ殺して。　シャキッと！',
'ありがとございます',
'ねえちょっと、みんな死んだらゴメンね',
'Mステあるから',
'いやぁ良かった',
'俺チンカスに・・・俺チンカスだった・・・',
'スカイさん殺していい？',
'スカイさん殺していい・・・？',
'スカイさーん？',
'殺していい？',
'ありがとう',
'誰だよ（食い気味）',
'ハンターキラー発射！',
'待ってください！F・・・なんだっけ？',
'スカイさんゴメン',
'おい！　あmasaさんか・・・',
'じゃいまからエレベーター行きますわ',
'殺していいすか？',
'ありがとー',
'マジっすこの人マジもうヤダ最高かわいい・・・///',
'うぉビックリしたぁ',
'あいざまーす',
'かっこいい！',
'あと１キルしたら僕のこと殺していいっすよ',
'俺があと１キルしたらじゃああと殺してください',
'あいがとざーまーす',
'殺していいっすよ',
'なんで？',
'FDさん',
'いいよ殺して！',
'はいおっけおっけ',
'はいチンカス乙',
'FDさん今から行きまーす',
'おいたいたいた',
'わーぁ眩しーいいよ殺して　おっけおっけありがとございまーす',
'はい、チンカス乙',
'FDさん後ろにいます！FDさん後ろ！　FDさん',
'FDさん後ろ！',
'おっけナイスです　FDさんここいます',
'殺しますよ？　ジャンプしてください',
'っ誰？　あ、スカイさん殺すよ？',
'お゛い゛ピネ゛ェ゛ェ゛！！',
'ピネ・・・',
'アハハ☆',
'あでもFDさんはねホントに神的にイイ人だから',
'ダメだFDさんは俺の・・・仲間だ',
'F・・・',
'んあ？・・・おぅ',
'痛って！　FDさんいいっすよもぅS2って奴殺していいっすよ',
'俺は殺しちゃダメッスS・・・',
'殺ねよマジSDおい！',
'ゴリラ',
'調子乗ってんじゃねーぞお前',
'あぁごめんなさいFDさんすいません！',
'ごめんなさいFDさん',
'SDかと思いましてほんとすいません',
'FDさん　殺していいっすか？',
'殺していいっすか？',
'あいがとございまーす',
'すげえFDさんホント分かってくれてるだって！',
'俺が『殺していいですか』だって',
'えー俺が殺したい　マジでお願い',
'ありがっとん♪',
'おーまっヤバい！',
'ﾔﾒﾃ、ﾔﾒﾃﾔﾒﾃﾔﾒﾃﾔﾒﾃﾔﾒﾃ・・・',
'あごめん、間違えて何か、押しちゃった',
'あ',
'ｵﾜﾁｬﾀﾖ',
'おい！ピネぇ！',
'FDさん本当ありがとね今度こｒ・・・あ！また殺してあげるから！',
'FDさんはホント神だから',
'調子のんなって',
'みんなでブーイングする？',
'えやだやだドミネ行くのヤダこのままでいい',
'え？',
'じゃ待て。じゃあこの人F・・・さん',
'やーやーじゃここはっぱ抜けよ抜けよ！',
'いいよ、抜け早く抜けろ']
sky = ['あぁｺﾞﾒﾝｺﾞﾒﾝｺﾞﾒﾝ',
'あｺﾞﾒﾝSD',
'SD？FD?（混乱）',
'う～わっ・・・',
'FDって人と、チャット、俺やんないよ？',
'なんなん？ジミー',
'おぉー強い！',
'これ終わったらドミノ行かない？',
'SDっていう人の後ろにいるよ',
'ﾎﾗ',
'いいよ',
'あいつ荒らしですよ',
'ピネと戦ってるよ今',
'早くコイや',
'ああ・・・wolf？',
'うーわ、コイツ・・・（小声）',
'FDさんを虐めた',
'ってことでドミネ行こう',
'ドミネ行こう？・・・ドミネ行こ？']
wolf = ['kouseiふざけんなマジぃ～',
'調子こいてっとKO☆RO☆SU☆ZO',
'ﾌｯ',
'じゃ殺さないからフレ消すねって言ったらどうする？',
'ﾌﾌｯ',
'え、だってさっきお前・・・ｺﾛ・・・殺されたよ？',
'いやー場所ばれてるって変えよ、もう',
'お前キメーぞピネェ？',
'キーモいわもー',
'あーもイライラする',
'つまんねえ',
'あーもテンション上っちゃう',
'テンション上っちゃう・・・↓',
'いやドミネ行く',
'ドミネ行こうよ',
'ドミネ行こう？']

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

@client.event
async def on_message(message):
    if message.author.bot:
        return
	if message.content == '/pine':
        await message.channel.send(random.choice(pine))
        return
    if message.content == '/kousei':
        await message.channel.send(random.choice(kousei))
        return
    if message.content == '/dodon':
        await message.channel.send(random.choice(dodon))
        return
    if message.content == '/wolf':
        await message.channel.send(random.choice(wolf))
        return
    if message.content == '/sky':
        await message.channel.send(random.choice(sky))
        return

bot.run(token)
