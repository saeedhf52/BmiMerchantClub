import os
import re

pres_path = r"D:\SaeedHf52\BmiMerchantClub\docs\03-management-presentation.html"

with open(pres_path, "r", encoding="utf-8") as f:
    html = f.read()

# Add SVG illustration styles to <style>
svg_styles = """
/* Visual Graphic Elements */
.svg-graphic { display: block; margin: 0 auto; max-width: 100%; height: auto; }
.hero-graphic { width: 420px; height: 260px; }
.chart-graphic { width: 480px; height: 220px; }
.flow-graphic { width: 750px; height: 180px; }
.pos-mockup { width: 240px; height: 280px; background: #1e293b; border-radius: 20px; border: 4px solid #334155; padding: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.3); text-align: center; color: white; }
.phone-mockup { width: 220px; height: 320px; background: #0f172a; border-radius: 30px; border: 5px solid #38bdf8; padding: 12px; box-shadow: 0 10px 30px rgba(14,165,233,0.3); text-align: center; color: white; }
.visual-flex { display: flex; align-items: center; justify-content: center; gap: 40px; margin-top: 20px; }
"""

html = html.replace('</style>', svg_styles + '\n</style>')

# Insert SVG Hero Diagram into Slide 1 (Cover)
hero_svg = """
<div style="margin-top: 30px;">
  <svg class="hero-graphic" viewBox="0 0 500 240" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="250" cy="120" r="90" stroke="#38bdf8" stroke-width="2" stroke-dasharray="6 6" />
    <circle cx="250" cy="120" r="50" fill="#2563eb" fill-opacity="0.2" stroke="#60a5fa" stroke-width="3" />
    <!-- POS Terminal Node -->
    <rect x="70" y="70" width="100" height="100" rx="16" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
    <text x="120" y="115" fill="#ffffff" font-size="28" text-anchor="middle">💳</text>
    <text x="120" y="145" fill="#94a3b8" font-size="12" font-family="Vazirmatn" text-anchor="middle">دستگاه POS</text>
    <!-- Bale App Node -->
    <rect x="330" y="70" width="100" height="100" rx="16" fill="#1e293b" stroke="#10b981" stroke-width="3"/>
    <text x="380" y="115" fill="#ffffff" font-size="28" text-anchor="middle">📱</text>
    <text x="380" y="145" fill="#94a3b8" font-size="12" font-family="Vazirmatn" text-anchor="middle">مینی‌اپ بله</text>
    <!-- Center Core Node -->
    <circle cx="250" cy="120" r="30" fill="#0ea5e9"/>
    <text x="250" y="126" fill="#ffffff" font-size="14" font-weight="bold" font-family="Vazirmatn" text-anchor="middle">QR Engine</text>
    <!-- Connecting Animated Lines -->
    <path d="M 170 120 L 220 120" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
    <path d="M 280 120 L 330 120" stroke="#10b981" stroke-width="3" stroke-linecap="round"/>
  </svg>
</div>
"""
html = html.replace('</div>\n</div>\n\n<!-- Slide 2: The Problem -->', hero_svg + '</div>\n</div>\n\n<!-- Slide 2: The Problem -->')

# Insert Visual Infographic into Slide 3 (Ecosystem Triangle)
eco_svg = """
<div style="margin-top: 20px;">
  <svg width="650" height="260" viewBox="0 0 650 260" fill="none">
    <!-- Connecting Triangle Lines -->
    <polygon points="325,30 120,210 530,210" fill="none" stroke="#0ea5e9" stroke-width="3" stroke-dasharray="8 6"/>
    <!-- Top Node: Bank/PSP -->
    <g transform="translate(265, 10)">
      <rect width="120" height="70" rx="14" fill="#1e293b" stroke="#2563eb" stroke-width="3"/>
      <text x="60" y="32" fill="#ffffff" font-size="20" text-anchor="middle">🏦</text>
      <text x="60" y="55" fill="#38bdf8" font-size="12" font-weight="bold" font-family="Vazirmatn" text-anchor="middle">بانک / PSP</text>
    </g>
    <!-- Left Node: Merchants -->
    <g transform="translate(60, 175)">
      <rect width="130" height="70" rx="14" fill="#1e293b" stroke="#f59e0b" stroke-width="3"/>
      <text x="65" y="32" fill="#ffffff" font-size="20" text-anchor="middle">🏪</text>
      <text x="65" y="55" fill="#fbbf24" font-size="12" font-weight="bold" font-family="Vazirmatn" text-anchor="middle">شبکه پذیرندگان</text>
    </g>
    <!-- Right Node: Customers (Bale) -->
    <g transform="translate(460, 175)">
      <rect width="130" height="70" rx="14" fill="#1e293b" stroke="#10b981" stroke-width="3"/>
      <text x="65" y="32" fill="#ffffff" font-size="20" text-anchor="middle">👥</text>
      <text x="65" y="55" fill="#34d399" font-size="12" font-weight="bold" font-family="Vazirmatn" text-anchor="middle">کاربران بله</text>
    </g>
    <!-- Center Synergy Glow -->
    <circle cx="325" cy="140" r="35" fill="#2563eb" fill-opacity="0.15" stroke="#38bdf8" stroke-width="2"/>
    <text x="325" y="145" fill="#2563eb" font-size="13" font-weight="bold" font-family="Vazirmatn" text-anchor="middle">اثر شبکه‌ای</text>
  </svg>
</div>
"""

html = html.replace('<!-- Slide 4: Ecosystem Triangle -->', eco_svg + '\n<!-- Slide 4: Ecosystem Triangle -->')

with open(pres_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Enriched presentation with SVG graphics successfully!")
