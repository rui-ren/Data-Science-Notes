
# A/B test
import statsmodels.api as sm


effect_size = sm.stats.proportion_effectsize(0.0131, 0.011)
analysis = sm.stats.TTestIndPower()
result = analysis.solve_power(effect_size=effect_size,
                               alpha=0.07, power=0.8, alternative='larger')
print('Sample size: %.3f' % result)




