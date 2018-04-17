import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

text = plt.text(0.5, 0.5, 'Knowledge effects the World!',
                path_effects=[path_effects.withSimplePatchShadow()])

plt.plot([0, 3, 2, 5], linewidth=4, color='black',
         path_effects=[path_effects.SimpleLineShadow(),
                       path_effects.Normal()])
plt.show()