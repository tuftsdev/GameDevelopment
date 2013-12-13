package com.google.development;

import android.app.Activity;
import android.os.Bundle;
import android.view.*;
import android.widget.*;
import java.util.Date;

public class ButtonNow1 extends Activity implements View.OnClickListener
{
	private Button b;
	
	public void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		b = new Button(this);
		b.setOnClickListener(this);
		updateTime();
		setContentView(b);
	}

	public void onClick(View v)
	{
		updateTime();
	}
	
	private void updateTime()
	{
		b.setText(new Date().toString());
	}
}
