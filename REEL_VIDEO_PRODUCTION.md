# Instagram Reel動画制作 — Script 1: "The $50K Math"

## Task
ffmpegまたはPython（moviepy/pillow）を使って、テキストアニメーション付きのInstagramリール動画（MP4）を作成してください。

## 動画の仕様
- 解像度: 1080x1920（縦型、9:16）
- 長さ: 12秒
- FPS: 30
- フォーマット: MP4 (H.264)
- 背景色: #0A0A0F（ほぼ黒）
- 保存先: ~/bg-growth-site/reels/reel_01_50k_math.mp4

## 動画の構成（3シーン）

### シーン1: フック（0〜4秒）
- 背景: #0A0A0F
- テキスト: "Most creators with 50K followers"（1行目、白 #F0F0F5、フォントサイズ大）
- テキスト: "make $0 from digital products"（2行目、ゴールド #C9A84C、フォントサイズ大）
- アニメーション: テキストがフェードイン（0.5秒かけて表示）
- 1行目が先に表示（0秒〜）、2行目が1秒後に表示
- 画面中央に配置

### シーン2: 計算（4〜9秒）
- 背景: #0A0A0F
- 中央にゴールドの横線（幅400px、#C9A84C）でシーン区切り
- テキストが1行ずつフェードイン:
  - 4.0秒: "50,000 followers"（白、中サイズ）
  - 5.0秒: "× 1% conversion"（白、中サイズ）
  - 6.0秒: "× $47 product"（白、中サイズ）
  - 7.5秒: "= $23,500"（ゴールド #C9A84C、特大サイズ、太字）
- 全テキスト中央揃え、縦に積み重ねる

### シーン3: CTA（9〜12秒）
- 背景: #0A0A0F
- テキスト: "Follow @boss_growth67"（ゴールド #C9A84C、大サイズ）
- テキスト: "for creator monetisation tips"（白 #F0F0F5、中サイズ）
- フェードイン表示
- 画面下部にゴールドの細い横線を装飾として配置

## フォント
- システムフォントを使用（Helvetica, Arial, またはDejaVu Sans）
- もしGoogle Fontsが使えるならInter（700 bold + 400 regular）

## アニメーション
- 各テキストはフェードイン（opacity 0→1、0.5秒）
- シーン間のトランジション: 0.3秒のクロスフェード

## BGMなし
BGMはInstagramアプリ側で投稿時に追加する。動画自体は無音で作成。

## 技術的な注意
- ffmpegが入っていなければ brew install ffmpeg
- Pythonのpillowやmoviepyを使ってもOK
- 最終出力は必ずMP4（H.264 + AAC）
- ファイルサイズは10MB以内に収める

## 完了後
ファイルパスを教えてください。
