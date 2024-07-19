library(tidyverse)
library(keras)
library(tensorflow)
library(reticulate)

model_name <- "bird_mod_15epochs_unoptimized"
setwd("birds")
label_list <- dir("train_small")
output_n <- length(label_list)
save(label_list, file="label_list.RData")

width <- 224
height<- 224
target_size <- c(width, height)
rgb <- 3 #color channels

path_train <- "train_small/"
train_data_gen <- image_data_generator(rescale = 1/255, 
  validation_split = .2)

train_images <- flow_images_from_directory(path_train,
  train_data_gen,
  subset = 'training',
  target_size = target_size,
  class_mode = "categorical",
  shuffle=F,
  classes = label_list,
  seed = 2021)

validation_images <- flow_images_from_directory(path_train,
 train_data_gen, 
  subset = 'validation',
  target_size = target_size,
  class_mode = "categorical",
  classes = label_list,
  seed = 2021)

mod_base <- application_xception(weights = 'imagenet', 
   include_top = FALSE, input_shape = c(width, height, 3))
freeze_weights(mod_base)


model_function <- function(learning_rate = 0.001, 
  dropoutrate=0.2, n_dense=1024){
  
  k_clear_session()
  
  model <- keras_model_sequential() %>%
    mod_base %>% 
    layer_global_average_pooling_2d() %>% 
    layer_dense(units = n_dense) %>%
    layer_activation("relu") %>%
    layer_dropout(dropoutrate) %>%
    layer_dense(units=output_n, activation="softmax")  
  model %>% compile(
    loss = "categorical_crossentropy",
    optimizer = optimizer_adam(lr = learning_rate),
    metrics = "accuracy"
  )
  
  return(model)
  
}
model <- model_function(n_dense=length(label_list))

batch_size <- 32
epochs <- 15

hist <- model %>% fit_generator(
  train_images,
  steps_per_epoch = (train_images$n %/% batch_size), 
  epochs = epochs, 
  validation_data = validation_images,
  validation_steps = validation_images$n %/% batch_size,
  verbose = 2
)

model %>% save_model_tf("bird_mod")


path_test <- "test_small/"

test_generator <- image_data_generator(rescale = 1/255)

test_images <- flow_images_from_directory(path_test,
   test_generator,
   target_size = target_size,
   class_mode = "categorical",
   classes = label_list,
   shuffle = F,
   seed = 2021)


model %>% evaluate_generator(test_images,
  steps = test_images$n)


predictions <- model %>% 
  predict_generator(
    generator = test_generator,
    steps = test_generator$n/epochs,
  ) %>% as.data.frame

names(predictions) <- paste0("Class",0:39)

predictions$predicted_class <- 
  paste0("Class",apply(predictions,1,which.max)-1)
predictions$true_class <- paste0("Class",test_generator$classes)

predictions %>% group_by(true_class) %>% 
  summarise(percentage_true = 100*sum(predicted_class == 
    true_class)/n()) %>% 
    left_join(data.frame(bird= names(test_generator$class_indices), 
    true_class=paste0("Class",0:39)),by="true_class") %>%
  select(bird, percentage_true) %>% 
  mutate(bird = fct_reorder(bird,percentage_true)) %>%
  ggplot(aes(x=bird,y=percentage_true,fill=percentage_true, 
    label=percentage_true)) +
  geom_col() + theme_minimal() + coord_flip() +
  geom_text(nudge_y = 3) + 
  ggtitle("Percentage correct classifications by bird species")

