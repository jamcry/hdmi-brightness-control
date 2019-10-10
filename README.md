# HDMI Brightness Control

A simple Python script for changing the brightness of external HDMI monitor.

## Usage
Just run the script with the desired percent of brightness as argument:
```bash
# One must be careful with low percentages!
$python3 main.py 50 # Sets brightness to 50%
```

Or, run without any arguments to reset to 100% brightness:
```bash
$python3 main.py # Resets brightness to 100%
```

## How it works
Basically, the script executes ```xrandr``` command with given brightness value for setting the brightness.

And ```subprocess``` library is used for executing terminal command.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
