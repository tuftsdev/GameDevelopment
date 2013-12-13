package leveleditor;

import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;

public class GameTile extends StaticLevelElement {

	public GameTile(double x, double y, int arrayIndex,
			double width, double height, BufferedImage image) {
		super(x, y, arrayIndex, width, height, image);
		// TODO Auto-generated constructor stub
	}
	
	public GameTile() {
		super();
	}
	
	public void drawSprite(Graphics g) {
		Graphics2D g2D = (Graphics2D)g;
		g2D.drawImage(image, (int)x, (int)y, null);
	}
	
}
