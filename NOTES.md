### Paper Notes

**LSD-SLAM: Large-Scale Direct Monocular SLAM**

![Algo]("./algo.png")

SLAM == Simultaneous Localization and Mapping

- direct (feature-less) monocular slam algorithm allows to build large-scale, consistent maps of the world.

- Along with highly accurate pose estimation based on direct image alignment, the 3D environment is reconstructed in real-time as pose-graph of keyframes with associated semi-dense depth maps.

- These are obtained by filtering over a large number of pixelwise small-baseline stereo comparisons.

- Major enablers are two key novelties:

  1. A novel direct tracking method which operates on sim(3), thereby explicitly detecting scale-drift, and
  2. An elegant probabilistic solution to include the effect of noisy depth values into tracking.

- The resulting direct monocular SLAM system runs in realtime on a CPU.
