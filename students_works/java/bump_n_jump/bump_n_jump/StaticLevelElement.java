package bump_n_jump;

import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Rectangle2D;
import java.awt.image.BufferedImage;

/*
 * Super class for level elements that don't change position
 */
public abstract class StaticLevelElement {
	protected BufferedImage image;
	protected double x, y;
	protected Rectangle2D rectangle;
	
	public StaticLevelElement(double x, double y, double width, double height, BufferedImage bi) {
		this.x = x;
		this.y = y;
		this.image = bi;
		rectangle = new Rectangle2D.Double();
		rectangle.setRect(x, y, width, height);
	}
	
	public StaticLevelElement(double x, double y, double width, double height) {
		this.x = x;
		this.y = y;
		rectangle = new Rectangle2D.Double();
		rectangle.setRect(x, y, width, height);
	}
	public StaticLevelElement(double realX, double realY, double x, double y, double width, double height) {
		this.x = realX;
		this.y = realY;
		rectangle = new Rectangle2D.Double();
		rectangle.setRect(x, y, width, height);
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
	
	
	
	
}
