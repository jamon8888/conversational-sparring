# Brand Guidelines Reference

## Anthropic Brand Colors

### Primary Colors

**Anthropic Orange**
- Hex: `#D97757`
- RGB: `rgb(217, 119, 87)`
- Usage: Primary brand color, CTAs, highlights

**Anthropic Cream**
- Hex: `#F4EDE4`
- RGB: `rgb(244, 237, 228)`
- Usage: Backgrounds, light sections

### Secondary Colors

**Dark Brown**
- Hex: `#1F1F1F`
- RGB: `rgb(31, 31, 31)`
- Usage: Text, headers, dark backgrounds

**Medium Brown**
- Hex: `#7A6C5D`
- RGB: `rgb(122, 108, 93)`
- Usage: Secondary text, borders

**Light Cream**
- Hex: `#FAF7F4`
- RGB: `rgb(250, 247, 244)`
- Usage: Subtle backgrounds, cards

## Typography

### Font Families

**Primary Font: ABC Diatype**
- Usage: Headers, UI elements
- Weights: Regular (400), Medium (500), Bold (700)
- Fallback: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`

**Secondary Font: ABC Diatype Mono**
- Usage: Code blocks, technical content
- Weights: Regular (400)
- Fallback: `"Courier New", Courier, monospace`

### Type Scale

**Headings**:
```css
h1 { font-size: 48px; font-weight: 700; line-height: 1.2; }
h2 { font-size: 36px; font-weight: 700; line-height: 1.3; }
h3 { font-size: 24px; font-weight: 500; line-height: 1.4; }
h4 { font-size: 20px; font-weight: 500; line-height: 1.4; }
```

**Body Text**:
```css
body { font-size: 16px; font-weight: 400; line-height: 1.6; }
small { font-size: 14px; font-weight: 400; line-height: 1.5; }
```

## Color Usage Guidelines

### Accessibility

**Contrast Ratios** (WCAG AA):
- Normal text: Minimum 4.5:1
- Large text (18px+): Minimum 3:1
- UI components: Minimum 3:1

**Approved Combinations**:
```
✅ Dark Brown (#1F1F1F) on Cream (#F4EDE4) - 12.5:1
✅ Dark Brown (#1F1F1F) on White (#FFFFFF) - 16.1:1
✅ Anthropic Orange (#D97757) on Dark Brown (#1F1F1F) - 4.8:1
❌ Anthropic Orange (#D97757) on Cream (#F4EDE4) - 2.1:1 (fails)
```

### Color Application

**Backgrounds**:
- Primary: Cream (#F4EDE4) or Light Cream (#FAF7F4)
- Dark mode: Dark Brown (#1F1F1F)
- Sections: Alternate between cream shades

**Text**:
- Primary: Dark Brown (#1F1F1F)
- Secondary: Medium Brown (#7A6C5D)
- On dark backgrounds: Cream (#F4EDE4)

**Interactive Elements**:
- Primary CTA: Anthropic Orange (#D97757)
- Hover state: Darken by 10%
- Links: Anthropic Orange (#D97757)
- Link hover: Underline

## Logo Usage

### Logo Variations

**Full Logo**:
- Use on light backgrounds
- Minimum size: 120px width
- Clear space: Equal to height of "A"

**Logomark Only**:
- Use when space is limited
- Minimum size: 32px × 32px
- Maintain square aspect ratio

### Incorrect Usage

❌ Don't stretch or distort
❌ Don't change colors
❌ Don't add effects (shadows, gradients)
❌ Don't place on busy backgrounds
❌ Don't rotate

## Spacing System

**Base Unit**: 8px

**Scale**:
```
xs:  4px  (0.5 × base)
sm:  8px  (1 × base)
md:  16px (2 × base)
lg:  24px (3 × base)
xl:  32px (4 × base)
2xl: 48px (6 × base)
3xl: 64px (8 × base)
```

**Application**:
- Padding: Use scale values
- Margins: Use scale values
- Grid gaps: Use scale values

## Component Styles

### Buttons

**Primary Button**:
```css
background: #D97757;
color: #1F1F1F;
padding: 12px 24px;
border-radius: 6px;
font-weight: 500;
```

**Secondary Button**:
```css
background: transparent;
color: #1F1F1F;
border: 2px solid #1F1F1F;
padding: 12px 24px;
border-radius: 6px;
font-weight: 500;
```

### Cards

```css
background: #FAF7F4;
border: 1px solid #E5DED3;
border-radius: 8px;
padding: 24px;
box-shadow: 0 2px 4px rgba(0,0,0,0.05);
```

### Forms

**Input Fields**:
```css
background: #FFFFFF;
border: 1px solid #7A6C5D;
border-radius: 4px;
padding: 10px 12px;
font-size: 16px;
```

**Focus State**:
```css
border-color: #D97757;
outline: 2px solid rgba(217, 119, 87, 0.2);
```

## Voice and Tone

### Brand Voice Attributes

**Clear**: Use simple, direct language
**Thoughtful**: Consider implications and nuance
**Helpful**: Focus on user needs
**Honest**: Transparent about capabilities and limitations

### Writing Guidelines

**Do**:
- Use active voice
- Write in second person ("you")
- Be concise
- Explain technical concepts simply

**Don't**:
- Use jargon unnecessarily
- Make exaggerated claims
- Use overly casual language
- Assume technical knowledge

### Example Transformations

❌ "Our AI leverages state-of-the-art LLMs to facilitate optimal outcomes"
✅ "Our AI helps you get better results"

❌ "Click here to access the platform"
✅ "Start using Claude"

## File Formats

### Images
- **Web**: WebP (preferred), PNG, JPEG
- **Print**: PDF, EPS
- **Icons**: SVG

### Documents
- **Presentations**: PDF export
- **Reports**: PDF
- **Templates**: Figma, Sketch

## Brand Applications

### Website
- Use cream backgrounds
- Anthropic orange for CTAs
- Dark brown for text
- Ample white space

### Marketing Materials
- Maintain color ratios (60% cream, 30% dark, 10% orange)
- Use approved fonts
- Follow spacing system

### Social Media
- Profile images: Use logomark
- Cover images: Use full logo on cream
- Posts: Maintain brand colors
- Hashtags: #Anthropic #Claude

## Quick Reference

**CSS Variables**:
```css
:root {
  --color-orange: #D97757;
  --color-cream: #F4EDE4;
  --color-dark: #1F1F1F;
  --color-medium: #7A6C5D;
  --color-light: #FAF7F4;
  
  --font-primary: "ABC Diatype", sans-serif;
  --font-mono: "ABC Diatype Mono", monospace;
  
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
}
```
