using UnityEngine;
using System.Collections;

public class MasterControl : MonoBehaviour {

	// class member variables...

	// We need a gem to copy
	public GameObject baseGem;

	// we need a place to put the gems
	public GameObject placementObject;

	// we need to get all of the possible gem sprites
	public Sprite[] gemSpriteArray;
	
	private const int ROWCOUNT = 8;
	private const int COLCOUNT = 8;
	public float GemSize;

	// keep track of the gems we create
	public GameObject[][] gemArray;
	
	// keep track of how many gems we have in each column for creating new ones
	private int[] gemsPerColumn;


	// let the gems notify us if they were clicked
	[HideInInspector]
	public GameObject ClickedGem = null;
	// and keep track of the last gem clicked for swapping
	[HideInInspector]
	public GameObject PreviousClickedGem = null;
	
	public GameObject GemSelector;
	


	// we need to track our state - if we are "updating" or not

	private bool Updating = false;
	
	// struct for defining where a match starts/ends
	struct sMatchingGems
	{
		public int rowStart, rowEnd, colStart, colEnd;
		
		public sMatchingGems(int rS, int rE, int cS, int cE)
		{
			rowStart = rS;
			rowEnd = rE;
			colStart = cS;
			colEnd = cE;
		}
	}

	private ArrayList matches;

	// Use this for initialization
	void Start () {

		gemArray = new GameObject[ROWCOUNT][];
		for (int j = 0; j < ROWCOUNT; j++) 
		{
			gemArray[j] = new GameObject[COLCOUNT];
		}
		
		gemsPerColumn = new int[COLCOUNT];
		matches = new ArrayList();

		GenerateNewBoard();

	}
	
	void GenerateNewBoard()
	{
		// generate our first 8x8 set of gems
		for(int j = 0; j < ROWCOUNT; j++)
		{
			for(int i = 0; i < COLCOUNT; i++)
			{
				gemArray[j][i] = GenerateRandomGemAtLocation(placementObject.transform.position + new Vector3(GemSize*i, GemSize*j, 0.0f), j);
			}
		}
		
		for(int i = 0; i < COLCOUNT; i++)
		{
			gemsPerColumn[i] = ROWCOUNT;
		}
	}
	
	void DestroyEntireBoard()
	{
		// destroy every object
		for(int j = 0; j < ROWCOUNT; j++)
		{
			for(int i = 0; i < COLCOUNT; i++)
			{
				Destroy(gemArray[j][i]);
				gemArray[j][i] = null;
			}
		}
	}
	
	// Update is called once per frame
	void Update () {

		// Generate gems on the space key being pressed
		if(Debug.isDebugBuild)
		{
			if (Input.GetKeyDown (KeyCode.Space)) {
				DestroyEntireBoard();
				GenerateNewBoard();
			}
		}


		// check all of the gems to see if they're stationary
		Updating = false;
		foreach (GameObject[] gems in gemArray) 
		{
			foreach (GameObject gem in gems) 
			{
					// need to null check this
					if (gem && gem.rigidbody2D.velocity.sqrMagnitude != 0.0f) 
					{
							Updating = true;
							break; // if one gem is moving, we're still updating
					}
			}			
		}
		
		if (Updating)	
		{		
			//Debug.Log ("Updating... Can't do anything else");
		}
		else
		{			
			// check for Gem Matches
			if(matches.Count > 0)
			{
				if(Debug.isDebugBuild)
				{
					foreach(object match in matches)
					{
						sMatchingGems sMatch = (sMatchingGems)match;
						
						GameObject startGem = gemArray[sMatch.rowStart][sMatch.colStart];
						GameObject endGem = gemArray[sMatch.rowEnd][sMatch.colEnd];
						
						//Debug.Log ("trying to draw line from " + startGem.transform.position.ToString() + " to " + endGem.transform.position.ToString());
						Debug.DrawLine(startGem.transform.position, endGem.transform.position, Color.green);
					}
				}							
				
				// clear matches
				if(DestroyMatchedGems())
				{						
					// we need to compact the gem array so that we fill in the holes left and can make the
					// gems fall into their new positions						
					UpdateGemArray();
					
					// fill the board back in
					GenerateNewGems();
				}					
					
				
			}
			else
			{				
				// Check for player input
				CheckForPlayerInput();
							
				CheckForMatches(ref matches, false);								
			}
			
			
		}

	}

