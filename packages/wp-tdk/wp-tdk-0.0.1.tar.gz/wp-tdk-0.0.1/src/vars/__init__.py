file_names = [
    "index",  # If your Theme provides its own templates, index.php must be present
    "comments",  # The comments template
    "front-page",  # The front page template
    "header",  # The head of the html document
    "home",  # The home page template, which is the front page by default. If you use a static front page this is the template for the page with the latest posts
    "single",  # Used when a single post is queried, index.php is used if the query template is not present.  Use also, "single-{post-type}.php" for displaying single posts of a custom post type
    "page",  # Used when a single page is queried
    "category",  # Used when a category is queried
    "tag",  # Used whe a tag is queried
    "taxonomy",  # Used when a term in a custom taxonomy is queried
    "author",  # Used when an author is queried
    "date",  # Used when a date or time is queried. Year, month, day, hour, minute, second
    "archive",  # Used when a category, author, or date is queried. Note that this template will be overridden by category.php, author.php, and date.php for their respective query types
    "search",  # Used when a search is performed
    "attachment",  # Used when viewing a single attachment
    "image",  # Used when viewing a single image attachment. If not present, attachment.php will be used
    "404",  # Used when WordPress cannot find a post or page that matches the query
    "functions",  # Default functions
    "style",  # Meta Data Sheet
    "main",  # Main Style Sheet.  If Sass is used this is the file to overwrite
    "footer",  # The foot of the html document
]