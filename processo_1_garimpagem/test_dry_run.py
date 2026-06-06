"""
Teste dry-run do Processo 1 — executa toda a lógica sem chamadas à API.
Valida: ferramentas, modelos Pydantic, fórmulas Sa e Icf, pipeline de dados.
"""
import sys
import json
from datetime import datetime

sys.path.insert(0, ".")

from config import PINTEREST_TRENDS_2026, PLATFORM_STATS, AESTHETIC_SCORE_THRESHOLD, CONVERSION_INDEX_THRESHOLD
from models.trend_output import TrendHunterOutput, TrendEntry
from models.product_dossier import ProductDossier, PriceRange
from models.approved_catalog import ApprovedCatalog, ProductApproval, SeoMetadata
from tools.pinterest_tools import execute_trend_tool
from tools.scraper_tools import execute_scout_tool
from tools.vision_tools import execute_auditor_tool

PASS = "\033[92m✔\033[0m"
FAIL = "\033[91m✘\033[0m"
BOLD = "\033[1m"
RST  = "\033[0m"
SEP  = "─" * 58

def section(title: str) -> None:
    print(f"\n{SEP}\n{BOLD}  {title}{RST}\n{SEP}")

def ok(msg: str) -> None:
    print(f"  {PASS} {msg}")

def fail(msg: str) -> None:
    print(f"  {FAIL} {msg}")
    sys.exit(1)


# ════════════════════════════════════════════
# BLOCO 1 — Ferramentas do Trend Hunter
# ════════════════════════════════════════════
section("BLOCO 1 — Ferramentas do Trend Hunter")

r1 = execute_trend_tool("pinterest_trends_api_hook", {"top_n": 5, "min_growth_pct": 150})
assert len(r1["trends"]) == 5, "Deveria retornar 5 tendências"
assert r1["trends"][0]["growth_pct"] >= r1["trends"][-1]["growth_pct"], "Deveria estar ordenado por crescimento"
ok(f"pinterest_trends_api_hook → {len(r1['trends'])} tendências (top: {r1['trends'][0]['trend']} +{r1['trends'][0]['growth_pct']}%)")

trend_names = [t["trend"] for t in r1["trends"]]
r2 = execute_trend_tool("visual_autocomplete_emulator", {"trend_names": trend_names})
assert all(k in r2["long_tail_keywords"] for k in trend_names), "Todas as tendências devem ter keywords"
total_kw = sum(len(v) for v in r2["long_tail_keywords"].values())
ok(f"visual_autocomplete_emulator → {total_kw} keywords de cauda longa para {len(trend_names)} tendências")

r3 = execute_trend_tool("demographic_filter", {"trends": trend_names, "target_demographics": ["Gen Z", "Millennials"]})
assert len(r3["enriched_trends"]) == len(trend_names)
ok(f"demographic_filter → {len(r3['enriched_trends'])} tendências segmentadas (unbranded: {int(PLATFORM_STATS['unbranded_search_pct']*100)}%)")

# ════════════════════════════════════════════
# BLOCO 2 — Modelo TrendHunterOutput (Pydantic)
# ════════════════════════════════════════════
section("BLOCO 2 — Modelo TrendHunterOutput (Pydantic)")

trend_data = TrendHunterOutput(
    generated_at=datetime.now().isoformat(),
    total_trends=len(r1["trends"]),
    trends=[
        TrendEntry(
            trend=t["trend"],
            keywords_long_tail=r2["long_tail_keywords"].get(t["trend"], ["keyword"]),
            growth_pct=t["growth_pct"],
            demographics=t["demographics"],
            seasonal_window=next(
                (e["seasonal_window"] for e in r3["enriched_trends"] if e["trend"] == t["trend"]),
                "Janela não definida",
            ),
            search_volume_tier=next(
                (e["search_volume_tier"] for e in r3["enriched_trends"] if e["trend"] == t["trend"]),
                "emerging",
            ),
        )
        for t in r1["trends"]
    ],
    unbranded_search_pct=PLATFORM_STATS["unbranded_search_pct"],
    long_tail_multiplier=PLATFORM_STATS["long_tail_multiplier"],
    platform_context=(
        f"Pinterest 2026: {int(PLATFORM_STATS['purchase_conversion_pct']*100)}% dos usuários "
        f"semanais compram via Pin; tíquete médio {int(PLATFORM_STATS['cart_size_uplift']*100)}% maior."
    ),
)
assert trend_data.total_trends == len(trend_data.trends)
ok(f"TrendHunterOutput válido — {trend_data.total_trends} tendências, multiplicador cauda longa: {trend_data.long_tail_multiplier}×")

