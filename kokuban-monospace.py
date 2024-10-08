from random import choice

import math
import os
import sys

from fontTools.ttLib import TTFont

FONT_NAME = "KokubanMonospace"

def random_letters(n):
    return ''.join(choice('abcdefghijklmnopqrstuvwxyz') for _ in range(n))

def create_html_demo(input_path: str):
    bg = "#1c2523"
    fg = "#e7dcc4"
    size = 16
    realwidth = size * (5/10)

    custom_font = "CustomFont-" + random_letters(8)

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Monospace Font Demo</title>
        <meta charset="UTF-8">
        <style>
            @font-face {{
                font-family: "{custom_font}";
                src: url("{input_path}");
            }}
            body {{
                font-family: "{custom_font}";
                max-width: 100vw;
                color: {fg};
                background-color: {bg};
            }}

            p {{
                white-space: pre-wrap;
                overflow-wrap: break-word;
                margin: 0;
                font-size: {size}px;
            }}

            .boxed-text {{
                border: 1px solid red;
                background-image: repeating-linear-gradient(90deg, {bg}, {bg} {realwidth-1}px, red {realwidth}px);
            }}

        </style>
    </head>
    <body>
        <p>The quick brown fox jumps over the lazy dog</p>
        <p>あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん</p>
        <p>アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン</p>
        <p>漢字勉強日本東京大阪学校先生生徒自然雨空海山木花家車電車飛行機時間お金水火風美術音楽仕事努力成功失敗機会経験友達家族動物食べ物飲み物本読書書道歴史世界社会環境健康</p>
        <p>今日は晴れているので公園に行って読書をしようと思います。最近仕事が忙しくてなかなかリラックスする時間が取れなかったので、久しぶりに自然の中で過ごせるのが楽しみです。公園には大きな木や花が咲いていて、鳥のさえずりが聞こえてとても心地よいです。</p>
        <p>{random_letters(255)}</p>
        <p>昨日は友達とオンラインで話しながらゲームをしましたが、思ったよりも盛り上がってしまい、気づいたら夜遅くまで遊んでしまいました。今日のミーティングはオンラインで行います。Let's discuss the new project timeline and make sure we are all on the same page before moving forward.プロジェクトの進捗状況についてもしっかりと確認しておきたいです。</p>
        <p>
            (.venv) {13:29}~/Code/font-playground ➭ cat ~/notes/project_compare.md
            ### 従来の開発プロセス
            1. 案件が出る
            2. 要件定義
            3. AIと製品のPoC
            4. 本番製品
                - AIを整える
                -
            (.venv) {13:29}~/Code/font-playground ➭ python monospacer.py KleeOne-Regular.ttf
            KleeOne-Monospace-Regular.ttf
            (.venv) {13:31}~/Code/font-playground ➭ python monospacer.py KleeOne-Regular.ttf
            KleeOne-Monospace-Regular.ttf
            (.venv) {13:32}~/Code/font-playground ➭
        </p>
        <p>
            プログラミング言語を設計していて、リストの先頭 (最初の要素) を返す head関数を提供したいとします。3つのオプションを検討できます。
       </p>
       <p>
abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん
アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン
abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
漢字勉強日本東京大阪学校先生生徒自然雨空海山木花家車電車飛行機時間お金水火風美術音楽仕事努力成功失敗機会経験友達家族動物食べ物飲み物本読書書道歴史世界社会環境健康
ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ
       </p>
       <p class="boxed-text">
abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん
アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン
abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
漢字勉強日本東京大阪学校先生生徒自然雨空海山木花家車電車飛行機時間お金水火風美術音楽仕事努力成功失敗機会経験友達家族動物食べ物飲み物本読書書道歴史世界社会環境健康
`~1234567890!@#$%^&*(),./;'[]-=<>?:"{{}}_+\\|1234567890!@#$%^&*(),./;'[]-=<>?:"{{}}_+\\|1234567890!@#$%^&*(),./;'[]-=<>?:"{{}}_+\\|1234567890!@#$%^&*(),./;'[]-=<>?:"{{}}_+\\|
ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ
           AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCbcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz
       </p>
       <p>fifififififlflflflflflflflfififififi. field flop floor fire</p>
       <p>
           abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
           ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ
           `~1234567890!@#$%^&*(),./;'[]-=<>?:"{{}}_+\\|1234567890!@#$%^&*(),./;'[]-=<>?:"{{}}_+\\|1234567890!@#$%^&*(),./;'[]-=<>?:"{{}}_+\\|1234567890!@#$%^&*(),./;'[]-=<>?:"{{}}_+\\|
ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ
           AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCbcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz

            多くのプログラミング言語で見られる最初のオプションは、空のリストが与えられた場合に例外を発生させることです。Elixirでの実装は次のようになります。
            $ list(a) -> a
            def head([head | _]), do: head
            def head([]), do: raise "empty list"
            型システムは空のリストと空でないリストを区別できないため、コンパイル時には型違反は検出されませんが、空のリストの場合は実行時にエラーが発生します。
