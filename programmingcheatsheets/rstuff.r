# R Programming Language Comprehensive Cheat Sheet

# Basic Operations and Data Types
# --------------------------------

# Arithmetic operations
x <- 10
y <- 5
sum <- x + y
difference <- x - y
product <- x * y
quotient <- x / y
power <- x ^ y
modulus <- x %% y

# Basic data types
numeric_var <- 42.5
integer_var <- 42L
character_var <- "Hello, R!"
logical_var <- TRUE
complex_var <- 3 + 4i

# Printing and concatenation
print(paste("The sum is:", sum))
cat("The difference is:", difference, "\n")

# Vectors
# -------
numeric_vector <- c(1, 2, 3, 4, 5)
character_vector <- c("apple", "banana", "cherry")
logical_vector <- c(TRUE, FALSE, TRUE)

# Vector operations
vector_sum <- numeric_vector + 10
vector_product <- numeric_vector * 2

# Accessing vector elements
first_element <- numeric_vector[1]
subset <- numeric_vector[2:4]

# Vector functions
length(numeric_vector)
sum(numeric_vector)
mean(numeric_vector)
median(numeric_vector)
max(numeric_vector)
min(numeric_vector)

# Matrices
# --------
matrix_data <- matrix(1:9, nrow = 3, ncol = 3)
rownames(matrix_data) <- c("R1", "R2", "R3")
colnames(matrix_data) <- c("C1", "C2", "C3")

# Matrix operations
transposed_matrix <- t(matrix_data)
matrix_product <- matrix_data %*% transposed_matrix

# Accessing matrix elements
element <- matrix_data[2, 3]
row <- matrix_data[1, ]
column <- matrix_data[, 2]

# Lists
# -----
my_list <- list(
  numbers = c(1, 2, 3),
  text = "Hello",
  matrix = matrix(1:4, nrow = 2)
)

# Accessing list elements
numbers <- my_list$numbers
text <- my_list[[2]]
matrix_element <- my_list$matrix[1, 2]

# Data Frames
# -----------
df <- data.frame(
  name = c("Alice", "Bob", "Charlie"),
  age = c(25, 30, 35),
  height = c(165, 180, 175)
)

# Accessing data frame elements
bob_age <- df$age[2]
charlie_data <- df[3, ]

# Adding new columns
df$weight <- c(60, 75, 70)

# Subsetting data frames
tall_people <- df[df$height > 170, ]

# Control Structures
# ------------------

# If-else statement
if (x > y) {
  print("x is greater than y")
} else if (x < y) {
  print("x is less than y")
} else {
  print("x is equal to y")
}

# For loop
for (i in 1:5) {
  print(paste("Iteration:", i))
}

# While loop
counter <- 1
while (counter <= 5) {
  print(paste("Counter:", counter))
  counter <- counter + 1
}

# Functions
# ---------
calculate_bmi <- function(weight, height) {
  bmi <- weight / (height / 100)^2
  return(bmi)
}

bmi_result <- calculate_bmi(70, 175)
print(paste("BMI:", round(bmi_result, 2)))

# Anonymous functions (lambda)
square <- function(x) x^2
sapply(1:5, square)

# Apply family of functions
# -------------------------
matrix_data <- matrix(1:9, nrow = 3)

# Apply function to rows or columns
row_sums <- apply(matrix_data, 1, sum)
col_means <- apply(matrix_data, 2, mean)

# lapply for lists
my_list <- list(a = 1:3, b = 4:6, c = 7:9)
squared_list <- lapply(my_list, function(x) x^2)

# sapply for simplified results
sapply_result <- sapply(my_list, sum)

# Error Handling
# --------------
tryCatch(
  expr = {
    result <- 10 / 0
  },
  error = function(e) {
    print(paste("Error:", e$message))
  },
  warning = function(w) {
    print(paste("Warning:", w$message))
  },
  finally = {
    print("This is always executed")
  }
)

# File I/O
# --------
# Writing to a file
write.csv(df, "data.csv", row.names = FALSE)

# Reading from a file
read_df <- read.csv("data.csv")

# Reading from URL
url_data <- read.csv("https://example.com/data.csv")

