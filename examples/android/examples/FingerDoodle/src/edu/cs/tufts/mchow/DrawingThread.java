package edu.cs.tufts.mchow;

import android.graphics.*;
import android.view.SurfaceHolder;

public class DrawingThread extends Thread
{
	private SurfaceHolder surfaceHolder;
	private FingerDoodleView fingerDoodleView;
	private boolean running;
	
	public DrawingThread (SurfaceHolder surfaceHolder, FingerDoodleView theView)
	{
		this.surfaceHolder = surfaceHolder;
		this.fingerDoodleView = theView;
		running = false;
	}
	
	public void setRunning (boolean running)
	{
		this.running = running;
	}
	
	public boolean isRunning()
	{
		return running;
	}
	
	public SurfaceHolder getSurfaceHolder()
	{
		return surfaceHolder;
	}
	
	public FingerDoodleView getFingerDoodleView()
	{
		return fingerDoodleView;
	}
	
	@Override
	public void run()
	{
		Canvas c;
		while (running) {
			c = null;
			try {
				c = surfaceHolder.lockCanvas();
				synchronized (surfaceHolder) {
					fingerDoodleView.onDraw(c);
				}
			}
			finally {
				if (c != null) {
					surfaceHolder.unlockCanvasAndPost(c);
				}
			}
		}
	}
}
