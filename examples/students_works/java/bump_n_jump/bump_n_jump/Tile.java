package bump_n_jump;

import java.awt.image.BufferedImage;

public class Tile extends StaticLevelElement {
	public static final double DEFAULT_WIDTH = 25;
	public static final double DEFAULT_HEIGHT = 25;
	
	
	public Tile(double x, double y, BufferedImage bi)  {
		super(x, y, DEFAULT_WIDTH, DEFAULT_HEIGHT, bi);
	}
	
	
	
}
