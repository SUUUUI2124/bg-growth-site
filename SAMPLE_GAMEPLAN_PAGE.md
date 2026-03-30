# Sample Gameplan Web Page

## Task
~/bg-growth-site/ 内に sample.html を新規作成する。
既存の index.html（ランディングページ）からリンクで飛べるサンプルGameplanページ。

## Purpose
DMを受け取ったクリエイターが「本当にちゃんとしたGameplanを作ってくれるのか？」と疑った時に見せるページ。実際のGameplan PDFと同じ6セクション構成をWebページとして表示する。

## Design
- style.cssを共有（ランディングページと統一デザイン）
- ダーク背景 #0A0A0F、ゴールド #C9A84C
- モバイルファースト
- Google Fonts: Inter

## Page Content（架空のクリエイター「Alex Rivera」@alexfitlife 向け）

### ヘッダー
- 左上: BGロゴ（ランディングページと同じ）
- 右上: "← Back to BG Growth" リンク（index.htmlに戻る）
- 中央: "SAMPLE MONETISATION GAMEPLAN"（Inter 600, 11px, gold, letter-spacing 2px）
- その下: "This is an example. Yours will be custom-built for your brand."（Inter 400, 14px, #9999AA）

### Section 1: The Audit
- 見出し: "01 — The Audit"（gold）
- クリエイター情報カード:
  - Name: Alex Rivera
  - Handle: @alexfitlife
  - Followers: 45,000
  - Engagement: 4.2%
  - Niche: Fitness / Home Workouts
  - Current Monetisation: Brand deals only. No digital products.
- "The Hidden Transformation" 小見出し
  - "Your followers don't just want workout videos. They want to feel confident, strong, and in control of their body. Fitness is the vehicle. Self-confidence is the destination."
- "Key Insight" 小見出し
  - "45,000 people trust you. But the only revenue from that trust is occasional brand deals. Your audience is ready to buy from you — you just haven't given them anything to buy yet."

### Section 2: The Opportunity
- 見出し: "02 — The Opportunity"
- 3つのカード（gold左ボーダー）:
  - Opportunity 01: "Home Workout Program"
    - "Your at-home workout posts consistently get 2x your average engagement. Your audience wants a structured program they can follow."
  - Opportunity 02: "Nutrition Guide"
    - "Your meal prep posts get the most saves — a signal that people want to reference your advice later. A guide would formalize this."
  - Opportunity 03: "Fitness Challenge"
    - "Your 30-day challenge posts drive the most comments and DMs. A paid challenge with community access would monetize this demand."

### Section 3: The Numbers
- 見出し: "03 — The Numbers"
- データ:
  - Followers: 45,000
  - Engagement: 4.2% (Strong)
  - Est. Conversion: 1.5%
- 3シナリオ:
  - Conservative: $47 product, 1% conversion = 450 sales = $21,150
  - Moderate: $47 product, 1.5% conversion = 675 sales = $31,725
  - Premium: $97 product, 1.5% conversion = 675 sales = $65,475
- 注記: "Your share (70%): $14,805 — $45,833"

### Section 4: Product Suggestion
- 見出し: "04 — Product Suggestion"
- メイン: "The Home Body Blueprint"
  - 8-week home workout program, $47
  - 内容リスト:
    - 8 weeks of progressive workouts (no equipment needed)
    - Nutrition guide with meal prep templates
    - Weekly accountability check-ins
    - Access to private community
- サブ: "Quick Start Guide (eBook) — $19"
  - Entry-level product to capture wider audience

### Section 5: Launch Strategy
- 見出し: "05 — Launch Strategy"
- 14日間の3フェーズ概要:
  - Phase 1 (Days 1-3): Warm-Up
  - Phase 2 (Days 4-9): Value Delivery
  - Phase 3 (Days 10-14): Launch & Sell
- 各フェーズに2-3行の説明

### Section 6: Demand Test
- 見出し: "06 — Demand Test"
- 3スライドの説明:
  - Slide 1: Hook question
  - Slide 2: Product concept
  - Slide 3: "DM me [KEYWORD] for early access"
- 注記: "If 50+ people DM the keyword, we build. If not, we pivot. Zero risk."

### フッター CTA
- "Want one built for YOUR brand?"
- ボタン: "Get your free gameplan →"（mailto:boss.growth67@gmail.com）
- "or DM us on Instagram →"（@boss_growth67リンク）
- "© 2026 BG Growth"

## Link from Landing Page
index.html の Sample Gameplan セクションに、カードの下にリンクを追加:
"See full sample gameplan →" （sample.htmlへのリンク、ゴールド色テキスト）

## After completing:
Run: git add -A && git commit -m "add sample gameplan page" && git push
