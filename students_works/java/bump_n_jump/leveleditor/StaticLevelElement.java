package leveleditor;

import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Rectangle2D;
import java.awt.image.BufferedImage;

/*
 * Super class for level elements
 */
public abstract class StaticLevelElement {
	protected BufferedImage image;
	protected double x, y;
	protected int arrayIndex;
	protected Rectangle2D rectangle;
	
	// These two are an offset which make it so the game objects don't start displaying at the very top-left corner.
	
	public StaticLevelElement(double x, double y, int arrayIndex, double width, double height, BufferedImage bi) {
		this.x = x;
		this.y = y;
		this.arrayIndex = arrayIndex;
		this.image = bi;
		rectangle = new Rectangle2D.Double();
		rectangle.setRect(x, y, width, height);
	}
	
	public StaticLevelElement() {
		this.image = null;
		this.x = 0;
		this.y = 0;
		this.arrayIndex = 0;
		this.rectangle = new Rectangle2D.Double();
	}
	
	public Rectangle2D getRectangle() {
		return rectangle;
	}

	public void drawSprite(Graphics g) {
		Graphics2D g2D = (Graphics2D)g;
		g2D.drawImage(image, (int)x, (int)y, null);
	}

	public double getX() {
		return x;
	}

	public double getY() {
		return y;
	}

	public BufferedImage getImage() {
		return image;
	}

	public void setImage(BufferedImage image) {
		this.image = image;
	}

	public int getArrayIndex() {
		return arrayIndex;
	}

	public void setArrayIndex(int arrayIndex) {
		this.arrayIndex = arrayIndex;
		this.setY((arrayIndex/30)*20+Editor.spaceFromTop);
		this.setX((arrayIndex%30)*20+Editor.spaceFromLeft);
	}

	public void setX(int x) {
		this.x = x;
	}

	public void setY(int y) {
		this.y = y;
	}

	public void setRectangle(Rectangle2D rectangle) {
		this.rectangle = rectangle;
	}
	
}