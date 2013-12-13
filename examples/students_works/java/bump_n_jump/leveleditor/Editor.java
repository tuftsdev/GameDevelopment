package leveleditor;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.lang.Character;

import javax.imageio.ImageIO;
import javax.swing.*;

/*
 * Editor - the class that contains the main game loop (is a panel).
 */
public class Editor extends JPanel implements Runnable, KeyListener, MouseListener  {

	private static final long serialVersionUID = 1L;
	private Thread mainLoop;
	
	private static final int DEFAULT_FPS = 50;
	private int fps, threadDelay;
	private Image offImage;
	private Graphics offGraphics;
	private Dimension offDimension;
	private Image backgroundImage;
	
	private boolean gameStarted;
	
	// Stuff that has to do with level editing:
	private char currentSelection;
	private int currentLevelNum;
	static StringBuffer filename;  // The filename of the levelX.txt file.
	private GameBoardArray gBA;
	private boolean levelReadyToClear = false;
	private boolean changesMade = false;  // Lets program know if no changes have been made.
	
	// The starting coordinates for the game board display.
	public static final int spaceFromTop = 50;
	public static final int spaceFromLeft = 50;
	public final static int tilesInRow = 30;  // Number of 20x20 tiles in each row -- assumed to be the same for all rows.
	public static final int sizeOfStandardTile = 20; // Everything here is based on 20 pixels (gameplay renders it in 25-pixel units)
	
	public Editor() {
		//initialize vars
		fps = DEFAULT_FPS;
		threadDelay = 1000 / fps;
		
		//mouse click info.
		addMouseListener(this);
		requestFocus();
		setFocusable(true);
		
		addKeyListener(this);
		requestFocus();
		setFocusable(true);

		// Maybe use for initial level import?   levelCreator = new LevelCreator();
		// nextLevel();
		
		GameBoardArray gBA = new GameBoardArray();
		currentLevelNum = 1;
		gBA.loadLevel("levels/level1.txt");
		//nextLevel(0);
		
		// Initially, it will be the blank tile selected.
		currentSelection = ' ';
		
		//create new thread
		mainLoop = new Thread(this);
		gameStarted = true;

	}
	
	// unsure...
	public void start() {
		mainLoop.start();
	}
	
