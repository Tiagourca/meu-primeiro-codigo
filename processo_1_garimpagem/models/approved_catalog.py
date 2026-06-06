from pydantic import BaseModel, Field
from typing import List, Optional


class SeoMetadata(BaseModel):
    alt_text: str = Field(description="Alt Text descritivo para +25% impressões")
    pin_title: str
    pin_description: str
    hashtags: List[str]


class ProductApproval(BaseModel):
    product_name: str
    source_platform: str
    affiliate_url: str
    trend_match: str

    # Métricas do Aesthetic Auditor
    aesthetic_score_sa: float = Field(
        ge=0.0, le=1.0,
        description="Sa = σ(P_color) × M_min × L_nat",
    )
    conversion_index_icf: float = Field(
        description="Icf = (C_out × A_v × M_net) / (I_p × P_spam)",
    )

    # Componentes individuais para rastreabilidade
    p_color: float
    m_min: float
    l_nat: float
    c_out: int
    a_v: float
    m_net: float
    i_p: int
    p_spam: float

    approved: bool
    rejection_reason: Optional[str] = None

    # Entregáveis para Processo 2
    midjourney_prompt: str
    dalle_prompt: str
    seo_metadata: SeoMetadata


class ApprovedCatalog(BaseModel):
    """Saída final do Processo 1 → entrada do Processo de Venda (Processo 2)."""
    process: str = "Processo 1 — Garimpagem Científica de Produtos"
    generated_at: str
    total_evaluated: int
    total_approved: int
    approval_rate_pct: float
    approved_products: List[ProductApproval]
    rejected_products: List[ProductApproval]
