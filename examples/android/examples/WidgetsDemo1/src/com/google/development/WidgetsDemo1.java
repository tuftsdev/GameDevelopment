package com.google.development;

import android.app.Activity;
import android.os.Bundle;
import android.widget.*;

public class WidgetsDemo1 extends Activity implements CompoundButton.OnCheckedChangeListener
{
	private CheckBox cb;
	
	public void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);
		cb = (CheckBox)findViewById(R.id.check);
		cb.setOnCheckedChangeListener(this);
	}
	
	public void onCheckedChanged(CompoundButton buttonView, boolean isChecked)
	{
		if (isChecked) {
			cb.setText("This checkbox is checked");
		}
		else {
			cb.setText("This checkbox is unchecked");
		}
	}
}
