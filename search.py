
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in source:
        print("{}が見つかりました".format(word))
    else:
        print("存在しません")
        source.append(word)
        print(source)
        with open ( 'source. csv' , 'a' ,encoding='UTF-8') as f :
            writer = csv . writer ( f )
            writer . writerow ( [source] )


if __name__ == "__main__":

    import csv
    with open('source.csv','r',encoding='UTF-8') as f :
        reader = csv.reader(f)
        for source in reader:
            search()