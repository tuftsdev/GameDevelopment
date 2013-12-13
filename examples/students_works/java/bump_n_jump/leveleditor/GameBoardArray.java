package leveleditor;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class GameBoardArray {

	private static ArrayList<Character> gameBoard;
	
	GameBoardArray() {
		gameBoard = new ArrayList<Character>();
	}

	public void setGameBoard(ArrayList<Character> gameBoard) {
		this.gameBoard = gameBoard;
	}

	public static ArrayList<Character> getGameBoard() {
		return gameBoard;
	}
	
	public static void addGameBoardElement(char c) {
		gameBoard.add(c);
	}
	
	public static char readGameBoardElement(int index) {
		return gameBoard.get(index);
	}
	
	// Loads an existing level into the array for editing.
	public static void loadLevel(String filename) {
		
		gameBoard.clear();  // Removes the current level so a new one can be loaded.
		
		try {
	        BufferedReader in = new BufferedReader(new FileReader(filename));
	        String str;
	        while ((str = in.readLine()) != null) {
	            //parse the string character by character.
	        	char[] array = str.toCharArray();
	        	for (int i = 0; i < array.length; i++) {
	        		addGameBoardElement(array[i]);  // Add each element into the gameBoard array.
	        	}
	        }
	        in.close();
	        
	    } 
		catch (IOException e) {
			System.err.println("Error reading file: " + e.toString());
	    }

	}
	
	// Loads a blank level into the array for editing.
	public static void loadLevel() {
		gameBoard.clear();
		for (int i=0; i < 29*30; i++) {
			addGameBoardElement(' ');
		}
		for (int i=0; i<30; i++) {
			addGameBoardElement('#');
		}
	}
	
	// This needs to be written/implemented/etc.
	// When saving, something needs to erase any "hidden tiles" (b/c of how I couldn't
	// get some good MouseListeners going).  Kinda like DisplayLevel's array
	// with the array elements that couldn't write out to the screen, but the reverse-ish.
	public static void saveLevel(String filename) {
		try {
	        BufferedWriter out = new BufferedWriter(new FileWriter(filename));

	        for (int y = 0; y<30; y++) {
	        	for (int x = 0; x<30; x++) {
	        		out.write(readGameBoardElement(y*30+x));
	        	}
	        	out.write("\n");
	        }
	        //this doesn't yet implement protections against hidden tiles,
	        //nor is there any protection on making sure ball, door, warp pair must be one
	        //and only one of each. I don't know where this check will happen.

	        out.close();
	        
	    } 
		catch (IOException e) {
			System.err.println("Error printing to file: " + e.toString());
	    }
	}
	
	private static int findArrayLocation(int x, int y) {
		// Offset for the starting point of the game board
		x -= Editor.spaceFromLeft;
		y -= Editor.spaceFromTop;
		
		// Now, find the top-left corner coordinate of the GameTile in question
		x -= x % Editor.sizeOfStandardTile;
		y -= y % Editor.sizeOfStandardTile;
		
		// Then, find the array location.
		x = x/Editor.sizeOfStandardTile;
		y = y/Editor.sizeOfStandardTile*Editor.tilesInRow;
		
		// Voila, the array location!
		return x+y;
	}
	
	public static void editGameBoard(int x, int y, char newTile) {
		// First, determine the array element being edited.
		int arrayLocation = findArrayLocation(x,y);
		
		// Now, edit it.
		gameBoard.remove(arrayLocation);
		gameBoard.add(arrayLocation, newTile);
	}
	
}
