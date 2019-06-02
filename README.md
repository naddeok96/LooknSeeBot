# LooknSeeBot
A robot that learns to look at dictated objects in a Lifelong learning fashion

## Objective
 *The human user should be able to say out loud to look at the "red pen" then a robotic arm holding a camera should move so that the red pen is in the center of the cameras vision. Once trainned the robot should be able to learn new tasks (ie identify a chess postions, look at the speaker)*
 
## Subtasks
- [ ] Robotic Arm
- Controlled by servos through a RaspberryPi
- Must have the power to hold the camera when fully outstretched

- [ ] Eye Contact
- With no instruction the bot should center its vision on a face (only one face should be present at a time)
- This will act as a proof of concept that the arm is capable
- When future tasks are learned the retention of this task will be used as a metrics of catasphic forgetting

- [ ] Natural Language Processing (NLP)
- When "red pen" is said out loud the robot must translate the signal into text

- [ ] Text to Image Segmentation
- When the text red pen is given, the classifier should identify it in the image

- [ ] NLP to Image Segmentation
- When "red pen" is said out loud the robot must translate the signal into text then identify it in an image

- [ ] Text to Video Segmentation
- When the text red pen is given, the classifier should identify it in a video

- [ ] NLP to Video Segmentation
- When "red pen" is said out loud the robot must translate the signal into text then identify it in a video

- [ ] Coexistence
- Have all subtasks work together to achieve the end goal

