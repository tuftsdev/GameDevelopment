package com.google.development;

import android.view.*;
import android.content.Context;
import android.graphics.*;

public class SimpleDrawingView extends View
{
	public SimpleDrawingView (Context context)
	{
		super(context);
	}
	
	public void onDraw (Canvas canvas)
	{
		super.onDraw(canvas);
		Paint p = new Paint();
		
		// Clear the background to white
		p.setColor(Color.WHITE);
		
		// Draw a blue circle
		canvas.drawPaint(p);
		p.setColor(Color.BLUE);
		canvas.drawCircle(100, 100, 25, p);
		
		// Draw red text
		p.setColor(Color.RED);
		p.setTextSize(24);
		p.setTypeface(Typeface.DEFAULT_BOLD);
		p.setAntiAlias(true);
		canvas.drawText("Hey, this works!", 20, 200, p);
		
		// Draw an image
		p.reset();
		Bitmap img = BitmapFactory.decodeResource(getResources(), R.drawable.krusty);
		canvas.drawBitmap(img, 25, 250, p);
	}
}
