def default_sass() -> str:
    return """
.overlay {
    position: relative;
    height: 100%;
    width: 100%;
    background-color: #fff;
    opacity: 0.8;
    z-index: 1;
}

#hero {
    position: relative;
    height: calc(100vh - 6.7rem);

    .call_to_action {
        position: absolute;
        top: 25vh;
        max-width: 90vw;
        z-index: 5;
    }
}
"""