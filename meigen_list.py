import random
import json


def futsukin_meigen():  # ふつきん名言を抽出
    per = random.randint(1, 100)  # UR2個 - SSR5個 - SR9個 - R18個 - N30個

    if 1 <= per <= 50:  # N 50%
        num = random.randint(10000, 10030)
        point = 5
    elif 51 <= per <= 80:  # R 28%
        num = random.randint(1000, 1020)
        point = 4
    elif 80 <= per <= 94:  # SR 15%
        num = random.randint(100, 109)
        point = 3
    elif 94 <= per <= 99:  # SSR 6%
        num = random.randint(10, 14)
        point = 2
    else:  # UR 1%
        num = random.randint(0, 1)
        point = 1

    if num == 0:
        saw = "**```css\n[UR] ふつきん『アイコンで全てを決めるな!』```**\n" \
              "http://livedoor.blogimg.jp/ren_yster/imgs/e/b/eb1b820e.jpg"
    elif num == 1:
        saw = "**```css\n[UR] ふつきん『チーム戦というのはやっている者同士が楽しめたらそれでいいのよ\n勝ち負けは二の次だと私は思ってる\n" \
              "今日は負けてしまったけど、その悔しさを次に生かして頑張ろうと思えればそれでいいのよ(オカマ風)』\n" \
              "https://twitter.com/futsukin_mk/status/461145986329370625```**"
    elif num == 10:
        saw = "そんなことはないで♪"
    elif num == 11:
        saw = "ハングオンがやりづらいのは万国共通!"
    elif num == 12:
        saw = "top5!!!!!!!\n〇〇(top5じゃなかった人)さんかなり展開きつそうだったね(ﾆﾔﾆﾔ)"
    elif num == 13:
        saw = "「よろしくお願いします」も言わずに「当たれ」はNG\nhttps://twitter.com/HiRy_toki/status/634005340065959937"
    elif num == 14:
        saw = "ラインを縫っていくイメージ\nhttp://futsugeorgeoretachi.blog.fc2.com/blog-entry-375.html"
    elif num == 100:
        saw = "こんなやつの為に自分が有り金はたいて買ったコントローラーを投げて壊すのは勿体ない"
    elif num == 101:
        saw = "(気持ち的な意味で)たまんねぇな～"
    elif num == 102:
        saw = "展開が良い人が前をミスしないように走って、悪かった人は落ちたなりに場を作ったりやれる事をすればいいだけの話だと思います\n" \
              "個人点はあくまで結果しか示しませんから、その過程が大事よ"
    elif num == 103:
        saw = "けつがラグいですね～"
    elif num == 104:
        saw = "こっちはリングやぞぉ！！！TAが足りねぇんじゃねぇのかぁ！！！？"
    elif num == 105:
        saw = "あぁ即投げありがとう(笑)、頭悪いねｗ"
    elif num == 106:
        saw = "無いのなら\n\t\t\t\t  開いて見せよう\n\t\t\t\t\t\t マリカ模擬"
    elif num == 107:
        saw = "アイコン的に一生ネタにされ続けられる運命にあるのかなー"
    elif num == 108:
        saw = "フフ～モテるモテるぅ～"
    elif num == 109:
        saw = "こういう苦しい環境で苦難を共にしてこそ本心をさらけ出せるんだよ"
    elif num == 1000:
        saw = "名言なんて考えて言うもんじゃないから(ドヤ顔)"
    elif num == 1001:
        saw = "ハング嫌いだなー..."
    elif num == 1002:
        saw = "バックスパム!"
    elif num == 1003:
        saw = "1位で引く赤は美味しいねぇ～"
    elif num == 1004:
        saw = "行けるぞ!諦めるな!!男だぞ!!!"
    elif num == 1005:
        saw = "ハングオン使い「下位潰しは俺らに任せろ!」"
    elif num == 1006:
        saw = "時が経てば人は変わるもの"
    elif num == 1007:
        saw = "自分が居なくても大丈夫だお＾。＾"
    elif num == 1008:
        saw = "(無意味な)停止赤して「俺活躍してるぜ!!!!!」って思わせておけば良いのよ"
    elif num == 1009:
        saw = "Twitter裏垢で嫌だとかラグイとか散々愚痴ってるくせに、そのところにわざわざ来るとかツンデレかよ"
    elif num == 1010:
        saw = "自分に手出すのは別に良いが、俺の仲間(だち)に手出したら許さんからな"
    elif num == 1011:
        saw = "個人名を挙げるな！！"
    elif num == 1012:
        saw = "寝落ちしたら首締め上げるぞ！この野郎！！"
    elif num == 1013:
        saw = "Tomsu最近誘ってくれてるのに断ってばかりだから、断ろう"
    elif num == 1014:
        saw = "スバラシイコォォォォーーース"
    elif num == 1015:
        saw = "自分のトーク力を発揮する時が来たか"
    elif num == 1016:
        saw = "今年入って一番泣きました。"
    elif num == 1017:
        saw = "右足の小指がががああああああああ！！！"
    elif num == 1018:
        saw = "FB投げる前にTAしろよ"
    elif num == 1019:
        saw = "点取っただけでbroとかbro安売りすんなよ。薄っぺらいの分かってんだよ"
    elif num == 1020:
        saw = "ラウンジは真のbroを見つける旅だから。クズはクズ"
    elif num == 10000:
        saw = "もっと情熱的になれ!!"
    elif num == 10001:
        saw = "棘受けは男の宿命"
    elif num == 10002:
        saw = "エキサイティングじゃねーよ、コラー(怒)"
    elif num == 10003:
        saw = "誰かが倒れた時は誰かがカバー出来ればそれでええんやで"
    elif num == 10004:
        saw = "ハンドルのゴーストは参考にならない"
    elif num == 10005:
        saw = "首締め上げてやろうか、この野郎!!"
    elif num == 10006:
        saw = "ありのままの姿が一番いい!"
    elif num == 10007:
        saw = "生半可な気持ちで真似されたら困る、真似るなら徹底的に真似ろ！"
    elif num == 10008:
        saw = "覚えていないので大丈夫でしゅよ"
    elif num == 10009:
        saw = "昨日の今日で忘れるな"
    elif num == 10010:
        saw = "ハングに刺受けさせるな"
    elif num == 10011:
        saw = "負けた時に立ち直るのが大事なんだよ"
    elif num == 10012:
        saw = "出会いがあれば別れもある"
    elif num == 10013:
        saw = "集計ツイ(遂)にあげますね"
    elif num == 10014:
        saw = "スリックはゴミ"
    elif num == 10015:
        saw = "人はいつ何時も学び成長してゆくもの、その心が大事"
    elif num == 10016:
        saw = "Nightは抜かさ「ないと」"
    elif num == 10017:
        saw = "最後ぐらい漢にならないと、乙女にはなりたくない"
    elif num == 10018:
        saw = "いいよ、いちいち「お疲れ様でした」とか言わなくてよ(怒)"
    elif num == 10019:
        saw = "即投げすんな脳無し"
    elif num == 10020:
        saw = "おいテメェ個人点意識でやってんじゃねぇよ"
    elif num == 10021:
        saw = "即投げする人間には即投げしないとなぁ"
    elif num == 10022:
        saw = "無視されたからチーム作ったんだよ！"
    elif num == 10023:
        saw = "それこそ名言に入れろよ、コロスゾ"
    elif num == 10024:
        saw = "K4Iさん絶対下位(K4I)取らないぞ"
    elif num == 10025:
        saw = "ハーゲンダッツのクッキークリームを食べたことないのは人生損してる"
    elif num == 10026:
        saw = "殺るぞ"
    elif num == 10027:
        saw = "まだまだこれからだぜ～～！！！！！"
    elif num == 10028:
        saw = "だーく『そんな日もある。』"
    elif num == 10029:
        saw = "お喋りのエンジンかけるわ"
    elif num == 10030:
        saw = "バカは死んで生まれないと直んないから"
    else:
        saw = None

    if point == 2:
        return "**```css\n[SSR] ふつきん『" + saw + "』```**"
    elif point == 3:
        return "**```ini\n[SR] ふつきん『" + saw + "』```**"
    elif point == 4:
        return "**```ini\n[R] ふつきん『" + saw + "』```**"
    elif point == 5:
        return "**```ini\n[N] ふつきん『" + saw + "』```**"
    else:
        return saw


