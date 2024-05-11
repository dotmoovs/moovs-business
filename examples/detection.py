from moovs_business import DetectionFlow, QVideo
import asyncio


async def main():
    # Load detection flow
    detector = DetectionFlow()

    # Instatiate a video
    video = QVideo("assets/surfing.mp4")

    # Detect all of the bounding boxes
    bbox_sequence = await detector(video)

    # View the output
    await bbox_sequence.view(video, "output.mp4")


asyncio.run(main())
