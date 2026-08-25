"""
Exemplo prático: diagnóstico de erro + tratamento de dados desbalanceados
--------------------------------------------------------------------------
Fluxo:
  1. Criar um dataset binário desbalanceado (classe minoritária = 5%)
  2. Treinar um modelo baseline (sem tratamento) e medir métricas corretas
  3. Montar uma planilha de error analysis (DataFrame)
  4. Aplicar 3 técnicas de correção: class_weight, oversampling manual, threshold tuning
  5. Comparar resultados

Requisitos: scikit-learn, pandas, numpy (todos padrão, sem dependências externas)
"""

import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    precision_recall_curve,
    f1_score,
    confusion_matrix,
)
from sklearn.utils import resample

RANDOM_STATE = 42

# ---------------------------------------------------------------------------
# 1. Criar dataset desbalanceado (95% classe 0, 5% classe 1)
# ---------------------------------------------------------------------------
X, y = make_classification(
    n_samples=5000,
    n_features=10,
    n_informative=5,
    n_redundant=2,
    weights=[0.95, 0.05],   # desbalanceamento proposital
    flip_y=0.02,            # um pouco de ruído/label noise, como em dados reais
    random_state=RANDOM_STATE,
)

X_train, X_dev, y_train, y_dev = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=RANDOM_STATE
)

print(f"Distribuição treino: {np.bincount(y_train)} (classe 0 / classe 1)")
print(f"Distribuição dev:    {np.bincount(y_dev)}\n")


# ---------------------------------------------------------------------------
# 2. Baseline: modelo simples, sem nenhum tratamento
# ---------------------------------------------------------------------------
def treinar_e_avaliar(X_tr, y_tr, X_ev, y_ev, class_weight=None, threshold=0.5, nome="modelo"):
    modelo = LogisticRegression(max_iter=1000, class_weight=class_weight, random_state=RANDOM_STATE)
    modelo.fit(X_tr, y_tr)

    probas = modelo.predict_proba(X_ev)[:, 1]
    preds = (probas >= threshold).astype(int)

    f1_minoritaria = f1_score(y_ev, preds, pos_label=1)
    print(f"--- {nome} (threshold={threshold}) ---")
    print(classification_report(y_ev, preds, digits=3))
    print(f"F1 (classe minoritária): {f1_minoritaria:.3f}\n")

    return modelo, probas, preds, f1_minoritaria


print("=" * 70)
print("BASELINE (sem tratamento algum)")
print("=" * 70)
modelo_base, probas_base, preds_base, f1_base = treinar_e_avaliar(
    X_train, y_train, X_dev, y_dev, nome="Baseline"
)


# ---------------------------------------------------------------------------
# 3. Planilha de Error Analysis
# ---------------------------------------------------------------------------
def montar_planilha_erros(X_ev, y_ev, preds, probas):
    df = pd.DataFrame(X_ev, columns=[f"feat_{i}" for i in range(X_ev.shape[1])])
    df["label_real"] = y_ev
    df["predicao"] = preds
    df["confianca"] = probas
    df["acertou"] = df["label_real"] == df["predicao"]

    erros = df[~df["acertou"]].copy()

    # Categorização heurística de erro (adaptar conforme o domínio real)
    def categorizar(row):
        if row["label_real"] == 1 and row["confianca"] < 0.3:
            return "Falso negativo - baixa confiança (padrão não capturado)"
        elif row["label_real"] == 1 and row["confianca"] >= 0.3:
            return "Falso negativo - caso limítrofe (perto do threshold)"
        elif row["label_real"] == 0 and row["confianca"] > 0.7:
            return "Falso positivo - alta confiança (possível ruído/outlier)"
        else:
            return "Falso positivo - caso limítrofe"

    erros["categoria_erro"] = erros.apply(categorizar, axis=1)
    return erros


erros_df = montar_planilha_erros(X_dev, y_dev, preds_base, probas_base)

