# CRC64ISO

Python 3.x package for calculating __64-bit Cyclic Redundancy Check__ according to the __ISO 3309__ standard.

Generator polynomial: x<sup>64</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1

Reference:
_W. H. Press, S. A. Teukolsky, W. T. Vetterling, and B. P. Flannery, "Numerical recipes in C", 2nd ed.,
Cambridge University Press. Pages 896ff._

### Examples

- Calculate 64-bit checksum from a string:

```
from crc64iso.crc64iso import crc64

checksum = crc64iso.crc64("ILOVEMATH")
```

- Calculate 64-bit checksum from incremental (bytes) data:

```
from crc64iso.crc64iso import crc64_pair, format_crc64_pair

crc_pair_1 = crc64_pair("ILOVE".encode())
crc_pair_2 = crc64_pair("MATH".encode(), crc_pair_1)
checksum = format_crc64_pair(crc_pair_2)
```



