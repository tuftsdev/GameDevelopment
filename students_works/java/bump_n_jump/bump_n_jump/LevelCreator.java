package bump_n_jump;

import java.awt.image.BufferedImage;
import java.io.*;
import java.util.ArrayList;

import javax.imageio.ImageIO;

public class LevelCreator {
	private static final double X_INCREMENT = 25;
	private static final double Y_INCREMENT = 25;
	
	private BallSprite ballSprite;
	private Door door;
	private ArrayList<Dog> dogs;
	private ArrayList<Tile> tiles;
	private ArrayList<Star> stars;
	private ArrayList<Spike> spikes;
	private ArrayList<Trampoline> tramps;
	private ArrayList<Warp> warps;
	private double initialBallX; //for setting the initial coords of the ball.
	private double initialBallY; //this is retrieved later if the ball has to respawn.
	private double exitX = 0, exitY = 0; //for holding warp zones.
	
	private BufferedImage blueTile, greenTile, orangeTile, purpleTile; //images of the tiles.
	//could rename these blueTile, redTile, etc to match what they represent.
	
	String backImageName;
	
	/**
	 * creates an instantiation of this class, sets up some of the vars.
	 */
	public LevelCreator() {
		dogs = new ArrayList<Dog>();
		tiles = new ArrayList<Tile>();
		stars = new ArrayList<Star>();
		spikes = new ArrayList<Spike>();
		tramps = new ArrayList<Trampoline>();
		warps = new ArrayList<Warp>();
		try {
			blueTile = ImageIO.read(getClass().getResource("../images/blueBlock.jpg"));
			greenTile = ImageIO.read(getClass().getResource("../images/greenBlock.jpg"));
			orangeTile = ImageIO.read(getClass().getResource("../images/orangeBlock.jpg"));
			purpleTile = ImageIO.read(getClass().getResource("../images/purpleBlock.jpg"));
		}
		catch (IOException e) {
			System.err.println("Error reading image:" + e.toString());
		}
	}
	
	/*
	 * Takes the filename and pointers to the level's contents. 
	 */
	public Level create(String filename) {
		dogs.clear();
		tiles.clear();
		stars.clear();
		spikes.clear();
		tramps.clear();
		warps.clear();
		
		try {
	        BufferedReader in = new BufferedReader(new FileReader(filename));
	        String str;
	        double x = 0;
			double y = 0;
	        while ((str = in.readLine()) != null) {
	            //parse the string character by character.
	        	char[] array = str.toCharArray();
	        	
	        	// Somewhere in here, insert something that
	        	// allows for custom backgrounds.
	        	// I might just be able to read in the first line as a string? maybe not -- I have to read up on it.
	        	// And then have that background image will be put in:
	        	// The resulting string will be backImageName.
	        	
	        	x = 0;
	        	for (int i = 0; i < array.length; i++) {
	        		interpretChar(array[i], x, y);
	        		x += X_INCREMENT;
	        	}
	        	y += Y_INCREMENT;
	        }
	        in.close();
	        
	        //deal with warp exit zone:
	        if (warps.size() == 1) {
	        	warps.get(0).setExitX(exitX);
	        	warps.get(0).setExitY(exitY);
	        }
	    } 
		catch (IOException e) {
			System.err.println("Error reading file: " + e.toString());
	    }
		
		// This line is temporary until custom backgrounds is implemented (see the note inside the While loop, above).
		backImageName = "../images/Warp_background.jpg";
		
		BufferedImage background = null;
		try {
			 background = ImageIO.read(getClass().getResource(backImageName));
		}
		catch (IOException e) {
			System.err.println(e.toString());
		}
		
		Level l = new Level(ballSprite, door, dogs, tiles, stars, spikes, tramps, 
				warps, initialBallX, initialBallY, filename, background, backImageName);
		return l;

	}
	
	private void interpretChar(char c, double x, double y) {
		switch (c) {
		case ' ':
			break;
		case 'o':
			ballSprite = new BallSprite(x, y);
			initialBallX = x;
			initialBallY = y;
			break;
			
		// Adds blue tile
		case '#':
			tiles.add(new Tile(x, y, blueTile));
			break;
			
		// Adds green tile
		case 'g':
			tiles.add(new Tile(x, y, greenTile));
			break;
				
		// Adds orange tile
		case '0':
			tiles.add(new Tile(x, y, orangeTile));
			break;
			
		// Adds purple tile
		case 'p':
			tiles.add(new Tile(x, y, purpleTile));
			break;
			
		case '*':
			stars.add(new Star(x+7.5,y+7.5));  // Stars are 35x35 pixels. This is the standard star offset.
			break;
			
		case '^':
			tramps.add(new Trampoline(x, y));
			break;
			
		case 'x':
			spikes.add(new Spike(x, y));
			break;
			
		case 'D':
			door = new Door(x, y);
			break;
			
		case '@':
			warps.add(new Warp(x, y));
			break;
			
		case 'E':
			exitX = x;
			exitY = y;
			break;
			
		case 'w':
			dogs.add(new Dog(x, y+10)); // Adjusts for the dog being only 40 pixels high.
			break;
			
			
		default:
			//don't do anything if the character isn't recognized.
			break;
		}	
	}
}