print("=" * 70)
print("ERROR ANALYSIS - resumo por categoria")
print("=" * 70)
resumo = erros_df["categoria_erro"].value_counts(normalize=True).mul(100).round(1)
print(resumo.to_string(), "\n")
print(f"Total de erros: {len(erros_df)} de {len(y_dev)} exemplos ({len(erros_df)/len(y_dev)*100:.1f}%)\n")

# Amostra da planilha (as 5 primeiras linhas de erro, como você exportaria pra CSV/Sheets)
colunas_relevantes = ["label_real", "predicao", "confianca", "categoria_erro"]
print("Amostra da planilha de erros:")
print(erros_df[colunas_relevantes].head(5).to_string(), "\n")

# Para uso real: erros_df.to_csv("error_analysis.csv", index=False)


# ---------------------------------------------------------------------------
# 4. Técnica A: class_weight="balanced"
# ---------------------------------------------------------------------------
print("=" * 70)
print("TÉCNICA A: class_weight='balanced'")
print("=" * 70)
modelo_cw, probas_cw, preds_cw, f1_cw = treinar_e_avaliar(
    X_train, y_train, X_dev, y_dev, class_weight="balanced", nome="Class Weight"
)


# ---------------------------------------------------------------------------
# 5. Técnica B: Oversampling manual da classe minoritária (equivalente ao
#    RandomOverSampler do imbalanced-learn, mas usando só sklearn.utils.resample
#    -- útil quando não se pode instalar a lib imbalanced-learn)
# ---------------------------------------------------------------------------
print("=" * 70)
print("TÉCNICA B: Oversampling manual (resample)")
print("=" * 70)

df_train = pd.DataFrame(X_train)
df_train["target"] = y_train

maioria = df_train[df_train["target"] == 0]
minoria = df_train[df_train["target"] == 1]

minoria_upsampled = resample(
    minoria,
    replace=True,                  # amostragem com reposição
    n_samples=len(maioria),        # iguala ao tamanho da classe majoritária
    random_state=RANDOM_STATE,
)

df_balanceado = pd.concat([maioria, minoria_upsampled])
X_train_bal = df_balanceado.drop(columns="target").values
y_train_bal = df_balanceado["target"].values

print(f"Distribuição após oversampling: {np.bincount(y_train_bal)}\n")

modelo_os, probas_os, preds_os, f1_os = treinar_e_avaliar(
    X_train_bal, y_train_bal, X_dev, y_dev, nome="Oversampling"
)


# ---------------------------------------------------------------------------
# 6. Técnica C: Threshold tuning (usando o modelo baseline, só ajustando o corte)
# ---------------------------------------------------------------------------
print("=" * 70)
print("TÉCNICA C: Threshold tuning")
print("=" * 70)

precisions, recalls, thresholds = precision_recall_curve(y_dev, probas_base)
f1_scores = 2 * (precisions * recalls) / (precisions + recalls + 1e-9)
melhor_idx = np.argmax(f1_scores[:-1])  # último ponto não tem threshold correspondente
melhor_threshold = thresholds[melhor_idx]

print(f"Melhor threshold encontrado: {melhor_threshold:.3f} (threshold padrão seria 0.5)\n")

_, _, preds_tuned, f1_tuned = treinar_e_avaliar(
    X_train, y_train, X_dev, y_dev, threshold=melhor_threshold, nome="Threshold Tuning"
)


# ---------------------------------------------------------------------------
# 7. Comparação final
# ---------------------------------------------------------------------------
print("=" * 70)
print("COMPARAÇÃO FINAL (F1 da classe minoritária)")
print("=" * 70)
comparacao = pd.DataFrame({
    "Estratégia": ["Baseline", "Class Weight", "Oversampling", "Threshold Tuning"],
    "F1 (classe minoritária)": [f1_base, f1_cw, f1_os, f1_tuned],
})
comparacao = comparacao.sort_values("F1 (classe minoritária)", ascending=False)
print(comparacao.to_string(index=False))