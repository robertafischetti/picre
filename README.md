## **Introduction**

**Picre** is a Playblasts In-Context REviewer (in development) designed for animators who use Maya. 
It is a small, artist-facing tool that make reviewing shots in context faster, without the need to publish on Flow first. 
It is made of two components: a Playblast Manager and a Playblasts Reviewer.

## **Playblast Manager**
- it captures the scene settings, reading the active camera, frame range and resolution;
- it validates names and paths, ensuring every playblast lands in the right folder with the right name at the next version;
- it adds burn-in overlays.

## **Playblasts Reviewer**
- It scans the folder where the playblasts have been exported and shows the animator what’s in there. 
- The artist ticks the shots he/she wants to review in context and the tool stiches them into a single clip (each shot will be recognizable thanks to the burn-ins added by the playblast manager).