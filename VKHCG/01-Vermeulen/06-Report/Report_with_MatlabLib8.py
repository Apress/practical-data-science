import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

fig = plt.figure(figsize=(21, 3))
t = fig.text(0.2, 0.5, 'Practical Data Science', fontsize=75, weight=1000, va='center')
t.set_path_effects([path_effects.PathPatchEffect(offset=(4, -4), hatch='xxxx',
          facecolor='gray'),
        path_effects.PathPatchEffect(edgecolor='white', linewidth=1.1,
         facecolor='black')])
plt.plot()
plt.show()