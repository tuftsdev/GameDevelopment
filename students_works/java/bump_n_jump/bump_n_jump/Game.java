package bump_n_jump;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import javax.imageio.ImageIO;
import javax.swing.*;

import java.lang.Long;

/*
 * Game - the class that contains the main game loop (is a panel).
 */
public class Game extends JPanel implements Runnable, KeyListener  {

	private static final long serialVersionUID = 1L;
	private Thread mainLoop;
	
	private static final int DEFAULT_FPS = 50;
	private int fps, threadDelay;
	private Image offImage;
	private Graphics offGraphics;
	private Dimension offDimension;
	private Image backgroundImage;
	
	private Level level;
	private LevelCreator levelCreator;
	private StringBuffer filename;
	private int levelNum, livesLeft, starsLeft;
	
	private boolean gameStarted;
	private boolean beatTheGame, gameOver;
	private int menuScreen;
	private static final int MENU = 0, INSTRUCTIONS = 1, CREDITS = 2;
	private Image menuImage, instructionsImage, menuImageBeat, menuImageGameOver, credits;
	private Image arrow;
	
	private static final int ARROWY1 = 230;
	private static final int ARROWY2 = 360;
	private static final int ARROWY3 = 505;
	private int arrowX = 115, arrowY = ARROWY1;
	
	//Sounds
	//private SoundPlayback	bounceSnd;
	private SoundPlayback	dogSnd;
	private	SoundPlayback	trampSnd;
	private SoundPlayback	deadSnd;
	private	SoundPlayback	starSnd;
	private SoundPlayback	newLevelSnd;
	private SoundPlayback	gameplaySnd;
	private SoundPlayback	openingSnd;

	// Timer-related stuffs.  Points are based on the timer.
	private int timeRemaining;
	private long lastTimerUpdate;
	private boolean paused;
	
	private long totalPointsEarned; // Cumulative
	private long pointsEarned;      // Specific to the level
	
	
	public Game() {
		//initialize vars
		fps = DEFAULT_FPS;
		threadDelay = 1000 / fps;
		
		//key press info.
		addKeyListener(this);
		requestFocus();
		setFocusable(true);

		
		
		//Initialize Sounds
		//bounceSnd		=	new SoundPlayback("music/Bounce.aif");
		dogSnd			=	new SoundPlayback("music/Dog.aif");
		trampSnd		=	new SoundPlayback("music/Tramp.aif");
		deadSnd			=	new SoundPlayback("music/Dead.aif");
		starSnd			=	new SoundPlayback("music/Star.aif");
		newLevelSnd		=	new SoundPlayback("music/NewLevel.aif");
		gameplaySnd		=	new SoundPlayback("music/gameplaymusic.aif", true);
		openingSnd		=	new SoundPlayback("music/openingmusic.aif");
		

		livesLeft = 6;
		totalPointsEarned = 0;
		pointsEarned = 0;
		// The below changes the starting level number.
		//levelNum = 6;
		levelNum = 1;
		
		levelCreator = new LevelCreator();
		nextLevel();
		
		//create new thread
		mainLoop = new Thread(this);
		gameStarted = beatTheGame = gameOver = false;
		menuScreen = MENU;
		try {
			menuImage = ImageIO.read(getClass().getResource("../images/menu.jpg"));
			instructionsImage = ImageIO.read(getClass().getResource("../images/instructions.jpg"));
			menuImageBeat = ImageIO.read(getClass().getResource("../images/winScreen.jpg"));
			menuImageGameOver = ImageIO.read(getClass().getResource("../images/gameOver.jpg"));
			credits = ImageIO.read(getClass().getResource("../images/credits.jpg"));
			arrow = ImageIO.read(getClass().getResource("../images/arrow.png"));
		}
		catch (IOException e) {
			System.err.println(e.toString());
		}
		openingSnd.start();
	}
	
	private void startEverythingOver() {
		gameplaySnd.stop();
		livesLeft = 6;
		levelNum = 0;
		totalPointsEarned = 0;
		pointsEarned = 0;
		levelCreator = new LevelCreator();
		nextLevel();
		
		//create new thread
		mainLoop = new Thread(this);
		gameStarted = beatTheGame = gameOver = false;
		menuScreen = MENU;
		gameplaySnd.stop();
		openingSnd.start();
		gameplaySnd.stop();
		menuScreen();
	}
	
	/**
	 * shows the menu screen with options to show instructions, play the game, and quit.
	 */
	public void menuScreen() {
		repaint();
	}
	
	
	public void start() {
		mainLoop.start();
	}
	
