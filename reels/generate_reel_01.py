#!/usr/bin/env python3
"""Generate Instagram Reel: The $50K Math"""

import subprocess
import struct
import sys
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FPS = 30
DURATION = 12
TOTAL_FRAMES = FPS * DURATION
BG_COLOR = (10, 10, 15)
WHITE = (240, 240, 245)
GOLD = (201, 168, 76)

OUTPUT = os.path.expanduser("~/bg-growth-site/reels/reel_01_50k_math.mp4")


def get_font(size, bold=False):
    """Try to load a good font, fallback to default."""
    candidates = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSDisplay.ttf",
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    if bold:
        bold_candidates = [
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/Library/Fonts/Arial Bold.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        ]
        candidates = bold_candidates + candidates

    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def fade_alpha(t_start, t_current, fade_duration=0.5):
    """Calculate fade-in alpha (0.0 to 1.0)."""
    if t_current < t_start:
        return 0.0
    elapsed = t_current - t_start
    if elapsed >= fade_duration:
        return 1.0
    return elapsed / fade_duration


def blend_color(color, alpha):
    """Blend color with background based on alpha."""
    return tuple(int(BG_COLOR[i] + (color[i] - BG_COLOR[i]) * alpha) for i in range(3))


def draw_centered_text(draw, y, text, font, color):
    """Draw text centered horizontally at given y."""
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (W - tw) // 2
    draw.text((x, y), text, fill=color, font=font)


def draw_horizontal_line(draw, y, width, color):
    """Draw a centered horizontal line."""
    x_start = (W - width) // 2
    draw.line([(x_start, y), (x_start + width, y)], fill=color, width=3)


def generate_frame(t):
    """Generate a single frame at time t seconds."""
    img = Image.new("RGB", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Scene 1: Hook (0-4s)
    if t < 4.3:  # slight overlap for crossfade
        scene_alpha = 1.0
        if t > 3.7:
            scene_alpha = (4.3 - t) / 0.6  # fade out

        font_large = get_font(64)
        line1 = "Most creators with 50K followers"
        line2 = "make $0 from digital products"

        a1 = fade_alpha(0.0, t) * scene_alpha
        a2 = fade_alpha(1.0, t) * scene_alpha

        if a1 > 0:
            c1 = blend_color(WHITE, a1)
            draw_centered_text(draw, H // 2 - 80, line1, font_large, c1)
        if a2 > 0:
            c2 = blend_color(GOLD, a2)
            draw_centered_text(draw, H // 2 + 10, line2, font_large, c2)

    # Scene 2: Calculation (4-9s)
    if 3.7 < t < 9.3:
        scene_alpha = 1.0
        if t < 4.3:
            scene_alpha = (t - 3.7) / 0.6  # fade in
        if t > 8.7:
            scene_alpha = (9.3 - t) / 0.6  # fade out

        # Gold divider line
        line_alpha = fade_alpha(4.0, t) * scene_alpha
        if line_alpha > 0:
            draw_horizontal_line(draw, H // 2 - 200, 400, blend_color(GOLD, line_alpha))

        font_med = get_font(52)
        font_xl = get_font(80, bold=True)

        lines = [
            (4.0, "50,000 followers", WHITE, font_med),
            (5.0, "× 1% conversion", WHITE, font_med),
            (6.0, "× $47 product", WHITE, font_med),
            (7.5, "= $23,500", GOLD, font_xl),
        ]

        y_start = H // 2 - 120
        for i, (start_t, text, color, font) in enumerate(lines):
            a = fade_alpha(start_t, t) * scene_alpha
            if a > 0:
                y = y_start + i * 100
                if i == 3:
                    y += 30  # extra spacing for the result
                draw_centered_text(draw, y, text, font, blend_color(color, a))

    # Scene 3: CTA (9-12s)
    if t > 8.7:
        scene_alpha = 1.0
        if t < 9.3:
            scene_alpha = (t - 8.7) / 0.6  # fade in

        font_large = get_font(60)
        font_med = get_font(44)

        a1 = fade_alpha(9.0, t) * scene_alpha
        a2 = fade_alpha(9.5, t) * scene_alpha

        if a1 > 0:
            c1 = blend_color(GOLD, a1)
            draw_centered_text(draw, H // 2 - 60, "Follow @boss_growth67", font_large, c1)
        if a2 > 0:
            c2 = blend_color(WHITE, a2)
            draw_centered_text(draw, H // 2 + 30, "for creator monetisation tips", font_med, c2)

        # Bottom decorative line
        line_a = fade_alpha(9.5, t) * scene_alpha
        if line_a > 0:
            draw_horizontal_line(draw, H - 200, 300, blend_color(GOLD, line_a))

    return img


def main():
    print(f"Generating {TOTAL_FRAMES} frames at {FPS}fps...")

    cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{W}x{H}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "-",
        "-an",
        "-vcodec", "libx264",
        "-preset", "medium",
        "-crf", "23",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        OUTPUT,
    ]

    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)

    for frame_num in range(TOTAL_FRAMES):
        t = frame_num / FPS
        img = generate_frame(t)
        try:
            proc.stdin.write(img.tobytes())
        except BrokenPipeError:
            print("ffmpeg pipe broke early", file=sys.stderr)
            break
        if frame_num % 30 == 0:
            print(f"  Frame {frame_num}/{TOTAL_FRAMES} ({t:.1f}s)")

    proc.stdin.close()
    proc.wait()

    if proc.returncode != 0:
        print(f"ffmpeg exited with code {proc.returncode}", file=sys.stderr)
        sys.exit(1)

    size_mb = os.path.getsize(OUTPUT) / (1024 * 1024)
    print(f"\nDone! Output: {OUTPUT}")
    print(f"File size: {size_mb:.1f}MB")


if __name__ == "__main__":
    main()
