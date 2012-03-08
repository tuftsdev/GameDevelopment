package leveleditor;

import java.awt.Graphics;
import java.awt.geom.Rectangle2D;
import java.awt.image.BufferedImage;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

import javax.imageio.ImageIO;

public class DisplayLevel {

	// Loads in all the images that will be used.
	private static BufferedImage blankTile, blueTile, greenTile, orangeTile, purpleTile, largeStar, trampoline,
			spike, door, warpEnter, warpExit, dog, ballSprite;

	protected static ArrayList<Integer> spaceOccupied;
	
	public static boolean spaceOccupied(int index) {
		return spaceOccupied.contains(index);
	}
	
	public DisplayLevel() {
		try {
			blankTile = ImageIO.read(getClass().getResource("../images_leveledit/blankBlock.jpg"));
			blueTile = ImageIO.read(getClass().getResource("../images_leveledit/blueBlock.jpg"));
			greenTile = ImageIO.read(getClass().getResource("../images_leveledit/greenBlock.jpg"));
			orangeTile = ImageIO.read(getClass().getResource("../images_leveledit/orangeBlock.jpg"));
			purpleTile = ImageIO.read(getClass().getResource("../images_leveledit/purpleBlock.jpg"));
			largeStar = ImageIO.read(getClass().getResource("../images_leveledit/largeStar.jpg"));
			trampoline = ImageIO.read(getClass().getResource("../images_leveledit/trampoline.jpg"));
			spike = ImageIO.read(getClass().getResource("../images_leveledit/spike.jpg"));
			door = ImageIO.read(getClass().getResource("../images_leveledit/door.jpg"));
			warpEnter = ImageIO.read(getClass().getResource("../images_leveledit/warpEnter.jpg"));
			warpExit = ImageIO.read(getClass().getResource("../images_leveledit/warpExit.jpg"));
			dog = ImageIO.read(getClass().getResource("../images_leveledit/dog.jpg"));
			ballSprite = ImageIO.read(getClass().getResource("../images_leveledit/ballSprite.jpg"));
		}
		catch (IOException e) {
			System.err.println("Error reading image:" + e.toString());
		}
	}
	
	
	/*
	 * Things that must happen:
	 * Each "tile" image has dimensions (20x20, 40x40 or 60x60) in order to get displayed as GameTile.
	 * It also has an array index.  It's one number that needs to be converted into "X"- and "Y"-ness.
	 * It also has a particular image.
	 * Each tile can get painted on screen right when it is parsed.
	 * 
	 *  this.x = x;
		this.y = y;
		this.arrayIndex1 = arrayIndex1;
		this.arrayIndex2 = arrayIndex2;
		this.image = bi;
		rectangle = new Rectangle2D.Double();
		rectangle.setRect(x, y, width, height);
	 */
	
	public static void displayTheLevel(GameBoardArray gBA, Graphics g) throws IOException {
		spaceOccupied = new ArrayList<Integer>();
		
		for (int i=0; i<gBA.getGameBoard().size(); i++) {
			if (!spaceOccupied.contains(i)) {
				interpretChar(gBA.readGameBoardElement(i), i).drawSprite(g);
			}
		}
		
	}
	