	public void run() {
		
		openingSnd.stop();
		gameplaySnd.start();

		while (Thread.currentThread() == mainLoop) {
			// Remember the starting time
			long tm = System.currentTimeMillis();
			BallSprite bs = level.getBallSprite();
			
			repaint();
			
			
			//check collisions between objects:
			checkCollisions();
			
			//update everybody's positions
			if (bs.isDead()) {
				deadSnd.stop();
				deadSnd.start();

				if (livesLeft == 0) {
					// Stop level music at end of game
					gameplaySnd.stop();
					gameStarted = false;
					gameOver = true;
					
					// Gives you credit for any points accumulated during that level.
					totalPointsEarned += pointsEarned;
					
					bs.getCircle().setFrame(-10, -10, 0,0);
					bs.setIsDead(false);
					try {
						Thread.sleep(1000L);
					} catch (InterruptedException e) {}
					repaint();
					//mainLoop.stop();
				}
				else {
					livesLeft--;
					Level doOver = levelCreator.create(level.filename);
					level = doOver;
					starsLeft = level.getNumStars();
					timeRemaining = 30;  // That arbitrary 30 seconds rule again.
					pointsEarned = 0;
				}
			}
			level.getBallSprite().updateCoordinates();
			level.getBallSprite().updateFrame();

			for (Iterator <Dog> iter = level.getDogs().iterator(); iter.hasNext();) {
				Dog d = iter.next();
				d.updateCoordinates();
				d.updateFrame();
			}
			
			
			
			//if there are no stars left, open the door.
			if (!level.isDoorOpen() && starsLeft == 0 && level.getDoor().open()) {
				//we get here if we are supposed to open the door and the door is done opening.
				level.setDoorOpen(true);
				
				// Points: 5 points per second remaining when door opens
				pointsEarned += 5*timeRemaining;
			}
			
			// Delay depending on how far we are behind
			try {
				tm += threadDelay;
				Thread.sleep(Math.max(0, tm - System.currentTimeMillis()));
			}
			catch (InterruptedException e) {
				System.err.println("An error occurred: " + e.toString());
				break;
			}
		}
	}
	
	/**
	 * steps through all the lists of elements and checks for relevant collisions.
	 */
	public void checkCollisions() {
		BallSprite b = level.getBallSprite();

		//check ball collisions with dogs:
		for (Iterator <Dog> iter = level.getDogs().iterator(); iter.hasNext();) {
			Dog d = iter.next();
			if(b.collisionWith(d))
			{
				//play dog sound when dog collides with ball
				dogSnd.stop();
				dogSnd.start();
				//dogSnd.stop();
			}

		}

		//check ball collisions with ground tiles
		for (Iterator <Tile> iter = level.getTiles().iterator(); iter.hasNext();) {
			Tile t = iter.next();
			b.collisionWithBottom(t);
			b.collisionWithSide(t);
			
			if (b.collisionWithTop(t)) {
				//plays bounce sound
				//bounceSnd.stop();
				//bounceSnd.start();
			}

		}

		//check dog collisions with sides of tiles (should reverse them)
		// Is this implemented? I don't think it is.
		for (Iterator <Dog> iter = level.getDogs().iterator(); iter.hasNext();) {
			Dog d = iter.next();
			for (Iterator <Tile> i = level.getTiles().iterator(); i.hasNext();) {
				Tile t = i.next();
				d.collisionWithWall(t);
			}
			
		}
		
		//check ball collisions with spikes
		for (Iterator <Spike> iter = level.getSpikes().iterator(); iter.hasNext();) {
			Spike s = iter.next();
			b.collisionWith(s);
		}
		
		//check collisions with the door
		if (level.isDoorOpen() && b.collidesWith(level.getDoor())) {
			// Points: 8 points per second remaining when door opens
			pointsEarned += 8*timeRemaining;
			totalPointsEarned += pointsEarned;
			pointsEarned = 0;  // Resets pointsEarned for the next level.
			try {
				Thread.sleep(1000L);
			} catch (InterruptedException e) {}
			nextLevel();
			repaint();
			
		}

		for (Iterator <Trampoline> iter = level.getTramps().iterator(); iter.hasNext();) {
			Trampoline t = iter.next();
			
			if(b.collisionWith(t))
			{
				//plays trampoline sound
				trampSnd.stop();
				trampSnd.start();
				//trampSnd.stop();
			}

		}
		//collisions with stars
		for (Iterator <Star> iter = level.getStars().iterator(); iter.hasNext();) {
			Star s = iter.next();
			if (b.collidesWith(s)) {
				starSnd.stop();
				starSnd.start();
				//starSnd.stop();
				
				// Points: 3 points per second remaining at collision
				pointsEarned += 3*timeRemaining;

				s.setIsExploding(true);
				starsLeft--;
			}
		}
		
		for (Iterator <Warp> iter = level.getWarps().iterator(); iter.hasNext();) {
			Warp w = iter.next();
			if (b.collidesWith(w)) {
				b.setX(w.getExitX());
				b.setY(w.getExitY());
				
				//play a woosh sound?
			}
		}
	}
	
	
	// This is taken from Zapped.
	private void updateTimer(Graphics2D g)
	{
		// Display the time left
		long curr = SystemTimer.getTime();
		if (curr - lastTimerUpdate > 1000)
		{
			if (!paused) timeRemaining -= (int) (curr - lastTimerUpdate) / 1000;
			// The counter, for game purposes, does not go negative.
			// Otherwise, you'd start having negative points accrue.
			// Having negative points is a neat idea, but not one I'm implementing yet.
			if (timeRemaining < 0) {
				timeRemaining = 0;
			}
			lastTimerUpdate = curr;
		}
		if (paused) 
		{
			g.setFont(new Font("Helvetica Bold", Font.BOLD, 30));
			g.setColor(Color.white);
			g.drawString("GAME PAUSED",300,300);
			g.setColor(Color.yellow);
		}
		Integer timeRem = new Integer(timeRemaining);
		g.drawString("Time Left: " + timeRem.toString(), 150, 20);
	}
	
	
	/**
	 * called every time we do a repaint(); starts the repainting process for all of the things in the level.
	 */
	public void paintComponent(Graphics g) {
		
		Dimension d = getSize();
		
		//The following was stolen from AnimatedSpriteDemoPanel.java
		// Create the offscreen graphics context
		if ((offGraphics == null) || (d.width != offDimension.width) || (d.height != offDimension.height)) {
			offDimension = d;
			offImage = createImage(d.width, d.height);
			offGraphics = offImage.getGraphics();
		}

		// Erase the previous image
		offGraphics.setColor(getBackground());
		offGraphics.fillRect(0, 0, d.width, d.height);
		offGraphics.setColor(Color.black);
		
		if (gameStarted) {
			// Paint the frame into the image
			paintFrame(offGraphics);
		}
		else {
			paintMenu(offGraphics);
		}

		// Paint the image onto the screen
		g.drawImage(offImage, 0, 0, null);
	}
	
