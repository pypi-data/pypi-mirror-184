def golden_content() -> str:
    """The Default Content for Empty PHP Files"""
    return """
<?php
    // Silence is Golden 
"""

def default_functions() -> str:
    return """
<?php

function load_css() {
    // Bootstrap
    wp_register_style('BootstrapCSS', 'https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css');
    wp_enqueue_style('BootstrapCSS');

    // Custom
    wp_register_style('mainCSS', get_template_directory_uri() . '/css/main.css', array(), '1.0');
    wp_enqueue_style('mainCSS');
}
add_action('wp_enqueue_scripts', 'load_css');

function load_js() {
    // FontAwesome 6
    wp_register_script('FontAwesome', 'https://kit.fontawesome.com/dc8a96ec90.js', array(), '6.2.1', false);
    wp_enqueue_script('FontAwesome');
    
    // Bootstrap
    wp_register_script('BootstrapJS', 'https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js', array(), '5.2.3', true);
    wp_enqueue_script('BootstrapJS');
}
add_action('wp_enqueue_scripts', 'load_js');
"""

def functions_no_bs() -> str:
    return """
<?php

function load_css() {
    wp_register_style('mainCSS', get_template_directory_uri() . '/css/main.css', array(), '1.0');
    wp_enqueue_style('mainCSS');
}
add_action('wp_enqueue_scripts', 'load_css');

function load_js() {
    // FontAwesome 6
    wp_register_script('FontAwesome', 'https://kit.fontawesome.com/dc8a96ec90.js', array(), '6.2.1', false);
    wp_enqueue_script('FontAwesome');
}
add_action('wp_enqueue_scripts', 'load_js');   
"""

def default_theme_options() -> str:
    return """
// Theme Options
add_theme_support('menus');

// Add Thumbnail Support
function thumbnail_support() {
    add_theme_support( 'post-thumbnails' );
}
add_action('after_setup_theme', 'thumbnail_support');
"""