def default_header_content() -> str:
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <?php wp_head(); ?>

    <title>Default Title | <?php the_title(); ?></title>
</head>
<body>
    <header>
        <nav class="navbar navbar-light navbar-expand-lg">
            <div class="container">
                <span class="navbar-brand mb-0 h1">
                    <img class="rounded" src="https://picsum.photos/80?grayscale" />
                </span>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                    aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <!-- Replace with wordpress menu if you like -->
                    <!--<?php  wp_nav_menu(
                        array(
                            'menu' => 'primary',
                            'menu_class' => 'navbar-nav'
                        )
                    ); ?>-->
                    <ul class="navbar-nav text-center">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="#">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Features</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Pricing</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link disabled">Disabled</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>
"""

def default_page_content() -> str:
    return """
<?php get_header(); ?>

<div class="container">
    <div class="dummy_text">
        <?php the_content(); ?>
    </div>
</div>

<?php get_footer(); ?>
"""

def default_home_content() -> str:
    return """
<?php get_header(); ?>

    <section id="hero" style="background-image: url('https://picsum.photos/1920/1080'); background-size: cover; background-attachment: fixed;">
        <div class="overlay"></div>
        <div class="container">
            <div class="call_to_action text-center">
                <h3 class="action_title">Are You Looking to <b><i>Build</i></b> and <b><i>Develop</i></b> a Custom Wordpress Theme?<br><b><i>I'm Here to
                            Help!</i></b></h3>
                <hr>
                <p class="action_desc">Contact Me Today For a <b><i>FREE</i></b> Home Staging Guide</p>
                <div class="row">
                    <div class="col">
                        <input type="text" class="form-control" placeholder="Email Address" />
                    </div>
                    <div class="col">
                        <a href="#" class="btn btn-info text-white"><b>CLAIM YOUR GUIDE</b></a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section id="#"></section>
    <section id="#"></section>
    <section id="#"></section>
    <section id="contact_us">
        <div class="container">
            <footer>
                <div class="container">
                    <small>&copy; Created by WSK | Powered by Python | <a href="#"><i class="fa-brands fa-facebook"></i></a>
                        <a href="#"><i class="fa-brands fa-youtube"></i></a> <a href="#"><i
                                class="fa-brands fa-instagram"></i></a> <a href="#"><i
                                class="fa-brands fa-twitter"></i></a></small>
                </div>
            </footer>
        </div>
    </section>

<?php get_footer(); ?>
"""

def default_footer_content() -> str:
    return """
        <?php wp_footer(); ?>
    </body>
</html>
"""