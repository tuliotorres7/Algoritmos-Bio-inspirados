import matplotlib
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot(range(10))
fig.savefig('temp.png')