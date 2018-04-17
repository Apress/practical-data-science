# library
library(igraph)

# Create data
data=matrix(sample(0:1, 400, replace=TRUE, prob=c(0.8,0.2)), nrow=20)
network=graph_from_adjacency_matrix(data , mode='undirected', diag=F )

# When ploting, we can use different layouts:
par(mfrow=c(2,2), mar=c(1,1,1,1))
plot(network, layout=layout.sphere, main="sphere")
plot(network, layout=layout.circle, main="circle")
plot(network, layout=layout.random, main="random")
plot(network, layout=layout.fruchterman.reingold, main="fruchterman.reingold")