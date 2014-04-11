using UnityEngine;
using System.Collections;

public class GemScript : MonoBehaviour {

	public float GemSize;

	// we can use a gameobject for this!
	public GameObject BottomRowOffsetObject;
	
	[HideInInspector]
	public MasterControl MasterControlScript;

	public int myRow;
	
	[HideInInspector]
	public bool myRowUpdated;

	public int myGemType;
	

	private float myRowPositionY;

	// Use this for initialization
	void Start () {
		Debug.Log ("Generating a Gem");
		// find that floor object
		BottomRowOffsetObject = GameObject.Find ("Floor");
		
		// find the master control script
		MasterControlScript = GameObject.Find ("Background").GetComponent<MasterControl>();
		
		
		myRowUpdated = false;
	}
	
	// Update is called once per frame
	void Update () {
		// kinda dumb, but generate the Y position from the row number
		// rows count up from the bottom
		myRowPositionY = (myRow * GemSize) + BottomRowOffsetObject.transform.position.y;
		
		if(myRowUpdated)
		{
			myRowUpdated = false;
			// turn gravity back on
			rigidbody2D.gravityScale = 1;
		}		
	}

	// fixed update is called before physics
	void FixedUpdate()
	{
		if (transform.position.y < myRowPositionY) 
		{
			// set it
			Vector3 newPosition = transform.position;
			newPosition.y = myRowPositionY;
			transform.position = newPosition;
			rigidbody2D.velocity = Vector2.zero;
			rigidbody2D.gravityScale = 0;
		}		
	}
	
	void OnMouseDown()
	{
		// gem clicked
		Debug.Log ("GEM CLICKED");
		
		// we want to tell the master control script that we were just clicked
		MasterControlScript.ClickedGem = transform.gameObject;
	}
	
}