	// return the gem we created
	GameObject GenerateRandomGemAtLocation(Vector3 newLocation, int row)
	{
		GameObject newGem;
		newGem = (GameObject)Instantiate(baseGem);
		
		// set new settings
		// Location?
		newGem.transform.position = newLocation;
		
		// sprite
		int randomIndex = 0;
		SpriteRenderer sprRend = newGem.GetComponent<SpriteRenderer>();
		if(sprRend)
		{
			// choose a random sprite - should this always be random?
			float randomNum = Random.value; // always between 0 and 1;
			
			// we need to map this [0,1] range to [0, len(gemSpriteArray)]
			randomIndex = (int)(randomNum * gemSpriteArray.GetLength(0));
			// That should work
			
			sprRend.sprite = gemSpriteArray[randomIndex];
			
			
		}
		else
		{
			Debug.LogError("Error - no sprite renderer");
		}

		// set the row position for the gem script
		GemScript script = newGem.GetComponent<GemScript> ();
		if(script)
		{
			script.myRow = row;
			
			// store sprite type
			script.myGemType = randomIndex;
		}
		else
		{
			Debug.LogError("Error - no gem script");
		}
		
		return newGem;
	}
	
	void CheckForPlayerInput()
	{
		if(Input.GetKeyDown(KeyCode.Escape))
		{
			// let us exit
			Application.Quit();
		}
	
		// check for a clicked gem
		if(ClickedGem)
		{
			Debug.Log ("Responding to clicked gem");
			// set the gem selector to select that gem
			GemSelector.transform.position = ClickedGem.transform.position;
			// make it visible
			GemSelector.GetComponent<SpriteRenderer>().enabled = true;			
			
			// see if we can swap this gem with the previous clicked gem
			if(PreviousClickedGem && PreviousClickedGem != ClickedGem)
			{
				// find the row/column of the previous clicked gem
				int previousRow, previousCol, clickedRow, clickedCol;
				if( FindRowAndColOfGem(PreviousClickedGem, out previousRow, out previousCol)
				   && FindRowAndColOfGem(ClickedGem, out clickedRow, out clickedCol))
				 {
				 	// see if we can swap them
				 	// Gems exactly 1 row/col away
					int rowDist = Mathf.Abs(clickedRow - previousRow);
					int colDist = Mathf.Abs(clickedCol - previousCol);
				 	if( (rowDist + colDist) == 1)
				 	{
						// TEST SWAP
						// swap the two gem types
						
						int oldClickedGemType = ClickedGem.GetComponent<GemScript>().myGemType;
						int oldPrevClickeddGemType = PreviousClickedGem.GetComponent<GemScript>().myGemType;				 	
						Debug.Log("Swapping gem types " + oldClickedGemType + " and " + oldPrevClickeddGemType);
						
						PreviousClickedGem.GetComponent<GemScript>().myGemType = oldClickedGemType;
						ClickedGem.GetComponent<GemScript>().myGemType = oldPrevClickeddGemType;
						
						// test for matches with a dummy arraylist
						ArrayList testMatches = new ArrayList();
						CheckForMatches(ref testMatches, false);			 	
						if(testMatches.Count > 0)
						{							
							// we can swap the gems!
							// restore the gem types
							PreviousClickedGem.GetComponent<GemScript>().myGemType = oldPrevClickeddGemType;
							ClickedGem.GetComponent<GemScript>().myGemType = oldClickedGemType;
							
							// ideally there would be an animation there, but just assign the references and make sure the myRows are correct
							Vector3 tempPosition = ClickedGem.transform.position;
							
							gemArray[previousRow][previousCol] = ClickedGem;
							ClickedGem.GetComponent<GemScript>().myRow = previousRow;
							ClickedGem.transform.position = PreviousClickedGem.transform.position;
							
							gemArray[clickedRow][clickedCol] = PreviousClickedGem;
							PreviousClickedGem.GetComponent<GemScript>().myRow = clickedRow;
							PreviousClickedGem.transform.position = tempPosition;
							
							Debug.Log("MADE THE SWAP");
							
							// make gem selector invis and invalidate the last clicked gem
							GemSelector.GetComponent<SpriteRenderer>().enabled = false;
							PreviousClickedGem = null;
							ClickedGem = null;
							return; // we're done
						}
						else
						{
							// restore the gem types
							PreviousClickedGem.GetComponent<GemScript>().myGemType = oldPrevClickeddGemType;
							ClickedGem.GetComponent<GemScript>().myGemType = oldClickedGemType;
							
							Debug.Log ("No swap - no new matches");
						}
				 	}
				 	else
				 	{
				 		Debug.Log ("No swap - too far away");
				 	}
				 	
				 }
				else
				{
					Debug.Log ("No swap - couldn't find rows/cols");
				}
			}
			
			PreviousClickedGem = ClickedGem;
			ClickedGem = null;	
				
		}
	}
	
