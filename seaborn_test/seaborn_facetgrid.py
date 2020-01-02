import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
sns.set_style('whitegrid')

titanic_pair = titanic[['age','pclass','fare']]
g = sns.pairplot(titanic_pair)
plt.show()