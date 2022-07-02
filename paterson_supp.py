# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# %%
data = pd.read_excel(
    r'/Users/michaelschaid/GitHub/Patterson_supplement/data/Breastfeeding_Support_Figure_Data.xlsx')

data = (data.rename(columns={'Time point-month': 'Time(months)',
                             'perception of support': 'Perception Of Support',
                             'breastfeeding intensity': 'Breastfeeding Intensity',
                             'risk ratio ': 'Risk Ratio'})

        )

# %%
color = ['red', 'black']
markers = {'high': 'o', 'medium': 's'}

sns.set(font_scale=2, style='white')
sns.relplot(data=data, y='Time(months)', x='Risk Ratio',
            hue='Perception Of Support', palette=color,
            style='Breastfeeding Intensity', markers=markers, s=125, edgecolor='black',
            height=8, legend='full')
# plt.spines['left'].set_position(('data', 0))
sns.despine(left=True)
plt.axvline(x=1, color='black')

# plt.xscale('log')
plt.ylim(6.5, 0.5)


for low, high, ratio in zip(data['CI low'], data['CI high'], data['Time(months)']):
    plt.plot((low, high), (ratio, ratio), '-', color='grey', alpha=0.75)

plt.rcParams['svg.fonttype'] = 'none'  # save text as text in svg
plt.savefig('/Users/michaelschaid/GitHub/Patterson_supplement/data/fig.tiff',
            dpi=300,
            transparent=True)
plt.savefig('/Users/michaelschaid/GitHub/Patterson_supplement/data/fig.svg',
            dpi=300,
            transparent=True)
plt.show()

# 



