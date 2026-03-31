#!/usr/bin/env python3
"""Batch generate Instagram Reels 02-10."""

import subprocess
import sys
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FPS = 30
BG_COLOR = (10, 10, 15)
WHITE = (240, 240, 245)
GOLD = (201, 168, 76)

REELS_DIR = os.path.expanduser("~/bg-growth-site/reels")

# Font cache
_font_cache = {}


def get_font(size, bold=False):
    key = (size, bold)
    if key in _font_cache:
        return _font_cache[key]
    candidates = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSDisplay.ttf",
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/Library/Fonts/Arial.ttf",
    ]
    if bold:
        candidates = [
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/Library/Fonts/Arial Bold.ttf",
        ] + candidates
    for path in candidates:
        if os.path.exists(path):
            try:
                f = ImageFont.truetype(path, size)
                _font_cache[key] = f
                return f
            except Exception:
                continue
    f = ImageFont.load_default()
    _font_cache[key] = f
    return f


def fade_alpha(t_start, t_current, fade_dur=0.5):
    if t_current < t_start:
        return 0.0
    e = t_current - t_start
    return min(1.0, e / fade_dur)


def blend(color, alpha):
    return tuple(int(BG_COLOR[i] + (color[i] - BG_COLOR[i]) * alpha) for i in range(3))


def draw_centered(draw, y, text, font, color):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) // 2, y), text, fill=color, font=font)


def draw_hline(draw, y, width, color):
    x = (W - width) // 2
    draw.line([(x, y), (x + width, y)], fill=color, width=3)


def scene_fade(t, scene_start, scene_end, fade=0.3):
    """Scene-level fade in/out multiplier."""
    if t < scene_start or t > scene_end:
        return 0.0
    a = 1.0
    if t < scene_start + fade:
        a = (t - scene_start) / fade
    if t > scene_end - fade:
        a = (scene_end - t) / fade
    return max(0.0, min(1.0, a))


def make_frame(t, reel):
    """Generate frame for a reel definition."""
    img = Image.new("RGB", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)
    dur = reel["duration"]

    # Scene timings
    s1_end = reel.get("s1_end", 3.5)
    s2_start = s1_end - 0.3
    s2_end = reel.get("s2_end", dur - 3.0 + 0.3)
    s3_start = s2_end - 0.3

    # Scene 1: Hook
    sa = scene_fade(t, 0, s1_end)
    if sa > 0:
        lines = reel["hook"]
        total_h = len(lines) * 90
        y_base = (H - total_h) // 2
        for i, (text, color) in enumerate(lines):
            a = fade_alpha(i * 0.8, t) * sa
            if a > 0:
                draw_centered(draw, y_base + i * 90, text, get_font(60), blend(color, a))

    # Scene 2: Main
    sa = scene_fade(t, s2_start, s2_end)
    if sa > 0:
        items = reel["main"]
        total_h = len(items) * 90
        y_base = (H - total_h) // 2
        for i, (start_t, text, color, size, is_bold) in enumerate(items):
            a = fade_alpha(start_t, t) * sa
            if a > 0:
                font = get_font(size, bold=is_bold)
                draw_centered(draw, y_base + i * 90, text, font, blend(color, a))

    # Scene 3: CTA
    sa = scene_fade(t, s3_start, dur)
    if sa > 0:
        lines = reel["cta"]
        total_h = len(lines) * 80
        y_base = (H - total_h) // 2
        for i, (text, color, size) in enumerate(lines):
            a = fade_alpha(s3_start + i * 0.5, t) * sa
            if a > 0:
                draw_centered(draw, y_base + i * 80, text, get_font(size), blend(color, a))
        # Bottom gold line
        la = fade_alpha(s3_start + 0.5, t) * sa
        if la > 0:
            draw_hline(draw, H - 200, 300, blend(GOLD, la))

    return img


