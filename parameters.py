# ADJUSTABLE PARAMETERS

class parameters:
    def __init__(self, mid_percent_save, crop_threshold_lev, resizing_filter, width_divisor, height_divisor, start_height, end_height, maxAllowableIterations, dimension_units):
        self.mps = mid_percent_save         # Save middle x% of images | Accepted Values in Interval: (0.0, 1.0]
        self.ctl = crop_threshold_lev       # Higher -> Cut off more of image | Lower -> Cut off less of image | Max ~155
        self.rf = resizing_filter           # See http://pillow.readthedocs.io/en/4.3.x/handbook/concepts.html#concept-filters
        self.wd = width_divisor             # Higher -> Reduce size of laplacian matrix | Lower -> Retain more pixels | Min ???
        self.hd = height_divisor            # Higher -> Reduce size of laplacian matrix | Lower -> Retain more pixels | Min ???
        self.sh = start_height              # Height of first image taken in 'rawImages/'
        self.eh = end_height                # Height of last image taken in 'rawImages/'
        self.mai = maxAllowableIterations   # Higher -> more noise in model | Lower -> less noise in model | Min -> 2
        self.du = dimension_units           # Currently supports: in, mm, and cm
