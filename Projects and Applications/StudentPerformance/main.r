require(ggplot2)

data <- read.csv("StudentPerformance/StudentsPerformance.csv")

# convert gender to binary
data$genderBIN = ifelse(data$gender == "male",1,0)
data$lunchBIN = ifelse(data$lunch == "standard",1,0)
data$testBIN = ifelse(data$test == "none",1,0)

# summary of data
print(summary(data))

# math vs reading
print(ggplot(data, aes(x=data$reading, y=data$math)) + geom_point() + geom_smooth(method=lm, se=FALSE))

# math vs writing
print(ggplot(data, aes(x=data$writing, y=data$math)) + geom_point() + geom_smooth(method=lm, se=FALSE))

# reading vs writing
print(ggplot(data, aes(x=data$writing, y=data$reading)) + geom_point() + geom_smooth(method=lm, se=FALSE))

# regression of gender vs math
print(summary(lm(data$genderBIN~data$math.score)))

# regression of gender vs reading
print(summary(lm(data$genderBIN~data$reading.score)))

# regression of gender vs writing
print(summary(lm(data$genderBIN~data$writing.score)))

# regression of lunch vs math
print(summary(lm(data$lunchBIN~data$math.score)))

# regression of lunch vs reading
print(summary(lm(data$lunchBIN~data$reading.score)))

# regression of lunch vs writing
print(summary(lm(data$lunchBIN~data$writing.score)))

# regression of test prep vs math
print(summary(lm(data$genderBIN~data$math.score)))

# regression of test prep vs reading
print(summary(lm(data$genderBIN~data$reading.score)))

# regression of test prep vs writing
print(summary(lm(data$genderBIN~data$writing.score)))