	public static GameTile interpretChar(char c, int arrayIndex) throws IOException {
		GameTile gT = new GameTile();

		gT.setArrayIndex(arrayIndex);
		
		switch (c) {
		
		// This is the blank tile.
		case ' ':
			gT.setImage(blankTile);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
			
		// This is the ball sprite.
		case 'o':
			gT.setImage(ballSprite);
			gT.rectangle.setRect(gT.x,gT.y,20,40);
			
			// Claims extra space so no blank tiles are painted over it.
			// Needs: 1 space below it (Y value, so arrayIndex1)
			spaceOccupied.add(arrayIndex+Editor.tilesInRow);
			break;
		
		// Adds blue tile
		case '#':
			gT.setImage(blueTile);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
			
		// Adds green tile
		case 'g':
			gT.setImage(greenTile);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
				
		// Adds orange tile
		case '0':
			gT.setImage(orangeTile);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
			
		// Adds purple tile
		case 'p':
			gT.setImage(purpleTile);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
			
		case '*':
			gT.setImage(largeStar);
			gT.rectangle.setRect(gT.x,gT.y,40,40);
			
			// Claims extra space so no blank tiles are painted over it.
			// Needs: 1 space below it (Y value, so arrayIndex1)
			spaceOccupied.add(arrayIndex+Editor.tilesInRow);
			// Needs: 1 space to right of it (X value, so arrayIndex2)
			spaceOccupied.add(arrayIndex+1);
			// Needs: 1 space to bottom-right of it (both X and Y values)
			spaceOccupied.add(arrayIndex+Editor.tilesInRow+1);
			break;
			
		case '^':
			gT.setImage(trampoline);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
			
		case 'x':
			gT.setImage(spike);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
			
		case 'D':
			gT.setImage(door);
			gT.rectangle.setRect(gT.x,gT.y,60,60);
			
			// Claims extra space so no blank tiles are painted over it.
			// Needs: 2 spaces to right of it
			for(int i=1; i<3; i++){
				spaceOccupied.add(arrayIndex+i);
			}
			// Needs: All 3 spaces in each of the next two rows
			for(int i=Editor.tilesInRow; i<Editor.tilesInRow+3; i++) {
				spaceOccupied.add(arrayIndex+i);
			}
			for(int i=Editor.tilesInRow*2; i<Editor.tilesInRow*2+3; i++) {
				spaceOccupied.add(arrayIndex+i);
			}
			break;
			
		case '@':
			gT.setImage(warpEnter);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
			
		case 'E':
			gT.setImage(warpExit);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
			
		case 'w':
			gT.setImage(dog);
			gT.rectangle.setRect(gT.x,gT.y,40,40);
			
			// Claims extra space so no blank tiles are painted over it.
			// Needs: 1 space below it (Y value, so arrayIndex1)
			spaceOccupied.add(arrayIndex+Editor.tilesInRow);
			// Needs: 1 space to right of it (X value, so arrayIndex2)
			spaceOccupied.add(arrayIndex+1);
			// Needs: 1 space to bottom-right of it (both X and Y values)
			spaceOccupied.add(arrayIndex+Editor.tilesInRow+1);
			break;
			
		default:
			// Maybe make an "error tile" that goes here to indicate something's strange.
			gT.setImage(blankTile);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
		}
		
		return gT;
	
	}
	
	public static GameTile interpretChar(char c, int x, int y) throws IOException {
		GameTile gT = new GameTile();
		
		gT.setX(x);
		gT.setY(y);
		
		switch (c) {
		
		// This is the blank tile.
		case ' ':
			gT.setImage(blankTile);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
			
		// This is the ball sprite.
		case 'o':
			gT.setImage(ballSprite);
			gT.rectangle.setRect(gT.x,gT.y,20,40);
			break;
		
		// Adds blue tile
		case '#':
			gT.setImage(blueTile);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
			
		// Adds green tile
		case 'g':
			gT.setImage(greenTile);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
				
		// Adds orange tile
		case '0':
			gT.setImage(orangeTile);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
			
		// Adds purple tile
		case 'p':
			gT.setImage(purpleTile);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
			
		case '*':
			gT.setImage(largeStar);
			gT.rectangle.setRect(gT.x,gT.y,40,40);
			break;
			
		case '^':
			gT.setImage(trampoline);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
			
		case 'x':
			gT.setImage(spike);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
			
		case 'D':
			gT.setImage(door);
			gT.rectangle.setRect(gT.x,gT.y,60,60);
			break;
			
		case '@':
			gT.setImage(warpEnter);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
			
		case 'E':
			gT.setImage(warpExit);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
			
		case 'w':
			gT.setImage(dog);
			gT.rectangle.setRect(gT.x,gT.y,40,40);
			break;
			
		default:
			// Maybe make an "error tile" that goes here to indicate something's strange.
			gT.setImage(blankTile);
			gT.rectangle.setRect(gT.x,gT.y,20,20);
			break;
		}
		
		return gT;
	
	}
	
}
