import numpy as np
import scipy.stats as st

np.random.seed(1)

# Create sample data.
nSet=5
if nSet==1:
    a = abs(np.random.randn(50))
    b = abs(50*np.random.randn(50))

if nSet==2:
    a=np.array([27.1,22.0,20.8,23.4,23.4,23.5,25.8,22.0,24.8,20.2,21.9,22.1,22.9,20.5,24.4])
    b=np.array([27.1,22.0,20.8,23.4,23.4,23.5,25.8,22.0,24.8,20.2,21.9,22.1,22.9,20.5,24.41])

if nSet==3:
    a=np.array([17.2,20.9,22.6,18.1,21.7,21.4,23.5,24.2,14.7,21.8])
    b=np.array([21.5,22.8,21.0,23.0,21.6,23.6,22.5,20.7,23.4,21.8])

if nSet==4:
    a=np.array([19.8,20.4,19.6,17.8,18.5,18.9,18.3,18.9,19.5,22.0])
    b=np.array([28.2,26.6,20.1,23.3,25.2,22.1,17.7,27.6,20.6,13.7])

if nSet==5:
    a = np.array([55.0, 55.0, 47.0, 47.0, 55.0, 55.0, 55.0, 63.0])
    b = np.array([55.0, 56.0, 47.0, 47.0, 55.0, 55.0, 55.0, 63.0])

obs = np.array([a,b])

chi2, p, dof, expected = st.chi2_contingency(obs)

msg = "Test Statistic : {}\np-value: {}\ndof: {}\n"
print( msg.format( chi2, p , dof,expected) )


P=1-p
if P < 0.001:
    print('Statistically highly significant:',P)
else:
    if P < 0.05:
        print('Statistically significant:',P)
    else:
        print('No conclusion')