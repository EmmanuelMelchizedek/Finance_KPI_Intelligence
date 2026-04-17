with base as (
    select * from {{ ref('staging_financials') }}
)
select
    month,
    sum(revenue) as revenue,
    sum(cost) as cost,
    sum(profit) as profit,
    sum(customers) as customers,
    sum(complaints) as complaints,
    round(sum(profit) / nullif(sum(revenue), 0) * 100, 2) as margin_pct
from base
group by month
order by month
