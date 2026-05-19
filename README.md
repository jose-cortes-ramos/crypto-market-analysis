# Crypto Market Analysis | Project Overview

## Strategic Context
Este repositorio constituye el nucleo de analisis exploratorio y serving de datos dentro de un ecosistema de datos de criptomonedas. Su funcion principal es actuar como el puente critico entre la infraestructura de datos en la nube (GCP) y el modelado de Machine Learning, proporcionando validacion estadistica para las señales de mercado.

## Data Lifecycle Integration
El proyecto se integra en una arquitectura de datos de extremo a extremo:
1. **Data Engineering:** [de-crypto-pipeline](https://github.com/jose-cortes-ramos/de-crypto-pipeline) - Ingesta automatizada y validacion de esquemas.
2. **Data Platform:** [gcp-data-platform-hub](https://github.com/jose-cortes-ramos/gcp-data-platform-hub) - Procesamiento en capas Medallion (Bronze, Silver, Gold).
3. **Analytical Hub:** (Este Repositorio) - Validacion de hipotesis, EDA y Serving Layer.
4. **Machine Learning:** [crypto-ml-predictor](https://github.com/jose-cortes-ramos/crypto-ml-predictor) - Clasificacion predictiva basada en anomalias de volumen.

## Key Findings: The Volume Shock Hypothesis
A traves de un analisis estadistico riguroso sobre la capa Gold, se han obtenido los siguientes hallazgos:
- **Negative Correlation Discovery:** Se identifico una correlacion de Spearman negativa significativa (-0.26, p < 0.0001) entre shocks extremos de volumen y retornos a 30 dias en Bitcoin.
- **Market Stress Indicators:** Los eventos de volumen masivos actuan frecuentemente como indicadores de capitulacion o estres de mercado en lugar de señales puramente alcistas.
- **Feature Validation:** Se validaron las variables `zscore_30d`, `price_vol_corr` y `volatility_30d` como predictores fundamentales para la fase de Machine Learning.

## Analytical Infrastructure (BigQuery Serving Layer)
Se han implementado vistas SQL optimizadas en BigQuery para centralizar la inteligencia de negocio y alimentar dashboards en Looker Studio:
- `v_dashboard_kpis.sql`: Metricas de precision y performance del ecosistema.
- `v_dashboard_timeseries.sql`: Analisis historico de precios y volumenes.
- `v_dashboard_table_tsunamis.sql`: Identificacion de eventos criticos de volumen.
- `vw_looker_master_intelligence.sql`: Vista maestra que consolida capas de tendencias, analitica y prediccion de ML.

## Technical Stack
- **Languages:** Python (Pandas, Scipy, Seaborn, Plotly), SQL (BigQuery Standard SQL).
- **Environment:** Google Cloud Platform (GCP), Virtual Environments, Jupyter Hub.
- **Methodology:** Statistical Hypothesis Testing, Medallion Architecture.

## Repository Structure
- `notebooks/`: Analisis estadistico y validacion de señales.
- `infra/bigquery/views/`: Definiciones de la capa de serving en SQL.
- `src/data/`: Conectores robustos para integracion con GCP.
