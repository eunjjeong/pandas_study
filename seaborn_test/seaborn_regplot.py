import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')

fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

sns.regplot(x='age',
            y='fare',
            data=titanic,
            ax=ax1)

sns.regplot(x='age',
            y='fare',
            data=titanic,
            fit_reg=False)

plt.show()