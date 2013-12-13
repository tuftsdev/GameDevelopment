package bump_n_jump;

import java.awt.Graphics2D;
import java.awt.GraphicsConfiguration;
import java.awt.GraphicsEnvironment;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.util.ArrayList;

import javax.imageio.ImageIO;

/**
 * The stars to collect
 * @author Aaron Haurwitz
 *
 */
public class Star extends StaticLevelElement {
	private static final double DEFAULT_WIDTH = 25;
	private static final double DEFAULT_HEIGHT = 25;
	private boolean shown;
	private ArrayList<BufferedImage> frames;
	private int currentFrame = 0;
	private static final int NUMFRAMES = 3;
	private boolean isExploding = false;
	
	public Star(double x, double y, BufferedImage bi) {
		super(x, y, DEFAULT_WIDTH, DEFAULT_HEIGHT, bi);
		shown = true;
	}
	
	public Star(double x, double y) {
		super(x, y, DEFAULT_WIDTH, DEFAULT_HEIGHT);
		try {
			image = ImageIO.read(getClass().getResource("../images/star.png"));
		}
		catch (IOException e) {
			System.err.println(e.toString());
		}
		shown = true;
		frames = loadStripImageArray("../images/starStrip.png", NUMFRAMES);
	}

	public boolean isShown() {
		return shown;
	}

	public void setShown(boolean shown) {
		this.shown = shown;
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
	
	/**
	 * called when a star is hit.
	 * @return
	 */
	public void explode() {
		if (currentFrame < 1) {
			x -= 13;
			y -= 13;
			rectangle.setRect(-10, -10, 0, 0);
		}

		
		image = frames.get(currentFrame);
		if (currentFrame == NUMFRAMES - 1) {
			isExploding = false;
			shown = false;
			return;
		}
		currentFrame++;
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

	public void setIsExploding(boolean isExploding) {
		this.isExploding = isExploding;
		rectangle.setRect(-10, -10, 0, 0);
	}

	public boolean isExploding() {
		return isExploding;
	}

}
