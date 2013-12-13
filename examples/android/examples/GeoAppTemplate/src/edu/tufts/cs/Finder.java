package edu.tufts.cs;

import android.app.Activity;
import android.location.LocationManager;
import android.os.Bundle;
import android.widget.TextView;

/*
 *  Debugging points
 *  
 *  geo fix -71.0975 42.346389
 *  geo fix -71.11982 42.406949
 *  geo fix -71.054456 42.366328
 *  geo fix -71.0512929 42.4931982
 */

public class Finder extends Activity
{
	// Constants
	private final int DEFAULT_GPS_MIN_TIME = 1; // in milliseconds
	private final int DEFAULT_GPS_MIN_DISTANCE = 1; // in meters
	
	// A simple text view
	protected TextView tv;
	
	// Location manager
	private LocationManager lm;
	
	// Location listener, necessary for location manager
	private MyLocationListener ll;
	
	@Override
	public void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		
		// Set up location detection stuff
		lm = (LocationManager) this.getSystemService(LOCATION_SERVICE);
	
		// Set up my location listener
		ll= new MyLocationListener(this);
		lm.requestLocationUpdates(LocationManager.GPS_PROVIDER,
				DEFAULT_GPS_MIN_TIME,
				DEFAULT_GPS_MIN_DISTANCE,
				ll);
		
		// Initialize text view
		tv = new TextView(this);
		tv.setText("This works!");
		tv.setHeight(18);
		setContentView(tv);
    }
}