	public void run() {

		while (Thread.currentThread() == mainLoop) {
			// Remember the starting time
			long tm = System.currentTimeMillis();
			
			repaint();
			
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
			try {
				paintFrame(offGraphics);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}

		// Paint the image onto the screen
		g.drawImage(offImage, 0, 0, null);
	}
	
	/** 
	 * steps through all level elements and repaints them.
	 * @param g
	 * @throws IOException 
	 */
	private void paintFrame(Graphics g) throws IOException {
		//paint the level #, lives, and stars left at the top of the window.
		Graphics2D g2D = (Graphics2D)g;
		g2D.drawImage(backgroundImage, 0, 0, null);
		
		g2D.setFont(new Font("Helvetica", Font.BOLD,  20));
		g2D.drawString("Current Level: " + currentLevelNum, 50, 30);
		
		g2D.setFont(new Font("Helvetica", Font.BOLD,  14));
		
		int startX = 750;
		int startY = 50;
		int spaceIncrement = 10;
		int adjustTilesToWordsVert = -15;
		int adjustTilesToWords20Horiz = -30;
		int adjustTilesToWords40Horiz = -50;
		int adjustTilesToWords60Horiz = -70;
		
		g2D.drawString("Current Selection: ", startX-75, startY-25);
		g2D.drawString("Blank Space = spacebar", startX, startY+sizeOfStandardTile+spaceIncrement);
		g2D.drawString("Blue Block = 1", startX, startY+((sizeOfStandardTile+spaceIncrement)*2));
		g2D.drawString("Green Block = 2", startX, startY+((sizeOfStandardTile+spaceIncrement)*3));
		g2D.drawString("Orange Block = 3", startX, startY+((sizeOfStandardTile+spaceIncrement)*4));
		g2D.drawString("Purple Block = 4", startX, startY+((sizeOfStandardTile+spaceIncrement)*5));
		g2D.drawString("Trampoline = T", startX, startY+((sizeOfStandardTile+spaceIncrement)*6));
		g2D.drawString("Spike = Z", startX, startY+((sizeOfStandardTile+spaceIncrement)*7));
		g2D.drawString("Warp Enter = K", startX, startY+((sizeOfStandardTile+spaceIncrement)*8));
		g2D.drawString("Warp Exit = L", startX, startY+((sizeOfStandardTile+spaceIncrement)*9));
		g2D.drawString("Small Star = A", startX, startY+((sizeOfStandardTile+spaceIncrement)*10));
		g2D.drawString("Large Star = S", startX, startY+((sizeOfStandardTile+spaceIncrement)*11));
		g2D.drawString("Dog = X", startX, startY+((sizeOfStandardTile+spaceIncrement)*13));
		g2D.drawString("Ball Sprite = B", startX, startY+((sizeOfStandardTile+spaceIncrement)*15));
		g2D.drawString("Door = 9", startX, startY+((sizeOfStandardTile+spaceIncrement)*17));
		
		g2D.drawString("To save level, press Enter", startX+75, startY+550);
		g2D.drawString("To clear level, press Backspace twice", startX+75, startY+575);
		g2D.drawString("Use left and right arrows to choose a level to edit", startX+75, startY+600);
		
		DisplayLevel dL = new DisplayLevel();
		dL.displayTheLevel(gBA, g);
				
		// Now, draw visual representations of the available choices -- in same order as the drawString commands.
		dL.interpretChar(currentSelection, startX+50, 5).drawSprite(g);
		
		dL.interpretChar(' ', startX+adjustTilesToWords20Horiz, startY+((sizeOfStandardTile+spaceIncrement))+adjustTilesToWordsVert).drawSprite(g);
		dL.interpretChar('#', startX+adjustTilesToWords20Horiz, startY+((sizeOfStandardTile+spaceIncrement)*2)+adjustTilesToWordsVert).drawSprite(g);
		dL.interpretChar('g', startX+adjustTilesToWords20Horiz, startY+((sizeOfStandardTile+spaceIncrement)*3)+adjustTilesToWordsVert).drawSprite(g);
		dL.interpretChar('0', startX+adjustTilesToWords20Horiz, startY+((sizeOfStandardTile+spaceIncrement)*4)+adjustTilesToWordsVert).drawSprite(g);
		dL.interpretChar('p', startX+adjustTilesToWords20Horiz, startY+((sizeOfStandardTile+spaceIncrement)*5)+adjustTilesToWordsVert).drawSprite(g);
		dL.interpretChar('^', startX+adjustTilesToWords20Horiz, startY+((sizeOfStandardTile+spaceIncrement)*6)+adjustTilesToWordsVert).drawSprite(g);
		dL.interpretChar('x', startX+adjustTilesToWords20Horiz, startY+((sizeOfStandardTile+spaceIncrement)*7)+adjustTilesToWordsVert).drawSprite(g);
		dL.interpretChar('@', startX+adjustTilesToWords20Horiz, startY+((sizeOfStandardTile+spaceIncrement)*8)+adjustTilesToWordsVert).drawSprite(g);
		dL.interpretChar('E', startX+adjustTilesToWords20Horiz, startY+((sizeOfStandardTile+spaceIncrement)*9)+adjustTilesToWordsVert).drawSprite(g);
		// Small Star not yet implemented -- that's why Level 5 is so barren!
		// dL.interpretChar(' ', startX+adjustTilesToWords20Horiz, startY+((sizeOfStandardTile+spaceIncrement)*10)+adjustTilesToWordsVert).drawSprite(g);
		dL.interpretChar('*', startX+adjustTilesToWords40Horiz, startY+((sizeOfStandardTile+spaceIncrement)*11)+adjustTilesToWordsVert).drawSprite(g);
		dL.interpretChar('w', startX+adjustTilesToWords40Horiz, startY+((sizeOfStandardTile+spaceIncrement)*13)+adjustTilesToWordsVert).drawSprite(g);
		dL.interpretChar('o', startX+adjustTilesToWords20Horiz, startY+((sizeOfStandardTile+spaceIncrement)*15)+adjustTilesToWordsVert).drawSprite(g);
		dL.interpretChar('D', startX+adjustTilesToWords60Horiz, startY+((sizeOfStandardTile+spaceIncrement)*17)+adjustTilesToWordsVert).drawSprite(g);
		
	}
	
	// The parameter is generally -1 (level down by 1) or 1 (level up by 1).
	// A parameter of 0 is used for loading the first level only.
	// This could be used to set custom first-level-to-load-in-editor stuffs.
	public void nextLevel(int augmentLevel) {
		
		currentLevelNum += augmentLevel;
		
		// This part gets the level loading going.
		
		filename = new StringBuffer("levels/level.txt");
		filename.insert(12, currentLevelNum);
		
		try {
			FileReader fR = new FileReader(filename.toString());
			fR.close();
			gBA.loadLevel(filename.toString());
		}

		// If file doesn't exist, create a new file! (and hope this isn't being thrown because of an error!)
		catch (IOException e) {
			System.err.println("Level does not yet exist...creating..." + e.toString());
			gBA.loadLevel();  // Loads a blank level for editing purposes.
		}
		
	}
	
	public boolean saveLevel() {
		if (!gBA.getGameBoard().contains('o') || !gBA.getGameBoard().contains('D')) {
			// IMPLEMENT Dialog box: Levels must contain a ball character and a gate before.
			// Also: Must make sure there isn't more than 1 of each?
			return false;
		}
		else {
			// IMPLEMENT Save the level! Use GameBoardArray's functions to write gBA.gameBoard out to the file.
			// This part gets the level loading going.
			
			filename = new StringBuffer("levels/level.txt");
			filename.insert(12, currentLevelNum);
			
			File f = new File(filename.toString());
			gBA.saveLevel(filename.toString());
			return true;
		}
	}
	
	public void mouseExited(MouseEvent e) {
		
	}
	public void mousePressed(MouseEvent e) {

	}
	public void mouseEntered(MouseEvent e) {

	}
	public void mouseReleased(MouseEvent e) {

	}
	public void mouseClicked(MouseEvent e) {
		// If click falls within the gameboard.
		if (e.getX() > spaceFromLeft-1 && e.getX() < spaceFromLeft + tilesInRow*sizeOfStandardTile) {
			if (e.getY() > spaceFromTop-1 && e.getX() < spaceFromTop + tilesInRow*sizeOfStandardTile) {
				// Determine the array position of the element clicked on, based on the X/Y coordinates clicked.
				gBA.editGameBoard(e.getX(), e.getY(), currentSelection);
				changesMade = true;
				repaint();
			}
		}
		
	}

	public void keyPressed(KeyEvent e) {
		// Requires backspace be pressed twice in succession for a level clearing to occur.
		if (levelReadyToClear) {
			if (e.getKeyCode() != KeyEvent.VK_BACK_SPACE) {
				levelReadyToClear = false;
			}
			else {
				gBA.loadLevel();
				changesMade = true;
				repaint();
				levelReadyToClear = false;
				return;
			}
		}
		
		if (e.getKeyCode() == KeyEvent.VK_BACK_SPACE) {
			levelReadyToClear = true;
		}
		else if (e.getKeyCode() == KeyEvent.VK_SPACE) {
			currentSelection = ' ';
		}
		else if (e.getKeyCode() == KeyEvent.VK_1) {
			currentSelection = '#';
		}
		else if (e.getKeyCode() == KeyEvent.VK_2) {
			currentSelection = 'g';
		}
		else if (e.getKeyCode() == KeyEvent.VK_3) {
			currentSelection = '0';
		}
		else if (e.getKeyCode() == KeyEvent.VK_4) {
			currentSelection = 'p';
		}
		else if (e.getKeyCode() == KeyEvent.VK_T) {
			currentSelection = '^';
		}
		else if (e.getKeyCode() == KeyEvent.VK_Z) {
			currentSelection = 'x';
		}
		else if (e.getKeyCode() == KeyEvent.VK_K) {
			currentSelection = '@';
		}
		else if (e.getKeyCode() == KeyEvent.VK_L) {
			currentSelection = 'E';
		}
		else if (e.getKeyCode() == KeyEvent.VK_A) {
			// TBA
		}
		else if (e.getKeyCode() == KeyEvent.VK_S) {
			currentSelection = '*';
		}
		else if (e.getKeyCode() == KeyEvent.VK_X) {
			currentSelection = 'w';
		}
		else if (e.getKeyCode() == KeyEvent.VK_B) {
			currentSelection = 'o';
		}
		else if (e.getKeyCode() == KeyEvent.VK_9) {
			currentSelection = 'D';
		}
		else if (e.getKeyCode() == KeyEvent.VK_ENTER) {
			// save level only if changes made.
			if (changesMade) {
				if (saveLevel()) {
					System.out.println("Level saved.");
				}
			}
		}
		else if (e.getKeyCode() == KeyEvent.VK_LEFT) {
			// if currentLevelNum <= 1, do nothing; return.
			// else:
			// save level
			// go to previous level
			if (currentLevelNum <= 1) {
				System.out.println("You can't go before Level 1.");
				return;
			}
			else if (changesMade = false) {
				// If no changes made, no save is necessary.
				return;
			}
			else {
				if (saveLevel()) {
					System.out.println("Level saved; now going to previous level.");
				}
				nextLevel(-1);
				changesMade = false;  // Resets for new level editing.
			}

		}
		else if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
			// save level, but only if changes made.
			if (changesMade) {
				if (saveLevel()) {
					System.out.println("Level saved; now going to next level.");
				}
			}
			
			// go to next level; if it doesn't exist, a blank one needs to happen.
			nextLevel(1);
			changesMade = false;  // Resets for new level editing.
		}
		// If the key isn't yet recognized, this is the catchall.
		else {
			// Do nothing.
			return;
		}
		repaint();
	}

	public void keyReleased(KeyEvent e) {
		// TODO Auto-generated method stub
		
	}

	public void keyTyped(KeyEvent e) {
		
	}

}