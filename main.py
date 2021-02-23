


def convert_to_int(question:str,min_val:int,max_val:int)->int:#指定された範囲内の整数を返す
    val=None
    while val==None:
        first_input=input(question)#最初に文字列で入力する

        try:
            to_int=int(first_input)#整数に変換 出来なかったら繰り返す

        except:
            print('整数で入力してください')

        else:
            if min_val<=to_int and to_int<=max_val:#指定された範囲内の時は繰り返し終了
                val=to_int

            else:#範囲外の時はメッセージを表示して繰り返し
                if to_int<min_val:
                    text=str(min_val)+'以上で入力してください'

                else:
                    text=str(max_val)+'以下で入力してください'

                print(text)

    return val



def coordinate_input(player_num:int):
    val=None
    while val==None:
        first_input=input('座標を入力してください','例：1,1,1').split(',')

        if len(first_input)==DIMENSION:#入力された座標が指定された次元かどうか
            pass

        else:
            print(str(DIMENSION)+'次元で入力してください')



if __name__=='__main__':
    DIMENSION=convert_to_int('何次元？',1,38)#何次元かを決める

    SIZE=convert_to_int('一辺の長さは？',3,36)#一辺の長さ（この数だけ1直線上に並ぶと勝ち）を決める

    TOTAL_GRID=SIZE**DIMENSION#すべてのマスの数

    PLAYER_COUNT=convert_to_int('何人で遊びますか？',1,TOTAL_GRID//SIZE)#プレイヤー数を決める プレイヤー数が多すぎると勝者がいなくなるので制限をかける

    player={}

    for i in range(PLAYER_COUNT):#プレイヤーの置いたマスを記録する辞書型
        player.setdefault(i,[])

    winner:int=None
    count=0

    while winner==None and count<TOTAL_GRID:#勝者が出るかますがすべて埋まるまで繰り返す
        count=count+1