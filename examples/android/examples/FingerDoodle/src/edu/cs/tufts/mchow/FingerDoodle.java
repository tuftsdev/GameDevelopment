package edu.cs.tufts.mchow;

import edu.cs.tufts.mchow.ColorPickerDialog.OnColorChangedListener;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.MenuInflater;
import android.widget.Toast;

public class FingerDoodle extends Activity
{
	private final int SHOW_ABOUT_DURATION = 25;
	private final int SHOW_NEW_DOODLE_DURATION = 5;
	private final CharSequence[] strokeList = {"Thinnest", "Thinner", "Default", "Thicker", "Thickest", "Eraser"};
	private FingerDoodleView fdv;
	
	@Override
	public void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		fdv = new FingerDoodleView(this);
		setContentView(fdv);
	}
	
	@Override
	public boolean onCreateOptionsMenu(Menu menu)
	{
		MenuInflater inflater = getMenuInflater();
	    inflater.inflate(R.menu.options, menu);
		return true;
	}
	
	@Override
	public boolean onOptionsItemSelected(MenuItem item)
	{
		switch (item.getItemId()) {
			case R.id.newd:
				fdv.doodle = new Doodle();
				Toast.makeText(this, R.string.newdToast, SHOW_NEW_DOODLE_DURATION).show();
				return true;
			case R.id.uBackground:
				new ColorPickerDialog(fdv.getContext(), new OnColorChangedListener() {
					public void colorChanged(int color) {
						fdv.doodle.backgroundColor = color;
						for (DoodlePath p: fdv.doodle.paths) {
							if (p.eraser) {
								p.paint.setColor(color);
							}
						}
					}},
					fdv.doodle.backgroundColor).show();
				return true;
			case R.id.uPaint:
				new ColorPickerDialog(fdv.getContext(), new OnColorChangedListener() {
					public void colorChanged(int color) {
						fdv.doodle.currentPaint.setColor(color);
					}},
					fdv.doodle.currentPaint.getColor()).show();
				return true;
			case R.id.uStroke:
				AlertDialog.Builder builder = new AlertDialog.Builder(this);
				builder.setTitle(R.string.dialog_change_stroke_width);
				builder.setSingleChoiceItems(strokeList, (int)fdv.doodle.currentPaint.getStrokeWidth() - 1, new DialogInterface.OnClickListener() {
					public void onClick(DialogInterface dialog, int item) {
						// The last item is the eraser
						if (item == strokeList.length - 1) {
							fdv.doodle.eraser = true;
						}
						else {
							fdv.doodle.eraser = false;
						}
						fdv.doodle.currentPaint.setStrokeWidth(item + 1);
						dialog.dismiss();
					}
				});
				AlertDialog alert = builder.create();
				alert.show();
				return true;
			case R.id.about:
				Toast.makeText(this, R.string.about_text, SHOW_ABOUT_DURATION).show();
				return true;
			default:
				return super.onOptionsItemSelected(item);
		}
	}
}
