package bump_n_jump;

import java.io.IOException;

import javax.imageio.ImageIO;

/**
 * A Warp objects sucks the player in and spits out at a different location in the level.
 * @author Aaron Haurwitz
 *
 */
public class Warp extends StaticLevelElement {
	private double exitX, exitY;
	private static final double DEFAULT_WIDTH = 25, DEFAULT_HEIGHT = 25;
	
	public Warp(double x, double y) {
		super(x, y, DEFAULT_WIDTH, DEFAULT_HEIGHT);
		try {
			image = ImageIO.read(getClass().getResource("../images/warp.png"));
		}
		catch (IOException e) {
			System.err.println(e.toString());
		}
	}

	

	public double getExitX() {
		return exitX;
	}

	public void setExitX(double exitX) {
		this.exitX = exitX;
	}

	public double getExitY() {
		return exitY;
	}

	public void setExitY(double exitY) {
		this.exitY = exitY;
	}
}