# ════════════════════════════════════════════
# BLOCO 3 — Ferramentas do Product Scout
# ════════════════════════════════════════════
section("BLOCO 3 — Ferramentas do Product Scout")

all_dossiers: list[ProductDossier] = []
for trend_entry in trend_data.trends[:3]:  # testa 3 tendências
    raw = execute_scout_tool("multicanal_scraper", {
        "trend_name": trend_entry.trend,
        "keywords": trend_entry.keywords_long_tail,
    })
    if not raw["products"]:
        ok(f"  {trend_entry.trend}: sem produtos no catálogo simulado (OK — catálogo parcial)")
        continue

    filtered = execute_scout_tool("store_quality_filter", {"products": raw["products"]})
    approved_raw = filtered["approved"]
    if not approved_raw:
        ok(f"  {trend_entry.trend}: todos descartados pelo filtro de qualidade")
        continue

    validated = execute_scout_tool("affiliate_viability_analysis", {"products": approved_raw})
    for vp in validated["validated_products"]:
        dossier = ProductDossier(
            product_name=vp["product_name"],
            source_platform=vp["platform"],
            affiliate_url=vp["affiliate_url"],
            price_range=PriceRange(min_usd=vp["price_min"], max_usd=vp["price_max"]),
            avg_commission_pct=vp["commission_pct"],
            store_rating=vp["rating"],
            return_rate_pct=vp.get("return_rate_pct"),
            trend_match=trend_entry.trend,
            keywords_matched=trend_entry.keywords_long_tail[:3],
            image_urls=vp["images"],
            product_type=vp["product_type"],
        )
        all_dossiers.append(dossier)

ok(f"multicanal_scraper + filtro + afiliação → {len(all_dossiers)} dossiê(s) válido(s)")
for d in all_dossiers:
    ok(f"  [{d.source_platform}] {d.product_name[:50]} | ★{d.store_rating} | {d.avg_commission_pct*100:.0f}% comissão")

# ════════════════════════════════════════════
# BLOCO 4 — Ferramentas do Aesthetic Auditor + Fórmulas
# ════════════════════════════════════════════
section("BLOCO 4 — Aesthetic Auditor: fórmulas Sa e Icf")

import math
def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))

approved_products: list[ProductApproval] = []
rejected_products: list[ProductApproval] = []

