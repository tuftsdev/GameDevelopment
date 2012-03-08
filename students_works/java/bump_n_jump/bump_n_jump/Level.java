package bump_n_jump;

import java.awt.image.BufferedImage;
import java.util.ArrayList;

/*
 * Level - tentative class for a level
 */
public class Level {
	
	protected BallSprite ballSprite;
	protected Door door;
	protected ArrayList<Dog> dogs;
	protected ArrayList<Tile> tiles;
	protected ArrayList<Star> stars;
	protected ArrayList<Spike> spikes;
	protected ArrayList<Trampoline> tramps;
	protected ArrayList<Warp> warps;
	protected double initialBallX; //for use when starting the level fresh after a death
	protected double initialBallY;
	protected int numStars;
	protected String filename, backImageName;
	protected boolean doorOpen;
	protected BufferedImage backImage;
	
	/**
	 * Level constructor.
	 * @param bs
	 * @param d
	 * @param dogs
	 * @param tiles
	 * @param stars
	 * @param spikes
	 * @param tramps
	 * @param warps
	 * @param initX
	 * @param initY
	 * @param filename
	 * @param backImage
	 */
	public Level(BallSprite bs, Door d, ArrayList<Dog> dogs, ArrayList<Tile> tiles, 
			ArrayList<Star> stars, ArrayList<Spike> spikes, ArrayList<Trampoline> tramps, ArrayList<Warp> warps,
			double initX, double initY, String filename, BufferedImage backImage, String backImageName) {
		this.ballSprite = bs;
		this.door = d;
		this.dogs = dogs;
		this.tiles = tiles;
		this.stars = stars;
		this.spikes = spikes;
		this.tramps = tramps;
		this.warps = warps;
		this.initialBallX = initX;
		this.initialBallY = initY;
		this.filename = filename;
		this.backImage = backImage;
		this.backImageName = backImageName;
		this.numStars = stars.size();
		this.doorOpen = false;
	}

	public BallSprite getBallSprite() {
		return ballSprite;
	}

	public ArrayList<Dog> getDogs() {
		return dogs;
	}
	
	public ArrayList<Tile> getTiles() {
		return tiles;
	}
	
	public Door getDoor() {
		return door;
	}

	public boolean isDoorOpen() {
		return doorOpen;
	}

	public void setDoorOpen(boolean doorOpen) {
		this.doorOpen = doorOpen;
	}

	public ArrayList<Star> getStars() {
		return stars;
	}

	public ArrayList<Spike> getSpikes() {
		return spikes;
	}

	public ArrayList<Trampoline> getTramps() {
		return tramps;
	}
	
	public int getNumStars() {
		return numStars;
	}

	public double getInitialBallX() {
		return initialBallX;
	}

	public double getInitialBallY() {
		return initialBallY;
	}

	public ArrayList<Warp> getWarps() {
		return warps;
	}

	public BufferedImage getBackImage() {
		return backImage;
	}

	public String getBackImageName() {
		return backImageName;
	}
	
	
	
}
