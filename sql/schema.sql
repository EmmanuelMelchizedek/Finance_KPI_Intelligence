CREATE TABLE financial_transactions (
    month DATE,
    region VARCHAR(50),
    product VARCHAR(50),
    revenue NUMERIC(14,2),
    cost NUMERIC(14,2),
    customers INTEGER,
    complaints INTEGER,
    profit NUMERIC(14,2),
    margin_pct NUMERIC(6,2)
);
