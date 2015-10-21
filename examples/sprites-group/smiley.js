Smiley.prototype = Object.create(Phaser.Sprite.prototype);
Smiley.prototype.constructor = Smiley;
Smiley.prototype.MAX_SPEED = 10;
Smiley.prototype.dx = 0;
Smiley.prototype.dy = 0;

function Smiley (game, x, y) {
    Phaser.Sprite.call(this, game, x, y, 'awesomeface');
    Smiley.prototype.game = game;
    this.dx = Math.floor(Math.random() * this.MAX_SPEED);
    this.dy = Math.floor(Math.random() * this.MAX_SPEED);
    this.scale.set(0.025, 0.025);
    this.anchor.setTo(0.5, 0.5);
    // The following is no longer necessary especially if you are adding sprite to a group
    //game.add.existing(this);
}

Smiley.prototype.update = function() {
    if ((this.x + this.dx) <= 0) {
        this.dx = this.dx * -1;
    }
    if ((this.x + this.dx) >= this.game.width) {
        this.dx = this.dx * -1;
    }
    if ((this.y + this.dy) <= 0) {
        this.dy = this.dy * -1;
    }
    if ((this.y + this.dy) >= this.game.height) {
        this.dy = this.dy * -1;
    }
    this.x = this.x + this.dx;
    this.y = this.y + this.dy;
}