def render_reel(reel):
    """Render a reel to MP4."""
    output = os.path.join(REELS_DIR, reel["filename"])
    dur = reel["duration"]
    total = int(dur * FPS)

    print(f"\n--- Generating {reel['filename']} ({dur}s, {total} frames) ---")

    cmd = [
        "ffmpeg", "-y", "-f", "rawvideo", "-vcodec", "rawvideo",
        "-s", f"{W}x{H}", "-pix_fmt", "rgb24", "-r", str(FPS),
        "-i", "-", "-an", "-vcodec", "libx264", "-preset", "medium",
        "-crf", "23", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        output,
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)

    for f in range(total):
        t = f / FPS
        img = make_frame(t, reel)
        try:
            proc.stdin.write(img.tobytes())
        except BrokenPipeError:
            print(f"  Pipe broke at frame {f}", file=sys.stderr)
            break
        if f % 60 == 0:
            print(f"  {f}/{total} frames")

    proc.stdin.close()
    proc.wait()

    if proc.returncode != 0:
        print(f"  FAILED: ffmpeg exit code {proc.returncode}", file=sys.stderr)
        return False

    size_mb = os.path.getsize(output) / (1024 * 1024)
    print(f"  Done: {output} ({size_mb:.1f}MB)")
    return True


# ── Reel definitions ──

