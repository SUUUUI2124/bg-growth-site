# Landing Page Update: Add Sample Gameplan Section

## Task
Add a new section to index.html between Section 4 (What You Get) and Section 5 (FAQ).

## New Section: "See a sample gameplan"
- Background: #1A1A2E
- Centered layout

### Heading
- Text: "Here's what a real gameplan looks like"
- Font: Inter 700, 32px, white

### Subtext
- Text: "Every gameplan is custom-built for your brand. Here's a preview of the format."
- Font: Inter 400, 16px, #CCCCDD

### Gameplan Preview Card (CSS only, no images)
Create a card that visually represents the Gameplan PDF cover:
- Card background: #0A0A0F
- Border: 1px solid #C9A84C (gold border)
- Border-radius: 12px
- Padding: 40px
- Max-width: 400px, centered
- Box-shadow: 0 20px 60px rgba(0,0,0,0.5)
- Hover effect: transform scale(1.02), transition 0.3s ease

Card contents (top to bottom):
1. "MONETISATION GAMEPLAN" — Inter 600, 11px, #C9A84C, letter-spacing 2px, centered
2. Gold line (width 60px, height 1px, #C9A84C, centered, margin 16px auto)
3. "YOUR NAME HERE" — Inter 700, 28px, #F0F0F5, centered
4. "@yourhandle" — Inter 400, 16px, #C9A84C, centered
5. Three stats in a row (flexbox, space-between):
   - "50K+" with label "Followers" below
   - "4.2%" with label "Engagement" below
   - "$75K+" with label "Revenue Potential" below
   - Numbers: Inter 700, 22px, #C9A84C
   - Labels: Inter 400, 10px, #9999AA

### Below the card: 6 section list
- Text: "What's inside:"
- Font: Inter 600, 18px, white, left-aligned, max-width 400px centered
- 6 items as simple text list:
  - "✦ Complete Audience Audit"
  - "✦ Revenue Projections with Real Numbers"
  - "✦ Custom Product Suggestions"
  - "✦ 14-Day Launch Strategy"
  - "✦ Demand Testing Framework"
  - "✦ Competitive Analysis"
- ✦ in gold #C9A84C
- Item text: Inter 400, 14px, #CCCCDD
- Line height: 2.0

### Fade-in animation
Apply the same scroll fade-in animation as other sections (.fade-in class)

## Important
- Keep all existing sections unchanged
- This new section should flow naturally between What You Get and FAQ
- Mobile responsive (card should be full-width with padding on mobile)