There are two sum functions: the first is called with an empty list, and the sum of an empty list is 0. The second is called when the list is not empty. The list is decomposed in head and tail, and a recursive call is executed to add the value of the head to the sum of the rest of the list.
            別の方法としては、関数が失敗する可能性がある (または失敗しない可能性がある) ことを適切にエンコードして、オプション型を返す方法があります。
            $ list(a) -> option(a)
            def head([head | _]), do: {{:ok, head}}
            def head([]), do: :none
            このアプローチは少し冗長かもしれません。オプション型を返すと、基本的に呼び出し元は返されたオプションに対してパターンマッチを行う必要があります。多くのプログラミング言語ではオプション値を構成する関数が提供されていますが、追加のラップを取り除いて、代わりにリストに対して直接パターンマッチを行うこともできます。つまり、次のコードの代わりに、次のように記述できます。
The Enum.reduce function receives the enumerable list to work with, and for every element of the list, it calls the function passed as the second parameter. This function receives the current value and an accumulator (the result of the previous iteration). So, to sum all the values, it just needs to add to the accumulator the current value.
            case head(list) do
              {{:ok, head}} -> # ヘッドがあります
              :none -> # 必要な処理を行います
            end
            次のように記述できます。

            case list do
              [head | _] -> # ヘッドがあります
              [] -> # 必要な処理を行います
            end
            上記の両方の例は、型システムが空のリストと空でないリストを区別できないため、実行時に処理する必要があるという制限があります。この制限を取り除けば、headを次のように定義できます。


            $ non_empty_list(a) -> a
            def head([head | _]), do: head
        </p>
    </body>
    </html>
    """

    with open("demo.html", "w") as f:
        f.write(html)


def make_font_monospace(input_path, lxgw_path, output_path):
    font = TTFont(input_path)
    lxgw = TTFont(lxgw_path)

    #####
    print("get resources")
    hmtx = font["hmtx"].metrics
    post = font["post"]
    glyf = font["glyf"]
    name = font["name"]
    gsub = font["GSUB"].table

    lxgw_hmtx = lxgw["hmtx"].metrics
    lxgw_glyf = lxgw["glyf"]

    ####
    print("lxgw swap")

    #for gl in to_swap:
    for gl in lxgw_glyf.keys():
        if gl[:3] != "uni" and gl in glyf:
            glyf[gl] = lxgw_glyf[gl]

    #####
    print("set general font metrics")

    # make monospace
    rw = 500 # roman character width
    jw = 1000 # japanese character width
    for gl, (width, lsb) in hmtx.items():
        if gl[:3] != "uni":
            hmtx[gl] = (rw, lsb)
        else:
            hmtx[gl] = (jw, lsb)

    #####
    print("specific letter customizations")

    ## remove letter combo ligatures (fi, fl, etc)
    lookups = gsub.LookupList.Lookup
    ligature_subst = next(lookups[16].iterSubTables()).value
    ligatures = ligature_subst.ligatures
    ligatures.pop('f')

    gl = "A"
    hmtx[gl] = (rw, 30)

    gl = "l"
    hmtx[gl] = (rw, 40)

    gl = "m"
    hmtx[gl] = (rw, 35)

    gl = "parenleft"
    hmtx[gl] = (rw, 140)

    gl = "parenright"
    hmtx[gl] = (rw, 100)

    gl = "braceright"
    hmtx[gl] = (rw, 100)

    gl = "bracketright"
    hmtx[gl] = (rw, 100)

    gl = "hyphen"
    hmtx[gl] = (rw, 110)

    gl = "question"
    hmtx[gl] = (rw, -30)

    gl = "colon"
    hmtx[gl] = (rw, 180)

    gl = "semicolon"
    hmtx[gl] = (rw, 50)

    gl = "less"
    hmtx[gl] = (rw, -10)

    gl = "greater"
    hmtx[gl] = (rw, -10)

    gl = "degree"
    hmtx[gl] = (rw, 250)


    ####
    print("set namerecords")
    original_font_name, variant_ext = output_path.split("-")
    font_name = FONT_NAME
    variant, ext = variant_ext.split(".")

    print(font_name)
    print(output_path)

    name.setName(font_name,                            1, 3, 1, 0x409)
    name.setName(font_name,                            1, 3, 1, 0x411)
    name.setName(f"1.1000;FWKS;{font_name}-{variant}", 3, 3, 1, 0x409)
    name.setName(f"{font_name} {variant}",             4, 3, 1, 0x409)
    name.setName(f"{font_name} {variant}",             4, 3, 1, 0x411)


    #####
    print("set monospace flag")
    post.isFixedPitch = 1

    #####
    print("save font")
    font.save(output_path)


if __name__ == "__main__":
    input_path = sys.argv[1]
    lxgw_path = sys.argv[2]

    font_filename = os.path.basename(input_path)
    original_font_name, variant_ext = font_filename.split("-")
    font_name = FONT_NAME
    output_path = f"{font_name}-{variant_ext}"

    print(output_path)

    make_font_monospace(input_path, lxgw_path, output_path)
    create_html_demo(output_path)