	/**
	 * paints the menu screen.
	 * @param g
	 */
	private void paintMenu(Graphics g) {
		if (menuScreen == MENU) {
			if (!beatTheGame && !gameOver) {
				g.drawImage(menuImage, 0, 0, null);
				//draw the arrow.
				g.drawImage(arrow, arrowX, arrowY, null);
			}
			else if (beatTheGame) {
				mainLoop = null;
				g.drawImage(menuImageBeat, 0, 0, null);
				g.drawString("Total Points: ", 350, 375);
				g.drawString(Long.toString(totalPointsEarned), 350, 400);
				
			}
			else if (gameOver) {
				mainLoop = null;
				g.drawImage(menuImageGameOver, 0, 0, null);
				g.drawString("Total Points: ", 350, 375);
				g.drawString(Long.toString(totalPointsEarned), 350, 400);
				deadSnd.stop();
			}
			
		}
		else if (menuScreen == INSTRUCTIONS) {
			g.drawImage(instructionsImage, 0, 0, null);
		}
		else if (menuScreen == CREDITS) {
			g.drawImage(credits, 0, 0, null);
		}
	}
	
	/** 
	 * steps through all level elements and repaints them.
	 * @param g
	 */
	private void paintFrame(Graphics g) {
		//paint the level #, lives, and stars left at the top of the window.
		Graphics2D g2D = (Graphics2D)g;
		g2D.drawImage(backgroundImage, 0, 0, null);
		
		g2D.setFont(new Font("Helvetica", Font.BOLD,  20));
		g2D.drawString("Lives: " + livesLeft, 40, 20);
		// The timer is updated in its own function.
		g2D.drawString("Level " + Integer.toString(levelNum), 325, 20);
		g2D.drawString("Points: " + Long.toString(totalPointsEarned + pointsEarned), 450, 20);
		g2D.drawString("Stars left: " + Integer.toString(starsLeft), 590, 20);
		
		// Updates timer and displays time remaining
		updateTimer(g2D);
		
		//draw the door
		level.getDoor().drawSprite(g);
		
		
		
		for (Iterator <Tile> it = level.getTiles().iterator(); it.hasNext();) {
			Tile t = it.next();
			
			//Draw the tile
			t.drawSprite(g);
		}
		for (Iterator <Star> it = level.getStars().iterator(); it.hasNext();) {
			Star s = it.next();
			
			//Draw the star
			if (s.isShown()) {
				if (s.isExploding()) {
					s.explode();
				}
				s.drawSprite(g);
			}
		}
		for (Iterator <Trampoline> it = level.getTramps().iterator(); it.hasNext();) {
			Trampoline t = it.next();
			
			//Draw the trampoline
			t.drawSprite(g);
		}
		for (Iterator <Spike> it = level.getSpikes().iterator(); it.hasNext();) {
			Spike s = it.next();
			
			//Draw the Spikes
			s.drawSprite(g);
		}
		for (Iterator <Warp> it = level.getWarps().iterator(); it.hasNext();) {
			Warp w = it.next();
			
			//Draw the Spikes
			w.drawSprite(g);
		}
		
		if (level.getDogs() != null) {
			for (Iterator <Dog> it = level.getDogs().iterator(); it.hasNext();) {
				Dog d = it.next();
				
				//Draw the dog
				d.drawSprite(g);
			}
		}
		//draw the ball		
		level.getBallSprite().drawSprite(g);
	}
	
