package bump_n_jump;

import java.awt.*;
import java.awt.image.*;
import java.io.*;
import javax.imageio.*;
import java.util.*;
/*
 * A sprite super class
 * Taken mostly from class examples.
 */
public abstract class Sprite
{
	protected ArrayList <BufferedImage> frames;
	protected int currentFrame;

	protected double x, y;
	
	
	public Sprite()
	{
		x = 0;
		y = 0;
		frames = new ArrayList<BufferedImage>();
		currentFrame = 0;
	}
	
	public Sprite (double initX, double initY)
	{
		x = initX;
		y = initY;
		frames = new ArrayList<BufferedImage>();
		currentFrame = 0;
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
	
	public double getX()
	{
		return x;
	}

	public void setX (double xCoord)
	{
		x = xCoord;
	}
	
	public double getY()
	{
		return y;
	}
	
	public void setY (double yCoord)
	{
		y = yCoord;
	}
	
	
	/*
	 * drawSprite - must implement this method. 
	 * We gotta see it right?
	 */
	public abstract void drawSprite (Graphics g);

	/*
	 * updateFrame - to be called to advance the sprite's image frame.
	 */
	public abstract void updateFrame();
	
	/*
	 * used to update the new coordinates of where the sprite should be.
	 */
	public abstract void updateCoordinates();
}
