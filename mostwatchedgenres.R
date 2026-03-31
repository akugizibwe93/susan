# Load required libraries
library(dplyr)
library(tidyr)
library(ggplot2)

# Read the dataset
df <- read.csv("E:\\Nexford-Python-Assignments2026\\module 4-assignment\\Netflix_shows_movies.csv", stringsAsFactors = FALSE)

# Split genres and count occurrences
genre_counts <- df %>%
  separate_rows(listed_in, sep = ", ") %>%   # split combined genres
  count(listed_in, sort = TRUE) %>%          # count frequency
  top_n(15, n)                               # select top 15

# Plot bar chart
ggplot(genre_counts, aes(x = n, y = reorder(listed_in, n))) +
  geom_bar(stat = "identity", fill = "red") +
  labs(
    title = "Most Watched Genres (Top 15)",
    x = "Count",
    y = "Genre"
  ) +
  theme_minimal()

