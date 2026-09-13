import os
import re

docs_dir = r"D:\SaeedHf52\BmiMerchantClub\docs"

for fname in ["01-research-and-discovery.html", "02-conceptual-initial-design.html"]:
    fpath = os.path.join(docs_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        content = re.sub(r'سپتامبر ۲۰۲۶', 'شهریور ۱۴۰۵', content)
        content = re.sub(r'September 2026', 'شهریور ۱۴۰۵', content)
        content = re.sub(r'۲۰۲۶', '۱۴۰۵', content)
        
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)

print("Dates converted to Persian Jalali successfully!")
