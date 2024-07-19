'%!in%' <- function(x,y)!('%in%'(x,y))
options(warn = 0)
simCities <- function(n_cities = 5) {
  cities <- matrix(runif(2*n_cities,-1,1),ncol=2)
  rownames(cities) <- 1:n_cities
  colnames(cities) <- c("x","y")
  return(cities)
}

plotCities <- function(cities, 
                       main="",
                       bg="white", 
                       main_col="black",
                       point_col="deepskyblue") {
  par(bg=bg)
  plot(cities, 
       pch=16, cex=3,
       col=point_col, 
       ylim=c(-1,1.1), xlim=c(-1,1),
       yaxt="n", xaxt="n",
       ylab="", xlab="",
       bty="n",
       main=main, col.main=main_col)
}

randomRoute <- function(cities){
  start <- as.numeric(rownames(cities)[1])
  
  route <- sample(as.numeric(rownames(cities))[-1])
  route <- c(start,route,start) # return back home
  return(route)
}

# function to plot route
plotRoute <- function(cities, 
                      route, 
                      dist=NULL, 
                      main="",
                      bg="white", 
                      main_col = "black",
                      point_col = "deepskyblue",
                      start_col = "red",
                      line_col = "black") {
  
  # plot cities
  city_colors <- c(start_col, rep(point_col,nrow(cities)))
  plotCities(cities, 
             bg=bg, 
             main=main, 
             main_col=main_col,
             point_col=city_colors[order(route)])
  
  # plot route
  for(i in 2:(length(route))) {
    lines(cities[c(route[i],route[i-1]),],
          col=line_col,
          lwd=1.5)
  }
  
  # add distance in legend
  if(!is.null(dist)) legend("topleft", 
                            bty="n", # no box around legend
                            legend=round(dist,4), 
                            bg="transparent", 
                            text.col="black")
  
}

calculateDistanceMatrix <- function(cities) return(as.matrix(dist(cities)))

calculateRouteDistance <- function(route,distMatrix=NULL){
 distance <- 0
 for (i in 2:nrow(distMatrix)) {
   distance <- distance + distMatrix[route[i-1],route[i]]
 }
 return(round(distance,digits=2))
}


generateInitialPopulation <- function(size=10,cities){
#  print(as.integer(rownames(cities)))
 # print(nrow(cities))
 # print(size)
  #print(c(runif(size,min=2,max=nrow(cities)),1))
  population <- randomRoute(cities)
  for(i in 2:size){
    population<-cbind(population,randomRoute(cities))
  }
  #print("population")
  #population <- matrix(c(replicate(n=size,c(sample(size,2:nrow(cities)),1))), ncol=nrow(cities))
  #print(population)
  return(population)
}

evaluateFitness <- function(population,distMatrix){
  fitness<-apply(population,2, calculateRouteDistance,distMatrix=distMatrix)
  population<-rbind(population,fitness)
  population<-population[,order(population[nrow(population),])]
  population<-population[-nrow(population),] #remove last row
  return(population)
}

removeLowFitness <- function(population,remove=3){
  for(i in 1:remove){
    population<-population[,1:ncol(population)]
  }
  return(population)
}

mutate <- function(child){
  p1<-runif(1, min=2, max=length(child)-1)
  p2<-p1
  while(p2==p1){
    p2<-runif(1,min=2, max=length(child)-1)
  }
  temp <- child[p1]
  child[p1] <- child[p2]
  child[p2] <-temp
  return(child)
}

generateChildren <- function(population,add=3,top=3,mutate=1){
  pop_size=ncol(population)
  for(i in 1:add){
    parent1<-floor(runif(1, min=1, max=top))
    parent2 <- parent1
    while( parent1 == parent2 ){
      parent2<-floor(runif(1, min=1, max=top))
    }
    #print(nrow(population))
    start <- floor(runif(1,min=2,max=nrow(population)-1))
    size <- floor(runif(1,min=2,max=nrow(population)-1))
    end <- min(start+size,nrow(population)-3)
    r_len <- nrow(population)
    child <- rep(-1,r_len)
    #print(child)
    child[1] <- 1
    child[r_len] <- 1
    #print(c("Start",start,end,population[start:end,parent1]))
    child[start:end] <- population[start:end,parent1]
    k<-2
    test <-0
    for( j in 1:r_len){
      #print(child)
      #print(c(j,child[j],parent1,parent2))
      if(child[j]==-1){
        while(k<nrow(population) && population[k,parent2] %in% child){
 	 k<-k+1
	}
	if(k>nrow(population)){
	  break
	}
        child[j] <- population[k,parent2]
      }
      a <- table(child)
      test<-a[names(a)==1]
      if(test>2)
	break
      if(child[1]!=1 && child[1]!=-1)
        break
    }
    if(test > 2){
        quit(save="no")
    }
    if(child[1]!=1 && child[1]!=-1)
        quit(save="no")

    mutate<-floor(runif(1,min=1,max=mutate))
    for( i in 1:mutate+1){
      child<-mutate(child)
    }
    population<-cbind(population,child)
  }
  return(population)
}



#cities<- simCities(n=20)
#save(cities,file = "cities.RData")
load("cities.RData")
#cities
distMatrix <- calculateDistanceMatrix(cities)
#distMatrix
#route <- randomRoute(cities)
#route
#calculateRouteDistance(route,distMatrix=distMatrix)


initialPop <- 100
generations <- 10
mutations <- 50
remove <- 10
top <- 1

pop <- generateInitialPopulation(size=initialPop,cities)
#print(nrow(pop))
best <- with(.Machine, double.base^double.digits)
lastPrint <- 0

for(i in 1:generations){
      pop <- evaluateFitness(pop,distMatrix=distMatrix)
      pop <- removeLowFitness(pop,remove)
      evaluateFitness(pop,distMatrix=distMatrix)
      pop <- generateChildren(pop,add=remove,top=top,mutate=mutations)
      dist = calculateRouteDistance(pop[,1],distMatrix=distMatrix)
      if(dist<best || i == lastPrint + 25){
	best<-dist
	lastPrint<-i
	print(c(as.integer(i),dist))
	plotRoute(cities,pop[,1],dist=dist)
      }
}


dist <- calculateRouteDistance(pop[,1],distMatrix=distMatrix)
print(dist)
plotRoute(cities,pop[,1],dist=dist)