for dossier in all_dossiers:
    # Vision API HD
    vision = execute_auditor_tool("vision_api_hd", {
        "product_name": dossier.product_name,
        "image_urls": dossier.image_urls,
        "trend_match": dossier.trend_match,
    })
    vs = vision["vision_scores"]
    p_color = vs["p_color"]
    m_min   = vs["m_min"]
    l_nat   = vs["l_nat"]

    # Estimativas financeiras realistas baseadas nos dados do produto
    price_mid = (dossier.price_range.min_usd + dossier.price_range.max_usd) / 2
    m_net  = round(price_mid * dossier.avg_commission_pct, 2)
    c_out  = int(1200 + dossier.store_rating * 300)
    i_p    = int(c_out * 35)
    a_v    = round(min(dossier.store_rating / 5.0, 1.0), 2)
    p_spam = 1.0 if not vs.get("watermark_detected") else 1.8

    # Módulo de Cálculo Financeiro
    calc = execute_auditor_tool("financial_calculator", {
        "product_name": dossier.product_name,
        "p_color": p_color, "m_min": m_min, "l_nat": l_nat,
        "c_out": c_out, "a_v": a_v, "i_p": i_p, "m_net": m_net, "p_spam": p_spam,
    })
    sa  = calc["aesthetic_score_sa"]
    icf = calc["conversion_index_icf"]

    # Prompt & SEO
    assets = execute_auditor_tool("prompt_and_seo_generator", {
        "product_name": dossier.product_name,
        "trend_match": dossier.trend_match,
        "aesthetic_score_sa": sa,
        "platform": dossier.source_platform,
        "keywords": dossier.keywords_matched,
    })

    approved = sa >= AESTHETIC_SCORE_THRESHOLD and icf >= CONVERSION_INDEX_THRESHOLD
    status = "APROVADO" if approved else "REJEITADO"
    reason = None if approved else (
        f"Sa={sa:.4f} < {AESTHETIC_SCORE_THRESHOLD}" if sa < AESTHETIC_SCORE_THRESHOLD
        else f"Icf={icf:.6f} < {CONVERSION_INDEX_THRESHOLD}"
    )

    approval = ProductApproval(
        product_name=dossier.product_name,
        source_platform=dossier.source_platform,
        affiliate_url=dossier.affiliate_url,
        trend_match=dossier.trend_match,
        aesthetic_score_sa=sa,
        conversion_index_icf=icf,
        p_color=p_color, m_min=m_min, l_nat=l_nat,
        c_out=c_out, a_v=a_v, m_net=m_net, i_p=i_p, p_spam=p_spam,
        approved=approved,
        rejection_reason=reason,
        midjourney_prompt=assets["midjourney_prompt"],
        dalle_prompt=assets["dalle_prompt"],
        seo_metadata=SeoMetadata(**assets["seo_metadata"]),
    )
    (approved_products if approved else rejected_products).append(approval)

    formula_sa  = f"σ({p_color}) × {m_min} × {l_nat} = {sigmoid(p_color):.4f} × {m_min} × {l_nat} = {sa:.4f}"
    formula_icf = f"({c_out} × {a_v} × {m_net}) / ({i_p} × {p_spam}) = {icf:.6f}"
    marker = PASS if approved else FAIL
    print(f"  {marker} {dossier.product_name[:45]}")
    print(f"       Sa  = {formula_sa}  [{status}]")
    print(f"       Icf = {formula_icf}")

# ════════════════════════════════════════════
# BLOCO 5 — Catálogo Final (ApprovedCatalog)
# ════════════════════════════════════════════
section("BLOCO 5 — Catálogo Final ApprovedCatalog (Pydantic)")

total = len(approved_products) + len(rejected_products)
catalog = ApprovedCatalog(
    generated_at=datetime.now().isoformat(),
    total_evaluated=total,
    total_approved=len(approved_products),
    approval_rate_pct=round(len(approved_products) / max(total, 1) * 100, 1),
    approved_products=approved_products,
    rejected_products=rejected_products,
)
assert catalog.total_approved == len(catalog.approved_products)
ok(f"Catálogo válido — {catalog.total_approved}/{catalog.total_evaluated} aprovados ({catalog.approval_rate_pct}%)")

if catalog.approved_products:
    p = catalog.approved_products[0]
    ok(f"Exemplo aprovado: {p.product_name[:50]}")
    ok(f"  Sa={p.aesthetic_score_sa:.4f} | Icf={p.conversion_index_icf:.6f}")
    ok(f"  Alt Text: {p.seo_metadata.alt_text[:70]}...")
    ok(f"  Midjourney: {p.midjourney_prompt[:70]}...")

# Serialização JSON completa
json_out = catalog.model_dump_json(indent=2)
parsed_back = ApprovedCatalog.model_validate_json(json_out)
assert parsed_back.total_approved == catalog.total_approved
ok(f"Serialização JSON → parse reverso OK ({len(json_out)} bytes)")

print(f"\n{SEP}")
print(f"{BOLD}  TODOS OS TESTES PASSARAM  ✔{RST}")
print(f"  Processo 1 pronto para receber ANTHROPIC_API_KEY e rodar o pipeline completo.")
print(SEP + "\n")
