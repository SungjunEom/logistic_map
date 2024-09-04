logistic = function(x, r){
  return(r*x*(1-x))
}

r <- seq(3.4, 4, 0.001)
x <- 0.2
record <- data.frame(x=c(0.0), r=c(0.0))
for(i in 1:1000){
  x=logistic(x,r)
  if(i>700){
    # plot(r,x)
    record <- rbind(record, list(x,r))
  }
}
record <- record[-1,]
plot(record$r, record$x, pch=20, cex=0.1)