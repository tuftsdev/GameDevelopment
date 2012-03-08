package bump_n_jump;

import java.awt.Graphics2D;
import java.awt.GraphicsConfiguration;
import java.awt.GraphicsEnvironment;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.util.ArrayList;

import javax.imageio.ImageIO;

public class Door extends StaticLevelElement {

	private static final double DEFAULT_WIDTH = 75;
	private static final double DEFAULT_HEIGHT = 75;
	//private BufferedImage openDoor;
	private ArrayList<BufferedImage> frames;
	private int currentFrame = 0;
	private static final int NUMFRAMES = 20;
	private boolean doneOpening = false;

	public Door(double x, double y) {
		super(x, y, x+DEFAULT_WIDTH / 2.0, y + DEFAULT_HEIGHT / 2.0, 1, 1);
		frames = loadStripImageArray("../images/doorStrip.png", NUMFRAMES);
		image = frames.get(0);
	}
	
	/**
	 * open the door.
	 */
	public boolean open() {
		currentFrame++;
		image = frames.get(currentFrame);
		if (currentFrame == NUMFRAMES - 1) {
			doneOpening = true;
		}
		return doneOpening;
	}
	
	public BufferedImage loadImageBuffered (String imageName)
	{
		GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
		GraphicsConfiguration gc = ge.getDefaultScreenDevice().getDefaultConfiguration();
		
		try {
			BufferedImage bi = ImageIO.read(getClass().getResource(imageName));
			int transparency = bi.getColorModel().getTransparency();
			BufferedImage copy = gc.createCompatibleImage(bi.getWidth(), bi.getHeight(), transparency);
			Graphics2D g2d = copy.createGraphics();
			g2d.drawImage(bi, 0, 0, null);
			g2d.dispose();
			return copy;
		}
		catch (IOException e)
		{
			System.err.println("Image loading error: " + e.toString());
			return null;
		}
	}

	public ArrayList <BufferedImage> loadStripImageArray(String imageName, int numImages)
	{
		ArrayList<BufferedImage> list = new ArrayList<BufferedImage>();
		GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
		GraphicsConfiguration gc = ge.getDefaultScreenDevice().getDefaultConfiguration();
		BufferedImage stripIm;
		
		if (numImages > 0) {
			stripIm = loadImageBuffered(imageName);
			if (stripIm != null) {
				int width = (int) stripIm.getWidth() / numImages;
				int height = stripIm.getHeight();
				int transparency = stripIm.getColorModel().getTransparency();

				Graphics2D stripGC;

				for (int i = 0; i < numImages; i++) {
					BufferedImage holder = gc.createCompatibleImage(width, height, transparency);
					list.add(holder);
					stripGC = holder.createGraphics();
					stripGC.drawImage(stripIm, 0, 0, width, height, i * width, 0, (i * width) + width, height, null);
					stripGC.dispose();
				}
				return list;
			}
		}
		return null;
	}
	
	
}