# Statistical Functions
# ---------------------
x <- c(1, 2, 3, 4, 5)
y <- c(2, 4, 5, 4, 5)

# Descriptive statistics
mean(x)
median(x)
sd(x)
var(x)
quantile(x)
summary(x)

# Correlation and covariance
cor(x, y)
cov(x, y)

# Linear regression
lm_model <- lm(y ~ x)
summary(lm_model)

# t-test
t.test(x, y)

# ANOVA
group <- factor(c(rep("A", 3), rep("B", 3), rep("C", 3)))
values <- c(25, 30, 35, 40, 45, 50, 55, 60, 65)
aov_result <- aov(values ~ group)
summary(aov_result)

# Data Manipulation with dplyr
# ----------------------------
library(dplyr)

# Filter rows
filtered_df <- df %>% filter(age > 25)

# Select columns
selected_df <- df %>% select(name, height)

# Arrange rows
arranged_df <- df %>% arrange(desc(age))

# Mutate (add new columns)
mutated_df <- df %>% mutate(bmi = weight / (height / 100)^2)

# Summarize data
summary_df <- df %>% 
  group_by(name) %>% 
  summarize(avg_height = mean(height))

# Data Visualization with ggplot2
# -------------------------------
library(ggplot2)

# Scatter plot
ggplot(df, aes(x = age, y = height)) +
  geom_point() +
  labs(title = "Age vs Height", x = "Age", y = "Height")

# Bar plot
ggplot(df, aes(x = name, y = age)) +
  geom_bar(stat = "identity") +
  labs(title = "Age by Name", x = "Name", y = "Age")

# Histogram
ggplot(df, aes(x = height)) +
  geom_histogram(bins = 10) +
  labs(title = "Height Distribution", x = "Height", y = "Count")

# Box plot
ggplot(df, aes(x = name, y = height)) +
  geom_boxplot() +
  labs(title = "Height Distribution by Name", x = "Name", y = "Height")

# Working with Dates and Times
# ----------------------------
library(lubridate)

# Creating date objects
date1 <- ymd("2023-06-20")
date2 <- dmy("20/06/2023")
datetime <- ymd_hms("2023-06-20 14:30:00")

# Date arithmetic
date_diff <- date2 - date1
future_date <- date1 + days(7)

# Extracting components
year(date1)
month(date1)
day(date1)
wday(date1, label = TRUE)

# String Manipulation
# -------------------
text <- "Hello, R Programming!"

# String functions
nchar(text)
tolower(text)
toupper(text)
substr(text, start = 1, stop = 5)
strsplit(text, split = " ")

# Regular expressions
grepl("R", text)
gsub("R", "Python", text)

# Working with Factors
# --------------------
gender <- factor(c("Male", "Female", "Male", "Female", "Male"))
levels(gender)
table(gender)

# Reordering factor levels
gender_reordered <- factor(gender, levels = c("Female", "Male"))

# Advanced Data Structures
# ------------------------
# Arrays
arr <- array(1:24, dim = c(2, 3, 4))

# Lists of lists
nested_list <- list(
  person1 = list(name = "Alice", age = 25),
  person2 = list(name = "Bob", age = 30)
)

# Environment
my_env <- new.env()
my_env$x <- 10
my_env$y <- 20

# Formulas
my_formula <- y ~ x + I(x^2)

# S3 and S4 Objects
# -----------------
# S3 class
person <- list(name = "Alice", age = 25)
class(person) <- "Person"

print.Person <- function(x) {
  cat("Name:", x$name, "\n")
  cat("Age:", x$age, "\n")
}

# S4 class
setClass("Employee",
  slots = c(
    name = "character",
    age = "numeric",
    salary = "numeric"
  )
)

# Create an S4 object
emp <- new("Employee", name = "Bob", age = 30, salary = 50000)

# Parallel Computing
# ------------------
library(parallel)

# Detect number of cores
num_cores <- detectCores()

# Create a cluster
cl <- makeCluster(num_cores)

# Parallel computation example
parSapply(cl, 1:1000000, sqrt)

# Stop the cluster
stopCluster(cl)

# Web Scraping
# ------------
library(rvest)

# Read HTML content
webpage <- read_html("https://example.com")

