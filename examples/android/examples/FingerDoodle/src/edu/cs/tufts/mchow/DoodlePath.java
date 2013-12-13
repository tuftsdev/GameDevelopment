package edu.cs.tufts.mchow;

import android.graphics.*;

public class DoodlePath
{
	protected Paint paint;
	protected Path path;
	protected boolean eraser;
	
	public DoodlePath (Path path, Paint p, boolean eraser)
	{
		this.path = path;
		this.paint = p;
		this.eraser = eraser;
	}
}
