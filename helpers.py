import seaborn as sns
import matplotlib.pyplot as plt

def dBox(data, x):
    return sns.boxplot(data=data, x=x)

def checkSkew(pandasColumn):
    res = ""
    if pandasColumn.skew() == 0:
        res = "distribusi normal"
    elif pandasColumn.skew() > 0:
        res = "right skewed"
    elif pandasColumn.skew() < 0:
        res = "left skewed"
    return res

def checkKurto(pandasColumn):
    res = ""
    if pandasColumn.kurtosis() == 3:
        res = "distribusi normal / mesokurtic"
    elif pandasColumn.kurtosis() > 0:
        res = "lepto kurtic (menjulang)"
    elif pandasColumn.kurtosis() < 0:
        res = "platy kurtic (melandai)"
    return res

def dHist(data, x):
    return sns.histplot(data=data, x=x)

def checkAgostino(df):
    from scipy.stats import normaltest
    # Uji normalitas dengan D'Agostino and Pearson's Test
    dagostino_stat, dagostino_p_value = normaltest(df['price'])

    if dagostino_p_value >= 0.05:
        # Ho
        print(f" pvalue={dagostino_p_value}, pvalue>=0.05, artinya gagal menolak Ho. Kita anggap Data terdistribusi normal")
    else:
        # H1/Ha
        print(f" pvalue={dagostino_p_value}, pvalue<=0.05, artinya berhasil menolak Ho. Kita anggap Data tidak terdistribusi normal")
