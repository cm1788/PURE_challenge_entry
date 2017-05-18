library("vegan")
library("bipartite")

setwd('Documents/postdoc/pure_challenge/')
getwd()
df=read.csv(file='R_edges.csv')
df$newcol <- rep(1,nrow(df)) # make new column
web=frame2webs(df, varnames=c("PUBLICATION_ID", "PERSON_ID","newcol"))
plotweb(web$`1`, col.interaction='purple')

web=read.csv(file='r_edges_p9742.csv')
plotweb(web[2], col.interaction='grey', low.spacing=0.1, bor.col.interaction='black', col.high='blue', col.low='green', bor.col.high='black', bor.col.low='black', low.lablength=0, high.lablength=0)

png("single_auhtor.png", width=1800, height=1200)
dx <- dev.cur()
dev.set(2)
dev.copy(which=dx)
dev.set(dx)
dev.off()

#visweb(web$`1`)
bw = betweenness_w(web$`1`)
head(bw)

aweb = web$`1`
aweb.node

nodespec(aweb)  ## specialisation..

metaComputeModules(aweb)
mods = computeModules(aweb)

plotModuleWeb(moduleWebObject, plotModules=TRUE, rank=FALSE, weighted=TRUE, display-
                Alabels=TRUE, displayBlabels=TRUE, labsize=1, plotsize=12, xlabel="", ylabel="", square.border="white",
              fromDepth=0, upToDepth=-1