	bool FindRowAndColOfGem(GameObject gem, out int row, out int col)
	{
		for(int r = 0; r < ROWCOUNT; r++)
		{
			for(int c = 0; c < COLCOUNT; c++)
			{
				if(gemArray[r][c] == gem)
				{
					// found
					row = r;
					col = c;
					return true;
				}
			}
		}
		
		// not found
		row = -1;
		col = -1;
		return false;
	}
	
	void CheckForMatches(ref ArrayList matchList, bool output)
	{		
		// In the bejeweled style, there are only vertical and horizontal matches.
	
		int currentMatchingType = -1; // invalid type
		int matchLength = 0;
		
		// loop through the rows looking for horizontal matches.
		for(int j = 0; j < ROWCOUNT; j++)
		{
			if(output)
			{
				Debug.Log("Row " + j);
			}
		
			// init to invalid
			currentMatchingType = -1;
			matchLength = 0;
			
			for(int i = 0; i < COLCOUNT; i++)
			{
				if(output)
				{
					Debug.Log("Col " + i);
				}
			
				if(gemArray[j][i])
				{
					GemScript gem = gemArray[j][i].GetComponent<GemScript>();
					if(gem)
					{
						if(output)
						{
							Debug.Log("Gem " + j + "," + i + " - Type " + gem.myGemType);
						}
						
						if(gem.myGemType == currentMatchingType)
						{
						
							if(output)
							{
								Debug.Log("Match");
							}
							// match
							matchLength++;	
							// if we match on this row
							if(matchLength >= 3)
							{
								// we need to be greedy and only display this if the next gem would break the chain (or is an edge)
								if(i < COLCOUNT-1) // OFF BY ONE ERROR
								{
									// look ahead
									// get the next gem
									GemScript nextGem = gemArray[j][i+1].GetComponent<GemScript>();
									if(nextGem.myGemType == currentMatchingType)
									{
										// we match, let the loop continue
										continue;
									}
								}
								// if we get to here, then the next gem breaks the chain, or is an edge
								
								// we need to log that we have a match so that we can take care of it later
								Debug.Log ("Match on row " + (j+1) + " of gem type " + currentMatchingType);
								
								// add an entry to our matches list
								matchList.Add(new sMatchingGems(j, j, i-(matchLength-1), i));
								
							}				
						}
						else
						{
							if(output)
							{
								Debug.Log("No Match");
							}
						
							// try to match this type
							currentMatchingType = gem.myGemType;
							matchLength = 1;
						}
						
					}
				}
			}
			
			
		}
		
		// loop through the columns looking for vertical matches.
		for(int j = 0; j < COLCOUNT; j++)
		{
			// init to invalid
			currentMatchingType = -1;
			matchLength = 0;
			
			for(int i = 0; i < ROWCOUNT; i++)
			{
				if(gemArray[i][j])
				{
					GemScript gem = gemArray[i][j].GetComponent<GemScript>();
					if(gem)
					{
						if(gem.myGemType == currentMatchingType)
						{
							// match
							matchLength++;	
							// if we match on this col
							if(matchLength >= 3)
							{
								// we need to be greedy and only display this if the next gem would break the chain (or is an edge)
								if(i < ROWCOUNT-1) // OFF BY ONE ERROR
								{
									// look ahead
									// get the next gem
									GemScript nextGem = gemArray[i+1][j].GetComponent<GemScript>();
									if(nextGem.myGemType == currentMatchingType)
									{
										// we match, let the loop continue
										continue;
									}
								}
								// if we get to here, then the next gem breaks the chain, or is an edge
								Debug.Log ("Match on column " + (j+1) + " of gem type " + currentMatchingType);
								
								// add an entry to our matches list
								matchList.Add(new sMatchingGems(i - (matchLength-1),  i, j, j));
								
							}				
						}
						else
						{
							// try to match this type
							currentMatchingType = gem.myGemType;
							matchLength = 1;
						}
					}
				}
			}
			
			
		}
	
	}
	
