# Tupper's self-referencial Formula (TSRF)
This is a simple but versatile implementation of the formula.

## What is TSRF?
It is a simple math formula that when plotted, it shows the formula itself.

![alt text](https://blogs.ams.org/mathgradblog/files/2016/05/eq.11.png "Definition of TSRF")

The catch is plotting an appropriate range of that function.
Basically, by only plotting 17 contiguous values on Y, given an offset k, it is possible to produce any binary image that fits in that space (including the formula itself).

![alt text](http://blogs.ams.org/mathgradblog/files/2016/05/Screenshot-2016-05-16-12.18.13-1.png "Plot of the TSRF")

The trick is finding the right offset k. For the plot of the formula itself

`k = 960939379918958884971672962127852754715004339660129306651505519271702802395266424689642842174350718121267153782770623355993237280874144307891325963941337723487857735749823926629715517173716995165232890538221612403238855866184013235585136048828693337902491454229288667081096184496091705183454067827731551705405381627380967602565625016981482083418783163849115590225610003652351370343874461848378737238198224849863465033159410054974700593138339226497249461751545728366702369745461014655997933798537483143786841806593422227898388722980000748404719`

For an introduction of what it is, refer to resources such as:
- The [AMS blog about TSRF](https://blogs.ams.org/mathgradblog/2016/05/18/tuppers-self-referential-formula/)

## Functionality
Two use cases are covered by this code:

1. Given a value of `k`, plot the resuling graph using TSRF.
2. Given a binary graph (of adequate size), compute the value of `k` for that map.

For use-case #1, the plot is simply shown on the screen. For use-case #2, you need to provide the path to an PNG image of size 106x17 pixels (height, width).
The image is binarized to calculate the corresponding value of `k`.
This value can be then stored and used for use-case #1.
If the image is larger, only a rectangular region (corresponding to the 106x17 area) will be considered.
If the image is smaller, it will be padded accordingly.

## Example
I created a music score with Adam Neely's version of ["The Lick"](https://www.youtube.com/watch?v=lSXxEdaOqgU) using [GIMP](https://gimp.org) and saved it as lossless PNG. Then I can simply execute the script to compute the value of `k` that produces said input.

```
$ python tupper.py -i thelick.png
k = 71439938339224208629805599350431207703767308845238963304555921996400268306073743024332467322051632302955765178713380085345571191717785318084043336147686340844952769368625974903442794358119140397729546708289004542177607710662776758984161009453796784640258224609393463285923152195833809558873349393121969357300071617296443415541883904749045763288537786129391257563426515907788583292216357674634784014590500156945647900613572576647950897657027777673189681550636297150513213522261225154937329129737294116494660978048186842881178387673705474949120
Press key
$
```

To re-generate the plot without the input image, the script can be used with the `-k` flag as follows:

```
$ python tupper.py -k 71439938339224208629805599350431207703767308845238963304555921996400268306073743024332467322051632302955765178713380085345571191717785318084043336147686340844952769368625974903442794358119140397729546708289004542177607710662776758984161009453796784640258224609393463285923152195833809558873349393121969357300071617296443415541883904749045763288537786129391257563426515907788583292216357674634784014590500156945647900613572576647950897657027777673189681550636297150513213522261225154937329129737294116494660978048186842881178387673705474949120
Using provided k...
Press key
$
```

### Requirements
- python 3.x
- numpy
- matplotlib
- argparse