	public void nextLevel() {
		//play sound for new level
		newLevelSnd.stop();
		newLevelSnd.start();

		try {
			Thread.sleep(1000L); //sleep one second for emphasis.
		}
		catch (InterruptedException e) {
			System.err.println("An error occurred: " + e.toString());
		}
		newLevelSnd.stop();
		
		levelNum++;
		
		filename = new StringBuffer("levels/level.txt");
		filename.insert(12, levelNum);
		try {
			FileReader fR = new FileReader(filename.toString());
			fR.close();
			level = levelCreator.create(filename.toString());
			starsLeft = level.getNumStars();
			backgroundImage = level.getBackImage();
			timeRemaining = 30;  // An arbitrary 30 seconds for each level.
			lastTimerUpdate = SystemTimer.getTime();

		}
		// If file doesn't exist, this either means I screwed up, or the game has been successfully completed.
		// Assuming the level editor worked properly, we'll go with the latter.
		catch (IOException e) {
			System.err.println("Next level file does not exist: " + e.toString());
			gameStarted = false;
			beatTheGame = true;
			gameplaySnd.stop();
			repaint();
			try {
				Thread.sleep(1000L); //sleep one second for emphasis.
			}
			catch (InterruptedException ee) {
				System.err.println("An error occurred: " + ee.toString());
			}
		}
			
	}
	
	public void keyTyped(KeyEvent e) {	
	}
	public void keyPressed(KeyEvent e) {
		if (e.getKeyCode() == KeyEvent.VK_LEFT) {
			level.getBallSprite().setLeftDown(true);
		}
		else if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
			level.getBallSprite().setRightDown(true);
		}
		else if (e.getKeyCode() == KeyEvent.VK_DOWN && !gameStarted && menuScreen == MENU) {
			//move the arrow down
			if (arrowY == ARROWY1)
				arrowY = ARROWY2;
			else if (arrowY == ARROWY2) 
				arrowY = ARROWY3;
			
			repaint();
		}
		else if (e.getKeyCode() == KeyEvent.VK_UP && !gameStarted && menuScreen == MENU) {
			//move arrow up.
			if (arrowY == ARROWY3)
				arrowY = ARROWY2;
			else if (arrowY == ARROWY2) 
				arrowY = ARROWY1;
			
			repaint();
		}
		else if (e.getKeyCode() == KeyEvent.VK_ENTER) {
			//do action that arrow is on.
			if (arrowY == ARROWY1) {
				//start the game.
				gameStarted = true;
				start();
				repaint();
			}
			else if (arrowY == ARROWY2) {
				//show instructions
				menuScreen = INSTRUCTIONS;
				repaint();
			}
			else if (arrowY == ARROWY3){
				menuScreen = CREDITS;
				repaint();
			}
		}
		else if (e.getKeyCode() == KeyEvent.VK_ESCAPE) {
			if (menuScreen == INSTRUCTIONS || menuScreen == CREDITS) {
				menuScreen = MENU;
				arrowY = ARROWY1;
				repaint();
			}
			else if ((gameOver && !gameStarted) || beatTheGame){
				gameOver = false;
				gameStarted = false;
				startEverythingOver();
			}
		}
		else if (e.getKeyCode() == KeyEvent.VK_F12) {
			nextLevel();
		}
	}
	public void keyReleased(KeyEvent e) {
		if (e.getKeyCode() == KeyEvent.VK_LEFT) {
			level.getBallSprite().setLeftDown(false);
		}
		else if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
			level.getBallSprite().setRightDown(false);
		}
	}

}