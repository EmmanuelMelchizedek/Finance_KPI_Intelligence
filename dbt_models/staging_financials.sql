select
    cast(month as date) as month,
    region,
    product,
    revenue,
    cost,
    customers,
    complaints,
    revenue - cost as profit,
    round(((revenue - cost) / nullif(revenue, 0)) * 100, 2) as margin_pct
from {{ source('raw', 'financial_transactions') }}