def syuzo_meigen():  # 修造名言を選出
    num = random.randint(1, 35)
    if num == 1:
        saw = "何言ってんだよ！！ その崖っぷちが最高のチャンスなんだぜ！！\n自分の全ての力を出し切れるんだから！！！\n崖っぷちありがとう！！ 最高だぁぁぁぁぁぁぁ！！！！"
    elif num == 2:
        saw = "諦めんなよ！諦めんなよ、お前！！\nどうしてそこでやめるんだ、そこで！！  " \
              "もう少し頑張ってみろよ！\nダメダメダメ！諦めたら！\n周りのこと思えよ、応援してる人たちのこと思ってみろって！\nあともうちょっとのところなんだから！\n" \
              "俺だってこのマイナス10度のところ、しじみがトゥルルって頑張ってんだよ！\nずっとやってみろ！必ず目標を達成できる！\nだからこそNever Give Up！！ "
    elif num == 3:
        saw = "一番になるっつったよな？ ナンバー1になるっつったよな！？\nまずは、形から入ってみろよ！\n今日からお前は！！一番だ！！！"
    elif num == 4:
        saw = "100回叩くと壊れる壁があったとする。\nでもみんな何回叩けば壊れるかわからないから、90回まで来ていても途中であきらめてしまう。"
    elif num == 5:
        saw = "本気になれば自分が変わる！ 本気になれば全てが変わる！！"
    elif num == 6:
        saw = "過去のことを思っちゃダメだよ。何であんなことしたんだろ・・・って怒りに変わってくるから。\n未来のことも思っちゃダメ。大丈夫かな、あはぁ～ん。\n不安になってくるでしょ？\n" \
              "ならば、一所懸命、一つの所に命を懸ける！\nそうだ！ 今ここを生きていけば、みんなイキイキするぞ！！ "
    elif num == 7:
        saw = "一番になるっていったよな？ 日本一なるっつったよな！\nぬるま湯なんかつかってんじゃねぇよお前！！\n今日からお前は！富士山だ！！"
    elif num == 8:
        saw = "言い訳してるんじゃないですか？ できないこと、無理だって、諦めてるんじゃないですか？\n駄目だ駄目だ！ あきらめちゃだめだ！\nできる！ できる！ 絶対にできるんだから！"
    elif num == 9:
        saw = "よく、時間が解決してくれると言うけれど、そうは思わない。\nでも、行動した時間なら解決してくれるはずだ。"
    elif num == 10:
        saw = "予想外の人生になっても、そのとき、幸せだったらいいんじゃないかな"
    elif num == 11:
        saw = "人の弱点を見つける天才よりも、人を褒める天才がいい"
    elif num == 12:
        saw = "褒め言葉よりも苦言に感謝"
    elif num == 13:
        saw = "強い心を持つ そのためには 心の根  しっかりした根っこを作り上げることだ\nほら！　見てください　お米の苗\nこれ…見てよ　根っこですよこれ全部\n" \
              "力強いよね～　台風が来たり　大雨が来たりしても  この根っこがあれば絶対負けないよね\nそうだよ！　お前もこの苗のように強い根っこを持て!　出来るよ！\nお米食べろ！！"
    elif num == 14:
        saw = "プレッシャーを感じられることは幸せなことだ"
    elif num == 15:
        saw = "人は完璧を求める。\nしかし、完璧だと思った時から全てがやり直しとなる。"
    elif num == 16:
        saw = "暑くなければ夏じゃない。熱くなければ人生じゃない！"
    elif num == 17:
        saw = "何かを認識してやってみることが「体験」\nその体験を二度三度重ねていくことで「経験」になっていく"
    elif num == 18:
        saw = "最初から何でも考えることが出来る人がいる\nでも、僕にはなかなかそれが出来ない\nだとしたら、努力によってつかむしかない"
    elif num == 19:
        saw = "もっと熱くなれよ 熱い血燃やしてけよ！\n- 人間熱くなった時が本当の自分に出会えるんだ！！\n- だからこそもっと熱くなれよおぉぉぉぉぉぉぉぉぉぉぉぉぉぉぉぉ！！！！！！"
    elif num == 20:
        saw = "眉間に皺を寄せていたところで怪我が早く治るわけでもない\nむしろ、明るく危機を受け止める姿勢にこそ早く治るきっかけがある"
    elif num == 21:
        saw = "弱気になったとき まず一ヵ月後の自分を想像してみる\nそれが自分の好きな姿だとしたら、そのために何をするべきかを考える\n" \
              "そうすれば、少なくともその日までは目的意識を保ち続けることができる"
    elif num == 22:
        saw = "気にすんなよ。くよくよすんなよ。\n大丈夫、どうにかなるって。\nDon't worry！ Be happy！"
    elif num == 23:
        saw = "ミスをすることは悪いことじゃない\nそれは上達するためには必ず必要なもの\nただし、同じミスはしないこと"
    elif num == 24:
        saw = "みんな！！竹になろうよ\n竹ってさあ台風が来てもしなやかじゃない\n台風負けないんだよ 雪が来てもね おもいっきりそれを跳ね除ける！！力強さがあるんだよ\n" \
              "そう、みんな！！！竹になろう！！！バンブー！！！"
    elif num == 25:
        saw = "泥まみれに生きるってかっこ悪いと思ってるんじゃないですか？\n見てくださいよ生き生きしてるよ！！\n自分らしさを感じられるよ！！\n泥んこばんざーーーい！！\nありがとうっ！！"
    elif num == 26:
        saw = "綺麗だよね…。輝っいてるよね。\nこの川のように、君の心もピュアだったじゃねーかよ！\nなんだよ…欲ばかり…。嫉妬、悪口　自分のことばっか考えてんじゃねぇか？\n" \
              "そんなのすべて洗い流しちゃえ！\n変われるよ…。そうすればこの川のように、みんなは君の思いを…飲み込んでくれるさ。\n自然が一番！"
    elif num == 27:
        saw = "偶然にもうまく使えたように見えるアイテム。\nしかし、僕にとっては何千回と練習をしたうちの1つだ。"
    elif num == 28:
        saw = "勝敗を分けるのはいつでもたった1つのアイテムだ。\nだが、プレーをしているときは、どれがその1つか分からない。"
    elif num == 29:
        saw = "一所懸命生きていれば、不思議なことに疲れない。"
    elif num == 30:
        saw = "何よりも大切なのは、あなた自身がどうしたいかだ。"
    elif num == 31:
        saw = "心の底から好きなことに本気で取り組めるなら、それは幸せ。"
    elif num == 32:
        saw = "勝ち負けなんか、ちっぽけなこと。\n大事なことは、本気だったかどうかだ！"
    elif num == 33:
        saw = "真剣に考えても、深刻になるな！"
    elif num == 34:
        saw = "悔しがればいい、泣けばいい、喜べばいい。\nそれが人間だ！"
    elif num == 35:
        saw = "君が次に使うアイテム1つで、壁は打ち破れるかもしれないんだ！"
    else:
        saw = None

    return "**```diff\n- " + saw + "```**"
