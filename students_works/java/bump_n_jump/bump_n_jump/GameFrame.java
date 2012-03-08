package bump_n_jump;

import java.awt.*;
import javax.swing.*;

/*
 * GameFrame - the JFrame that contains the game panel.
 * Main method is here.
 */
public class GameFrame extends JFrame {

	private static final long serialVersionUID = 1L;
	private int frameWidth = 750, frameHeight = 772;
	
	/**
	 * Main method - create a new game frame.
	 */
	public static void main(String args[]) {
		GameFrame gf = new GameFrame();
		gf.setDefaultCloseOperation(EXIT_ON_CLOSE);
	}
	
	
	/**
	 * GameFrame constructor - create the frame and add the game object to it.
	 */
	public GameFrame() {
		setTitle("Bump 'n' Jump!");
		setSize(frameWidth, frameHeight);
		Game g = new Game();
		Container contentPane = getContentPane();
		contentPane.add(g);
		setVisible(true);
	}
	
	
	
	
}
