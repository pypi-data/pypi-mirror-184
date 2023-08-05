# myimagelib

myimagelib is a collection of image analysis code, including particle tracking, PIV, file manipulations and more. These code are initially just for my own convenience. As time goes on, they gradually become an integral part of my daily coding. When I share my code with friends, I always find it a problem when they cannot import in their local environment, and I have to ask them to download the code from my GitHub, or rewrite my code using packages that are already available on PyPI. This has been a PITA for a while, and I realize that it could be useful to make the code available on PyPI, too. So that my friend can download my code with a simple `pip install`. 

I understand that this package consists of code for many different purposes and they are not organized very nicely. It is only intended for people who are going to run my notebooks, but need the functions that I wrote earlier in this library. 







## Milestones

#### v1.2 

1. Reorganize the repo as a PyPI package and publish on PyPI.

#### v1.1 (all met)

1. All the functions and scripts that output PIV data should put PIV in a .mat container, which only save x, y, mask, labels in formation once, and save u, v as 3D arrays. 

2. The operations that based on \*.tif images should be transformed to work on raw images. The affected operations are: 

- PIV
- gen_preview
- remove_background
