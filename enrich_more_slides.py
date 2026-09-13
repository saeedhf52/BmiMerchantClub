import os

pres_path = r"D:\SaeedHf52\BmiMerchantClub\docs\03-management-presentation.html"

with open(pres_path, "r", encoding="utf-8") as f:
    html = f.read()

# Add SVG illustration to Slide 6 (QR Security)
qr_svg = """
<div style="margin-top: 25px; text-align: center;">
  <svg width="550" height="200" viewBox="0 0 550 200" fill="none">
    <!-- User Phone -->
    <rect x="40" y="30" width="120" height="140" rx="16" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
    <rect x="65" y="55" width="70" height="70" fill="#ffffff" rx="6"/>
    <path d="M 75 65 H 100 V 90 H 75 Z M 105 65 H 125 V 80 H 105 Z M 75 95 H 95 V 115 H 75 Z" fill="#0f172a"/>
    <text x="100" y="155" fill="#38bdf8" font-size="11" font-family="Vazirmatn" text-anchor="middle">QR پویا (۶۰s)</text>
    
    <!-- Encrypted Security Arrow -->
    <path d="M 180 100 L 350 100" stroke="#f59e0b" stroke-width="4" stroke-dasharray="6 6"/>
    <circle cx="265" cy="100" r="22" fill="#f59e0b"/>
    <text x="265" y="106" fill="#ffffff" font-size="14" text-anchor="middle">🔒</text>
    <text x="265" y="138" fill="#d97706" font-size="11" font-weight="bold" font-family="Vazirmatn" text-anchor="middle">AES-256 + HMAC</text>
    
    <!-- POS Terminal / Scanner -->
    <rect x="390" y="30" width="120" height="140" rx="16" fill="#1e293b" stroke="#10b981" stroke-width="3"/>
    <circle cx="450" cy="80" r="25" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="2"/>
    <text x="450" y="87" fill="#10b981" font-size="20" text-anchor="middle">📷</text>
    <text x="450" y="130" fill="#ffffff" font-size="12" font-weight="bold" font-family="Vazirmatn" text-anchor="middle">اسکنر صندوق‌دار</text>
    <text x="450" y="155" fill="#34d399" font-size="11" font-family="Vazirmatn" text-anchor="middle">اعتبارسنجی &lt; ۳ ثانیه</text>
  </svg>
</div>
"""

html = html.replace('<!-- Slide 7: Core Modules -->', qr_svg + '\n<!-- Slide 7: Core Modules -->')

# Add SVG illustration to Slide 14 (Roadmap Timeline)
roadmap_svg = """
<div style="margin-top: 20px;">
  <svg width="720" height="140" viewBox="0 0 720 140" fill="none">
    <line x1="60" y1="70" x2="660" y2="70" stroke="#38bdf8" stroke-width="4"/>
    <!-- Phase 1 -->
    <circle cx="100" cy="70" r="18" fill="#2563eb" stroke="#ffffff" stroke-width="3"/>
    <text x="100" y="75" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">۱</text>
    <text x="100" y="35" fill="#1e293b" font-size="12" font-weight="bold" font-family="Vazirmatn" text-anchor="middle">طراحی Core</text>
    <text x="100" y="105" fill="#64748b" font-size="10" font-family="Vazirmatn" text-anchor="middle">شهریور ۱۴۰۵</text>

    <!-- Phase 2 -->
    <circle cx="240" cy="70" r="18" fill="#0ea5e9" stroke="#ffffff" stroke-width="3"/>
    <text x="240" y="75" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">۲</text>
    <text x="240" y="35" fill="#1e293b" font-size="12" font-weight="bold" font-family="Vazirmatn" text-anchor="middle">مینی‌اپ بله</text>
    <text x="240" y="105" fill="#64748b" font-size="10" font-family="Vazirmatn" text-anchor="middle">آبان ۱۴۰۵</text>

    <!-- Phase 3 -->
    <circle cx="380" cy="70" r="18" fill="#f59e0b" stroke="#ffffff" stroke-width="3"/>
    <text x="380" y="75" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">۳</text>
    <text x="380" y="35" fill="#1e293b" font-size="12" font-weight="bold" font-family="Vazirmatn" text-anchor="middle">پایلوت منطقه‌ای</text>
    <text x="380" y="105" fill="#64748b" font-size="10" font-family="Vazirmatn" text-anchor="middle">دی ۱۴۰۵</text>

    <!-- Phase 4 -->
    <circle cx="520" cy="70" r="18" fill="#7c3aed" stroke="#ffffff" stroke-width="3"/>
    <text x="520" y="75" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">۴</text>
    <text x="520" y="35" fill="#1e293b" font-size="12" font-weight="bold" font-family="Vazirmatn" text-anchor="middle">هوش مصنوعی AI</text>
    <text x="520" y="105" fill="#64748b" font-size="10" font-family="Vazirmatn" text-anchor="middle">اسفند ۱۴۰۵</text>

    <!-- Phase 5 -->
    <circle cx="660" cy="70" r="18" fill="#10b981" stroke="#ffffff" stroke-width="3"/>
    <text x="660" y="75" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">۵</text>
    <text x="660" y="35" fill="#1e293b" font-size="12" font-weight="bold" font-family="Vazirmatn" text-anchor="middle">توسعه سراسری</text>
    <text x="660" y="105" fill="#64748b" font-size="10" font-family="Vazirmatn" text-anchor="middle">۱۴۰۶ به بعد</text>
  </svg>
</div>
"""

html = html.replace('<!-- Slide 15: Execution Roadmap -->', roadmap_svg + '\n<!-- Slide 15: Execution Roadmap -->')

with open(pres_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Enriched extra slides with visual SVGs successfully!")