	bool DestroyMatchedGems()
	{
		// we need to destroy the matching gems
		foreach(object m in matches)
		{
			sMatchingGems sMatch = (sMatchingGems)m;
			for(int i = sMatch.rowStart; i <= sMatch.rowEnd; i++)
			{
				for(int j = sMatch.colStart; j <= sMatch.colEnd; j++)
				{
					if(gemArray[i][j])
					{
						Destroy(gemArray[i][j]);
						gemArray[i][j] = null;
						// update our count, subtract one for the destroyed gem
						gemsPerColumn[j]--;									
					}
				}
			}
		}
		
		bool matchesCleared = matches.Count > 0;		
		matches.Clear();
		return matchesCleared;
	}
	
	void UpdateGemArray()
	{
		// iterate over the columns
		for(int col = 0; col < COLCOUNT; col++)
		{
			// counting up from the bottom
			for(int row = 0; row < ROWCOUNT; row++)
			{
				if(gemArray[row][col])
				{					
					continue;
				}
				else
				{								
					// this gem is null, assign the gem above it to this slot and make that one null
					// we need to find a gem above this one that's not null
					int higherRow = -1; // invalid
					for(int countUp = row+1; countUp < ROWCOUNT; countUp++)
					{
						if(gemArray[countUp][col])
						{
							higherRow = countUp;
							break; // found it
						}
					}
					
					if(higherRow != -1) // found a gem to bring down
					{
						// update the array
						gemArray[row][col] = gemArray[higherRow][col];
						gemArray[higherRow][col] = null; // cascade up
						
						// we need to update the gem so that it falls to the right position
						GemScript gemToUpdate = gemArray[row][col].GetComponent<GemScript>();
						gemToUpdate.myRow = row;
						// set the gem to fall again
						gemToUpdate.myRowUpdated = true;
					}	
					// else case is that there are no new gems above us - that's fine, we're going to create new ones
					
				}
			}
		}
	}
	
	void GenerateNewGems()	
	{
		// now we can use the gemsPerColumn variable to see how many new gems we need per column		
		
		for(int i = 0; i < COLCOUNT; i++)
		{
			if(gemsPerColumn[i] != ROWCOUNT)
			{
				// we need more gems
				Debug.Log("COL " + i + " needs " + (ROWCOUNT - gemsPerColumn[i]));				
				
				// if we have 3 gems missing, we need to generate gems for rows 8-3 = 5,6,7 (zero-indexed)
				// so we have the missing row count stored already
				for(int missingGemRow = gemsPerColumn[i]; missingGemRow < ROWCOUNT; missingGemRow++)
				{
					// we want to generate the gems right above the top row, and then up from there.
					Debug.Log("Generating gem for [" + missingGemRow + "][" + i + "]");
					gemArray[missingGemRow][i] = GenerateRandomGemAtLocation(placementObject.transform.position + new Vector3(GemSize*i, GemSize*(missingGemRow - gemsPerColumn[i]), 0.0f), missingGemRow);
				}
				
				// reset the count
				gemsPerColumn[i] = ROWCOUNT;
			}
		}
	}
	
	
}
