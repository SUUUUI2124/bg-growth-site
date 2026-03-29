# BG Growth Landing Page — Design Specification

## Background
BG Growth is a Growth Marketing service for Instagram micro-creators (10K-100K followers). We build digital products and launch strategies for creators. Revenue share: creator 70%, BG Growth 30%. No upfront cost to creators.

## Purpose
When creators receive our DM and check our Instagram profile, they click our website link. This landing page must convince them "this is a legitimate business." The ONLY goal is trust-building.

## Visitor Profile
- English-speaking Instagram micro-creators (US, UK, Canada, Australia)
- 10K-100K followers, niches: Fitness, Business, Tech
- Age 20s-40s
- Visiting from smartphone (Instagram bio link)
- Skeptical: "Is this person legit or a scam?"

## Tech Stack
- Static site: index.html, style.css, script.js (3 files only)
- No frameworks (no React, no Bootstrap)
- Hosting: GitHub Pages (free)
- Google Fonts: Inter (weights 400, 600, 700 only)
- Mobile-first responsive (375px to 1440px)
- No external images. Logo via CSS/SVG only
- Fast load speed is critical

## Color Palette (strict)
- Background main: #0A0A0F
- Background secondary: #141420
- Background tertiary: #1A1A2E
- Gold main: #C9A84C
- Gold dark: #8A7B3C
- Text white: #F0F0F5
- Text gray: #9999AA
- Text light: #CCCCDD
- Accent green: #27AE60

## Critical Design Rules
1. Must NOT look like an AI-generated template site. Must look human-designed.
2. Vary layout per section (mix left-aligned, centered, right-aligned)
3. Don't over-align. Allow natural whitespace variation for organic feel.
4. Animations: subtle fade-in on scroll only. No flashy effects.
5. No images. Logo implemented in CSS/SVG.
6. Section dividers via subtle background color changes, not lines.

## Page Structure (single page, 6 sections)

### Section 1: Hero
- Background: #0A0A0F
- Logo "BG" at top: B in white #F0F0F5, | divider in gold #C9A84C, G in gold #C9A84C (SVG or CSS)
- Headline: "We help creators turn their audience into income."
  - Font: Inter 700, desktop 48px, mobile 32px
  - The word "income" in gold #C9A84C, rest in white
- Subheadline: "You built the audience. We build the product. You keep 70%."
  - Font: Inter 400, 18px, color #CCCCDD
- CTA button: "Get your free gameplan →"
  - Background: #C9A84C, text: #0A0A0F, border-radius: 8px
  - Hover: slightly brighter background
  - Link: mailto:boss.growth67@gmail.com?subject=I%20want%20my%20free%20gameplan
- Below button, small text: "No upfront cost. No risk. Just results." (color #9999AA, 14px)

### Section 2: The Problem
- Background: #0A0A0F (same as hero, separated by whitespace)
- Layout: left-aligned
- Heading: "The creator monetisation gap" (Inter 600, 28px, white)
- Body paragraphs (each separated by 20px):
  - "Most creators with 10K-100K followers have done the hardest part — building an audience that trusts them."
  - "But almost none of them have a product to sell."
  - "They rely on brand deals that come and go. One algorithm change and their income drops to zero."
  - "The audience is there. The trust is there. The missing piece is a product and a system to sell it."
- Small gold accent line at bottom (width 60px, height 2px)

### Section 3: How It Works
- Background: #141420
- Heading: "How it works" (centered, Inter 600, 28px)
- 3 steps in row (desktop) / stacked (mobile):
  - Step 01: "We analyze your audience"
    - Description: "We dig into your content, engagement patterns, and follower demographics to find exactly what product your audience would pay for."
    - Number "01" in large gold text (Inter 700, 48px, #C9A84C)
  - Step 02: "We build your product"
    - Description: "Using AI-powered tools, we create a complete digital product — eBook, course, or template — tailored to your audience. You review and approve everything."
    - Number "02" in gold
  - Step 03: "We launch together"
    - Description: "We create a 14-day Instagram Story sequence that systematically turns your followers into customers. You post the stories. We handle the strategy."
    - Number "03" in gold
- Below steps, highlight text:
  - "You keep 70% of all revenue. We keep 30%. No upfront cost."
  - Inter 600, 20px, gold, centered

### Section 4: What You Get
- Background: #0A0A0F
- Heading: "Your free monetisation gameplan includes:" (left-aligned, Inter 600, 28px)
- 6 items as simple vertical list (NOT cards):
  - "✦ Complete audience audit — who follows you and what they want to buy"
  - "✦ Revenue projections — real numbers based on your actual engagement"
  - "✦ Custom product suggestions — specific to your niche and audience"
  - "✦ 14-day launch strategy — the exact sequence to turn followers into buyers"
  - "✦ Demand testing framework — validate before building anything"
  - "✦ Full competitive analysis — what similar creators are earning"
- ✦ symbols in gold #C9A84C
- Item text in #CCCCDD, Inter 400, 16px
- Below list: "Built specifically for your brand. Not a generic template." (#9999AA, italic)

### Section 5: FAQ
- Background: #141420
- Heading: "Questions you probably have" (centered, Inter 600, 28px)
- Accordion style (click to expand), 4 items:
  - Q: "Is this actually free?"
    A: "Yes. The gameplan is 100% free with no obligations. If you decide to partner with us, we work on a 70/30 revenue share — you keep 70%. We only make money when you make money."
  - Q: "Do I need to create the product myself?"
    A: "No. We handle product creation from start to finish. You focus on what you do best — creating content and engaging with your audience."
  - Q: "What kind of products do you build?"
    A: "It depends on your audience. Could be an eBook, online course, template pack, coaching program, or community membership. We analyze your content to determine what sells best."
  - Q: "How long until I see results?"
    A: "From partnership to first sale, typically 3-4 weeks. The launch itself runs over 14 days."
- Closed state: question text (#F0F0F5) + "+" icon on right (gold)
- Open state: answer slides in below (#CCCCDD), "+" becomes "−"
- Implement with vanilla JS (no libraries)

### Section 6: Final CTA
- Background: #1A1A2E
- Centered layout
- Heading: "Ready to see what your audience is really worth?" (Inter 700, 32px, white)
- Subtext: "Get a free, custom monetisation gameplan built specifically for your brand." (Inter 400, 16px, #CCCCDD)
- CTA button: same as hero button
  - Link: mailto:boss.growth67@gmail.com?subject=I%20want%20my%20free%20gameplan
- Below button: "or DM us on Instagram →" (text link, gold, links to https://instagram.com/boss_growth67)
- Footer: "© 2026 BG Growth" (#9999AA, 12px)

## Additional Requirements
- Section spacing: desktop 100px+, mobile 60px+
- Scroll fade-in animation via Intersection Observer API (each section fades up on entering viewport)
- CSS scroll-behavior: smooth
- Meta description: "BG Growth helps Instagram creators monetise their audience with digital products. Free custom gameplan. No upfront cost."
- Include Open Graph tags (og:title, og:description)
- No favicon for now

## What NOT to include
- No fake testimonials or reviews
- No unverified numbers (no "$100M+" claims)
- No "guaranteed results" language
- No stock photos or placeholder images

## Final instruction
Build all 3 files (index.html, style.css, script.js) completely. Make sure the site works when opened locally in a browser. The site should look premium, trustworthy, and professional.
