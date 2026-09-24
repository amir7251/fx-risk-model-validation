# GBP/USD Value at Risk: Model Validation

This project compares two ways of estimating GBP/USD risk: historical Value at Risk (VaR) and filtered historical VaR, which adjusts for changing volatility.

I used exchange-rate data from FRED covering 2005–2025 to build rolling forecasts at the 95% and 99% confidence levels. Both models use the previous 500 observations to estimate their thresholds. The filtered model also uses an EWMA volatility estimate.

The comparison covers **4,260 matching forecast periods from December 2008 to December 2025**.

## Results

A breach occurs when the actual return falls below the model’s forecast threshold. The expected breach rates are 5% for 95% VaR and 1% for 99% VaR.

| Measure | Historical VaR | Filtered VaR |
|---|---:|---:|
| 95% breach rate | 4.32% | 4.91% |
| 99% breach rate | 1.06% | 1.03% |
| Average 95% exceedance | 0.438 pp | 0.311 pp |
| Average 99% exceedance | 0.570 pp | 0.395 pp |
| 95% breach rate immediately after a breach | 10.87% | 5.74% |

Exceedance measures how far a return fell below its threshold, in percentage points (pp). Each average covers that model’s own breaches.

The filtered model’s overall breach rates were closer to the expected levels. Its average misses were also smaller, and breaches showed less tendency to follow one another.

## Performance across years

![Annual 95% VaR breach rates](reports/figures/annual_breach_rates_95.png)

![Annual 99% VaR breach rates](reports/figures/annual_breach_rates_99.png)

The annual results show that neither model performed consistently across the whole period. At 99% VaR, filtering reduced the breach rate from **3.98% to 1.20% in 2016**, but increased it from **0.80% to 2.39% in 2024**.

The charts exclude 2008 because it contains only seven matching forecasts.

## Further checks

The Kupiec coverage test rejected the historical model’s 95% coverage at the 5% significance level, with fewer breaches than expected. It did not reject either model’s 99% coverage or the filtered model’s 95% coverage. Non-rejection does not prove that a model is correct.

Changing the filtered model’s volatility decay factor from 0.94 to 0.97 produced relatively small changes in overall breach rates: **4.91% to 4.84%** at 95% VaR and **1.03% to 0.94%** at 99% VaR.

## Conclusion

The filtered model performed better on several measures in this sample: its overall breach rates were closer to their targets, average exceedances were smaller, and consecutive breaches were less common.

However, the yearly results show that volatility adjustment does not always improve forecasts. My main takeaway is that judging a risk model by its overall breach rate alone can hide important weaknesses. The size and timing of its failures matter too.

These findings are limited to one currency pair and one historical sample. The common comparison period excludes most of the 2008 financial crisis, and there is no separate untouched holdout sample. The clustering comparison is descriptive, while dependence between breaches limits interpretation of the coverage test.
