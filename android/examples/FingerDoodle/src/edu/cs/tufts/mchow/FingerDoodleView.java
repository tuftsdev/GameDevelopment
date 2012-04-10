package edu.cs.tufts.mchow;

import android.content.Context;
import android.graphics.*;
//import android.util.Log;
import android.view.*;

public class FingerDoodleView extends SurfaceView implements SurfaceHolder.Callback
{
	protected Doodle doodle;
	protected DrawingThread thread;
	
	public FingerDoodleView (Context context)
	{
		super(context);
		doodle = new Doodle();
		getHolder().addCallback(this);
		thread = new DrawingThread(getHolder(), this);
		setFocusable(true);
	}

	public DrawingThread getDrawingThread()
	{
		return thread;
	}
	
	@Override
	public void surfaceChanged(SurfaceHolder holder, int format, int width, int height) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void surfaceCreated(SurfaceHolder holder)
	{
		// Resolves the ERROR/AndroidRuntime(327): java.lang.IllegalThreadStateException: Thread already started.
		// See explanation for this at http://code.google.com/p/android/issues/detail?id=972
		if (thread.getState() == Thread.State.TERMINATED) {
			thread = new DrawingThread(getHolder(), this);
			thread.setRunning(true);
			thread.start();
		}
		else {
			thread.setRunning(true);
			thread.start();
		}
	}

	@Override
	public void surfaceDestroyed(SurfaceHolder holder)
	{
		boolean retry = true;
		thread.setRunning(false);
		while (retry) {
			try {
				thread.join();
				retry = false;
			}
			catch (InterruptedException e) {
			}
		}
	}
	
	@Override
	public void onDraw (Canvas canvas)
	{
		Paint backgroundPaint = new Paint();
		backgroundPaint.setColor(doodle.backgroundColor);
		canvas.drawPaint(backgroundPaint);
		for (DoodlePath p: doodle.paths) {
			canvas.drawPath(p.path, p.paint);
		}
	}
	
	private void add (MotionEvent event)
	{
		synchronized (thread.getSurfaceHolder()) {
			float x = event.getX();
			float y = event.getY();

			if (doodle.started) {
				if (event.getAction() == MotionEvent.ACTION_MOVE && doodle.touchDown) {
					Path p = new Path();
					p.moveTo(doodle.lastX, doodle.lastY);
					p.lineTo(x, y);
					doodle.add(p);
					doodle.lastX = x;
					doodle.lastY = y;
				}
				else if (event.getAction() == MotionEvent.ACTION_DOWN && !doodle.touchDown) {
					doodle.touchDown = true;
					doodle.lastX = x;
					doodle.lastY = y;
				}
				else if (event.getAction() == MotionEvent.ACTION_UP) {
					doodle.touchDown = false;
					doodle.lastX = x;
					doodle.lastY = y;
				}
			}
			else {
				doodle.started = true;
				if (event.getAction() == MotionEvent.ACTION_DOWN && !doodle.touchDown) {
					doodle.touchDown = true;
					doodle.lastX = x;
					doodle.lastY = y;
					
					// For the case of drawing a "dot"
					Path p = new Path();
					p.moveTo(doodle.lastX, doodle.lastY);
					p.lineTo(x, y);
					doodle.add(p);
				}
			}
		}
	}
	
	@Override
	public boolean onTouchEvent (MotionEvent event)
	{
		add(event);
		return true;
	}
	
	@Override
	public boolean onTrackballEvent (MotionEvent event)
	{
		add(event);
		return true;		
	}
}
