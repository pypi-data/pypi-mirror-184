def meta_data() -> str:
    """The Meta Data for the Custom Wordpress Theme"""
    return """
/*
Theme Name: Custom Theme
Author: Author Name
Description: A custom WP Theme made with WSK
Version: 1.0
*/
"""

def default_style() -> str:
    """The Default CSS Content"""
    return """
#hero {
    position: relative;
    height: calc(100vh - 6.7rem);
}

.overlay {
    position: relative;
    height: 100%;
    width: 100%;
    background-color: #fff;
    opacity: 0.8;
    z-index: 1;
}

.call_to_action {
    position: absolute;
    top: 25vh;
    max-width: 90vw;
    z-index: 5;
}
"""