"""
Processo 1 — Garimpagem Científica de Produtos
Cadeia sequencial determinística: Trend Hunter → Product Scout → Aesthetic Auditor
"""
import json
import sys
from datetime import datetime
from pathlib import Path

from agents.trend_hunter import TrendHunterAgent
from agents.product_scout import ProductScoutAgent
from agents.aesthetic_auditor import AestheticAuditorAgent
from models.approved_catalog import ApprovedCatalog


def _log(stage: str, msg: str) -> None:
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] [{stage}] {msg}", flush=True)


def run_pipeline(output_path: str | None = None) -> ApprovedCatalog:
    """Executa a cadeia completa e retorna o catálogo aprovado."""
    print("\n" + "=" * 60)
    print("  PROCESSO 1 — GARIMPAGEM CIENTÍFICA DE PRODUTOS")
    print("  Cadeia: Trend Hunter → Product Scout → Aesthetic Auditor")
    print("=" * 60 + "\n")

    # ─────────────────────────────────────────────
    # ETAPA 1 — Subagente 1: Trend Hunter
    # ─────────────────────────────────────────────
    _log("TREND HUNTER", "Iniciando varredura de tendências Pinterest 2026...")
    trend_agent = TrendHunterAgent()
    trend_output = trend_agent.run()
    _log("TREND HUNTER", f"Concluído. {trend_output.total_trends} tendências identificadas.")
    for t in trend_output.trends:
        _log("TREND HUNTER", f"  • {t.trend} (+{t.growth_pct}%) — {', '.join(t.demographics)}")

    # ─────────────────────────────────────────────
    # ETAPA 2 — Subagente 2: Product Scout
    # ─────────────────────────────────────────────
    _log("PRODUCT SCOUT", "Iniciando garimpagem multicanal de produtos...")
    scout_agent = ProductScoutAgent()
    dossiers = scout_agent.run(trend_output)
    _log("PRODUCT SCOUT", f"Concluído. {len(dossiers)} dossiê(s) de produto gerado(s).")
    for d in dossiers:
        price_str = f"US$ {d.price_range.min_usd:.2f}–{d.price_range.max_usd:.2f}"
        _log("PRODUCT SCOUT", f"  • [{d.source_platform}] {d.product_name} | {price_str} | ★{d.store_rating}")

    # ─────────────────────────────────────────────
    # ETAPA 3 — Subagente 3: Aesthetic Auditor
    # ─────────────────────────────────────────────
    _log("AESTHETIC AUDITOR", "Iniciando auditoria estética e modelagem financeira...")
    auditor_agent = AestheticAuditorAgent()
    catalog = auditor_agent.run(dossiers)
    _log("AESTHETIC AUDITOR", (
        f"Concluído. {catalog.total_approved}/{catalog.total_evaluated} produtos aprovados "
        f"({catalog.approval_rate_pct:.1f}%)."
    ))

    # ─────────────────────────────────────────────
    # SUMÁRIO FINAL
    # ─────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  CATÁLOGO APROVADO — PRONTO PARA PROCESSO 2")
    print("=" * 60)
    for p in catalog.approved_products:
        print(f"\n  PRODUTO : {p.product_name}")
        print(f"  Tendência: {p.trend_match}")
        print(f"  Plataforma: {p.source_platform}")
        print(f"  Sa  = {p.aesthetic_score_sa:.4f}  (σ({p.p_color}) × {p.m_min} × {p.l_nat})")
        print(f"  Icf = {p.conversion_index_icf:.6f}")
        print(f"  URL : {p.affiliate_url}")
        print(f"  Alt Text: {p.seo_metadata.alt_text[:80]}...")

    if catalog.rejected_products:
        print(f"\n  REJEITADOS ({len(catalog.rejected_products)}):")
        for p in catalog.rejected_products:
            print(f"  ✗ {p.product_name} — {p.rejection_reason}")

    # Persistência opcional do catálogo em JSON
    if output_path:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            catalog.model_dump_json(indent=2, exclude_none=False),
            encoding="utf-8",
        )
        _log("PIPELINE", f"Catálogo salvo em: {out.resolve()}")

    print("\n" + "=" * 60 + "\n")
    return catalog


if __name__ == "__main__":
    output_file = sys.argv[1] if len(sys.argv) > 1 else "output/catalogo_aprovado.json"
    catalog = run_pipeline(output_path=output_file)
    sys.exit(0 if catalog.total_approved > 0 else 1)
