# MARKET MAKER / INVENTORY-RESPONSIVE QUOTING

## Ведущая идея и реализованное математическое ядро

Research implementation of reservation price, spread floor, market-volatility adjustment and inventory-dependent hedge proposal. The current quote(mid,inventory,sigma,config) disables quotes at max inventory, otherwise returns bid/ask about a skewed reservation price.

## Количественное описание

With tau=horizon_seconds/(365*24*3600), reservation=mid*(1-inventory*gamma*sigma^2*tau). HalfSpread=max(mid*min_half_spread_bps/10000,mid*(gamma*sigma^2*tau/2 + log(1+gamma/kappa)/gamma)) for positive gamma,kappa. Quote is not actual order fill.

## Новая экспериментальная программа

Use synchronized L2 order books and tick size to compare the strategy to fixed-spread baseline; measure fill rate, adverse selection, inventory drift, turnover and net realized spread under fees and slippage.

## Интеграция в институциональную архитектуру

Исходные сигналы остаются исследовательскими рекомендациями. Перед допуском в execution необходимы независимая валидация QuantLab, свежий риск-стейт RiskGuard и явные права оператора. Положительный исследовательский score, котировка или вес стратегии не означают исполненную или прибыльную торговую операцию.

## Источники и правила публикации

- [src/synergy_market_maker/core.py](../src/synergy_market_maker/core.py)
- [src/synergy_market_maker/synergy_contracts.py](../src/synergy_market_maker/synergy_contracts.py)
- [tests/](../tests/)

Следующая версия должна фиксировать source SHA, dataset hash, временные окна, конфигурацию и воспроизведённые результаты. Прежняя документация сохраняется целиком.
