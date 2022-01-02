# everyone_smile
全員が笑顔の写真を抽出するプログラムです。  
判定したい写真の入ったフォルダと移動先のフォルダを選択すると、  
全員が笑顔の写真だけを移動先のフォルダに移動させます。

## how to use
1. Azure Face APIの登録。キーとエンドポイントを取得。
2. .envファイルの作成
3. .envファイルに以下の記述を追加
```
CONGNITIVE_SERVICE_KEY=[Azure Face APIのキー]
CONFNITIVE_SERVICE_ENDPOINT=[Azure Face APIのエンドポイント]
```
4. ```python3 main.py```で実行。
5. 判定対象のフォルダと移動先のファイル選択。
