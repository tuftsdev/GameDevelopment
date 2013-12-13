package edu.cs.tufts.mchow;

import android.graphics.*;
import android.graphics.Paint.Cap;
import android.graphics.Paint.Style;
import android.graphics.Paint.Join;

import java.util.*;

public class Doodle
{
	public static final int DEFAULT_STROKE_WIDTH = 3;
	protected int backgroundColor;
	protected Paint currentPaint;
	protected float lastX, lastY;
	protected ArrayList <DoodlePath> paths;
	protected boolean started;
	protected boolean touchDown;
	protected boolean eraser;
	
	public Doodle()
	{
		backgroundColor = Color.BLACK;
		currentPaint = new Paint();
		currentPaint.setColor(Color.GREEN);
		currentPaint.setStrokeWidth(DEFAULT_STROKE_WIDTH);
		setPaintDefaults(currentPaint);
		paths = new ArrayList<DoodlePath>();
		lastX = 0;
		lastY = 0;
		started = false;
		touchDown = false;
		eraser = false;
	}
	
	private void setPaintDefaults (Paint p)
	{
		p.setDither(true);
		p.setStrokeCap(Cap.ROUND);
		p.setStrokeJoin(Join.ROUND);
		p.setStyle(Style.FILL_AND_STROKE);		
	}
	
	public void add (Path path)
	{
		Paint p = new Paint();
		p.setStrokeWidth(currentPaint.getStrokeWidth());
		setPaintDefaults(p);
		if (eraser) {
			p.setColor(backgroundColor);
			paths.add(new DoodlePath(path, p, true));
		}
		else {
			p.setColor(currentPaint.getColor());
			paths.add(new DoodlePath(path, p, false));
		}
	}
}
