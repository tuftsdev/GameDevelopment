var NUM_SPRITES = 10;
var SCREEN_WIDTH = 800;
var SCREEN_HEIGHT = 600;

window.onload = function() {
    var game = new Phaser.Game(SCREEN_WIDTH, SCREEN_HEIGHT, Phaser.AUTO, 'game', { preload: preload, create: create });
    var awesomegroup;

    function preload() {
        game.load.image('awesomeface', 'awesomeface.png');
    }

    function create() {
    	awesomegroup = game.add.group(); // Create new group
        for (var count = 0; count < NUM_SPRITES; count++) {
            smiley = new Smiley(game, Math.floor(Math.random() * SCREEN_WIDTH), Math.floor(Math.random() * SCREEN_HEIGHT));
        	awesomegroup.add(smiley);
        }
        //console.log(awesomegroup);
    }
};
