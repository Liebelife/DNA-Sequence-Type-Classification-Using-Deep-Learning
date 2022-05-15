import pandas as pd
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns

class ClassificationMetrics: # .(torch.utils.data.Dataset) e.g. to inherit a class
    def ConfMatrix(true_labels, pred_lab, LabelNames, SuperTitle, SaveToPathName):
        cm = metrics.confusion_matrix(true_labels, pred_lab, normalize='true')
        # confusion matrix
        sns.set(font_scale=1.8)
        plt.figure(figsize=(8, 6))
        df_cm = pd.DataFrame(cm)
        df_cm.columns = LabelNames
        df_cm.index = LabelNames
        plt.suptitle(SuperTitle, size=25, x = 0.45) # for baseline and ML 0.5, for adapter 0.45
        plt.title('Confusion Matrix, normalized', fontsize=20)
        # sns.set(font_scale=1.6)
        sns.heatmap(df_cm, annot=True, cmap='Blues', annot_kws={"size": 25})  
        plt.savefig(f"{SaveToPathName}", transparent=False, dpi=80, bbox_inches="tight")
        plt.show()