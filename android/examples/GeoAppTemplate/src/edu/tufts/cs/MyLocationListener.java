package edu.tufts.cs;

import android.location.Location;
import android.location.LocationListener;
import android.os.Bundle;

public class MyLocationListener implements LocationListener
{
	private Finder copyOfStationFinder;
	
	public MyLocationListener(Finder f)
	{
		copyOfStationFinder = f;
	}
	
	@Override
	public void onLocationChanged(Location arg0)
	{
		double latitude = arg0.getLatitude();
		double longitude = arg0.getLongitude();
		String newDispLabel = "You are at " + Double.toString(latitude) + ", " + Double.toString(longitude);
		
		// Set string in text view to the new lat, lng pair
		copyOfStationFinder.tv.setText(newDispLabel);
	}

	@Override
	public void onProviderDisabled(String arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void onProviderEnabled(String arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void onStatusChanged(String arg0, int arg1, Bundle arg2) {
		// TODO Auto-generated method stub
		
	}
}
