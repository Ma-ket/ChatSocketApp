## user_addrの取り扱い
```
>>> print(f"a: {a}\nb: {b}\nc: {c}\nd: {d}\ne: {e}")
a: {'A': (1, [10, 20, 30])}
b: (1, [10, 20, 30])
c: [10, 20, 30]
d: 1
e: A
```

## gitの使い方メモ
### カレントディレクトリ内の変更点とステージング
```
$ git add .
```

### コミット
```
$ git commit -m "<メッセージ内容>"
```

### 変更点残したままbranchを移動したい
こんな感じのエラー
```
$ git checkout <branch名>
error: Your local changes to the following files would be overwritten by checkout:
	ファイル
Please commit your changes or stash them before you switch branches.
Aborting
```
消したくないし、手動で覚えるのも嫌。
そこで、保存機能がある。stashである。
[【git stash】コミットはせずに変更を退避したいとき](https://qiita.com/chihiro/items/f373873d5c2dfbd03250)
```
$ git stash -u
```
そのままcheckout

### stashの中から取り出す
```
$ git stash list
```
で確認
```
# リストの中身消さない
$ git stash apply stash@{0}
or
# リストの中身消す
$ git stash pop statsh@{0}
```

### 作業を退避するときにメッセージをつける
```
$ git stash save "<メッセージの内容>"
```
