import os
import re

docs_dir = r"D:\SaeedHf52\BmiMerchantClub\docs"

# Add extra detailed sections and rich SVGs into 01-research-and-discovery.html
doc1_path = os.path.join(docs_dir, "01-research-and-discovery.html")
with open(doc1_path, "r", encoding="utf-8") as f:
    html1 = f.read()

# Add diagram visual box into section 8
svg_arch = """
<div class="diagram-container" style="background:#0f172a; padding:25px; border-radius:16px; margin:20px 0; color:#fff;">
  <h4 style="color:#38bdf8; text-align:center; margin-bottom:20px;">نمای تعاملی زیرساخت Adapter مینی‌اپ بله</h4>
  <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:15px;">
    <div style="background:#1e293b; border:2px solid #3b82f6; padding:15px; border-radius:12px; width:220px; text-align:center;">
      <div style="font-size:1.5rem;">📱</div>
      <strong style="color:#60a5fa;">مینی‌اپ بله (Client)</strong>
      <p style="font-size:0.75rem; color:#94a3b8; margin-top:5px;">JS SDK | Bale InitData | Web View</p>
    </div>
    <div style="color:#38bdf8; font-size:1.5rem; font-weight:bold;">⟷ REST / WSS ⟷</div>
    <div style="background:#1e293b; border:2px solid #10b981; padding:15px; border-radius:12px; width:240px; text-align:center;">
      <div style="font-size:1.5rem;">⚙️</div>
      <strong style="color:#34d399;">Channel Adapter Layer</strong>
      <p style="font-size:0.75rem; color:#94a3b8; margin-top:5px;">OAuth2 Token | Auth Middleware | Rate Limiter</p>
    </div>
    <div style="color:#38bdf8; font-size:1.5rem; font-weight:bold;">⟷ gRPC ⟷</div>
    <div style="background:#1e293b; border:2px solid #f59e0b; padding:15px; border-radius:12px; width:220px; text-align:center;">
      <div style="font-size:1.5rem;">🏢</div>
      <strong style="color:#fbbf24;">هسته اصلی اکوسیستم</strong>
      <p style="font-size:0.75rem; color:#94a3b8; margin-top:5px;">Core API | Campaign | QR Engine</p>
    </div>
  </div>
</div>
"""

html1 = html1.replace('</section>\n\n    <!-- SECTION 9 -->', svg_arch + '</section>\n\n    <!-- SECTION 9 -->')

with open(doc1_path, "w", encoding="utf-8") as f:
    f.write(html1)

print("Enriched 01-research-and-discovery.html with visual diagrams!")
