from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional


class PriceRange(BaseModel):
    min_usd: float = Field(gt=0)
    max_usd: float = Field(gt=0)


class ProductDossier(BaseModel):
    """Contrato de saída do Subagente 2 → entrada do Subagente 3."""
    product_name: str
    source_platform: str = Field(description="Amazon | Etsy | Hotmart | Shopify")
    affiliate_url: str = Field(description="URL limpa sem redirecionadores mascarados")
    price_range: PriceRange
    avg_commission_pct: float = Field(ge=0.0, le=1.0)
    store_rating: float = Field(ge=0.0, le=5.0)
    return_rate_pct: Optional[float] = Field(default=None, ge=0.0, le=1.0)
    trend_match: str = Field(description="Nome da tendência que originou este produto")
    keywords_matched: List[str]
    image_urls: List[str] = Field(min_length=1)
    product_type: str = Field(description="physical | digital | custom_order")
