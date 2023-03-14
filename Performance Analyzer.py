from common import *

network, df = specifyNetwork()

# Create a scatter plot of packet loss vs latency/signal
plt.scatter( df['Packet Loss(%)'], df['Latency(ms)'])
plt.xlabel('Packet Loss (%)')
plt.ylabel('Latency (ms)')
plt.title(f"Network performance for {network}")
plt.show()
