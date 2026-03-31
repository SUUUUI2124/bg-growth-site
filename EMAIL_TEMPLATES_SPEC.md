# メールアウトリーチ準備 — メールテンプレートのHTMLツール作成

## Task
~/bg-growth-site/email-templates.html を作成してください。
これはBOSS自身がメール送信時に参照するためのページ。公開リンクは貼らない。

## デザイン
- ダークアカデミアスタイル（現在のindex.htmlと統一）
- 各テンプレートがカード形式で表示
- 「Copy」ボタンをクリックするとテンプレート本文がクリップボードにコピーされる

## テンプレート4種類

### Template 1: 初回メール
件名: quick idea for [name]'s brand

本文:
hi [name],

this might seem out of the blue but I was genuinely impressed by what you've built on instagram. [1行のカスタム褒めポイント]

i run a small growth marketing service where we help creators launch digital products — and i actually went ahead and built a free monetisation gameplan specifically for your brand. real numbers, real strategy.

here's what a sample looks like: https://suuuui2124.github.io/bg-growth-site/sample.html

yours would be fully customized to your content and audience. want me to send it over? no cost, no strings.

best,
BG Growth
boss.growth67@gmail.com

### Template 2: フォローアップメール（5日後）
件名: re: quick idea for [name]'s brand

本文:
hi [name],

just following up on my last email — i built a free monetisation gameplan for your brand and would love to share it.

quick overview of what's inside:
- audience audit with engagement analysis
- 3 revenue scenarios based on your actual numbers
- custom product suggestion for your niche
- 14-day launch strategy

sample: https://suuuui2124.github.io/bg-growth-site/sample.html

no cost, no strings. just thought it could be valuable.

best,
BG Growth

### Template 3: Gameplan送付メール（YES返信後）
件名: your monetisation gameplan is ready

本文:
hi [name],

thanks for getting back to me! here's your custom gameplan:

[PDF添付 or リンク]

the highlights:
- your audience is worth more than brand deals alone (section 3)
- there's a product idea that fits your brand perfectly (section 4)
- the launch plan is designed for your exact audience (section 5)

next step if you're interested: a simple demand test. i'll create a 3-slide carousel for you to post and we'll see how your audience responds. zero commitment until you're ready.

best,
BG Growth

### Template 4: フィードバック依頼メール（断られた後）
件名: re: quick idea for [name]'s brand

本文:
totally understand, and thanks for letting me know.

quick question if you don't mind — what was the main thing that didn't feel right? the approach, the offer, or something else?

just trying to improve. any feedback is appreciated.

thanks,
BG Growth

## JavaScript機能
- 各テンプレートカードの右上に「Copy」ボタン
- クリック時にテンプレート本文（件名は含めない）をクリップボードにコピー
- コピー成功時にボタンが一瞬「Copied!」に変わり、2秒後に「Copy」に戻る
- [name] の部分はゴールド色（#C9A84C）でハイライト表示（手動で置き換える箇所が分かるように）
- 件名もクリック可能にして、別途コピーできるようにする

## 追加: フッターにメールアドレス表示
index.htmlの最下部フッターの「© 2026 BG Growth」の上に以下を追加:
"For business inquiries: boss.growth67@gmail.com"（mailtoリンク、色: #9B8E7E、14px）

## 完了後
git add -A && git commit -m "add email templates and footer email" && git push
