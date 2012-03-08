package bump_n_jump;

import java.awt.image.BufferedImage;
import java.io.IOException;

import javax.imageio.ImageIO;

public class Trampoline extends StaticLevelElement {
	private static final double DEFAULT_WIDTH = 25;
	private static final double DEFAULT_HEIGHT = 25;

	public Trampoline(double x, double y) {
		super(x, y, DEFAULT_WIDTH, DEFAULT_HEIGHT);
		try {
			image = ImageIO.read(getClass().getResource("../images/trampoline.png"));
		}
		catch (IOException e) {
			System.err.println(e.toString());
		}
	}
	
	public Trampoline(double x, double y, BufferedImage bi) {
		super(x, y, DEFAULT_WIDTH, DEFAULT_HEIGHT, bi);
	}
}
