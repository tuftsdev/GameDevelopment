var NUM_SPRITES = 10;
var SCREEN_WIDTH = 800;
var SCREEN_HEIGHT = 600;

window.onload = function() {
    var game = new Phaser.Game(SCREEN_WIDTH, SCREEN_HEIGHT, Phaser.AUTO, 'game', { preload: preload, create: create });

    function preload() {
        game.load.image('awesomeface', 'awesomeface.png');
    }

    function create() {
        for (var count = 0; count < NUM_SPRITES; count++) {
            var smiley = new Smiley(game, Math.floor(Math.random() * SCREEN_WIDTH), Math.floor(Math.random() * SCREEN_HEIGHT));
        }
    }
};
