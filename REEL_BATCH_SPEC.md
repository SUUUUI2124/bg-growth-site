# Remaining 9 Reel Videos — Batch Generation

## Task
reel_01_50k_math.mp4 と同じ方法（generate_reel.py）を使って、残り9本のリール動画を一括生成してください。

## 共通仕様（全動画共通）
- 解像度: 1080x1920（縦型）
- 長さ: 10〜12秒
- FPS: 30
- 形式: MP4（H.264）
- 背景: #0A0A0F
- テキスト色: 白 #FFFFFF、ゴールド #C9A84C
- アニメーション: テキストのフェードイン（reel_01と同じ方式）
- 保存先: ~/bg-growth-site/reels/

## 9本のスクリプト

### reel_02_brand_deals.mp4
シーン1（フック）: "Brand deal: $500. One time."
シーン2（メイン）: "Digital product:" → "$47 × 500 sales" → "= $23,500" （ゴールドで強調） → "And it sells while you sleep."
シーン3（CTA）: "Which would you choose?" → "Follow @boss_growth67"

### reel_03_stay_broke.mp4
シーン1（フック）: "3 reasons creators with 10K+ followers stay broke"
シーン2（メイン）: 1行ずつ表示 → "1. No product" → "2. No email list" → "3. No launch strategy"
シーン3（CTA）: "DM 'GAMEPLAN' for a free plan" → "Follow @boss_growth67"

### reel_04_14day_launch.mp4
シーン1（フック）: "How to launch a digital product in 14 days"
シーン2（メイン）: "Days 1-3: Warm up" → "Days 4-9: Give value" → "Days 10-14: Sell" → 各行が順番にフェードイン
シーン3（CTA）: "Save this." → "Follow @boss_growth67"

### reel_05_followers_waiting.mp4
シーン1（フック）: "Your followers want to buy from you"
シーン2（メイン）: "They already trust you." → "They already engage." → "You just haven't given them anything to buy yet." → 最終行がゴールド
シーン3（CTA）: "We build the product for you." → "DM 'GAMEPLAN'"

### reel_06_demand_test.mp4
シーン1（フック）: "Don't build a product until you do this"
シーン2（メイン）: "Post 3 slides" → "Ask your audience to DM a keyword" → "50+ DMs = green light" → "Under 50 = pivot" → "Zero risk." ゴールド
シーン3（CTA）: "Follow @boss_growth67 for more"

### reel_07_micro_macro.mp4
シーン1（フック）: "10K followers > 100K followers"
シーン2（メイン）: "10K × 5% engagement = 500 fans" → "100K × 0.5% = 500 fans" → "Same number. Less work." ゴールド
シーン3（CTA）: "Size doesn't matter. Strategy does." → "Follow @boss_growth67"

### reel_08_250b_economy.mp4
シーン1（フック）: "The creator economy is worth $250 billion"
シーン2（メイン）: "$250B" 巨大ゴールド文字 → "Projected: $530B by 2030" → "Will you capture any of it?"
シーン3（CTA）: "Follow @boss_growth67 to start"

### reel_09_stop_trading.mp4
シーン1（フック）: "Brand deals = trading time for money"
シーン2（メイン）: "Digital products = building an asset" → "One launch. Passive income." → "You keep 70%." ゴールド
シーン3（CTA）: "Ready to build?" → "DM 'GAMEPLAN'"

### reel_10_what_we_do.mp4
シーン1（フック）: "We help creators launch digital products"
シーン2（メイン）: "1. We analyze your audience" → "2. We build the product" → "3. We create the launch plan" → "4. You post. We handle the rest."
シーン3（CTA）: "Zero upfront cost. You keep 70%." ゴールド → "DM us."

## 実行方法
generate_reel.py を改良して、スクリプトデータを引数やJSONで受け取れるようにし、9本を連続生成してください。
もしくは、1本ずつ生成しても構いません。

## 完了後
全10本のリールが ~/bg-growth-site/reels/ に揃ったことを確認:
ls -la ~/bg-growth-site/reels/
