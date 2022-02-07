let mix = require('laravel-mix');

mix.setPublicPath('./')
    .js('assets/js/background.js', 'dist/js')
    .js('assets/js/foreground.js', 'dist/js')
    .css('assets/css/highlight.css', 'dist/css')
    .js('assets/js/popup.js', 'dist/js').vue()
