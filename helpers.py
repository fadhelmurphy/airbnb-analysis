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
    return sns.histplot(data=data, x=x, kde=True)
