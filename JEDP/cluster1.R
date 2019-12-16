library(tidyverse)

# Import Bible data set.
bible <- read_tsv("asv/asv_utf8.txt", skip = 7)

# Import "Index to Name" Mapping.
book_names <- read_tsv("asv/book_names.txt", col_names = c("orig_book_index", "name"))

# Add "name" column to bible.
bible <- plyr::join(bible, book_names, by = "orig_book_index")