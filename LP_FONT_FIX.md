# Landing Page — フォントサイズ・可読性の修正

## Task
~/bg-growth-site/ のランディングページ（style.css, sample.css）のフォントサイズを全体的に見やすく修正してください。

## 問題点
- 大きい部分は大きすぎ、小さい部分は小さすぎてバランスが悪い
- 特に小さいテキストが読みにくい

## 修正ルール

### デスクトップ（641px以上）
- h1（ヒーローの見出し）: 48px
- h2（セクション見出し）: 32px
- h3（カード見出し）: 22px
- 本文テキスト（p）: 17px, line-height: 1.8
- サブテキスト・補足テキスト: 15px（14px以下にしない）
- ボタンテキスト: 16px
- ナビゲーション・フッター: 14px
- 最小フォントサイズ: 14px（これより小さいフォントは全て14pxに引き上げる）

### モバイル（640px以下）
- h1: 32px
- h2: 24px
- h3: 18px
- 本文テキスト: 16px, line-height: 1.7
- サブテキスト: 14px
- 最小フォントサイズ: 13px

### 追加の可読性改善
- letter-spacingが2px以上のテキストは1.5pxに下げる（読みにくいため）
- テキストの色のコントラストを確認。背景との差が弱いテキストがあれば色を明るくする
- 本文のfont-weightが300（Light）になっている箇所があれば400（Regular）に変更

## 対象ファイル
- style.css
- sample.css

## 確認方法
修正後、以下をブラウザで開いて確認:
open ~/bg-growth-site/index.html

## 完了後
git add -A && git commit -m "fix font sizes for readability" && git push
