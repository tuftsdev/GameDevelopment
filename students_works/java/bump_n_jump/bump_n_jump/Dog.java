package bump_n_jump;

import java.awt.*;
import java.awt.geom.Rectangle2D;
/*
 * Dog - represents the enemy character that kills the ball on impact. 
 */
public class Dog extends Sprite {

	private static final int NUMFRAMES = 4; //number of frames in the image strip.
	private int direction;
	private static final int LEFT = 0;
	private static final int RIGHT = 1; //for if the dog is walking left or right.
	private static final double SPRITE_WIDTH = 200.0; //set to be the width and height of the image used.
	private static final double SPRITE_HEIGHT = 35;
	private static final double DEFAULT_SPEED = 1.5; //default speed for the dog to move.
	private static final double DEFAULT_ROOM = 200;
	private double roomToRun; // Total of how far a dog will move before changing direction. Doesn't change after set.
	private double distanceToTravel;  // How far a dog is able to move before changing direction. Updates.
	private double xComponent; //how fast the dog should move in the x direction.
	private Rectangle2D rect; //the containing rectangle.
	
	/*
	 * Constructor that takes an initial x and y.
	 */
	
	public Dog(double x, double y, double speed, double lengthToMove) {
		super(x,y);
		xComponent = speed;
		frames = loadStripImageArray("../images/dogStrip.png", NUMFRAMES);
		rect = new Rectangle2D.Double();
		rect.setRect(x, y, SPRITE_WIDTH/NUMFRAMES - 3, SPRITE_HEIGHT);
		direction = RIGHT;
		roomToRun = lengthToMove;
		distanceToTravel = roomToRun;
	}
	
	public Dog(double x, double y, double roomToMove) {
		super(x,y);
		xComponent = DEFAULT_SPEED;
		frames = loadStripImageArray("../images/dogStrip.png", NUMFRAMES);
		rect = new Rectangle2D.Double();
		rect.setRect(x, y, SPRITE_WIDTH/NUMFRAMES, SPRITE_HEIGHT);
		direction = RIGHT;
		roomToRun = roomToMove;
		distanceToTravel = roomToRun;
	}
	
	public Dog(double x, double y) {
		super(x,y);
		xComponent = DEFAULT_SPEED;
		frames = loadStripImageArray("../images/dogStrip.png", NUMFRAMES);
		rect = new Rectangle2D.Double();
		rect.setRect(x, y, SPRITE_WIDTH/NUMFRAMES, SPRITE_HEIGHT);
		direction = RIGHT;
		roomToRun = DEFAULT_ROOM;
		distanceToTravel = roomToRun;
	}
	
	
	/*
	 * drawSprite - called whenever we draw the screen.
	 */
	public void drawSprite(Graphics g) {
		Graphics2D g2D = (Graphics2D)g;
		g2D.drawImage(frames.get(currentFrame), (int)x, (int)y, null);
	}

	
	/*
	 * updateFrame - advances the frame of the sprite we are working with.
	 */
	public void updateFrame() {
		if (direction == RIGHT) {
			//change between the going left frames (2 and 3)
			if (currentFrame == 2) currentFrame++;
			else if (currentFrame == 3) currentFrame--;
			else currentFrame = 2;
		}
		else if (direction == LEFT) {
			//change between the going right frames (0 and 1)
			if (currentFrame == 0) currentFrame++;
			else if (currentFrame == 1) currentFrame--;
			else currentFrame = 0;
		}

	}
	
	/**
	 * checks if a collision has happened with a tile and will change dog's direction.
	 * @param t
	 */
	public void collisionWithWall(Tile t) {
		if (rect.intersects(t.getRectangle())) {
			changeDirection();
		}
	}
	
	/**
	 * changeDirection - to be called whenever the dog needs to change directions.
	 */
	private void changeDirection() {
		if (direction == LEFT)
			direction = RIGHT;
		else
			direction = LEFT;
	}
	
	/**
	 * moves the dog along on its path.
	 */
	public void updateCoordinates() {
		// Ensures that dogs don't wander further than we allow them to.
		if ((distanceToTravel - xComponent) < 0) {
			changeDirection();
			distanceToTravel = roomToRun;
		}
		
		if (direction == LEFT) {
			x -= xComponent;
		}
		else {
			x += xComponent;
		}

		distanceToTravel -= xComponent;
		rect.setRect(x, y, SPRITE_WIDTH/NUMFRAMES, SPRITE_HEIGHT);
	}
	
	public Rectangle2D getRectangle() {
		return rect;
	}

}