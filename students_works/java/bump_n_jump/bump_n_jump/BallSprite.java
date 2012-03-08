package bump_n_jump;

import java.awt.*;
import java.awt.geom.*;
/*
 * BallSprite - extends Sprite. Represents the bouncing ball.
 * Includes physics and sprite rendering.
 */

public class BallSprite extends Sprite {

	private static final double GRAVITY = .4;
	private static final double DEFAULT_XSPEED = 3.0; //default movement along the x axis when moving left and right.
	private static final double DEFAULT_YSPEED = 7.0;
	private static final int NUMFRAMES = 24; //number of frames in the image strip.
	private static final int SPRITE_WIDTH = 25; //width and height of the sprite image. used for the containing circle.
	private static final int SPRITE_HEIGHT = 25;
	private double currentGravityEffect;
	private double xComponent; //won't be zero when the player hits left or right arrow key.
	private double yComponent; //represents the player's velocity.
						   //changes only when a trampoline or something is hit.
						   //this alone will dictate how high the ball will bounce.
	private Ellipse2D circle;
	private boolean leftDown; //whether the left arrow is held down or not.
	private boolean rightDown;
	private boolean collidingWithWall;
	private boolean isDead;
	
	

	/**
	 * Constructor for BallSprite
	 * @param x
	 * @param y
	 */
	public BallSprite(double x, double y) {
		super(x,y);
		frames = loadStripImageArray("../images/colorBallSprite.png", NUMFRAMES);
		circle = new Ellipse2D.Double();
		circle.setFrame((int)x, (int)y, SPRITE_WIDTH, SPRITE_HEIGHT);
		xComponent = 0;
		yComponent = DEFAULT_YSPEED;
		currentGravityEffect = 0;
		leftDown = rightDown = collidingWithWall = false;
		isDead = false;

	}

	public boolean isDead() {
		return isDead;
	}

	public void setIsDead(boolean b) {
		isDead = b;
	}
	/*
	 * updateCoordinates() - This method is to be called on every pass through the main game loop.
	 * it updates the ball's location based on what the gravity and initial upwards velocity are.
	 */
	public void updateCoordinates() {
		if (leftDown && !collidingWithWall){
			xComponent = -DEFAULT_XSPEED;
		}
		else if (rightDown && !collidingWithWall) {
			xComponent = DEFAULT_XSPEED;
		}
		else {
			xComponent = 0;
		}
		x += xComponent;
		y -= (yComponent - currentGravityEffect);
		//update the bounding circle.
		circle.setFrame((int)x, (int)y, SPRITE_WIDTH, SPRITE_HEIGHT);

		currentGravityEffect += GRAVITY;
	}

	/**
	 * called when the left key is pressed
	 * @param leftDown
	 */
	public void setLeftDown(boolean leftDown) {
		this.leftDown = leftDown;
	}
	/**
	 * called when the right key is pressed.
	 * @param rightDown
	 */
	public void setRightDown(boolean rightDown) {
		this.rightDown = rightDown;
	}

	/**
	 * set each time we check if we're colliding with a wall.
	 * @param collidingWithWall
	 */
	public void setCollidingWithWall(boolean collidingWithWall) {
		this.collidingWithWall = collidingWithWall;
	}

	public void resetYComponent() {
		yComponent = DEFAULT_YSPEED;
	}

	/**
	 * drawSprite - called whenever we refresh the screen.
	 */
	public void drawSprite(Graphics g) {
		Graphics2D g2D = (Graphics2D)g;
		g2D.drawImage(frames.get(currentFrame), (int)x, (int)y, null);
	}

	/**
	 * updateFrame - changes the frame of animation.
	 */
	public void updateFrame() {
		if (currentFrame + 1 == frames.size()) {
			currentFrame = 0;
		}
		else currentFrame++;
	}

	/**
	 * what to do if the ball collides with the top of a ground tile.
	 */
	public boolean collisionWithTop(Tile t) {
		Point p = new Point((int)circle.getCenterX(), (int)circle.getMaxY());
		
		if (t.getRectangle().contains(p)) {
			currentGravityEffect = 0;
			yComponent = DEFAULT_YSPEED;
			return true;
		}
		return false;
	}

	/**
	 * what to do if the ball collides with the side of a ground tile
	 * @param t
	 */
	public void collisionWithSide(Tile t)
	{
		Rectangle2D r = t.getRectangle();
		//get the point on the far left center of the ball.
		Point left = new Point((int)circle.getMinX(), (int)circle.getCenterY());
		//get the point on the far right center of the ball.
		Point right = new Point((int)circle.getMaxX(), (int)circle.getCenterY());
		
		if (r.contains(left)) {
			//move right to correct.
			x += r.getMaxX() - left.x;
			collidingWithWall = true;
		}
		else if (r.contains(right)) {
			//move left to correct.
			x -= right.x - r.getMinX();
			collidingWithWall = true;
		}
		else {
			collidingWithWall = false;
		}
	}

	/**
	 * what to do if the ball collides with the bottom of a ground tile
	 * (stop it from going up.)
	 * @param t
	 */
	public void collisionWithBottom(Tile t) {
		Point p = new Point((int)circle.getCenterX(), (int)circle.getMinY());
		if (t.getRectangle().contains(p)) {
			currentGravityEffect = yComponent;
			y += (t.getRectangle().getMaxY() - p.y);
		}
	}

	/*
	 * Given a dog object, find out if we collide with him.
	 */
	public boolean collisionWith(Dog dog) {
		if (circle.intersects(dog.getRectangle()) ) {
			isDead = true;
			return true;
		}
		return false;
	}

	public void collisionWith(Spike s) {
		if (circle.intersects(s.getRectangle())) {
			isDead = true;
		}
	}

	public boolean collidesWith(Star s) {
		return (circle.intersects(s.getRectangle()));
	}

	public boolean collidesWith(Door d) {
		return (circle.intersects(d.getRectangle())) ;
	}
	
	public boolean collidesWith(Warp w) {
		return (circle.intersects(w.getRectangle()));
	}

	public boolean collisionWith(Trampoline t) {
		if (circle.intersects(t.getRectangle())) {
			currentGravityEffect = 0;
			yComponent = DEFAULT_YSPEED * 2;
			return true;
		}
		return false;
	}

	public Ellipse2D getCircle() {
		return circle;
	}

}
