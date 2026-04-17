-- Monthly profitability trend
SELECT month, SUM(revenue) AS revenue, SUM(cost) AS cost, SUM(profit) AS profit
FROM financial_transactions
GROUP BY month
ORDER BY month;

-- Best performing region-product combinations
SELECT region, product, SUM(profit) AS profit, ROUND(SUM(profit) / NULLIF(SUM(revenue),0) * 100, 2) AS margin_pct
FROM financial_transactions
GROUP BY region, product
ORDER BY profit DESC;
