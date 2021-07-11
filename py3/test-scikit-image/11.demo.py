from skimage import io, data
from skimage.color import (separate_stains, combine_stains, hdx_from_rgb, rgb_from_hdx)


img = data.astronaut()

# hdx
ihc_hdx = separate_stains(img, hdx_from_rgb)
# rgb
ihc_rgb = combine_stains(ihc_hdx, rgb_from_hdx)

io.imshow(ihc_hdx)
io.show()
