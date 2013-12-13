package bump_n_jump;

import java.net.URL;
import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.DataLine;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.SourceDataLine;
import javax.sound.sampled.UnsupportedAudioFileException;

/**
 * stolen directly from Zapped!
 * @author Aaron Haurwitz
 *
 */
public class SoundPlayback implements Runnable
{
	private final int bufSize = 16384;
	private AudioFormat format;
	private AudioInputStream audioInputStream;
	private SourceDataLine line;
	private Thread thread;
	private URL soundURL;
	private boolean loop = false;
	
	public SoundPlayback (String fName)
	{
		soundURL = this.getClass().getClassLoader().getResource(fName);
	}
	
	public SoundPlayback (String fName, boolean loop)
	{
		soundURL = this.getClass().getClassLoader().getResource(fName);
		this.loop = loop;
	}
	
	public void start()
	{
		thread = new Thread(this);
		thread.setName("Playback");
		thread.start();
	}
	
	public void stop()
	{
		thread = null;
	}

	private void shutDown (String message)
	{
		if (thread != null) {
			thread = null;
		}
	}
	
	private void doLoop() {
		start();
	}

	public void run()
	{
		// Make sure we have something to play
		if (soundURL != null) {
			// Set an AudioInputStream of the desired format for playback
			try {
				audioInputStream = AudioSystem.getAudioInputStream(soundURL);
				format = audioInputStream.getFormat();
			}
			catch (UnsupportedAudioFileException e) {
				System.err.println("Error with creating audio input stream! " + e.toString());				
			}
			catch (Exception e) {
				System.err.println("Error with creating audio input stream! " + e.toString());
			}
			AudioInputStream playbackInputStream = AudioSystem.getAudioInputStream(format, audioInputStream);
			try {
				if (playbackInputStream == null) {
					shutDown("Unable to convert stream of format " + audioInputStream + " to format " + format);
					return;
				}
						
				// Define the required attributes for our line, and make sure a compatible line is supported.
				DataLine.Info info = new DataLine.Info(SourceDataLine.class, format);
				if (!AudioSystem.isLineSupported(info)) {
					shutDown("Line matching " + info + " not supported.");
					return;
				}
						
				// Get and open the source data line for playback.
				try {
					line = (SourceDataLine) AudioSystem.getLine(info);
					line.open(format, bufSize);
				}
				catch (LineUnavailableException ex) {
					shutDown("Unable to open the line: " + ex);
					return;
				}
						
				// Play back the captured audio data
				int frameSizeInBytes = format.getFrameSize();
				int bufferLengthInFrames = line.getBufferSize() / 8;
				int bufferLengthInBytes = bufferLengthInFrames * frameSizeInBytes;
				byte[] data = new byte[bufferLengthInBytes];
				int numBytesRead = 0;
						
				// Start the source data line
				
					
					line.start();
					while (thread != null) {
						try {
							if ((numBytesRead = playbackInputStream.read(data)) == -1) {
								break;
							}
							int numBytesRemaining = numBytesRead;
							while (numBytesRemaining > 0) {
								numBytesRemaining -= line.write(data, 0, numBytesRemaining);
							}
						}
						catch (Exception e) {
							shutDown("Error during playback: " + e);
							break;
						}
					}
							
					// We reached the end of the stream.  let the data play out, then stop and close the line.
					if (thread != null) {
						line.drain();
					}
					line.stop();
					line.close();
					line = null;
					shutDown(null);
				
					
			}
			catch (Exception e) {
				shutDown("Unable to create playback steam: "+e);
			}
			if (loop)
				doLoop();
		}
	}
}