REELS = [
    {
        "filename": "reel_02_brand_deals.mp4",
        "duration": 12,
        "s1_end": 3.5,
        "s2_end": 9.3,
        "hook": [
            ("Brand deal: $500.", WHITE),
            ("One time.", GOLD),
        ],
        "main": [
            (3.5, "Digital product:", WHITE, 52, False),
            (4.5, "$47 × 500 sales", WHITE, 52, False),
            (5.5, "= $23,500", GOLD, 80, True),
            (7.0, "And it sells while you sleep.", WHITE, 48, False),
        ],
        "cta": [
            ("Which would you choose?", WHITE, 52),
            ("Follow @boss_growth67", GOLD, 56),
        ],
    },
    {
        "filename": "reel_03_stay_broke.mp4",
        "duration": 12,
        "s1_end": 3.5,
        "s2_end": 9.3,
        "hook": [
            ("3 reasons creators with", WHITE),
            ("10K+ followers stay broke", GOLD),
        ],
        "main": [
            (3.5, "1. No product", WHITE, 56, False),
            (4.8, "2. No email list", WHITE, 56, False),
            (6.1, "3. No launch strategy", WHITE, 56, False),
        ],
        "cta": [
            ("DM 'GAMEPLAN' for a free plan", GOLD, 48),
            ("Follow @boss_growth67", WHITE, 52),
        ],
    },
    {
        "filename": "reel_04_14day_launch.mp4",
        "duration": 12,
        "s1_end": 3.5,
        "s2_end": 9.3,
        "hook": [
            ("How to launch a digital product", WHITE),
            ("in 14 days", GOLD),
        ],
        "main": [
            (3.5, "Days 1-3: Warm up", WHITE, 52, False),
            (5.0, "Days 4-9: Give value", WHITE, 52, False),
            (6.5, "Days 10-14: Sell", GOLD, 64, True),
        ],
        "cta": [
            ("Save this.", WHITE, 56),
            ("Follow @boss_growth67", GOLD, 56),
        ],
    },
    {
        "filename": "reel_05_followers_waiting.mp4",
        "duration": 12,
        "s1_end": 3.5,
        "s2_end": 9.3,
        "hook": [
            ("Your followers want to", WHITE),
            ("buy from you", GOLD),
        ],
        "main": [
            (3.5, "They already trust you.", WHITE, 52, False),
            (4.8, "They already engage.", WHITE, 52, False),
            (6.2, "You just haven't given them", WHITE, 48, False),
            (6.2, "anything to buy yet.", GOLD, 56, True),
        ],
        "cta": [
            ("We build the product for you.", WHITE, 48),
            ("DM 'GAMEPLAN'", GOLD, 60),
        ],
    },
    {
        "filename": "reel_06_demand_test.mp4",
        "duration": 12,
        "s1_end": 3.5,
        "s2_end": 9.3,
        "hook": [
            ("Don't build a product", WHITE),
            ("until you do this", GOLD),
        ],
        "main": [
            (3.5, "Post 3 slides", WHITE, 52, False),
            (4.3, "Ask your audience to DM a keyword", WHITE, 44, False),
            (5.3, "50+ DMs = green light", WHITE, 52, False),
            (6.3, "Under 50 = pivot", WHITE, 52, False),
            (7.3, "Zero risk.", GOLD, 64, True),
        ],
        "cta": [
            ("Follow @boss_growth67", GOLD, 56),
            ("for more creator tips", WHITE, 48),
        ],
    },
    {
        "filename": "reel_07_micro_macro.mp4",
        "duration": 12,
        "s1_end": 3.5,
        "s2_end": 9.3,
        "hook": [
            ("10K followers > 100K followers", WHITE),
            ("(here's why)", GOLD),
        ],
        "main": [
            (3.5, "10K × 5% engagement = 500 fans", WHITE, 48, False),
            (5.0, "100K × 0.5% = 500 fans", WHITE, 48, False),
            (6.5, "Same number. Less work.", GOLD, 60, True),
        ],
        "cta": [
            ("Size doesn't matter.", WHITE, 52),
            ("Strategy does.", GOLD, 60),
            ("Follow @boss_growth67", WHITE, 48),
        ],
    },
    {
        "filename": "reel_08_250b_economy.mp4",
        "duration": 12,
        "s1_end": 3.5,
        "s2_end": 9.3,
        "hook": [
            ("The creator economy is worth", WHITE),
            ("$250 billion", GOLD),
        ],
        "main": [
            (3.5, "$250B", GOLD, 120, True),
            (5.0, "Projected: $530B by 2030", WHITE, 48, False),
            (6.5, "Will you capture any of it?", WHITE, 48, False),
        ],
        "cta": [
            ("Follow @boss_growth67", GOLD, 56),
            ("to start", WHITE, 48),
        ],
    },
    {
        "filename": "reel_09_stop_trading.mp4",
        "duration": 12,
        "s1_end": 3.5,
        "s2_end": 9.3,
        "hook": [
            ("Brand deals =", WHITE),
            ("trading time for money", GOLD),
        ],
        "main": [
            (3.5, "Digital products =", WHITE, 52, False),
            (3.5, "building an asset", WHITE, 52, False),
            (5.0, "One launch. Passive income.", WHITE, 48, False),
            (6.5, "You keep 70%.", GOLD, 64, True),
        ],
        "cta": [
            ("Ready to build?", WHITE, 56),
            ("DM 'GAMEPLAN'", GOLD, 60),
        ],
    },
    {
        "filename": "reel_10_what_we_do.mp4",
        "duration": 12,
        "s1_end": 3.5,
        "s2_end": 9.3,
        "hook": [
            ("We help creators launch", WHITE),
            ("digital products", GOLD),
        ],
        "main": [
            (3.5, "1. We analyze your audience", WHITE, 48, False),
            (4.5, "2. We build the product", WHITE, 48, False),
            (5.5, "3. We create the launch plan", WHITE, 48, False),
            (6.5, "4. You post. We handle the rest.", WHITE, 48, False),
        ],
        "cta": [
            ("Zero upfront cost.", WHITE, 48),
            ("You keep 70%.", GOLD, 60),
            ("DM us.", WHITE, 52),
        ],
    },
]


def main():
    ok = 0
    fail = 0
    for reel in REELS:
        if render_reel(reel):
            ok += 1
        else:
            fail += 1
    print(f"\n=== Batch complete: {ok} succeeded, {fail} failed ===")


if __name__ == "__main__":
    main()
