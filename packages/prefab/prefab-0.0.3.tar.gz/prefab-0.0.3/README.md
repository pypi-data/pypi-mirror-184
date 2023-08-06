<img src="assets/logo.png" title="PreFab" alt="PreFab">

# PreFab
`PreFab` (Prediction of Fabrication) is used for modelling fabrication process induced variations in integrated photonic devices using deep convolutional neural networks.

Trained models predict variations such as corner rounding (both over and under etching), washing away of small lines and islands, and filling of narrow holes and channels in planar photonic structures. Once predicted, the designer resimulates their design to rapidly prototype the expected performance and make any necessary corrections prior to (costly) fabrication.

![](assets/promo.png)
*Predicted fabrication variation of a simple star structure on a 220 nm silicon-on-insulator electron-beam lithography process. Prediction time of 8.2 seconds.*

## Models
The models currently included in `/models` are of the NanoSOI process from [Applied Nanotools Inc.](https://www.appliednt.com/nanosoi-fabrication-service/) These are alpha-stage models that are currently in development.

## License
This project is licensed under the terms of the GPL-3.0 license. © 2022 PreFab Photonics.
