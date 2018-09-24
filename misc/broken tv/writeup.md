# Defcamp 2018 Quals: Broken TV

![date](https://img.shields.io/badge/date-22.09.2018-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)  
![misc category](https://img.shields.io/badge/category-misc-lightgrey.svg)
![score](https://img.shields.io/badge/score-83-blue.svg)
![solves](https://img.shields.io/badge/solves-73-brightgreen.svg)

## Description
Guys, I've asked Google for this flag! But my only monitor is this Broken TV..   
Target: https://broken-tv.dctfq18.def.camp/ 

## Summary
Circular shift of image rows until the flag appears

## Flag
```
DCTF{1e20cabc8098b16cfeefb05af0a9032bb953871d6d627e7f88b81d1a3c5fa809}
```

## Detailed solution
After we enter to the challenge page, we inspect the page and see that the image is changed every 1 minute, making a request on `blur.png?r=`, where the parameter `r` depend on timestamp.  
After viewing some images, for `r` between 0 and 10, we find out the place of the flag in image. Then, we download the `r=0` png, we crop the screen part and open in **Photoshop**. There, after some circular shifts made with *selection* and *move tools*, we can view the plaintext flag.
