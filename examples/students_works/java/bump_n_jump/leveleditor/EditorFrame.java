package leveleditor;

import java.awt.*;
import javax.swing.*;

/*
 * GameFrame - the JFrame that contains the game panel.
 * Main method is here.
 */
public class EditorFrame extends JFrame {

	private static final long serialVersionUID = 1L;
	private int frameWidth = 1200, frameHeight = 700;
	
	/**
	 * Main method - create a new game frame.
	 */
	public static void main(String args[]) {
		EditorFrame gf = new EditorFrame();
		gf.setDefaultCloseOperation(EXIT_ON_CLOSE);
	}
	
	
	/**
	 * EditorFrame constructor - create the frame and add the game object to it.
	 */
	public EditorFrame() {
		setTitle("Bump 'n' Jump!");
		setSize(frameWidth, frameHeight);
		Editor g = new Editor();
		Container contentPane = getContentPane();
		contentPane.add(g);
		setVisible(true);
	}
	
	
}