# Extract specific elements
titles <- webpage %>% html_nodes("h2") %>% html_text()

# Database Interaction
# --------------------
library(RSQLite)

# Connect to SQLite database
con <- dbConnect(RSQLite::SQLite(), "my_database.sqlite")

# Write data to database
dbWriteTable(con, "my_table", df)

# Read data from database
result <- dbGetQuery(con, "SELECT * FROM my_table")

# Close connection
dbDisconnect(con)

# Machine Learning with caret
# ---------------------------
library(caret)

# Split data into training and testing sets
set.seed(123)
train_index <- createDataPartition(df$height, p = 0.8, list = FALSE)
train_data <- df[train_index, ]
test_data <- df[-train_index, ]

# Train a model
model <- train(height ~ age + weight, data = train_data, method = "lm")

# Make predictions
predictions <- predict(model, newdata = test_data)

# Evaluate the model
mse <- mean((test_data$height - predictions)^2)
print(paste("Mean Squared Error:", mse))

# Creating R Packages
# -------------------
# This is a conceptual example and cannot be run directly

# Package structure
# my_package/
# ├── DESCRIPTION
# ├── NAMESPACE
# ├── R/
# │   └── functions.R
# ├── man/
# │   └── function_documentation.Rd
# └── tests/
#     └── testthat/
#         └── test_functions.R

# Example function in functions.R
#' Add two numbers
#'
#' @param x A numeric value
#' @param y A numeric value
#' @return The sum of x and y
#' @export
add_numbers <- function(x, y) {
  return(x + y)
}

# Example test in test_functions.R
test_that("add_numbers works correctly", {
  expect_equal(add_numbers(2, 3), 5)
})

# Building and checking the package
# In the terminal:
# R CMD build my_package
# R CMD check my_package_1.0.tar.gz

# Interactive Visualizations
# --------------------------
library(plotly)

# Create an interactive scatter plot
p <- plot_ly(df, x = ~age, y = ~height, type = "scatter", mode = "markers",
             text = ~paste("Name:", name, "<br>Age:", age, "<br>Height:", height),
             hoverinfo = "text")

# Add layout details
p <- p %>% layout(title = "Interactive Age vs Height Plot",
                  xaxis = list(title = "Age"),
                  yaxis = list(title = "Height"))

# Display the plot
p

# Reproducible Research
# ---------------------
# This is a conceptual example of using R Markdown

# ---
# title: "My R Markdown Report"
# author: "Your Name"
# date: "`r Sys.Date()`"
# output: html_document
# ---

# ```{r setup, include=FALSE}
# knitr::opts_chunk$set(echo = TRUE)
# ```

# ## Introduction

# This is an R Markdown document. Markdown is a simple formatting syntax for authoring HTML, PDF, and MS Word documents.

# ```{r cars}
# summary(cars)
# ```

# ## Including Plots

# You can also embed plots, for example:

# ```{r pressure, echo=FALSE}
# plot(pressure)
# ```

# Performance Optimization
# ------------------------
# Vectorization
slow_sum <- function(x) {
  sum <- 0
  for (i in x) {
    sum <- sum + i
  }
  return(sum)
}

fast_sum <- function(x) {
  return(sum(x))
}

# Profiling
Rprof("profile.out")
result <- slow_sum(1:1000000)
Rprof(NULL)
summaryRprof("profile.out")

# Memory management
object.size(df)
gc()  # Garbage collection

# Advanced Topics
# ---------------
# Closures
create_counter <- function() {
  count <- 0
  function() {
    count <<- count + 1
    return(count)
  }
}

counter <- create_counter()
counter()  # 1
counter()  # 2

# Metaprogramming
my_function <- function(x) {
  x^2
}

body(my_function) <- quote({
  x^3
})

# Non-standard evaluation
library(rlang)

my_summarize <- function(data, var) {
  var <- enquo(var)
  summarize(data, mean = mean(!!var), sd = sd(!!var))
}

my_summarize(df, age)

# This cheat sheet covers a wide range of R programming concepts and techniques.
# It's designed to be comprehensive, but remember that R has many more packages and functionalities.
# Always refer to official documentation and keep learning!