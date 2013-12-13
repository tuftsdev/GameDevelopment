package com.google.development;

import android.app.Activity;
import android.os.Bundle;

public class DrawingTest extends Activity
{
	public void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(new SimpleDrawingView(this));
	}
}
